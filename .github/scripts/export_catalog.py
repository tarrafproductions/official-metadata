#!/usr/bin/env python3
"""Build reproducible, neutral catalog exports from the canonical JSON-LD graph."""

from __future__ import annotations

import argparse
import csv
import io
import json
import re
import sys
from decimal import Decimal
from pathlib import Path
from typing import Any


FIELDS = (
    'recording_id', 'recording_title', 'recording_alternate_titles',
    'recording_artist_credit', 'recording_artist_ids', 'isrc',
    'duration_iso8601', 'duration_ms', 'release_id', 'release_title',
    'release_artist_credit', 'upc', 'release_date', 'release_status',
    'track_number', 'record_label', 'musicbrainz_release_id', 'reference_urls',
)
ARRAY_FIELDS = {'recording_alternate_titles', 'recording_artist_ids', 'reference_urls'}
DURATION = re.compile(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?')


def as_list(value: Any) -> list:
    return value if isinstance(value, list) else [] if value is None else [value]


def duration_ms(value: Any) -> int:
    match = DURATION.fullmatch(value) if isinstance(value, str) else None
    if not match or not any(match.groups()):
        raise ValueError(f'Invalid duration: {value!r}')
    result = sum(Decimal(v or 0) * f for v, f in zip(match.groups(), (3600000, 60000, 1000)))
    if result <= 0 or result != result.to_integral_value():
        raise ValueError(f'Duration must be positive with at most millisecond precision: {value!r}')
    return int(result)


def walk(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def build_catalog(root: Path) -> dict:
    documents = [json.loads(p.read_text(encoding='utf-8')) for p in sorted(root.rglob('*.jsonld')) if '.git' not in p.relative_to(root).parts]
    nodes = {node['@id']: node for doc in documents for node in walk(doc) if '@id' in node and '@type' in node}
    catalog = nodes['https://github.com/tarrafproductions/official-metadata#catalog']
    as_of = catalog['dateModified']

    def party_name(party):
        return nodes.get(party.get('@id'), party).get('name', '')

    def credit(node, field='byArtist'):
        value = node.get('creditText')
        # Live album creditText lists production roles, not a display artist.
        return value if isinstance(value, str) else ', '.join(party_name(p) for p in as_list(node.get(field)))

    rows = []
    for release in sorted((n for n in nodes.values() if n.get('@type') == 'MusicRelease'), key=lambda n: n['@id']):
        album = nodes[release['releaseOf']['@id']]
        upcs = [i['value'] for i in as_list(release.get('identifier')) if i.get('propertyID') == 'UPC']
        if len(upcs) != 1 or not isinstance(upcs[0], str):
            raise ValueError(f"Release requires one string UPC: {release['@id']}")
        track = nodes[album['track']['@id']]
        entries = track['itemListElement'] if track['@type'] == 'ItemList' else [{'position': 1, 'item': {'@id': track['@id']}}]
        release_date = release['datePublished']
        status = release.get('creativeWorkStatus') or album.get('creativeWorkStatus') or ('Scheduled for release' if release_date > as_of else 'Published')
        mbids = [u.rstrip('/').rsplit('/', 1)[-1] for u in as_list(release.get('sameAs')) if re.fullmatch(r'https://musicbrainz\.org/release/[0-9a-f-]{36}/?', u)]
        for entry in entries:
            recording = nodes[entry['item']['@id']]
            rows.append({
                'recording_id': recording['@id'],
                'recording_title': recording['name'],
                'recording_alternate_titles': as_list(recording.get('alternateName')),
                'recording_artist_credit': credit(recording),
                'recording_artist_ids': [p['@id'] for p in as_list(recording.get('byArtist')) if '@id' in p],
                'isrc': recording['isrcCode'],
                'duration_iso8601': recording['duration'],
                'duration_ms': duration_ms(recording['duration']),
                'release_id': release['@id'],
                'release_title': album['name'],
                'release_artist_credit': credit(album),
                'upc': upcs[0],
                'release_date': release_date,
                'release_status': status,
                'track_number': entry['position'],
                'record_label': ', '.join(party_name(p) for p in as_list(release.get('recordLabel'))),
                'musicbrainz_release_id': mbids[0] if mbids else '',
                'reference_urls': as_list(recording.get('sameAs')),
            })
    return {
        'schema_version': 1,
        'as_of': as_of,
        'description': 'One row per recording appearance on a release. ISRC identifies a recording; UPC identifies a release. Repeated ISRCs across different releases are intentional.',
        'submission_status': 'Neutral metadata export; no external registration or rights claim is implied. Recipient-specific mapping and required rights fields remain separate.',
        'counts': {'rows': len(rows), 'recordings': len({r['recording_id'] for r in rows}), 'isrcs': len({r['isrc'] for r in rows}), 'releases': len({r['release_id'] for r in rows}), 'upcs': len({r['upc'] for r in rows})},
        'rows': rows,
    }


def export_contents(root: Path) -> dict[str, str]:
    catalog = build_catalog(root)
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=FIELDS, quoting=csv.QUOTE_ALL, lineterminator='\n')
    writer.writeheader()
    for row in catalog['rows']:
        writer.writerow({key: json.dumps(value, ensure_ascii=False) if key in ARRAY_FIELDS else value for key, value in row.items()})
    return {
        'exports/catalog.json': json.dumps(catalog, ensure_ascii=False, indent=2) + '\n',
        'exports/catalog.csv': stream.getvalue(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--check', action='store_true', help='Fail if committed exports differ from the canonical graph.')
    args = parser.parse_args()
    stale = []
    for name, expected in export_contents(args.root).items():
        path = args.root / name
        if args.check:
            if not path.exists() or path.read_bytes() != expected.encode('utf-8'):
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding='utf-8', newline='')
    if stale:
        print('Stale exports: ' + ', '.join(stale), file=sys.stderr)
        print('Run python3 .github/scripts/export_catalog.py', file=sys.stderr)
        return 1
    print('Catalog exports are current' if args.check else 'Catalog exports generated')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
