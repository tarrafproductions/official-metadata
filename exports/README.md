# Catalog exports

Download [`catalog.csv`](catalog.csv) for a flat table or [`catalog.json`](catalog.json)
for typed data and array fields. Both files are generated from the canonical
JSON-LD and checked against it in CI.

The export contains **339 recording appearances, 338 distinct ISRCs and 278
release UPCs**: 275 standalone single products plus 64 ordered track positions
across three live albums. `Still Yours (LIVE)` appears on its original single and
Vol. III with the same recording ID and ISRC. It must not be registered as a new
recording for the album appearance.

| Field | Meaning |
| --- | --- |
| `recording_id` / `isrc` | Stable recording identity / assigned ISRC |
| `recording_title` | Owner-supplied canonical title |
| `recording_alternate_titles` | Same-ISRC platform titles, without replacing the canonical title |
| `recording_artist_credit` | Catalog performance credit; never a songwriter or ownership inference |
| `duration_ms` / `duration_iso8601` | Duration in milliseconds / Schema.org-compatible ISO 8601 |
| `release_id` / `upc` | Release identity / barcode; several rows can share a release UPC |
| `release_date` / `release_status` | Product date and stated availability status |
| `track_number` | One-based position on the release |
| `musicbrainz_release_id` | Existing linked release MBID; blank when absent |
| `reference_urls` | Exact source/catalog links associated with the recording |

CSV is UTF-8 with every cell quoted. Import UPC and ISRC columns as **text**;
spreadsheet programs can still coerce quoted identifiers into numbers. Array
fields contain JSON arrays inside the CSV cells. JSON keeps identifiers as
strings and durations/track positions as numbers.

These are neutral catalog exports, not a universal registry import template.
SoundExchange, MusicBrainz and other recipients have their own mappings and
submission requirements. No writer split, ownership percentage, collection
territory or registration acceptance is asserted by this export. Vol. III remains
scheduled for September 25, 2026, as of the September 7 audit.

Rebuild after editing canonical JSON-LD:

```sh
python3 .github/scripts/validate_jsonld.py
python3 .github/scripts/export_catalog.py
python3 .github/scripts/export_catalog.py --check
```

Source coverage and outstanding discrepancies are documented in
[`docs/catalog-audit-2026-09-07.md`](../docs/catalog-audit-2026-09-07.md).
