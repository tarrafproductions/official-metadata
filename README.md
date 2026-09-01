# TARRAF PRODUCTIONS — Official Metadata

[![Validate JSON-LD](https://github.com/tarrafproductions/official-metadata/actions/workflows/validate-jsonld.yml/badge.svg?branch=main&event=push)](https://github.com/tarrafproductions/official-metadata/actions/workflows/validate-jsonld.yml)

**Current version:** [v1.0.0 — TARRAF PRODUCTIONS Official Metadata](https://github.com/tarrafproductions/official-metadata/releases/tag/v1.0.0)

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
- [`docs/website-integration.md`](docs/website-integration.md) — implementation contract for multilingual Vite/React pages, pre-rendering, canonical URLs, `hreflang`, and JSON-LD.

Planned additions will document individual recordings, release identifiers, and other verified projects.

## Validation

Every JSON-LD or validator change is checked automatically on pull requests and
matching pushes. Validation covers UTF-8 JSON syntax, Schema.org context,
graph-node structure, unique entity definitions, internal `@id` references,
and catalog coverage of every published dataset.

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
