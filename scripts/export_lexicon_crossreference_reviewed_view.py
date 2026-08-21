#!/usr/bin/env python3
"""Export a deterministic reviewed view of historical lexical cross-references.

The canonical graph remains the strict normalized-equality layer produced by
``export_lexicon_crossreference_graph.py``. This exporter overlays explicit
source-review records on strict ``not_located`` rows to create a separate view
for research use. Editorial proposals never become canonical strict edges.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

from export_lexicon_crossreference_graph import (
    article_number,
    build_resolution,
    load_articles,
)

ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "data/lexicon/review"
REVIEW_PATTERN = "crossreference_source_review_*.jsonl"

JSONL_NAME = "chd_lexicon_crossreference_reviewed_view.jsonl"
CSV_NAME = "chd_lexicon_crossreference_reviewed_view.csv"
GRAPH_NAME = "chd_lexicon_crossreference_reviewed_graph.json"
MANIFEST_NAME = "manifest.json"

CSV_FIELDS = [
    "sourceArticleId",
    "sourcePageDigital",
    "sourceColumn",
    "sourceGuideRaw",
    "crossReferenceIndex",
    "markerRaw",
    "targetRaw",
    "canonicalStrictStatus",
    "reviewedViewStatus",
    "effectiveTargetArticleId",
    "edgeAuthority",
    "reviewId",
    "reviewDecisionStatus",
    "reviewStatus",
    "humanVerified",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_source_reviews() -> tuple[dict[tuple[str, int], dict[str, Any]], list[str]]:
    reviews: dict[tuple[str, int], dict[str, Any]] = {}
    source_files: list[str] = []
    for path in sorted(REVIEW_DIR.glob(REVIEW_PATTERN)):
        source_files.append(path.relative_to(ROOT).as_posix())
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}:{line_number}: {exc}") from exc
            key = (row.get("sourceArticleId"), row.get("crossReferenceIndex"))
            if not isinstance(key[0], str) or not isinstance(key[1], int):
                raise SystemExit(f"invalid source-review key in {path}:{line_number}")
            if key in reviews:
                raise SystemExit(f"duplicate source-review overlay for {key}")
            reviews[key] = row
    return reviews, source_files


def reviewed_status(strict_row: dict[str, Any], review: dict[str, Any] | None) -> tuple[str, str | None, str]:
    strict_status = strict_row["resolutionStatus"]
    if strict_status == "exact_unique":
        return "strict_exact_unique", strict_row["exactUniqueTargetArticleId"], "strict_exact_normalized_equality"
    if strict_status == "not_busca":
        return "not_busca", None, "none"
    if strict_status == "non_normalizable":
        return "strict_non_normalizable", None, "none"
    if strict_status == "exact_multiple":
        return "strict_exact_multiple", None, "none"
    if strict_status != "not_located":
        raise SystemExit(f"unexpected strict cross-reference status: {strict_status}")

    if review is None:
        return "strict_not_located_unreviewed", None, "none"

    decision = review["decisionStatus"]
    if decision == "source_supports_unique_target":
        target = review.get("selectedTargetArticleId")
        if not isinstance(target, str) or not target:
            raise SystemExit(f"review {review.get('reviewId')} supports unique target but has no selected target")
        return "editorial_source_supported_unique", target, "editorial_source_review"
    if decision == "source_supports_multiple_targets":
        return "editorial_source_supported_multiple", None, "none"
    if decision == "candidate_rejected":
        return "editorial_candidate_rejected", None, "none"
    if decision == "target_not_located":
        return "editorial_target_not_located", None, "none"
    if decision == "source_or_destination_requires_recollation":
        return "editorial_requires_recollation", None, "none"
    if decision == "pending_source_collation":
        return "editorial_pending_source_collation", None, "none"
    if decision == "unresolved":
        return "editorial_unresolved", None, "none"
    raise SystemExit(f"unexpected review decisionStatus: {decision}")


def build_view() -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    strict_rows, strict_graph, article_count, canonical_files = build_resolution()
    reviews, review_files = load_source_reviews()
    articles, _ = load_articles()
    by_id = {article["articleId"]: article for article in articles}

    rows: list[dict[str, Any]] = []
    used_reviews: set[tuple[str, int]] = set()
    for strict in strict_rows:
        key = (strict["sourceArticleId"], strict["crossReferenceIndex"])
        review = reviews.get(key)
        if review is not None:
            used_reviews.add(key)
            if strict["resolutionStatus"] != "not_located":
                raise SystemExit(f"source-review overlay may only attach to strict not_located rows: {key}")
            if review.get("canonicalStrictStatus") != "not_located":
                raise SystemExit(f"source-review overlay has non-not_located canonicalStrictStatus: {key}")
            if review.get("targetRaw") != strict["targetRaw"]:
                raise SystemExit(f"source-review targetRaw drift for {key}")

        status, effective_target, authority = reviewed_status(strict, review)
        row = {
            "sourceArticleId": strict["sourceArticleId"],
            "sourcePageDigital": strict.get("sourcePageDigital"),
            "sourceColumn": strict.get("sourceColumn"),
            "sourceGuideRaw": strict.get("sourceGuideRaw"),
            "crossReferenceIndex": strict["crossReferenceIndex"],
            "markerRaw": strict["markerRaw"],
            "markerClass": strict["markerClass"],
            "targetRaw": strict["targetRaw"],
            "targetNormalized": strict["targetNormalized"],
            "canonicalStrictStatus": strict["resolutionStatus"],
            "reviewedViewStatus": status,
            "effectiveTargetArticleId": effective_target,
            "edgeAuthority": authority,
            "reviewId": review.get("reviewId") if review else None,
            "reviewDecisionStatus": review.get("decisionStatus") if review else None,
            "reviewStatus": review.get("reviewStatus") if review else None,
            "humanVerified": bool(review.get("humanVerified")) if review else False,
        }
        rows.append(row)

    unused_reviews = sorted(set(reviews) - used_reviews)
    if unused_reviews:
        raise SystemExit(f"source-review overlays not attached to canonical strict rows: {unused_reviews}")

    rows.sort(key=lambda row: (article_number(row["sourceArticleId"]), row["crossReferenceIndex"]))

    edges = []
    for row in rows:
        target_id = row["effectiveTargetArticleId"]
        if not target_id:
            continue
        if target_id not in by_id:
            raise SystemExit(f"effective reviewed target article does not exist: {target_id}")
        edges.append(
            {
                "sourceArticleId": row["sourceArticleId"],
                "targetArticleId": target_id,
                "targetRaw": row["targetRaw"],
                "relation": "see",
                "edgeAuthority": row["edgeAuthority"],
                "reviewedViewStatus": row["reviewedViewStatus"],
                "reviewId": row["reviewId"],
                "humanVerified": row["humanVerified"],
            }
        )

    node_ids = {
        article_id
        for edge in edges
        for article_id in (edge["sourceArticleId"], edge["targetArticleId"])
    }
    graph = {
        "sourceId": "ALC1737",
        "graphSemantics": "strict exact edges plus explicitly labelled source-reviewed editorial edges; canonical strict graph remains unchanged",
        "nodeCount": len(node_ids),
        "edgeCount": len(edges),
        "strictExactEdgeCount": sum(edge["edgeAuthority"] == "strict_exact_normalized_equality" for edge in edges),
        "editorialSourceReviewedEdgeCount": sum(edge["edgeAuthority"] == "editorial_source_review" for edge in edges),
        "humanVerifiedEditorialEdgeCount": sum(
            edge["edgeAuthority"] == "editorial_source_review" and edge["humanVerified"] for edge in edges
        ),
        "nodes": [
            {
                "articleId": article_id,
                "spanishGuideRaw": by_id[article_id].get("spanishGuideRaw"),
                "sourcePageDigital": by_id[article_id].get("sourcePageDigital"),
            }
            for article_id in sorted(node_ids, key=article_number)
        ],
        "edges": edges,
    }

    status_counts = Counter(row["reviewedViewStatus"] for row in rows)
    authority_counts = Counter(row["edgeAuthority"] for row in rows if row["edgeAuthority"] != "none")
    review_decision_counts = Counter(
        row["reviewDecisionStatus"] for row in rows if row["reviewDecisionStatus"] is not None
    )
    metadata = {
        "articleCountScanned": article_count,
        "canonicalCrossReferenceCount": len(rows),
        "strictGraphEdgeCount": strict_graph["edgeCount"],
        "strictGraphCycleCount": strict_graph["cycleCount"],
        "sourceReviewRecordCount": len(reviews),
        "reviewedViewStatusCounts": dict(sorted(status_counts.items())),
        "edgeAuthorityCounts": dict(sorted(authority_counts.items())),
        "reviewDecisionCounts": dict(sorted(review_decision_counts.items())),
        "reviewedViewEdgeCount": len(edges),
        "canonicalArticlesModified": False,
        "canonicalStrictGraphModified": False,
        "editorialReviewsPromotedToCanonical": False,
        "humanValidationInferred": False,
        "deterministic": True,
        "canonicalInputs": canonical_files,
        "reviewInputs": review_files,
    }
    return rows, graph, metadata


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def csv_value(value: Any) -> Any:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
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
        default=ROOT / "build/lexicon-crossreference-reviewed-view",
    )
    args = parser.parse_args()

    rows, graph, metadata = build_view()
    if not rows:
        raise SystemExit("reviewed cross-reference view is empty")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    graph_bytes = (json.dumps(graph, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
        GRAPH_NAME: graph_bytes,
    }
    (args.out_dir / GRAPH_NAME).write_bytes(graph_bytes)

    manifest = {
        "sourceId": "ALC1737",
        "dataset": "historical_lexical_crossreference_reviewed_view",
        "derivation": "canonical strict normalized-equality graph overlaid with explicit source-review records; editorial edges remain non-canonical",
        **metadata,
        "formats": {
            name: {"bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(payloads.items())
        },
    }
    (args.out_dir / MANIFEST_NAME).write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    for name, info in manifest["formats"].items():
        actual = (args.out_dir / name).read_bytes()
        if len(actual) != info["bytes"] or sha256_bytes(actual) != info["sha256"]:
            raise SystemExit(f"post-write integrity check failed for {name}")

    print(
        "exported reviewed cross-reference view: "
        f"{manifest['canonicalCrossReferenceCount']} references; "
        f"strictEdges={manifest['strictGraphEdgeCount']}; "
        f"reviewRecords={manifest['sourceReviewRecordCount']}; "
        f"viewEdges={manifest['reviewedViewEdgeCount']}; "
        f"statuses={manifest['reviewedViewStatusCounts']}; "
        "canonical strict graph modified=0"
    )
    for name, info in manifest["formats"].items():
        print(f"  {name}: {info['bytes']} bytes; sha256 {info['sha256']}")


if __name__ == "__main__":
    main()
