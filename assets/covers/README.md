# TARRAF PRODUCTIONS cover-art archive

This directory preserves 282 first-party artwork files supplied by TARRAF PRODUCTIONS: the original 279 files and three additional covers supplied by the catalog owner on September 10, 2026. All 275 singles and three live albums now have verified artwork.

## Contents

- `archive/cover-001.webp` through `archive/cover-279.webp` — square WebP derivatives, maximum 1200 × 1200 px, quality 84.
- `archive/cover-280.webp` through `archive/cover-282.webp` — the three owner-supplied additions, converted from the supplied 800 × 800 JPEGs to lossless WebP with identical decoded RGB pixels.
- `manifest.json` — stable cover IDs, original OneDrive filenames, repository paths, dimensions, byte sizes, and SHA-256 checksums.
- `by-release/cover-NNN.webp` — verified single artwork whose number matches `SNG-NNN`. These are exact copies of the corresponding archive files.
- `by-release/live-vol-i.webp`, `live-vol-ii.webp`, `live-vol-iii.webp` — verified live album artwork.
- `release-map.json` — explicit links from catalog IDs, release identities and UPCs to artwork, including verification evidence and unresolved entries.

## Website integration

Import `release-map.json` and join each release by `catalogId`, `releaseId` or UPC. Resolve its `coverPath` relative to the same pinned repository snapshot. Use a placeholder when the status is `needs-review` and `coverPath` is null.

The archive retains its original source order. `archive/cover-004.webp` is COV-004, which depicts SNG-020; `by-release/cover-004.webp` is the verified artwork for SNG-004 (VVERH VNIZ), copied from COV-029. Do not use the archive number as a release ID.

See the [complete mapping](../../docs/cover-mapping.md) and the [review record](../../docs/cover-review-needed.md). All archive files are preserved, including four duplicate or alternate files.

## Maintaining the mapping

Record supported associations in [`sources/cover-art-review-2026-09-10.json`](../../sources/cover-art-review-2026-09-10.json), then run:

```sh
python3 .github/scripts/build_cover_mapping.py
python3 .github/scripts/build_cover_mapping.py --check --require-complete
```

The generator validates archive checksums, release identities, assigned filenames and generated documentation. CI requires complete coverage, so adding a release without a verified cover fails validation.

## Rights

All artwork remains © TARRAF PRODUCTIONS. No reuse license is granted by its presence in this repository.
