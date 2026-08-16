#!/usr/bin/env python3
"""Validate lexical-article JSONL files in Cahíta Histórico Digital.

Checks performed with the Python standard library only:
- every nonblank line is valid JSON;
- every object has a nonempty articleId;
- articleId values are globally unique across data/lexicon/articles/*.jsonl;
- humanVerified=true iff reviewStatus=human_verified.

Exit status is non-zero when any error is found.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTICLES_DIR = ROOT / "data" / "lexicon" / "articles"


def main() -> int:
    errors: list[str] = []
    locations: dict[str, list[str]] = defaultdict(list)
    object_count = 0

    files = sorted(ARTICLES_DIR.glob("*.jsonl"))
    if not files:
        print(f"ERROR: no JSONL files found in {ARTICLES_DIR}", file=sys.stderr)
        return 2

    for path in files:
        with path.open("r", encoding="utf-8") as handle:
            for line_number, raw in enumerate(handle, start=1):
                line = raw.strip()
                if not line:
                    continue
                object_count += 1
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"{path.relative_to(ROOT)}:{line_number}: invalid JSON: {exc}")
                    continue

                article_id = obj.get("articleId")
                if not isinstance(article_id, str) or not article_id:
                    errors.append(f"{path.relative_to(ROOT)}:{line_number}: missing/non-string articleId")
                else:
                    locations[article_id].append(f"{path.relative_to(ROOT)}:{line_number}")

                review_status = obj.get("reviewStatus")
                human_verified = obj.get("humanVerified")
                if human_verified is True and review_status != "human_verified":
                    errors.append(
                        f"{path.relative_to(ROOT)}:{line_number}: humanVerified=true but reviewStatus={review_status!r}"
                    )
                if review_status == "human_verified" and human_verified is not True:
                    errors.append(
                        f"{path.relative_to(ROOT)}:{line_number}: reviewStatus=human_verified but humanVerified is not true"
                    )

    for article_id, refs in sorted(locations.items()):
        if len(refs) > 1:
            errors.append(f"duplicate articleId {article_id}: " + "; ".join(refs))

    print(f"Lexicon QA: {object_count} objects across {len(files)} JSONL files; {len(locations)} unique articleId values.")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} error(s).", file=sys.stderr)
        return 1

    print("OK: JSONL parsing, articleId uniqueness, and human-verification state checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
