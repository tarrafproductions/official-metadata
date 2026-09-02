# TARRAF PRODUCTIONS LIVE — Production Credits

This document separates recording-event, album, recording, visual-production,
label, and rights roles for the three-part **TARRAF PRODUCTIONS LIVE** project.
It is the human-readable companion to the structured data in
[`entities/creative-universe.jsonld`](../entities/creative-universe.jsonld) and
[`releases/live-trilogy.jsonld`](../releases/live-trilogy.jsonld).

## Project scope

| Level | Official work | Scope |
| --- | --- | ---: |
| Recording event | TARRAF LIVE SHOW — Fujairah Live Recording | June 8, 2026 |
| Volume I | TARRAF PRODUCTIONS LIVE, Vol. I: The Opening | 22 recordings |
| Volume II | TARRAF PRODUCTIONS LIVE, Vol. II: The Fire | 23 recordings |
| Volume III | TARRAF PRODUCTIONS LIVE, Vol. III: The Encore | 19 recordings |
| Full project | TARRAF PRODUCTIONS LIVE | 64 recordings |

## Verified production team

| Entity | Verified credit | Metadata scope |
| --- | --- | --- |
| **Alik Tarraf** | Producer; recording engineer; video producer | Recording event and live recordings |
| **Manik Bhatheja** | Executive producer; executive director; head of dance production | Recording event and live project |
| **Ivan Dolhopiat** | Producer | Live recordings |
| **Ihor Kvilinskyi** | Producer | Live recordings |
| **Waleed Robbie** | Producer | Live recordings |
| **Nazarii Storozhuk** | Producer | Live recordings |
| **Marina Tarraf** | Director; editor; choreography | Recording event and visual production |
| **Smriti Bhatheja** | Creative director; art director | Recording event and visual production |
| **TARRAF PRODUCTIONS** | Production and recording entity; management; record label; ℗ holder | Project, albums, releases, and master recordings |

## Modeling rules

1. `byArtist` and `creditedTo` preserve the published artist credits and are not
   expanded merely because someone holds a production role.
2. `producer` identifies the people and organization that produced each album;
   `creditText` preserves distinctions such as **executive producer** and
   **recording engineer**.
3. Marina Tarraf's `director` relationship is attached to the recording event.
   Her direction and editing are not mislabeled as audio production.
4. TARRAF PRODUCTIONS is represented as producer, record label, and copyright
   holder where those roles are verified. A music-publisher claim is not inferred
   for a work unless the relevant registration or release record states it.
5. Individual-track credits must match the authoritative release and recording
   records before they are expanded beyond the album-level production graph.
