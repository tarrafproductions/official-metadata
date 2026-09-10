#!/usr/bin/env python3
"""Build and validate release artwork without changing the source archive."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REVIEW = 'sources/cover-art-review-2026-09-10.json'

def load(root, path):
    return json.loads((root / path).read_text(encoding='utf-8'))

def canonical_releases(root):
    result = {}
    for path in ('releases/studio-singles.jsonld', 'releases/live-trilogy.jsonld'):
        nodes = {n['@id']: n for n in load(root, path)['@graph']}
        for release in nodes.values():
            if release.get('@type') != 'MusicRelease':
                continue
            album = nodes[release['releaseOf']['@id']]
            identifiers = {v['propertyID']: v['value'] for v in release.get('identifier', [])}
            catalog_id = identifiers.get('TARRAF Catalog Release ID')
            if not catalog_id:
                match = re.search(r'-vol-(iii|ii|i)-', release['@id'])
                if not match:
                    raise ValueError('Unknown release identity: ' + release['@id'])
                catalog_id = 'LIVE-' + match[1].upper()
            if catalog_id in result:
                raise ValueError('Duplicate catalog ID: ' + catalog_id)
            result[catalog_id] = {'catalogId': catalog_id, 'releaseId': release['@id'],
                                  'title': album['name'], 'upc': identifiers['UPC']}
    return result

def target_path(catalog_id):
    if re.fullmatch(r'SNG-\d{3}', catalog_id):
        name = 'cover-' + catalog_id[4:] + '.webp'
    elif catalog_id in ('LIVE-I', 'LIVE-II', 'LIVE-III'):
        name = 'live-vol-' + catalog_id[5:].lower() + '.webp'
    else:
        raise ValueError('Invalid catalog ID: ' + catalog_id)
    return 'assets/covers/by-release/' + name

def build(root):
    review = load(root, REVIEW)
    manifest = load(root, 'assets/covers/manifest.json')
    covers = {c['coverId']: c for c in manifest['covers']}
    if len(covers) != manifest['coverCount']:
        raise ValueError('Duplicate or missing archive cover IDs')
    source_data = {}
    for cover_id, c in covers.items():
        path = c['path']
        if not re.fullmatch(r'assets/covers/archive/cover-\d{3}\.webp', path):
            raise ValueError('Invalid archive path: ' + path)
        data = (root / path).read_bytes()
        if len(data) != c['bytes'] or hashlib.sha256(data).hexdigest() != c['sha256']:
            raise ValueError('Archive checksum mismatch: ' + cover_id)
        source_data[cover_id] = data
    releases = canonical_releases(root)
    assignments = {}
    assigned_covers = set()
    for match in review['matches']:
        catalog_id, cover_id = match['catalogId'], match['coverId']
        if catalog_id not in releases or cover_id not in covers:
            raise ValueError('Unknown release or cover: ' + str(match))
        if catalog_id in assignments:
            raise ValueError('Multiple primary covers for ' + catalog_id)
        if not match.get('method'):
            raise ValueError('Missing verification method: ' + catalog_id)
        assignments[catalog_id] = match
        assigned_covers.add(cover_id)
    unassigned_ids = [c['coverId'] for c in review['unassignedCovers']]
    if len(unassigned_ids) != len(set(unassigned_ids)):
        raise ValueError('Repeated unassigned cover')
    if set(unassigned_ids) & assigned_covers or set(unassigned_ids) | assigned_covers != set(covers):
        raise ValueError('Every archive cover needs exactly one disposition')
    rows, files = [], {}
    for catalog_id, canonical in releases.items():
        row = dict(canonical)
        match = assignments.get(catalog_id)
        if match:
            c = covers[match['coverId']]
            path = target_path(catalog_id)
            row.update(status='verified', coverId=c['coverId'], coverPath=path,
                       sourcePath=c['path'], sha256=c['sha256'], verification=match)
            files[path] = source_data[c['coverId']]
        else:
            row.update(status='needs-review', coverId=None, coverPath=None,
                       sourcePath=None, sha256=None,
                       verification={'note': 'No verified cover association; do not infer from file order.'})
        rows.append(row)
    rows.sort(key=lambda r: (r['catalogId'].startswith('LIVE-'), r['catalogId']))
    counts = {'releases': len(rows), 'mappedReleases': len(assignments),
              'unmappedReleases': len(rows) - len(assignments), 'archiveFiles': len(covers),
              'unassignedArchiveFiles': len(unassigned_ids)}
    output = {'schemaVersion': 1, 'reviewedOn': review['reviewedOn'],
              'sourceCommit': review['sourceCommit'],
              'pathBase': 'Repository root of the same pinned snapshot',
              'counts': counts, 'releases': rows,
              'unassignedCovers': review['unassignedCovers']}
    files['assets/covers/release-map.json'] = (json.dumps(output, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    table = ['# Release artwork mapping', '',
             f"{counts['mappedReleases']} of {counts['releases']} release products have a verified artwork association; {counts['unmappedReleases']} remain explicitly unassigned.", '',
             'Generated from the [visual review](../' + REVIEW + '). Archive filenames are source-order IDs, not release IDs.', '',
             'Use `coverPath` from [release-map.json](../assets/covers/release-map.json), joined by `catalogId`, `releaseId` or UPC. Resolve paths relative to the same pinned repository snapshot.', '',
             '| Catalog ID | Release | UPC | Artwork |', '| --- | --- | --- | --- |']
    for r in rows:
        artwork = '[%s](../%s)' % (Path(r['coverPath']).name, r['coverPath']) if r['coverPath'] else '**Needs review**'
        table.append('| %s | %s | %s | %s |' % (r['catalogId'], r['title'].replace('|', '\\|'), r['upc'], artwork))
    files['docs/cover-mapping.md'] = ('\n'.join(table) + '\n').encode('utf-8')
    discography_path = 'docs/discography.md'
    discography = (root / discography_path).read_text(encoding='utf-8')
    artwork_summary = (
        '<!-- BEGIN GENERATED ARTWORK STATUS -->\n'
        f"{counts['mappedReleases']} of {counts['releases']} release products have a verified cover association "
        f"({counts['unmappedReleases']} still need review). "
        'The [complete mapping](cover-mapping.md) includes singles and all three live albums; '
        'the [review list](cover-review-needed.md) shows unresolved artwork.\n'
        '<!-- END GENERATED ARTWORK STATUS -->'
    )
    discography, replaced = re.subn(
        r'<!-- BEGIN GENERATED ARTWORK STATUS -->.*?<!-- END GENERATED ARTWORK STATUS -->',
        lambda _: artwork_summary, discography, flags=re.S)
    if replaced != 1:
        raise ValueError('Missing or repeated generated artwork status in discography')
    discography = discography.replace(
        '| Catalog ID | Date | Release | Credited artist(s) | UPC | ISRC | Verification |\n'
        '| --- | --- | --- | --- | --- | --- | --- |',
        '| Catalog ID | Date | Release | Credited artist(s) | UPC | ISRC | Verification | Artwork |\n'
        '| --- | --- | --- | --- | --- | --- | --- | --- |')
    by_id = {r['catalogId']: r for r in rows}
    seen = set()
    lines = []
    for line in discography.splitlines():
        match = re.match(r'^\| (SNG-\d{3}) \|', line)
        if match:
            catalog_id = match[1]
            if catalog_id not in by_id or catalog_id in seen:
                raise ValueError('Unknown or duplicate discography row: ' + catalog_id)
            seen.add(catalog_id)
            cells = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
            if len(cells) not in (7, 8):
                raise ValueError('Unexpected discography columns: ' + catalog_id)
            r = by_id[catalog_id]
            artwork = '[%s](../%s)' % (Path(r['coverPath']).name, r['coverPath']) if r['coverPath'] else '**Needs review**'
            line = '| ' + ' | '.join(cells[:7] + [artwork]) + ' |'
        lines.append(line)
    if seen != {r['catalogId'] for r in rows if r['catalogId'].startswith('SNG-')}:
        raise ValueError('Discography does not contain every canonical single')
    files[discography_path] = ('\n'.join(lines) + '\n').encode('utf-8')
    pending = ['# Обложки: что осталось подтвердить', '',
               'Проверенные пары уже включены в `assets/covers/release-map.json`. Оставшиеся вопросы и подтверждения владельца приведены ниже. Номер COV относится к исходному архиву, номер SNG — к релизу.', '',
               '## Релизы без подтверждённой обложки', '',
               '| ID | Название | UPC |', '| --- | --- | --- |']
    for r in rows:
        if not r['coverPath']:
            pending.append('| %s | %s | %s |' % (r['catalogId'], r['title'], r['upc']))
    needs_review = [item for item in review['unassignedCovers']
                    if item['status'] not in ('duplicate', 'alternate-artwork')]
    if needs_review:
        pending += ['', '## Картинки для уточнения', '',
                    'Для картинки достаточно указать название релиза или его SNG-ID. Если нужной обложки здесь нет, нужен её исходный файл. Статусы дубликатов приведены отдельно ниже.', '',
                    '| Обложка | Что нужно уточнить |', '| --- | --- |']
        for item in needs_review:
            pending.append('| **%s** ![%s](../%s) | %s |' % (item['coverId'], item['coverId'], covers[item['coverId']]['path'], item['note']))
    else:
        pending += ['', 'Все архивные файлы сопоставлены с релизами либо отмечены как дубликаты или альтернативные варианты. Для релизов из списка выше нужны их обложки или подтверждение, какой из имеющихся файлов использовать.']
    owner_matches = [m for m in review['matches'] if m['method'] == 'catalog-owner-confirmation']
    if owner_matches:
        pending += ['', '## Подтверждения владельца', '',
                    'Эти соответствия уточнены владельцем каталога Аликом Таррафом и уже применены.', '',
                    '| Архивная обложка | Релиз | Название в каталоге |', '| --- | --- | --- |']
        for m in owner_matches:
            pending.append('| %s | %s | %s |' % (m['coverId'], m['catalogId'], by_id[m['catalogId']]['title']))
    pending += ['', '## Дубликаты и альтернативные файлы', '', '| Файл | Пояснение |', '| --- | --- |']
    for item in review['unassignedCovers']:
        if item['status'] in ('duplicate', 'alternate-artwork'):
            pending.append('| %s | %s |' % (item['coverId'], item['note']))
    if not by_id['SNG-015']['coverPath']:
        pending += ['', 'PROSTO (SNG-015): на проверенной странице Apple Music изображена Марина на оранжевом фоне с надписью «ПРОСТО» без remix. В исходном архиве найденные COV-034 и COV-186 имеют другую композицию и надпись remix; использовать их для SNG-015 без подтверждения нельзя.']
    files['docs/cover-review-needed.md'] = ('\n'.join(pending) + '\n').encode('utf-8')
    return files, output

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--require-complete', action='store_true')
    args = parser.parse_args()
    files, mapping = build(args.root)
    stale = []
    for name, data in files.items():
        path = args.root / name
        if args.check:
            if not path.is_file() or path.read_bytes() != data:
                stale.append(name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    unexpected = set(p.relative_to(args.root).as_posix() for p in (args.root / 'assets/covers/by-release').glob('*.webp')) - set(files)
    if stale or unexpected:
        raise SystemExit('Stale or unexpected artwork files: ' + ', '.join(stale + sorted(unexpected)))
    print(json.dumps(mapping['counts'], ensure_ascii=False))
    if args.require_complete and mapping['counts']['unmappedReleases']:
        raise SystemExit('Artwork mapping is incomplete; see docs/cover-review-needed.md')

if __name__ == '__main__':
    main()
