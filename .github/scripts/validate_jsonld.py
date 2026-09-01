#!/usr/bin/env python3
"""Validate the repository's JSON-LD syntax and graph integrity."""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import unquote, urlparse


SCHEMA_CONTEXT = "https://schema.org"
RAW_CONTENT_HOST = "raw.githubusercontent.com"
RAW_CONTENT_REPOSITORY = ("tarrafproductions", "official-metadata")
INTERNAL_ID_PREFIXES = (
    "https://aliktarraf.com/",
    "https://github.com/tarrafproductions/official-metadata",
)


def walk_json(value: Any, location: str = "$") -> Iterator[tuple[Any, str]]:
    """Yield every JSON value together with a readable source location."""
    yield value, location

    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk_json(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_json(child, f"{location}[{index}]")


def has_schema_context(value: Any) -> bool:
    if value == SCHEMA_CONTEXT:
        return True
    return isinstance(value, list) and SCHEMA_CONTEXT in value


def is_absolute_identifier(value: str) -> bool:
    if value.startswith("_:"):
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def repository_path_from_raw_url(value: str) -> str | None:
    """Return a repository path from a branch-, tag-, or commit-pinned raw URL."""
    parsed = urlparse(value)
    parts = [unquote(part) for part in parsed.path.split("/") if part]

    if parsed.netloc != RAW_CONTENT_HOST or len(parts) < 4:
        return None
    if tuple(parts[:2]) != RAW_CONTENT_REPOSITORY:
        return None

    # owner / repository / ref / path...
    return "/".join(parts[3:])


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    documents: dict[Path, Any] = {}
    definitions: dict[str, list[str]] = defaultdict(list)
    references: dict[str, list[str]] = defaultdict(list)
    catalog_paths: list[str] = []

    files = sorted(
        path
        for path in root.rglob("*.jsonld")
        if ".git" not in path.relative_to(root).parts
    )

    if not files:
        return ["No .jsonld files found."]

    for path in files:
        relative_path = path.relative_to(root)
        try:
            with path.open(encoding="utf-8") as source:
                document = json.load(source)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            errors.append(f"{relative_path}: invalid UTF-8 JSON ({error})")
            continue

        documents[relative_path] = document

        if not isinstance(document, dict):
            errors.append(f"{relative_path}: the document root must be an object")
            continue

        if not has_schema_context(document.get("@context")):
            errors.append(
                f"{relative_path}: root @context must include {SCHEMA_CONTEXT}"
            )

        graph = document.get("@graph")
        if graph is not None:
            if not isinstance(graph, list) or not graph:
                errors.append(f"{relative_path}: @graph must be a non-empty array")
            else:
                for index, node in enumerate(graph):
                    location = f"{relative_path}:$['@graph'][{index}]"
                    if not isinstance(node, dict):
                        errors.append(f"{location}: graph node must be an object")
                        continue
                    if "@id" not in node:
                        errors.append(f"{location}: graph node is missing @id")
                    if "@type" not in node:
                        errors.append(f"{location}: graph node is missing @type")
        else:
            if "@id" not in document:
                errors.append(f"{relative_path}: root object is missing @id")
            if "@type" not in document:
                errors.append(f"{relative_path}: root object is missing @type")

        for value, json_location in walk_json(document):
            location = f"{relative_path}:{json_location}"

            if isinstance(value, dict) and "@id" in value:
                identifier = value["@id"]
                if not isinstance(identifier, str) or not identifier.strip():
                    errors.append(f"{location}: @id must be a non-empty string")
                elif not is_absolute_identifier(identifier):
                    errors.append(
                        f"{location}: @id must be an absolute HTTP(S) URL "
                        "or a blank-node identifier"
                    )
                elif set(value) == {"@id"}:
                    references[identifier].append(location)
                else:
                    definitions[identifier].append(location)

            if isinstance(value, dict) and value.get("@type") == "DataDownload":
                content_url = value.get("contentUrl")
                if not isinstance(content_url, str):
                    errors.append(
                        f"{location}: DataDownload.contentUrl must be a string"
                    )
                else:
                    repository_path = repository_path_from_raw_url(content_url)
                    if repository_path is not None:
                        catalog_paths.append(repository_path)

    for identifier, locations in sorted(definitions.items()):
        if len(locations) > 1:
            errors.append(
                f"Duplicate definition for {identifier}: " + ", ".join(locations)
            )

    for identifier, locations in sorted(references.items()):
        if identifier.startswith(INTERNAL_ID_PREFIXES) and identifier not in definitions:
            errors.append(
                f"Unresolved internal @id reference {identifier}: "
                + ", ".join(locations)
            )

    expected_catalog_paths = {
        path.as_posix() for path in documents if path.as_posix() != "catalog.jsonld"
    }
    actual_catalog_paths = set(catalog_paths)

    for missing in sorted(expected_catalog_paths - actual_catalog_paths):
        errors.append(f"catalog.jsonld does not publish {missing}")

    for unknown in sorted(actual_catalog_paths - expected_catalog_paths):
        errors.append(f"catalog.jsonld points to a missing dataset: {unknown}")

    if len(catalog_paths) != len(actual_catalog_paths):
        errors.append("catalog.jsonld contains duplicate dataset distributions")

    if not errors:
        print("JSON-LD validation passed")
        print(f"  Files: {len(documents)}")
        print(f"  Defined @id values: {len(definitions)}")
        print(f"  Internal references checked: {sum(map(len, references.values()))}")
        print(f"  Catalog datasets: {len(actual_catalog_paths)}")

    return errors


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = validate_repository(root)

    if errors:
        print("JSON-LD validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
