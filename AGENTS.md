# Repository editing rules

- Each entity is defined once in its canonical JSON-LD graph under `entities/` or `releases/`. References use its existing `@id`. Preserve recording identities, UPCs and ISRCs.
- Current cover images exist only in `assets/covers/by-release/`. For `SNG-NNN`, replace `cover-NNN.webp` in place. The three albums use `live-vol-i.webp`, `live-vol-ii.webp`, and `live-vol-iii.webp`. Never add an artwork archive, backup folder, alternate numbering, symlink or duplicate image copy. Git history preserves prior versions.
- The filename and catalog ID determine the association. Never match by array position, source upload order or a second manual mapping list. Check the visual title/version before replacing artwork.
- `assets/covers/release-map.json`, `exports/catalog.json`, `exports/catalog.csv`, and the marked singles table in `docs/discography.md` are generated outputs, not editing sources. Change the canonical graph or image, then regenerate. Do not add another current catalog or mapping table.
- Historical platform observations in `sources/` are evidence as of their stated date, not inputs that override the current canonical catalog. Keep historical identifiers out of the current export unless explicitly reconciled.
- After a catalog or artwork change, run:

  ```sh
  python3 .github/scripts/build_cover_mapping.py --require-complete
  python3 .github/scripts/export_catalog.py
  python3 .github/scripts/validate_jsonld.py
  python3 .github/scripts/build_cover_mapping.py --check --require-complete
  python3 .github/scripts/export_catalog.py --check
  python3 -m unittest discover -s .github/scripts -p 'test_*.py'
  ```

- Keep changes scoped. Do not regenerate or re-upload unchanged image bytes. Report the commit and actual validation outcome. A repository update is not a website deployment.
