#!/usr/bin/env python3
"""Reconstruct and verify the canonical ALC1737 v0.2 candidate inventory.

The canonical row-level JSONL is stored losslessly as ordered base64 shards of
a deterministic gzip stream because the repository write interface used during
curation accepts UTF-8 text artifacts. This script verifies every representation
before optionally writing the reconstructed JSONL.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--candidate-dir",
        type=Path,
        default=Path("data/lexicon/candidates"),
        help="Directory containing manifest and ordered base64 shards.",
    )
    ap.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional path for reconstructed JSONL. If omitted, verification only.",
    )
    args = ap.parse_args()

    manifest_path = args.candidate_dir / "candidate_inventory_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    encoded_parts: list[bytes] = []
    for part in manifest["parts"]:
        path = args.candidate_dir / part["filename"]
        raw = path.read_bytes()
        if len(raw) != part["chars"]:
            raise SystemExit(
                f"size mismatch for {path}: {len(raw)} != {part['chars']}"
            )
        digest = sha256_bytes(raw)
        if digest != part["sha256"]:
            raise SystemExit(
                f"SHA-256 mismatch for {path}: {digest} != {part['sha256']}"
            )
        encoded_parts.append(raw)

    encoded = b"".join(encoded_parts)
    encoded_digest = sha256_bytes(encoded)
    if encoded_digest != manifest["base64Sha256"]:
        raise SystemExit(
            f"base64 aggregate SHA-256 mismatch: {encoded_digest} != "
            f"{manifest['base64Sha256']}"
        )

    compressed = base64.b64decode(encoded, validate=True)
    gzip_digest = sha256_bytes(compressed)
    if gzip_digest != manifest["gzipSha256"]:
        raise SystemExit(
            f"gzip SHA-256 mismatch: {gzip_digest} != {manifest['gzipSha256']}"
        )

    jsonl = gzip.decompress(compressed)
    jsonl_digest = sha256_bytes(jsonl)
    if jsonl_digest != manifest["jsonlSha256"]:
        raise SystemExit(
            f"JSONL SHA-256 mismatch: {jsonl_digest} != "
            f"{manifest['jsonlSha256']}"
        )

    rows = [line for line in jsonl.splitlines() if line.strip()]
    if len(rows) != manifest["candidateCount"]:
        raise SystemExit(
            f"row-count mismatch: {len(rows)} != {manifest['candidateCount']}"
        )

    parsed_rows = []
    for number, line in enumerate(rows, 1):
        try:
            obj = json.loads(line)
            parsed_rows.append(obj)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSON on reconstructed row {number}: {exc}")

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_bytes(jsonl)

    print(
        "verified canonical candidate inventory: "
        f"{len(rows)} rows; JSONL SHA-256 {jsonl_digest}"
    )
    for obj in parsed_rows:
        if obj.get("sourcePageDigital") == 174:
            print("P174CAND " + json.dumps(obj, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
