#!/usr/bin/env python3
"""Generate the byte-exact scientific-data freeze manifest for CHD v1.0."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "release" / "v1_data_manifest.json"
FREEZE_ID = "CHD-v1-data-2026-08-21"
VERSION = "1.0.0"

DATA_ROOTS = (
    "data/lexicon/articles",
    "data/lexicon/candidates",
    "data/lexicon/review",
    "data/grammar",
)
ALLOWED_SUFFIXES = {".json", ".jsonl", ".csv"}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect_files() -> list[Path]:
    files: list[Path] = []
    for relative_root in DATA_ROOTS:
        root = ROOT / relative_root
        if not root.is_dir():
            raise SystemExit(f"missing v1 data root: {relative_root}")
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in ALLOWED_SUFFIXES:
                files.append(path)
    files = sorted(set(files), key=lambda p: p.relative_to(ROOT).as_posix())
    if not files:
        raise SystemExit("v1 data freeze selected no files")
    return files


def root_label(relative: str) -> str:
    for data_root in DATA_ROOTS:
        if relative == data_root or relative.startswith(data_root + "/"):
            return data_root
    raise SystemExit(f"file escaped configured data roots: {relative}")


def build_manifest() -> dict[str, Any]:
    files = collect_files()
    records: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    bytes_by_root: Counter[str] = Counter()
    for path in files:
        relative = path.relative_to(ROOT).as_posix()
        size = path.stat().st_size
        label = root_label(relative)
        counts[label] += 1
        bytes_by_root[label] += size
        records.append({
            "path": relative,
            "bytes": size,
            "sha256": sha256_file(path),
        })

    manifest: dict[str, Any] = {
        "freezeId": FREEZE_ID,
        "project": "Cahíta Histórico Digital",
        "sourceId": "ALC1737",
        "version": VERSION,
        "scope": "byte-exact canonical and editorial scientific data selected for v1.0",
        "derivedArtifactsIncluded": False,
        "facsimileIncluded": False,
        "thirdPartyReproductionsRelicensed": False,
        "humanVerificationInferred": False,
        "dataRoots": list(DATA_ROOTS),
        "allowedSuffixes": sorted(ALLOWED_SUFFIXES),
        "fileCount": len(records),
        "totalBytes": sum(int(item["bytes"]) for item in records),
        "fileCountByRoot": {root: int(counts[root]) for root in DATA_ROOTS},
        "bytesByRoot": {root: int(bytes_by_root[root]) for root in DATA_ROOTS},
        "files": records,
        "evolutionPolicy": {
            "silentChangesAllowedUnderSameFreezeId": False,
            "postV1ScientificDataChangesRequireNewVersionOrExplicitFreeze": True,
            "derivedOutputsRemainRebuildableFromVersionedInputs": True,
        },
    }
    return manifest


def write_manifest(output: Path) -> dict[str, Any]:
    manifest = build_manifest()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    manifest = write_manifest(args.output)
    print(
        "generated v1 scientific-data freeze: "
        f"files={manifest['fileCount']}; bytes={manifest['totalBytes']}; "
        f"roots={manifest['fileCountByRoot']}; humanVerificationInferred=false"
    )


if __name__ == "__main__":
    main()
