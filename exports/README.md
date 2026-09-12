# Catalog exports

Download [`catalog.csv`](catalog.csv) for a flat table or [`catalog.json`](catalog.json)
for typed data and array fields. Both files and the marked discography table are generated from the canonical
JSON-LD and checked against it in CI. Never edit generated rows by hand.

The export contains **339 recording appearances, 338 distinct ISRCs and 278
release UPCs**: 275 standalone single products plus 64 ordered track positions
across three live albums. `Still Yours (LIVE)` appears on its original single and
Vol. III with the same recording ID and ISRC. It must not be registered as a new
recording for the album appearance.

| Field | Meaning |
| --- | --- |
| `recording_id` / `isrc` | Stable recording identity / assigned ISRC |
| `recording_title` | Owner-supplied canonical title |
| `recording_alternate_titles` | Verified alternate titles and historical spellings for the same catalog recording |
| `recording_artist_credit` | Exact canonical performance display credit; separators are significant; never a songwriter or ownership inference |
| `recording_artist_ids` | Structured primary-artist IDs; a joint display string links existing people, not a new combined artist |
| `duration_ms` / `duration_iso8601` | Duration in milliseconds / Schema.org-compatible ISO 8601 |
| `catalog_id` / `cover_path` | Release catalog ID (`SNG-NNN` or `LIVE-I`/`LIVE-II`/`LIVE-III`) and the matching file in the sole image directory; repeated album tracks share both values |
| `release_id` / `upc` | Release identity / barcode; several rows can share a release UPC |
| `release_date` / `release_status` | Product date and stated availability status |
| `track_number` | One-based position on the release |
| `musicbrainz_release_id` | Existing linked release MBID; blank when absent |
| `reference_urls` | Exact source/catalog links associated with the recording |

The [DistroKid follow-up](../docs/distrokid-reconciliation-2026-09-07.md) preserves `Alik Tarraf Marina Tarraf` for GODDESS and New World, `Alik Tarraf, Marina Tarraf` for BANINA BANINA YALLA TARRAF and studio STILL YOURS, and `Alik Tarraf` for Sila Lyubvi. The 17 historical identifier pairs are retained in the separate review and excluded from these exports.

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
