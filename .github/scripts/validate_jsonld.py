#!/usr/bin/env python3
"""Validate the repository's JSON-LD syntax and graph integrity."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import date
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
LIVE_EVENT_ID = "https://aliktarraf.com/#tarraf-live-recording-2026-06-08"
LIVE_SERIES_ID = "https://aliktarraf.com/#tarraf-productions-live"
LIVE_ALBUM_IDS = (
    "https://aliktarraf.com/#tarraf-productions-live-vol-i-the-opening",
    "https://aliktarraf.com/#tarraf-productions-live-vol-ii-the-fire",
    "https://aliktarraf.com/#tarraf-productions-live-vol-iii-the-encore",
)
MARINA_TARRAF_ID = "https://aliktarraf.com/#marina-tarraf"
EXPECTED_LIVE_PRODUCERS = {
    "https://aliktarraf.com/#tarraf-productions",
    "https://aliktarraf.com/#alik-tarraf",
    "Manik Bhatheja",
    "Ivan Dolhopiat",
    "Ihor Kvilinskyi",
    "Waleed Robbie",
    "Nazarii Storozhuk",
}
EXPECTED_ALBUM_CREDIT_TEXT = {
    "Producer and recording engineer: Alik Tarraf",
    "Executive producer: Manik Bhatheja",
    "Producers: Ivan Dolhopiat, Ihor Kvilinskyi, Waleed Robbie, and Nazarii Storozhuk",
    "Production and recording: TARRAF PRODUCTIONS",
}
STUDIO_SINGLES_PATH = Path("releases/studio-singles.jsonld")
STUDIO_SINGLE_MINIMUM = 216
STUDIO_UPC_MINIMUM = 216
CATALOG_RELEASE_ID_PREFIX = "https://aliktarraf.com/#catalog-sng-"
CATALOG_RECORDING_ID_PREFIX = "https://aliktarraf.com/#catalog-trk-"
ISRC_PATTERN = re.compile(r"^[A-Z]{2}[A-Z0-9]{3}[0-9]{7}$")
UPC_PATTERN = re.compile(r"^[0-9]{12,14}$")
RELEASE_DATE_PATTERN = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
FORBIDDEN_PUBLIC_VALUES = {"690", "Needs verification"}


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


def relation_party_keys(value: Any) -> set[str]:
    """Return stable identifiers or names from a Person/Organization relation."""
    items = value if isinstance(value, list) else [value]
    keys: set[str] = set()

    for item in items:
        if not isinstance(item, dict):
            continue
        identifier = item.get("@id")
        name = item.get("name")
        if isinstance(identifier, str):
            keys.add(identifier)
        elif isinstance(name, str):
            keys.add(name)

    return keys


def validate_live_production_graph(nodes: dict[str, dict[str, Any]]) -> list[str]:
    """Protect the verified TARRAF PRODUCTIONS LIVE production-credit contract."""
    errors: list[str] = []
    event = nodes.get(LIVE_EVENT_ID)

    if event is None:
        errors.append(f"Missing live recording event definition: {LIVE_EVENT_ID}")
    elif relation_party_keys(event.get("director")) != {MARINA_TARRAF_ID}:
        errors.append(
            "The Fujairah live recording event must identify Marina Tarraf "
            "as director"
        )

    for identifier in (LIVE_SERIES_ID, *LIVE_ALBUM_IDS):
        node = nodes.get(identifier)
        if node is None:
            errors.append(f"Missing live production work definition: {identifier}")
            continue

        actual_producers = relation_party_keys(node.get("producer"))
        if actual_producers != EXPECTED_LIVE_PRODUCERS:
            missing = sorted(EXPECTED_LIVE_PRODUCERS - actual_producers)
            unexpected = sorted(actual_producers - EXPECTED_LIVE_PRODUCERS)
            errors.append(
                f"{identifier}: production team mismatch; "
                f"missing={missing}, unexpected={unexpected}"
            )

        if identifier in LIVE_ALBUM_IDS:
            credit_text = node.get("creditText")
            actual_credit_text = (
                set(credit_text) if isinstance(credit_text, list) else set()
            )
            if not EXPECTED_ALBUM_CREDIT_TEXT.issubset(actual_credit_text):
                missing = sorted(EXPECTED_ALBUM_CREDIT_TEXT - actual_credit_text)
                errors.append(
                    f"{identifier}: missing verified production credit text: {missing}"
                )

    return errors


def property_values(node: dict[str, Any], property_id: str) -> list[str]:
    """Return PropertyValue values matching a propertyID."""
    identifiers = node.get("identifier", [])
    items = identifiers if isinstance(identifiers, list) else [identifiers]
    return [
        item["value"]
        for item in items
        if isinstance(item, dict)
        and item.get("@type") == "PropertyValue"
        and item.get("propertyID") == property_id
        and isinstance(item.get("value"), str)
    ]


def is_valid_gtin(value: str) -> bool:
    """Validate a 12–14 digit GTIN, including its check digit."""
    if not UPC_PATTERN.fullmatch(value):
        return False

    payload = reversed(value[:-1])
    total = sum(
        int(digit) * (3 if offset % 2 == 0 else 1)
        for offset, digit in enumerate(payload)
    )
    return (-total) % 10 == int(value[-1])


def is_valid_release_date(value: Any) -> bool:
    """Require a real ISO 8601 calendar date."""
    if not isinstance(value, str) or not RELEASE_DATE_PATTERN.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_studio_singles(document: Any) -> list[str]:
    """Validate the public studio-single register without inventing source gaps."""
    errors: list[str] = []
    if not isinstance(document, dict) or not isinstance(document.get("@graph"), list):
        return [f"{STUDIO_SINGLES_PATH}: expected an @graph array"]

    graph = document["@graph"]
    albums = [
        node
        for node in graph
        if isinstance(node, dict)
        and node.get("@type") == "MusicAlbum"
        and str(node.get("@id", "")).startswith(CATALOG_RELEASE_ID_PREFIX)
        and not str(node.get("@id", "")).endswith("-digital-release")
    ]
    releases = [
        node
        for node in graph
        if isinstance(node, dict)
        and node.get("@type") == "MusicRelease"
        and str(node.get("@id", "")).startswith(CATALOG_RELEASE_ID_PREFIX)
    ]
    recordings = [
        node
        for node in graph
        if isinstance(node, dict)
        and node.get("@type") == "MusicRecording"
        and str(node.get("@id", "")).startswith(CATALOG_RECORDING_ID_PREFIX)
    ]

    counts = {
        "single release works": len(albums),
        "digital releases": len(releases),
        "studio recordings": len(recordings),
    }
    for label, count in counts.items():
        if count < STUDIO_SINGLE_MINIMUM:
            errors.append(
                f"{STUDIO_SINGLES_PATH}: expected at least "
                f"{STUDIO_SINGLE_MINIMUM} {label}, found {count}"
            )
    if len(set(counts.values())) != 1:
        errors.append(
            f"{STUDIO_SINGLES_PATH}: release/recording layer counts differ: {counts}"
        )

    for node in [*albums, *releases, *recordings]:
        identifier = node.get("@id", "<missing @id>")
        if not is_valid_release_date(node.get("datePublished")):
            errors.append(f"{identifier}: missing or invalid datePublished")

    isrcs: list[str] = []
    for node in recordings:
        identifier = node.get("@id", "<missing @id>")
        isrc = node.get("isrcCode")
        if not isinstance(isrc, str) or not ISRC_PATTERN.fullmatch(isrc):
            errors.append(f"{identifier}: missing or invalid isrcCode")
        else:
            isrcs.append(isrc)
        if not node.get("name") or not node.get("byArtist"):
            errors.append(f"{identifier}: recording requires name and byArtist")

    if len(isrcs) != len(set(isrcs)):
        errors.append(f"{STUDIO_SINGLES_PATH}: duplicate ISRC values found")

    upcs: list[str] = []
    for node in releases:
        identifier = node.get("@id", "<missing @id>")
        if not node.get("releaseOf") or not node.get("recordLabel"):
            errors.append(f"{identifier}: release requires releaseOf and recordLabel")
        node_upcs = property_values(node, "UPC")
        if len(node_upcs) != 1:
            errors.append(f"{identifier}: release requires exactly one UPC")
        for upc in node_upcs:
            if not is_valid_gtin(upc):
                errors.append(f"{identifier}: invalid UPC format or check digit {upc!r}")
            else:
                upcs.append(upc)

    if len(upcs) != STUDIO_UPC_MINIMUM:
        errors.append(
            f"{STUDIO_SINGLES_PATH}: expected exactly {STUDIO_UPC_MINIMUM} "
            f"verified UPC values, found {len(upcs)}"
        )
    if len(upcs) != len(set(upcs)):
        errors.append(f"{STUDIO_SINGLES_PATH}: duplicate UPC values found")

    for value, location in walk_json(document):
        if isinstance(value, str) and value in FORBIDDEN_PUBLIC_VALUES:
            errors.append(
                f"{STUDIO_SINGLES_PATH}:{location}: forbidden placeholder {value!r}"
            )
        if isinstance(value, str) and "/search" in value:
            errors.append(
                f"{STUDIO_SINGLES_PATH}:{location}: search URL cannot be sameAs evidence"
            )

    return errors


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    documents: dict[Path, Any] = {}
    definitions: dict[str, list[str]] = defaultdict(list)
    definition_nodes: dict[str, dict[str, Any]] = {}
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
                    definition_nodes[identifier] = value

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

    errors.extend(validate_live_production_graph(definition_nodes))
    studio_document = documents.get(STUDIO_SINGLES_PATH)
    if studio_document is None:
        errors.append(f"Missing studio singles dataset: {STUDIO_SINGLES_PATH}")
    else:
        errors.extend(validate_studio_singles(studio_document))

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
