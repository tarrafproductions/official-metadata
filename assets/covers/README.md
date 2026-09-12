# Release artwork

The only current image source is `by-release/`. Replace the existing file in place:

- `SNG-NNN` → `by-release/cover-NNN.webp`.
- `LIVE-I`, `LIVE-II`, `LIVE-III` → `by-release/live-vol-i.webp`, `live-vol-ii.webp`, `live-vol-iii.webp`.

Numbers identify releases, never upload order. Check the title and version before replacing a cover. Git history contains previous artwork and its review evidence; there is no second image directory or manual association list.

`release-map.json` is a generated integration index. Its release identities, titles and UPCs come from canonical JSON-LD. Paths follow the rule above; SHA-256 and byte size are read directly from each image. Never edit this index by hand. The generator never writes an image.

After replacing a cover or editing the canonical catalog:

```sh
python3 .github/scripts/build_cover_mapping.py --require-complete
python3 .github/scripts/export_catalog.py
```

CI checks missing files, unexpected copies, file containers, current checksums, catalog identities and reproducible outputs. The retained `verified` status represents the reviewed association; automated checks validate file integrity and correspondence, not the text depicted in an image.

For the website, `exports/catalog.json` supplies `catalog_id` and `cover_path` on every recording appearance. The compatible `release-map.json` fields `catalogId`, `releaseId`, `title`, `upc`, `status`, `coverPath` and `sha256` remain available. Schema version 2 removes archive IDs, archive paths, repeated verification lists and archive counts. Resolve all paths from one pinned repository commit.

All artwork remains © TARRAF PRODUCTIONS. No reuse license is granted by its presence in this repository.
