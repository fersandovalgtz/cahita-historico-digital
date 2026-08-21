#!/usr/bin/env python3
"""Export a deterministic, non-binding diagnostic queue for unresolved Buſca references.

Canonical cross-reference resolution remains the strict normalized-equality graph
implemented by ``export_lexicon_crossreference_graph.py``. This exporter uses the
same transparent diagnostic scoring already exposed by
``audit_crossreference_candidates.py`` only to prioritize later source collation.
It never creates canonical links, rewrites articles, or infers semantic identity.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

from audit_crossreference_candidates import candidate_score
from export_lexicon_crossreference_graph import (
    article_number,
    load_articles,
    marker_class,
    normalize_guide,
)

ROOT = Path(__file__).resolve().parents[1]
JSONL_NAME = "chd_crossreference_candidate_diagnostics.jsonl"
CSV_NAME = "chd_crossreference_candidate_pairs.csv"
MANIFEST_NAME = "manifest.json"
STRONG_THRESHOLD = 0.90

CSV_FIELDS = [
    "sourceArticleId",
    "sourcePageDigital",
    "sourceColumn",
    "sourceGuideRaw",
    "crossReferenceIndex",
    "targetRaw",
    "targetNormalized",
    "candidateRank",
    "candidateArticleId",
    "candidatePageDigital",
    "candidateColumn",
    "candidateGuideRaw",
    "diagnosticClass",
    "diagnosticScore",
    "strongCandidate",
    "policy",
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def build_diagnostics(max_candidates: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if max_candidates <= 0:
        raise SystemExit("--max-candidates must be greater than zero")

    articles, source_files = load_articles()
    guide_rows: list[tuple[str, str, str, int | None, str | None]] = []
    guide_index: dict[str, list[str]] = {}

    for article in articles:
        raw = article.get("spanishGuideRaw")
        if not isinstance(raw, str) or not raw.strip():
            continue
        normalized = normalize_guide(raw)
        if not normalized:
            continue
        guide_rows.append(
            (
                article["articleId"],
                raw,
                normalized,
                article.get("sourcePageDigital"),
                article.get("column"),
            )
        )
        guide_index.setdefault(normalized, []).append(article["articleId"])

    unresolved: list[dict[str, Any]] = []
    for article in articles:
        for ref_index, ref in enumerate(article.get("crossReferences") or []):
            marker_raw = ref.get("markerRaw")
            target_raw = ref.get("targetRaw")
            if not isinstance(marker_raw, str) or marker_class(marker_raw) != "busca":
                continue
            if not isinstance(target_raw, str) or not target_raw:
                continue

            target = normalize_guide(target_raw)
            if target and guide_index.get(target):
                continue

            candidates: list[dict[str, Any]] = []
            for candidate_id, candidate_raw, candidate_norm, candidate_page, candidate_column in guide_rows:
                score, reason = candidate_score(target, candidate_norm)
                if score <= 0.0:
                    continue
                candidates.append(
                    {
                        "articleId": candidate_id,
                        "sourcePageDigital": candidate_page,
                        "column": candidate_column,
                        "spanishGuideRaw": candidate_raw,
                        "guideNormalized": candidate_norm,
                        "diagnosticClass": reason,
                        "diagnosticScore": round(score, 6),
                    }
                )

            candidates.sort(
                key=lambda row: (
                    -row["diagnosticScore"],
                    article_number(row["articleId"]),
                )
            )
            candidates = candidates[:max_candidates]
            for rank, candidate in enumerate(candidates, 1):
                candidate["rank"] = rank

            strong = [
                candidate
                for candidate in candidates
                if candidate["diagnosticScore"] >= STRONG_THRESHOLD
            ]
            unresolved.append(
                {
                    "sourceArticleId": article["articleId"],
                    "sourcePageDigital": article.get("sourcePageDigital"),
                    "sourceColumn": article.get("column"),
                    "sourceGuideRaw": article.get("spanishGuideRaw"),
                    "crossReferenceIndex": ref_index,
                    "targetRaw": target_raw,
                    "targetNormalized": target,
                    "candidateCountShown": len(candidates),
                    "strongCandidateCountShown": len(strong),
                    "candidates": candidates,
                    "policy": "diagnostic_only_no_resolution",
                }
            )

    unresolved.sort(
        key=lambda row: (article_number(row["sourceArticleId"]), row["crossReferenceIndex"])
    )

    top_classes = Counter(
        row["candidates"][0]["diagnosticClass"] if row["candidates"] else "no_candidate"
        for row in unresolved
    )
    score_bands = Counter()
    strong_cardinality = Counter()
    candidate_pair_count = 0

    for row in unresolved:
        candidate_pair_count += len(row["candidates"])
        score = row["candidates"][0]["diagnosticScore"] if row["candidates"] else 0.0
        if score >= STRONG_THRESHOLD:
            score_bands[">=0.90"] += 1
        elif score >= 0.84:
            score_bands["0.84-0.899999"] += 1
        elif score >= 0.72:
            score_bands["0.72-0.839999"] += 1
        else:
            score_bands["<0.72_or_none"] += 1

        strong_count = row["strongCandidateCountShown"]
        if strong_count == 0:
            strong_cardinality["none"] += 1
        elif strong_count == 1:
            strong_cardinality["unique_shown"] += 1
        else:
            strong_cardinality["multiple_shown"] += 1

    summary = {
        "sourceId": "ALC1737",
        "dataset": "historical_crossreference_candidate_diagnostics",
        "canonicalResolutionPolicy": "strict_normalized_equality_only_unchanged",
        "diagnosticPolicy": "non_binding_candidate_prioritization_only",
        "canonicalInputPattern": "data/lexicon/articles/*.jsonl",
        "canonicalInputFileCount": len(source_files),
        "canonicalArticleCountScanned": len(articles),
        "strictNotLocatedAudited": len(unresolved),
        "candidatePairCount": candidate_pair_count,
        "maxCandidatesShownPerReference": max_candidates,
        "strongThreshold": STRONG_THRESHOLD,
        "strongCandidateCardinality": dict(sorted(strong_cardinality.items())),
        "topCandidateClass": dict(sorted(top_classes.items())),
        "topScoreBand": dict(sorted(score_bands.items())),
        "diagnosticOnly": True,
        "destinationResolutionPerformed": False,
        "canonicalResolutionsModified": False,
        "canonicalArticlesModified": False,
        "canonicalFuzzyMatchingUsed": False,
        "diagnosticGraphicSimilarityUsed": True,
        "linguisticSimilarityUsed": False,
        "semanticEquivalenceInferred": False,
        "philologicalCorrectionInferred": False,
        "humanVerificationPerformed": False,
        "deterministic": True,
        "sortOrder": "numeric sourceArticleId ascending, crossReferenceIndex ascending; candidates score descending then numeric articleId",
        "canonicalInputs": source_files,
    }
    return unresolved, summary


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            candidates = row["candidates"] or [None]
            for candidate in candidates:
                writer.writerow(
                    {
                        "sourceArticleId": row["sourceArticleId"],
                        "sourcePageDigital": row.get("sourcePageDigital"),
                        "sourceColumn": row.get("sourceColumn"),
                        "sourceGuideRaw": row.get("sourceGuideRaw"),
                        "crossReferenceIndex": row["crossReferenceIndex"],
                        "targetRaw": row["targetRaw"],
                        "targetNormalized": row["targetNormalized"],
                        "candidateRank": candidate.get("rank") if candidate else "",
                        "candidateArticleId": candidate.get("articleId") if candidate else "",
                        "candidatePageDigital": candidate.get("sourcePageDigital") if candidate else "",
                        "candidateColumn": candidate.get("column") if candidate else "",
                        "candidateGuideRaw": candidate.get("spanishGuideRaw") if candidate else "",
                        "diagnosticClass": candidate.get("diagnosticClass") if candidate else "none",
                        "diagnosticScore": candidate.get("diagnosticScore") if candidate else 0.0,
                        "strongCandidate": (
                            candidate.get("diagnosticScore", 0.0) >= STRONG_THRESHOLD
                            if candidate
                            else False
                        ),
                        "policy": row["policy"],
                    }
                )
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "build/crossreference-candidate-diagnostics",
    )
    parser.add_argument("--max-candidates", type=int, default=5)
    args = parser.parse_args()

    rows, manifest = build_diagnostics(args.max_candidates)
    if not rows:
        raise SystemExit("no strict-not-located Buſca references found; refusing empty diagnostic export")

    args.out_dir.mkdir(parents=True, exist_ok=True)
    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
    }
    manifest["formats"] = {
        name: {"bytes": len(data), "sha256": sha256_bytes(data)}
        for name, data in sorted(payloads.items())
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
        "exported cross-reference candidate diagnostics: "
        f"{manifest['strictNotLocatedAudited']} strict-not-located references; "
        f"{manifest['candidatePairCount']} candidate pairs; "
        f"strongCardinality={manifest['strongCandidateCardinality']}; "
        "canonical resolutions modified=0"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()
