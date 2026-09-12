"""Regression checks for master identity, release mapping and export fidelity."""

import csv
import io
import json
import unittest
from tempfile import TemporaryDirectory
from copy import deepcopy
from pathlib import Path

from export_catalog import ARRAY_FIELDS, build_catalog, duration_ms, export_contents, walk
from validate_jsonld import validate_recordings_and_tracklists
from build_cover_mapping import build as build_artwork, MAP_PATH, target_path


ROOT = Path(__file__).resolve().parents[2]


class CatalogIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nodes = {}
        for path in ROOT.rglob('*.jsonld'):
            for node in walk(json.loads(path.read_text(encoding='utf-8'))):
                if '@id' in node and '@type' in node:
                    cls.nodes[node['@id']] = node

    def test_shared_master_has_one_identity_and_two_releases(self):
        rows = [r for r in build_catalog(ROOT)['rows'] if r['isrc'] == 'QT3FE2691958']
        self.assertEqual({r['upc'] for r in rows}, {'883369720266', '882321270177'})
        self.assertEqual({r['recording_id'] for r in rows}, {'https://aliktarraf.com/#catalog-trk-0260'})
        self.assertEqual({r['duration_ms'] for r in rows}, {323800})
        encore = next(r for r in rows if r['upc'] == '882321270177')
        self.assertEqual(encore['release_status'], 'Scheduled for release')
        self.assertEqual(encore['track_number'], 4)

    def test_csv_round_trip_preserves_identifiers_unicode_and_lists(self):
        exports = export_contents(ROOT)
        canonical = json.loads(exports['exports/catalog.json'])['rows']
        rows = list(csv.DictReader(io.StringIO(exports['exports/catalog.csv'])))
        self.assertEqual(len(rows), len(canonical))
        for actual, expected in zip(rows, canonical):
            for key, value in expected.items():
                self.assertEqual(json.loads(actual[key]) if key in ARRAY_FIELDS else actual[key], value if key in ARRAY_FIELDS else str(value))

    def test_duplicate_isrc_definition_is_rejected(self):
        nodes = deepcopy(self.nodes)
        original = next(n for n in nodes.values() if n.get('@type') == 'MusicRecording')
        duplicate = deepcopy(original)
        duplicate['@id'] = 'https://aliktarraf.com/#invalid-duplicate-master'
        nodes[duplicate['@id']] = duplicate
        self.assertTrue(any('already defines' in e for e in validate_recordings_and_tracklists(nodes)))

    def test_wrong_live_order_and_missing_reciprocal_album_are_rejected(self):
        nodes = deepcopy(self.nodes)
        tracklist = next(n for n in nodes.values() if n.get('@type') == 'ItemList')
        tracklist['itemListElement'][0]['position'] = 2
        recording_id = tracklist['itemListElement'][0]['item']['@id']
        nodes[recording_id]['inAlbum'] = {'@id': 'https://aliktarraf.com/#wrong-album'}
        errors = validate_recordings_and_tracklists(nodes)
        self.assertTrue(any('consecutive and ordered' in e for e in errors))
        self.assertTrue(any('reciprocal inAlbum' in e for e in errors))

    def test_invalid_and_empty_durations_are_rejected(self):
        for value in (None, '', 'PT', 'PT0S', '-PT1S', 'PT0.0001S'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                duration_ms(value)

    def test_every_export_row_uses_its_release_artwork(self):
        _, artwork = build_artwork(ROOT)
        by_release = {r['releaseId']: r for r in artwork['releases']}
        self.assertEqual(len({r['coverPath'] for r in by_release.values()}), len(by_release))
        for row in build_catalog(ROOT)['rows']:
            image = by_release[row['release_id']]
            self.assertEqual(row['catalog_id'], image['catalogId'])
            self.assertEqual(row['cover_path'], image['coverPath'])
            self.assertEqual(row['upc'], image['upc'])


class ArtworkSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'releases').mkdir()
        (self.root / 'assets/covers/by-release').mkdir(parents=True)
        self.single_path = self.root / 'releases/studio-singles.jsonld'
        self.graph = {'@graph': [
            {'@id': 'album', '@type': 'MusicAlbum', 'name': 'Original title'},
            {'@id': 'release', '@type': 'MusicRelease', 'releaseOf': {'@id': 'album'},
             'identifier': [{'propertyID': 'TARRAF Catalog Release ID', 'value': 'SNG-001'},
                            {'propertyID': 'UPC', 'value': '199326055495'}]},
        ]}
        self.single_path.write_text(json.dumps(self.graph))
        (self.root / 'releases/live-trilogy.jsonld').write_text('{"@graph": []}')
        self.image = self.root / target_path('SNG-001')
        self.image.write_bytes((ROOT / target_path('SNG-001')).read_bytes())

    def test_replacement_and_title_change_flow_from_sources_without_copying_images(self):
        before, _ = build_artwork(self.root)
        replacement = (ROOT / target_path('SNG-002')).read_bytes()
        self.image.write_bytes(replacement)
        self.graph['@graph'][0]['name'] = 'Updated title'
        self.single_path.write_text(json.dumps(self.graph))
        after, mapping = build_artwork(self.root)
        self.assertEqual(set(after), {MAP_PATH})
        self.assertNotEqual(before[MAP_PATH], after[MAP_PATH])
        self.assertEqual(mapping['releases'][0]['title'], 'Updated title')
        self.assertEqual(self.image.read_bytes(), replacement)

    def test_missing_image_and_second_directory_are_detected(self):
        self.image.unlink()
        _, mapping = build_artwork(self.root)
        self.assertEqual(mapping['counts']['unmappedReleases'], 1)
        self.assertIsNone(mapping['releases'][0]['coverPath'])
        (self.root / 'assets/covers/archive').mkdir()
        with self.assertRaisesRegex(ValueError, 'duplicate directory'):
            build_artwork(self.root)

    def test_extra_filename_and_duplicate_release_id_are_rejected(self):
        extra = self.image.with_name('cover-999.webp')
        extra.write_bytes(self.image.read_bytes())
        with self.assertRaisesRegex(ValueError, 'Unexpected artwork'):
            build_artwork(self.root)
        extra.unlink()
        duplicate = deepcopy(self.graph['@graph'][1])
        duplicate['@id'] = 'another-release'
        self.graph['@graph'].append(duplicate)
        self.single_path.write_text(json.dumps(self.graph))
        with self.assertRaisesRegex(ValueError, 'Duplicate catalog ID'):
            build_artwork(self.root)


if __name__ == '__main__':
    unittest.main()
