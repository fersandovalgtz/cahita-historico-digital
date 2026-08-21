#!/usr/bin/env python3
"""Build a non-binding diagnostic queue for unresolved historical Buſca targets.

This audit never resolves, rewrites, or promotes a cross-reference. Canonical
resolution remains the strict normalized-equality layer implemented in
`export_lexicon_crossreference_graph.py`. The heuristics below exist only to
prioritize subsequent source collation and are labelled as diagnostic evidence.
"""
from __future__ import annotations

import argparse
import difflib
import json
from collections import Counter
from typing import Any

from export_lexicon_crossreference_graph import (
    article_number,
    load_articles,
    marker_class,
    normalize_guide,
)


def token_set(value: str) -> set[str]:
    return {token for token in value.split() if token}


def candidate_score(target: str, guide: str) -> tuple[float, str]:
    """Return a transparent diagnostic score and class, never a resolution."""
    if not target or not guide:
        return 0.0, "none"

    target_tokens = token_set(target)
    guide_tokens = token_set(guide)
    overlap = len(target_tokens & guide_tokens)
    union = len(target_tokens | guide_tokens)
    jaccard = overlap / union if union else 0.0

    if len(target) >= 4 and (target in guide or guide in target):
        shorter = min(len(target), len(guide))
        longer = max(len(target), len(guide))
        containment = shorter / longer if longer else 0.0
        return max(0.90, containment), "normalized_containment"

    ratio = difflib.SequenceMatcher(a=target, b=guide, autojunk=False).ratio()
    if jaccard >= 0.67:
        return max(0.82, jaccard), "high_token_overlap"
    if ratio >= 0.84:
        return ratio, "high_graphic_similarity"
    if jaccard >= 0.40:
        return max(0.70, jaccard), "partial_token_overlap"
    if ratio >= 0.72:
        return ratio, "moderate_graphic_similarity"
    return 0.0, "none"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--print-rows", action="store_true")
    parser.add_argument("--max-candidates", type=int, default=5)
    args = parser.parse_args()

    articles, _source_files = load_articles()
    guide_rows: list[tuple[str, str, str]] = []
    guide_index: dict[str, list[str]] = {}
    for article in articles:
        raw = article.get("spanishGuideRaw")
        if not isinstance(raw, str) or not raw.strip():
            continue
        normalized = normalize_guide(raw)
        if not normalized:
            continue
        guide_rows.append((article["articleId"], raw, normalized))
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
            for candidate_id, candidate_raw, candidate_norm in guide_rows:
                score, reason = candidate_score(target, candidate_norm)
                if score <= 0.0:
                    continue
                candidates.append(
                    {
                        "articleId": candidate_id,
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
            candidates = candidates[: args.max_candidates]
            unresolved.append(
                {
                    "sourceArticleId": article["articleId"],
                    "sourcePageDigital": article.get("sourcePageDigital"),
                    "sourceGuideRaw": article.get("spanishGuideRaw"),
                    "crossReferenceIndex": ref_index,
                    "targetRaw": target_raw,
                    "targetNormalized": target,
                    "candidateCountShown": len(candidates),
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
    for row in unresolved:
        score = row["candidates"][0]["diagnosticScore"] if row["candidates"] else 0.0
        if score >= 0.90:
            score_bands[">=0.90"] += 1
        elif score >= 0.84:
            score_bands["0.84-0.899999"] += 1
        elif score >= 0.72:
            score_bands["0.72-0.839999"] += 1
        else:
            score_bands["<0.72_or_none"] += 1

    print(
        "cross-reference diagnostic audit: "
        f"{len(unresolved)} strict-not-located Buſca references; "
        f"topClasses={dict(sorted(top_classes.items()))}; "
        f"scoreBands={dict(sorted(score_bands.items()))}; "
        "canonical resolutions modified=0"
    )
    if args.print_rows:
        for row in unresolved:
            print("XREFDIAG " + json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
