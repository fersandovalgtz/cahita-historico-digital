#!/usr/bin/env python3
"""Inspect one page of the canonical ALC1737 v0.2 candidate inventory.

The repository stores the canonical JSONL as deterministic gzip data encoded in
ordered base64 shards. This utility reconstructs that inventory in memory and
prints a page-scoped view without altering the canonical representation.
"""
from __future__ import annotations

import argparse
import base64
import gzip
import json
from pathlib import Path


def load_rows(candidate_dir: Path) -> list[dict]:
    manifest = json.loads((candidate_dir / "candidate_inventory_manifest.json").read_text(encoding="utf-8"))
    encoded = b"".join((candidate_dir / part["filename"]).read_bytes() for part in manifest["parts"])
    payload = gzip.decompress(base64.b64decode(encoded, validate=True))
    rows = [json.loads(line) for line in payload.splitlines() if line.strip()]
    if len(rows) != manifest["candidateCount"]:
        raise SystemExit(f"candidate count mismatch: {len(rows)} != {manifest['candidateCount']}")
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate-dir", type=Path, default=Path("data/lexicon/candidates"))
    ap.add_argument("--page", type=int, required=True)
    ap.add_argument("--column", choices=["left", "right"], default=None)
    ap.add_argument("--count-only", action="store_true")
    args = ap.parse_args()

    rows = [r for r in load_rows(args.candidate_dir) if r.get("sourcePageDigital") == args.page]
    if args.column is not None:
        rows = [r for r in rows if r.get("column") == args.column]

    if args.count_only:
        print(len(rows))
        return

    for row in rows:
        print(json.dumps(row, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
