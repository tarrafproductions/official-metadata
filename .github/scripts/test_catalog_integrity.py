"""Regression checks for master identity, release mapping and export fidelity."""

import csv
import io
import json
import unittest
from copy import deepcopy
from pathlib import Path

from export_catalog import ARRAY_FIELDS, build_catalog, duration_ms, export_contents, walk
from validate_jsonld import validate_recordings_and_tracklists


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


if __name__ == '__main__':
    unittest.main()
