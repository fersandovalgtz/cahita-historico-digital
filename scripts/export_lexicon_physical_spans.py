#!/usr/bin/env python3
"""Export a deterministic audit of lexical physical spans and continuity flags.

The canonical articles remain unchanged. This derived layer records articles
that expose physical-continuity metadata and surfaces conservative consistency
flags for later editorial review; it performs no automatic repair.
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

JSONL_NAME = "chd_lexicon_physical_spans_audit.jsonl"
CSV_NAME = "chd_lexicon_physical_spans_audit.csv"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "articleId",
    "sourcePageDigital",
    "column",
    "spanishGuideRaw",
    "continuesFromPreviousPage",
    "continuesToNextPage",
    "spanCount",
    "distinctPageCount",
    "distinctColumnCount",
    "crossPageDerived",
    "crossColumnDerived",
    "sourceSpans",
    "auditFlags",
    "reviewStatus",
    "humanVerified",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def article_number(article_id: str) -> int:
    return int(article_id.rsplit("-", 1)[1])


def derive_flags(article: dict[str, Any], spans: list[dict[str, Any]]) -> list[str]:
    flags: list[str] = []
    from_previous = bool(article.get("continuesFromPreviousPage"))
    to_next = bool(article.get("continuesToNextPage"))

    pages = {span.get("pageDigital") for span in spans if span.get("pageDigital") is not None}
    columns = {span.get("column") for span in spans if span.get("column") is not None}
    cross_page = len(pages) > 1

    if (from_previous or to_next) and not spans:
        flags.append("continuity_flag_without_source_spans")
    if cross_page and not (from_previous or to_next):
        flags.append("cross_page_source_spans_without_page_continuity_flag")
    if spans and article.get("sourcePageDigital") not in pages:
        flags.append("article_source_page_absent_from_source_spans")
    if spans and article.get("column") not in columns:
        flags.append("article_source_column_absent_from_source_spans")
    if (from_previous or to_next) and len(spans) == 1:
        flags.append("page_continuity_flag_with_single_source_span")

    return sorted(set(flags))


def load_audit() -> tuple[list[dict[str, Any]], int, list[str]]:
    rows: list[dict[str, Any]] = []
    article_count = 0
    source_files: list[str] = []

    for path in sorted(ARTICLE_DIR.glob("*.jsonl")):
        source_files.append(path.relative_to(ROOT).as_posix())
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                article = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}:{line_number}: {exc}") from exc
            article_count += 1

            spans = article.get("sourceSpans") or []
            from_previous = bool(article.get("continuesFromPreviousPage"))
            to_next = bool(article.get("continuesToNextPage"))
            if not spans and not from_previous and not to_next:
                continue

            pages = {span.get("pageDigital") for span in spans if span.get("pageDigital") is not None}
            columns = {span.get("column") for span in spans if span.get("column") is not None}
            flags = derive_flags(article, spans)

            rows.append(
                {
                    "articleId": article["articleId"],
                    "sourcePageDigital": article.get("sourcePageDigital"),
                    "column": article.get("column"),
                    "spanishGuideRaw": article.get("spanishGuideRaw"),
                    "continuesFromPreviousPage": from_previous,
                    "continuesToNextPage": to_next,
                    "spanCount": len(spans),
                    "distinctPageCount": len(pages),
                    "distinctColumnCount": len(columns),
                    "crossPageDerived": len(pages) > 1,
                    "crossColumnDerived": len(columns) > 1,
                    "sourceSpans": spans,
                    "auditFlags": flags,
                    "reviewStatus": article.get("reviewStatus"),
                    "humanVerified": bool(article.get("humanVerified")),
                }
            )

    rows.sort(key=lambda row: article_number(row["articleId"]))
    return rows, article_count, source_files


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def csv_value(value: Any) -> Any:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return compact_json(value)
    if value is None:
        return ""
    return value


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: csv_value(row.get(field)) for field in CSV_FIELDS})
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/lexicon-physical-spans",
        help="Directory for derived physical-span audit outputs.",
    )
    args = parser.parse_args()

    rows, article_count, source_files = load_audit()
    if not rows:
        raise SystemExit("no physical-span or page-continuity metadata found in canonical lexicon")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
    }

    flag_counts = Counter(flag for row in rows for flag in row["auditFlags"])
    flagged_rows = [row for row in rows if row["auditFlags"]]
    flagged_articles = len(flagged_rows)
    flagged_article_ids = [row["articleId"] for row in flagged_rows]
    manifest = {
        "sourceId": "ALC1737",
        "dataset": "lexical_physical_spans_audit",
        "derivation": "deterministic audit of canonical sourceSpans and page-continuity flags",
        "canonicalInputPattern": "data/lexicon/articles/*.jsonl",
        "canonicalInputFileCount": len(source_files),
        "canonicalArticleCountScanned": article_count,
        "articleCountWithPhysicalMetadata": len(rows),
        "articleCountWithSourceSpans": sum(bool(row["sourceSpans"]) for row in rows),
        "articleCountWithPageContinuityFlags": sum(
            bool(row["continuesFromPreviousPage"] or row["continuesToNextPage"])
            for row in rows
        ),
        "crossPageDerivedCount": sum(bool(row["crossPageDerived"]) for row in rows),
        "crossColumnDerivedCount": sum(bool(row["crossColumnDerived"]) for row in rows),
        "flaggedArticleCount": flagged_articles,
        "flaggedArticleIds": flagged_article_ids,
        "auditFlagCounts": dict(sorted(flag_counts.items())),
        "automaticRepairPerformed": False,
        "philologicalCorrectionInferred": False,
        "deterministic": True,
        "sortOrder": "numeric articleId ascending",
        "formats": {
            name: {"bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(payloads.items())
        },
        "canonicalInputs": source_files,
    }
    (args.out_dir / MANIFEST_NAME).write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    for name, metadata in manifest["formats"].items():
        actual = (args.out_dir / name).read_bytes()
        if len(actual) != metadata["bytes"] or sha256_bytes(actual) != metadata["sha256"]:
            raise SystemExit(f"post-write integrity check failed for {name}")

    print(
        "exported physical-span audit: "
        f"{len(rows)} articles with physical metadata; "
        f"{flagged_articles} flagged {flagged_article_ids}; "
        f"flags={dict(sorted(flag_counts.items()))}; "
        f"outputs in {args.out_dir}"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()
