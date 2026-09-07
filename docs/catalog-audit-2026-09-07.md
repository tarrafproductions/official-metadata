# Catalog metadata audit — September 7, 2026

The 275 observed single products and all 64 live-album track positions now have
ISRCs and durations. The neutral CSV/JSON export links every recording appearance
to its release UPC. The scope is the supplied canonical catalog; this audit does
not establish registration in an external database.

| Check | Before | After |
| --- | ---: | ---: |
| Single products with UPC and release date | 275 / 275 | 275 / 275 |
| Single recordings with ISRC | 275 / 275 | 275 / 275 |
| Single recordings with duration | 99 / 275 | 275 / 275 |
| Live track positions with ISRC and duration | 0 / 64 | 64 / 64 |
| Stable identities for live track positions | 0 / 64 | 64 / 64 |
| Recording appearances in a unified export | 0 | 339 |

## Changes

- Added 176 missing single durations using **exact ISRC matches** in the Apple
  Music catalog, retaining source millisecond precision.
- Added 80 same-recording platform titles as `alternateName` and 191 exact
  reference URLs to single recordings. Canonical owner-supplied titles, artist
  credits, release dates and existing identifiers were retained.
- Added 63 live recording definitions with stable IDs, ISRC, duration, principal
  artist links and reciprocal album links. The 64th position references the
  existing `Still Yours (LIVE)` recording, `QT3FE2691958`, originally released on
  June 21, 2026, under UPC `883369720266` and reused on Vol. III, UPC `882321270177`.
- Recomputed live album durations from their track durations: Vol. I
  `PT1H39M56.72S`, Vol. II `PT1H40M21.019S`, Vol. III `PT1H23M50.8S`.
  Vol. III source durations are rounded to whole seconds except the existing
  single; the total reflects that mixed source precision.
- Added the Apple Music Vol. II album link after matching UPC `882197185506`.
- Corrected catalog descriptions: the standalone singles register includes
  studio, remix and live releases. The existing filename is retained for stable
  integrations.
- Added deterministic CSV/JSON exports and automated checks for ISRC identity,
  UPC check digits, positive duration, ordered track positions, reciprocal album
  links, live duration totals and stale exports.

The combined graph contains **338 distinct recording identities/ISRCs**, appearing
in **339 release-track rows** across **278 release UPCs**. Album appearances do not
create new masters. All existing entity IDs, producer credits and canonical
performance credits are preserved.

## Evidence

- [`apple-music-observations-2026-09-07.json`](../sources/apple-music-observations-2026-09-07.json)
  contains selected public source metadata only. Live Vol. I/II matches require
  album identity, position and title together. Fuzzy search results with other
  ISRCs were rejected.
- [`live-vol-iii-owner-metadata-2026-09-07.json`](../sources/live-vol-iii-owner-metadata-2026-09-07.json)
  extracts public identifiers and durations from the supplied earlier register
  and prepared ingest worksheet. All 19 ISRC/UPC pairs agree between them.
  This is owner-supplied prerelease metadata, not proof of platform availability
  or SoundExchange acceptance. Vol. III remains scheduled for September 25.
- [`catalog-enrichment-audit-2026-09-07.json`](../sources/catalog-enrichment-audit-2026-09-07.json)
  records individual changes and platform differences against the baseline
  commit `3f2792d248b3ca86cfbf143bbade7a7b4e347f78`.
- Existing September 4 DistroKid evidence remains the source for its 59
  reconciled single products.

## Outstanding reconciliation

Thirty sampled single recordings have an artist-credit, release-date or existing
duration difference between the owner-supplied catalog and Apple Music. Some are
display conventions such as omitted featured artists; they are not all proven
errors. The exact differences are recorded in the enrichment audit. Owner-supplied
canonical credits and dates were retained. Apple Music additionally lists Lezzy
on some live tracks; the source observations retain that display credit for
reconciliation, while the graph retains the owner-supplied principal artists.

The earlier identifier workbook also contains **17 distinct ISRC/UPC pairs**
outside the canonical product set: 15 additional ISRCs and two additional UPC
appearances of already known ISRCs. They are recorded in
[`historical-identifier-review-2026-09-07.json`](../sources/historical-identifier-review-2026-09-07.json).
Current release status and release dates are not confirmed by that workbook.
They must not be merged into similarly named masters or declared active/deleted
without distributor evidence. They are excluded from the current export pending
reconciliation.

No data was submitted to MusicBrainz, SoundExchange, GS1 or other external music
databases as part of this GitHub correction.
