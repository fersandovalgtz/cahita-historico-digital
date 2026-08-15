#!/usr/bin/env python3
"""Validate every JSON object in a JSONL file against a JSON Schema."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import jsonschema


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", type=Path, required=True)
    ap.add_argument("--jsonl", type=Path, required=True)
    args = ap.parse_args()

    schema = json.loads(args.schema.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )

    count = 0
    failures = []
    with args.jsonl.open(encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if not line.strip():
                continue
            count += 1
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                failures.append((line_no, f"invalid JSON: {exc}"))
                continue
            for err in validator.iter_errors(obj):
                path = ".".join(str(p) for p in err.absolute_path)
                failures.append((line_no, f"{path}: {err.message}"))

    if failures:
        for line_no, message in failures[:100]:
            print(f"line {line_no}: {message}")
        raise SystemExit(
            f"FAILED: {len(failures)} schema error(s) in {count} record(s)"
        )
    print(f"VALID: {count} record(s)")


if __name__ == "__main__":
    main()
