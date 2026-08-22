#!/usr/bin/env python3
"""Validate the frozen CHD v1 production data contracts."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from build_v1_contract_manifest import MANIFEST_PATH, build_manifest, serialize

EXPECTED_DIALECT = "https://json-schema.org/draft/2020-12/schema"
EXPECTED_MANIFEST_SHA256 = "c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56"


def main() -> None:
    if not MANIFEST_PATH.is_file():
        raise SystemExit(f"missing frozen v1 contract manifest: {MANIFEST_PATH}")

    frozen_text = MANIFEST_PATH.read_text(encoding="utf-8")
    frozen = json.loads(frozen_text)
    current = build_manifest()
    current_text = serialize(current)

    if frozen != current:
        frozen_by_path = {item["path"]: item for item in frozen.get("contracts", [])}
        current_by_path = {item["path"]: item for item in current.get("contracts", [])}
        added = sorted(set(current_by_path) - set(frozen_by_path))
        removed = sorted(set(frozen_by_path) - set(current_by_path))
        changed = sorted(
            path for path in set(frozen_by_path) & set(current_by_path)
            if frozen_by_path[path] != current_by_path[path]
        )
        raise SystemExit(
            "v1 contract freeze drift detected; "
            f"added={added}; removed={removed}; changed={changed}. "
            "Do not update the frozen manifest silently; a contract change requires an explicit release-scope decision."
        )

    if frozen["schemaContractCount"] != 22 or frozen["sourceScopeMetadataCount"] != 4:
        raise SystemExit("unexpected v1 contract counts")
    if frozen["contractCount"] != 26:
        raise SystemExit("unexpected total v1 contract count")
    if frozen["policy"]["exactBytesFrozenForV1"] is not True:
        raise SystemExit("v1 freeze must require exact bytes")
    if frozen["policy"]["silentContractChangesAllowed"] is not False:
        raise SystemExit("v1 freeze must forbid silent contract changes")
    if frozen["policy"]["releaseIdentityMetadataFrozenHere"] is not False:
        raise SystemExit("release identity metadata must remain assigned to the later tag/release gate")

    schema_items = [item for item in frozen["contracts"] if item["kind"] == "json_schema"]
    ids = [item.get("schemaId") for item in schema_items]
    if any(item.get("schemaDialect") != EXPECTED_DIALECT for item in schema_items):
        raise SystemExit("all frozen v1 JSON Schemas must use Draft 2020-12")
    if any(not value for value in ids) or len(set(ids)) != len(ids):
        raise SystemExit("frozen v1 JSON Schema $id values must be present and unique")

    manifest_sha = hashlib.sha256(frozen_text.encode("utf-8")).hexdigest()
    generated_sha = hashlib.sha256(current_text.encode("utf-8")).hexdigest()
    if manifest_sha != EXPECTED_MANIFEST_SHA256 or generated_sha != EXPECTED_MANIFEST_SHA256:
        raise SystemExit(
            "v1 contract manifest serialization drifted: "
            f"frozen={manifest_sha}; generated={generated_sha}; expected={EXPECTED_MANIFEST_SHA256}"
        )

    print(
        "v1 contract freeze QA OK: "
        f"schemas={frozen['schemaContractCount']}; "
        f"sourceMetadata={frozen['sourceScopeMetadataCount']}; "
        f"contracts={frozen['contractCount']}; "
        f"manifestSha256={manifest_sha}; silentChangesAllowed=false"
    )


if __name__ == "__main__":
    main()
