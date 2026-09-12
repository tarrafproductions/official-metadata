#!/usr/bin/env python3
"""Index canonical artwork. Images are inputs and are never copied or rewritten."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMAGE_DIR = 'assets/covers/by-release'
MAP_PATH = 'assets/covers/release-map.json'


def release_catalog_id(release):
    values = [i['value'] for i in release.get('identifier', [])
              if i.get('propertyID') == 'TARRAF Catalog Release ID']
    if len(values) > 1:
        raise ValueError('Multiple catalog IDs: ' + release['@id'])
    if values:
        catalog_id = values[0]
    else:
        match = re.fullmatch(
            r'https://aliktarraf.com/#tarraf-productions-live-vol-(iii|ii|i)-digital-release',
            release['@id'])
        if not match:
            raise ValueError('Missing catalog ID: ' + release['@id'])
        catalog_id = 'LIVE-' + match[1].upper()
    target_path(catalog_id)
    return catalog_id


def target_path(catalog_id):
    if re.fullmatch(r'SNG-\d{3}', catalog_id):
        name = 'cover-' + catalog_id[4:] + '.webp'
    elif catalog_id in ('LIVE-I', 'LIVE-II', 'LIVE-III'):
        name = 'live-vol-' + catalog_id[5:].lower() + '.webp'
    else:
        raise ValueError('Invalid catalog ID: ' + catalog_id)
    return IMAGE_DIR + '/' + name


def canonical_releases(root):
    result = {}
    for path in ('releases/studio-singles.jsonld', 'releases/live-trilogy.jsonld'):
        document = json.loads((root / path).read_text(encoding='utf-8'))
        nodes = {n['@id']: n for n in document['@graph']}
        for release in nodes.values():
            if release.get('@type') != 'MusicRelease':
                continue
            album = nodes[release['releaseOf']['@id']]
            catalog_id = release_catalog_id(release)
            if catalog_id in result:
                raise ValueError('Duplicate catalog ID: ' + catalog_id)
            upcs = [i['value'] for i in release.get('identifier', [])
                    if i.get('propertyID') == 'UPC']
            if len(upcs) != 1 or not isinstance(upcs[0], str):
                raise ValueError('Release requires one string UPC: ' + catalog_id)
            result[catalog_id] = {'catalogId': catalog_id, 'releaseId': release['@id'],
                                  'title': album['name'], 'upc': upcs[0]}
    return result


def build(root):
    releases = canonical_releases(root)
    expected = {target_path(catalog_id) for catalog_id in releases}
    allowed = expected | {MAP_PATH, 'assets/covers/README.md'}
    actual = {p.relative_to(root).as_posix()
              for p in (root / 'assets/covers').rglob('*') if p.is_file()}
    unexpected = actual - allowed
    if (root / 'assets/covers/archive').exists():
        unexpected.add('assets/covers/archive')
    if unexpected:
        raise ValueError('Unexpected artwork files or duplicate directory: ' + ', '.join(sorted(unexpected)))
    rows = []
    for catalog_id, canonical in releases.items():
        row = dict(canonical)
        path = target_path(catalog_id)
        image = root / path
        if image.is_symlink():
            raise ValueError('Artwork must be a regular file: ' + path)
        if image.is_file():
            data = image.read_bytes()
            if (data[:4] != b'RIFF' or data[8:12] != b'WEBP'
                    or int.from_bytes(data[4:8], 'little') + 8 != len(data)):
                raise ValueError('Invalid WebP container: ' + path)
            row.update(status='verified', coverPath=path,
                       sha256=hashlib.sha256(data).hexdigest(), bytes=len(data))
        else:
            row.update(status='needs-review', coverPath=None, sha256=None, bytes=None)
        rows.append(row)
    rows.sort(key=lambda r: (r['catalogId'].startswith('LIVE-'), r['catalogId']))
    mapped = sum(r['coverPath'] is not None for r in rows)
    output = {
        'schemaVersion': 2,
        'generated': True,
        'generatedFrom': ['releases/studio-singles.jsonld', 'releases/live-trilogy.jsonld', IMAGE_DIR],
        'pathBase': 'Repository root of the same pinned snapshot',
        'counts': {'releases': len(rows), 'mappedReleases': mapped,
                   'unmappedReleases': len(rows) - mapped, 'coverFiles': mapped},
        'releases': rows,
    }
    return {MAP_PATH: (json.dumps(output, ensure_ascii=False, indent=2) + '\n').encode('utf-8')}, output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--require-complete', action='store_true')
    args = parser.parse_args()
    files, mapping = build(args.root)
    if args.require_complete and mapping['counts']['unmappedReleases']:
        raise SystemExit('Missing artwork: ' + ', '.join(
            r['catalogId'] for r in mapping['releases'] if not r['coverPath']))
    for name, data in files.items():
        path = args.root / name
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                raise SystemExit('Stale artwork index; run python3 .github/scripts/build_cover_mapping.py')
        else:
            path.write_bytes(data)
    print(json.dumps(mapping['counts'], ensure_ascii=False))


if __name__ == '__main__':
    main()
