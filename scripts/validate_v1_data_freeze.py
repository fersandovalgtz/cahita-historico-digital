#!/usr/bin/env python3
"""Validate the byte-exact CHD v1.0 scientific-data freeze."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from generate_v1_data_freeze import DATA_ROOTS, FREEZE_ID, VERSION, build_manifest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "release" / "v1_data_manifest.json"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if not MANIFEST_PATH.is_file():
        raise SystemExit("missing release/v1_data_manifest.json")
    stored = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    current = build_manifest()

    if stored != current:
        stored_files = {item["path"]: item for item in stored.get("files", [])}
        current_files = {item["path"]: item for item in current.get("files", [])}
        added = sorted(set(current_files) - set(stored_files))
        removed = sorted(set(stored_files) - set(current_files))
        changed = sorted(
            path for path in set(stored_files) & set(current_files)
            if stored_files[path] != current_files[path]
        )
        raise SystemExit(
            "v1 scientific-data freeze drifted: "
            f"added={added[:10]}, removed={removed[:10]}, changed={changed[:10]}"
        )

    if stored.get("freezeId") != FREEZE_ID or stored.get("version") != VERSION:
        raise SystemExit("unexpected v1 data freeze identity")
    if stored.get("dataRoots") != list(DATA_ROOTS):
        raise SystemExit("unexpected v1 data freeze roots")
    if stored.get("derivedArtifactsIncluded") is not False:
        raise SystemExit("derived artifacts must not be frozen as canonical inputs")
    if stored.get("facsimileIncluded") is not False:
        raise SystemExit("third-party facsimile must not be included in data freeze")
    if stored.get("humanVerificationInferred") is not False:
        raise SystemExit("v1 data freeze must not infer human verification")
    if stored.get("fileCount", 0) < 230:
        raise SystemExit(f"unexpectedly small v1 data freeze: {stored.get('fileCount')} files")
    if stored.get("fileCountByRoot", {}).get("data/lexicon/articles") != 211:
        raise SystemExit("v1 freeze must contain exactly 211 canonical lexicon article files")
    if stored.get("fileCountByRoot", {}).get("data/grammar", 0) < 24:
        raise SystemExit("v1 freeze grammar selection is unexpectedly small")

    policy = stored.get("evolutionPolicy", {})
    if policy.get("silentChangesAllowedUnderSameFreezeId") is not False:
        raise SystemExit("silent scientific-data changes must remain forbidden")
    if policy.get("postV1ScientificDataChangesRequireNewVersionOrExplicitFreeze") is not True:
        raise SystemExit("post-v1 data-change policy drifted")

    print(
        "v1 scientific-data freeze QA OK: "
        f"files={stored['fileCount']}; bytes={stored['totalBytes']}; "
        f"manifestSha256={sha256_file(MANIFEST_PATH)}; roots={stored['fileCountByRoot']}; "
        "humanVerificationInferred=false"
    )


if __name__ == "__main__":
    main()
