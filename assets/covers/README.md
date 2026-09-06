# TARRAF PRODUCTIONS cover-art archive

This directory preserves the 279 first-party artwork files supplied by TARRAF PRODUCTIONS in a web-ready form.

## Contents

- `archive/cover-001.webp` through `archive/cover-279.webp` — square WebP derivatives, maximum 1200 × 1200 px, quality 84.
- `manifest.json` — stable cover IDs, original OneDrive filenames, repository paths, dimensions, byte sizes, and SHA-256 checksums.

## Website integration

The stable lookup key is `coverId` (`COV-001` through `COV-279`). Import `manifest.json`, then resolve the relative `path` field from the repository root.

The archive is intentionally indexed in the source folder's displayed order. Most supplied source filenames are camera-generated names such as `IMG_*.JPG` or `photo-output *.PNG`; therefore release-to-cover associations are not guessed. Add a verified `catalogId` association only after the artwork has been visually matched to the canonical release register in [`releases/studio-singles.jsonld`](../../releases/studio-singles.jsonld) or to the live-trilogy entities.

## Rights

All artwork remains © TARRAF PRODUCTIONS. No reuse license is granted by its presence in this repository.
