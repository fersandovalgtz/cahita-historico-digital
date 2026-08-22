#!/usr/bin/env python3
"""Build the deterministic v1 data-contract freeze manifest for CHD.

The manifest freezes production JSON Schemas and source-scope metadata by
SHA-256. Release-identifying metadata such as CITATION.cff, codemeta.json,
version tags and DOI fields is intentionally excluded because it is finalized
at the tag/release gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FREEZE_ID = "CHD-v1-contracts-2026-08-21"
MANIFEST_PATH = ROOT / "release" / "v1_contract_manifest.json"
SOURCE_METADATA_PATHS = [
    "data/source/alc1737/metadata.json",
    "data/source/alc1737/ingest_manifest.json",
    "data/source/alc1737/sections.json",
    "data/source/alc1737/page_manifest.csv",
]


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def record(path: Path, kind: str) -> dict[str, Any]:
    payload = path.read_bytes()
    rel = path.relative_to(ROOT).as_posix()
    item: dict[str, Any] = {
        "path": rel,
        "kind": kind,
        "bytes": len(payload),
        "sha256": sha256_bytes(payload),
    }
    if kind == "json_schema":
        parsed = json.loads(payload.decode("utf-8"))
        if not isinstance(parsed, dict):
            raise SystemExit(f"schema is not a JSON object: {rel}")
        item["schemaDialect"] = parsed.get("$schema")
        item["schemaId"] = parsed.get("$id")
    elif path.suffix == ".json":
        json.loads(payload.decode("utf-8"))
    return item


def build_manifest() -> dict[str, Any]:
    schemas = sorted((ROOT / "schemas").glob("*.schema.json"))
    if not schemas:
        raise SystemExit("no production schemas found")
    records = [record(path, "json_schema") for path in schemas]
    for relative in SOURCE_METADATA_PATHS:
        path = ROOT / relative
        if not path.is_file():
            raise SystemExit(f"missing source-scope metadata contract: {relative}")
        records.append(record(path, "source_scope_metadata"))
    records.sort(key=lambda item: item["path"])

    return {
        "freezeId": FREEZE_ID,
        "status": "release_candidate_contract_freeze",
        "sourceId": "ALC1737",
        "targetRelease": "v1.0.0",
        "policy": {
            "exactBytesFrozenForV1": True,
            "silentContractChangesAllowed": False,
            "postV1ChangesRequireNewFreezeManifest": True,
            "releaseIdentityMetadataFrozenHere": False,
            "releaseIdentityMetadataReason": "CITATION.cff, codemeta.json, version/tag and DOI are finalized at the later tag/release gate.",
        },
        "schemaContractCount": len(schemas),
        "sourceScopeMetadataCount": len(SOURCE_METADATA_PATHS),
        "contractCount": len(records),
        "contracts": records,
    }


def serialize(manifest: dict[str, Any]) -> str:
    return json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stdout", action="store_true")
    parser.add_argument("--output", type=Path, default=MANIFEST_PATH)
    args = parser.parse_args()

    manifest = build_manifest()
    payload = serialize(manifest)
    if args.stdout:
        print(payload, end="")
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload, encoding="utf-8")
    print(
        "built v1 contract manifest: "
        f"schemas={manifest['schemaContractCount']}; "
        f"sourceMetadata={manifest['sourceScopeMetadataCount']}; "
        f"contracts={manifest['contractCount']}; "
        f"sha256={sha256_bytes(payload.encode('utf-8'))}"
    )


if __name__ == "__main__":
    main()
