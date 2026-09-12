# TARRAF PRODUCTIONS — Official Metadata

[![Validate JSON-LD](https://github.com/tarrafproductions/official-metadata/actions/workflows/validate-jsonld.yml/badge.svg?branch=main&event=push)](https://github.com/tarrafproductions/official-metadata/actions/workflows/validate-jsonld.yml)

**Latest tagged release:** [v1.0.0 — TARRAF PRODUCTIONS Official Metadata](https://github.com/tarrafproductions/official-metadata/releases/tag/v1.0.0)

Official, version-controlled identity, project, and catalog metadata for **TARRAF PRODUCTIONS®** and its creative universe.

## Purpose

This repository provides a consistent public reference for:

- canonical names and stable entity identifiers;
- official links and external authority records;
- machine-readable JSON-LD for websites and technical integrations;
- structured documentation for music, live, visual, and narrative projects;
- future catalog preservation and metadata auditing.

The repository is a source of truth and a version history. Publishing JSON-LD here does **not** by itself guarantee a Google Knowledge Panel, rich result, ranking change, or automatic ingestion by any search or AI system. Structured data must also be implemented on the relevant public website pages and must accurately match their visible content.

## Core entities

| Entity | Schema.org type | Stable identifier |
| --- | --- | --- |
| TARRAF PRODUCTIONS | `Organization` | `https://aliktarraf.com/#tarraf-productions` |
| Alik Tarraf | `Person` | `https://aliktarraf.com/#alik-tarraf` |
| Marina Tarraf | `Person` | `https://aliktarraf.com/#marina-tarraf` |

## Files

- [`catalog.jsonld`](catalog.jsonld) — machine-readable catalog and distribution index for all published JSON-LD datasets.
- [`entities/core.jsonld`](entities/core.jsonld) — connected JSON-LD graph for the organization, Alik Tarraf, and Marina Tarraf.
- [`entities/creative-universe.jsonld`](entities/creative-universe.jsonld) — connected JSON-LD graph for Epic Evolution Music, TARRAF LIVE SHOW, TARRAF PRODUCTIONS LIVE, TARRAF EPIC CHOIR, and OBARABO.
- [`releases/live-trilogy.jsonld`](releases/live-trilogy.jsonld) — linked JSON-LD graph for the TARRAF PRODUCTIONS LIVE recording event, its three albums, and their digital releases.
- [`releases/live-tracklists.jsonld`](releases/live-tracklists.jsonld) — official ordered track lists for all three TARRAF PRODUCTIONS LIVE volumes (64 recordings in total).
- [`releases/studio-singles.jsonld`](releases/studio-singles.jsonld) — verified canonical register of 275 digital single releases and their 275 recordings, including studio, remix and live singles, with stable internal identifiers and ISRC values.
- [`sources/distrokid-dashboard-observations-2026-09-04.json`](sources/distrokid-dashboard-observations-2026-09-04.json) — first-party DistroKid evidence and reconciled identifiers for the 59 releases added as SNG-217 through SNG-275.
- [`sources/distrokid-reconciliation-observations-2026-09-07.json`](sources/distrokid-reconciliation-observations-2026-09-07.json) — selected public facts from 23 additional DistroKid screenshots, including exact artist strings and explicit visibility limits.
- [`docs/discography.md`](docs/discography.md) — human-readable discography register with documented coverage and source provenance.
- [`docs/live-production-credits.md`](docs/live-production-credits.md) — verified production-credit matrix for the Fujairah recording event, live trilogy, and 64 recordings.
- [`docs/website-integration.md`](docs/website-integration.md) — implementation contract for multilingual Vite/React pages, pre-rendering, canonical URLs, `hreflang`, and JSON-LD.
- [`assets/covers/release-map.json`](assets/covers/release-map.json) — generated artwork index; current images exist only in `assets/covers/by-release/`, with filenames matching release IDs.

The first-party DistroKid catalog evidence supplied on 2026-09-04 confirms 275 standalone single products. The canonical JSON-LD register now covers all 275 observed products; the 59 formerly pending items were reconciled from verified release dates, UPCs, ISRCs, durations, and explicit-content statuses. Missing values are never inferred.

Current artwork is stored only in `assets/covers/by-release/`. For example, `cover-004.webp` belongs to `SNG-004`. Previous versions are available in Git history. See the [artwork editing rules](assets/covers/README.md) and [September 12 correction note](docs/catalog-corrections-2026-09-12.md).

## One source per topic

Edit current entity and release data in their canonical JSON-LD graphs. Edit images only in `assets/covers/by-release/`. The artwork index, JSON/CSV exports and marked discography table are generated views of those inputs and must never be edited by hand. Historical `sources/` records document evidence as of their stated dates; they do not override current data. The permanent [repository rules](AGENTS.md) define the update commands.

## Unified catalog export

The [CSV](exports/catalog.csv) and [JSON](exports/catalog.json) exports contain 339 recording appearances across 278 release UPCs, representing 338 distinct ISRCs. All 275 single recordings and all 64 live track positions have durations. `Still Yours (LIVE)` reuses one recording identity across its single and Vol. III album appearance.

See the [export format](exports/README.md) and [September 7 metadata audit](docs/catalog-audit-2026-09-07.md) for the initial enrichment evidence. The [DistroKid follow-up](docs/distrokid-reconciliation-2026-09-07.md) reconciles 23 screenshots and owner clarifications: five exact artist credits corrected, four Marina primary-artist credits confirmed, APOCALYPSE recorded as owner-reported deleted, and AKFA EMPIRE linked as a same-master reupload. Of 17 historical identifier pairs, 15 still lack an owner-confirmed disposition; all 17 remain outside the current export. The exports provide catalog data for recipient-specific mapping; they do not assert an external registration or rights claim.

## Validation

Every JSON-LD or validator change is checked automatically on pull requests and
matching pushes. Validation covers UTF-8 JSON syntax, Schema.org context,
graph-node structure, unique entity definitions, internal `@id` references,
catalog coverage of every published dataset, complete recording identifiers and durations, UPC check digits, live track ordering and totals, and exact agreement between the graph and generated exports.

## Data principles

1. Include only public, verified, and current information.
2. Reuse the same names, URLs, identifiers, and descriptions across official platforms.
3. Never publish passwords, recovery codes, private addresses, private telephone numbers, contracts, or unpublished personal data.
4. Record meaningful changes through clear commit messages.
5. Treat MusicBrainz, ISNI, DSP, and other external identifiers as references—not as substitutes for the official source.

## Implementation note

The JSON-LD follows [Schema.org](https://schema.org/) vocabulary. Google recommends JSON-LD when structured data is implemented on a website, but does not guarantee any specific search appearance even when markup is valid. Website implementations should be tested and kept consistent with visible page content.

## Rights

Unless a file contains an explicit license stating otherwise, no license is granted for reuse of music, recordings, lyrics, artwork, trademarks, brand materials, or original concepts. Factual identifiers may be referenced for accurate identification and attribution.

---

**TARRAF PRODUCTIONS® · EPIC EVOLUTION MUSIC**

© 2025–2026 TARRAF PRODUCTIONS. All rights reserved.
