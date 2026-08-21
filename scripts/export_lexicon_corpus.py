#!/usr/bin/env python3
"""Generate deterministic consolidated exports of historical lexical articles.

The canonical editorial objects remain the JSONL files under
``data/lexicon/articles``. This script creates reproducible *derived* views and
never rewrites those canonical inputs.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARTICLE_DIR = ROOT / "data/lexicon/articles"
PHASE2_SUMMARY = ROOT / "data/lexicon/reconciliation/phase2_open_work_summary.json"

JSONL_NAME = "chd_lexicon_articles.jsonl"
JSON_NAME = "chd_lexicon_articles.json"
CSV_NAME = "chd_lexicon_articles.csv"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "articleId",
    "sourceId",
    "sourcePageDigital",
    "sourcePagePrinted",
    "column",
    "articleType",
    "spanishGuideRaw",
    "sourceGroupingRaw",
    "cahitaFormsRaw",
    "crossReferences",
    "abbreviationsRaw",
    "notesRaw",
    "transcriptionRaw",
    "editorialNote",
    "continuesFromPreviousPage",
    "continuesToNextPage",
    "derivedFromCandidates",
    "sourceSpans",
    "reviewStatus",
    "humanVerified",
    "provenance",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def article_number(article: dict[str, Any]) -> int:
    return int(article["articleId"].rsplit("-", 1)[1])


def load_articles() -> tuple[list[dict[str, Any]], list[str]]:
    articles: list[dict[str, Any]] = []
    source_files: list[str] = []

    for path in sorted(ARTICLE_DIR.glob("*.jsonl")):
        source_files.append(path.relative_to(ROOT).as_posix())
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}:{line_number}: {exc}") from exc
            articles.append(obj)

    ids = [a.get("articleId") for a in articles]
    duplicates = sorted(article_id for article_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        raise SystemExit(f"duplicate articleId values in canonical inputs: {duplicates[:10]}")

    articles.sort(key=article_number)
    return articles, source_files


def expected_article_count() -> int:
    summary = json.loads(PHASE2_SUMMARY.read_text(encoding="utf-8"))
    return int(summary["summary"]["currentCuratorialArticleCount"])


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def csv_value(value: Any) -> Any:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return compact_json(value)
    return value


def write_jsonl(path: Path, articles: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(article) for article in articles) + "\n").encode("utf-8")
    path.write_bytes(data)
    return data


def write_json(path: Path, articles: list[dict[str, Any]]) -> bytes:
    data = (
        json.dumps(articles, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")
    path.write_bytes(data)
    return data


def write_csv(path: Path, articles: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=CSV_FIELDS,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        for article in articles:
            writer.writerow({field: csv_value(article.get(field)) for field in CSV_FIELDS})
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/lexicon-exports",
        help="Directory for derived exports (default: build/lexicon-exports).",
    )
    parser.add_argument(
        "--allow-count-mismatch",
        action="store_true",
        help="Do not fail when canonical article count differs from Phase II summary.",
    )
    args = parser.parse_args()

    articles, source_files = load_articles()
    expected = expected_article_count()
    if len(articles) != expected and not args.allow_count_mismatch:
        raise SystemExit(
            f"article-count mismatch: canonical inputs contain {len(articles)} objects; "
            f"Phase II summary declares {expected}"
        )

    args.out_dir.mkdir(parents=True, exist_ok=True)

    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, articles),
        JSON_NAME: write_json(args.out_dir / JSON_NAME, articles),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, articles),
    }

    review_status_counts = Counter(str(a.get("reviewStatus")) for a in articles)
    human_verified_count = sum(bool(a.get("humanVerified")) for a in articles)

    manifest = {
        "sourceId": "ALC1737",
        "dataset": "historical_lexical_articles",
        "derivation": "deterministic export from data/lexicon/articles/*.jsonl",
        "canonicalInputPattern": "data/lexicon/articles/*.jsonl",
        "canonicalInputFileCount": len(source_files),
        "articleCount": len(articles),
        "expectedArticleCountFromPhase2Summary": expected,
        "sortOrder": "numeric articleId ascending",
        "humanVerifiedCount": human_verified_count,
        "reviewStatusCounts": dict(sorted(review_status_counts.items())),
        "deterministic": True,
        "formats": {
            name: {
                "bytes": len(data),
                "sha256": sha256_bytes(data),
            }
            for name, data in sorted(payloads.items())
        },
        "canonicalInputs": source_files,
    }

    manifest_bytes = (
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")
    (args.out_dir / MANIFEST_NAME).write_bytes(manifest_bytes)

    # Self-check the bytes after writing so filesystem/newline surprises cannot
    # silently change the hashes recorded in the manifest.
    for name, metadata in manifest["formats"].items():
        actual = (args.out_dir / name).read_bytes()
        digest = sha256_bytes(actual)
        if digest != metadata["sha256"] or len(actual) != metadata["bytes"]:
            raise SystemExit(f"post-write integrity check failed for {name}")

    print(
        "exported lexical corpus: "
        f"{len(articles)} articles from {len(source_files)} canonical JSONL files; "
        f"outputs in {args.out_dir}"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()
