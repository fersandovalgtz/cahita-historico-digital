#!/usr/bin/env python3
"""Validate explicit source-review overlays for historical Buſca references.

The review layer is deliberately separate from the canonical strict graph. This
validator checks that every reviewed source reference is still `not_located`
under strict normalized equality, that its priority tier matches the current
deterministic diagnostic export, and that proposed targets/evidence are explicit.
Tier-C source recoveries may select a canonical article that was not present in
the weak diagnostic shortlist, but only under explicit same-witness and canonical
article-structure evidence. Such recoveries remain editorial, never canonical.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

from export_crossreference_candidate_diagnostics import build_diagnostics
from export_lexicon_crossreference_graph import build_resolution, load_articles

ROOT = Path(__file__).resolve().parents[1]
REVIEW_DIR = ROOT / "data/lexicon/review"
SCHEMA_PATH = ROOT / "schemas/crossreference-source-review.schema.json"
REVIEW_PATTERN = "crossreference_source_review_*.jsonl"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSON in {path}:{line_number}: {exc}") from exc
        if not isinstance(value, dict):
            raise SystemExit(f"non-object JSON value in {path}:{line_number}")
        value["__file"] = path.relative_to(ROOT).as_posix()
        value["__line"] = line_number
        rows.append(value)
    return rows


def fail(row: dict[str, Any], message: str) -> None:
    raise SystemExit(f"{row['__file']}:{row['__line']}: {message}")


def public_row(row: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in row.items() if not key.startswith("__")}


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    review_files = sorted(REVIEW_DIR.glob(REVIEW_PATTERN))
    if not review_files:
        raise SystemExit("no source-review overlay files found")

    reviews: list[dict[str, Any]] = []
    for path in review_files:
        reviews.extend(load_jsonl(path))
    if not reviews:
        raise SystemExit("source-review overlay files contain no records")

    strict_rows, _graph, _article_count, _source_files = build_resolution()
    strict_index = {
        (row["sourceArticleId"], row["crossReferenceIndex"]): row
        for row in strict_rows
    }
    diagnostics, _diagnostic_manifest = build_diagnostics(5)
    diagnostic_index = {
        (row["sourceArticleId"], row["crossReferenceIndex"]): row
        for row in diagnostics
    }
    articles, _article_files = load_articles()
    article_ids = {article["articleId"] for article in articles}

    seen_review_ids: set[str] = set()
    seen_reference_keys: set[tuple[str, int]] = set()
    decision_counts: Counter[str] = Counter()
    tier_counts: Counter[str] = Counter()
    selected_target_count = 0
    selected_outside_diagnostics_count = 0

    for row in reviews:
        value = public_row(row)
        errors = sorted(validator.iter_errors(value), key=lambda error: list(error.path))
        if errors:
            formatted = "; ".join(
                f"{'/'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
                for error in errors
            )
            fail(row, f"schema validation failed: {formatted}")

        review_id = row["reviewId"]
        if review_id in seen_review_ids:
            fail(row, f"duplicate reviewId {review_id}")
        seen_review_ids.add(review_id)

        key = (row["sourceArticleId"], row["crossReferenceIndex"])
        if key in seen_reference_keys:
            fail(row, f"duplicate review for source reference {key}")
        seen_reference_keys.add(key)

        strict = strict_index.get(key)
        if strict is None:
            fail(row, f"source reference {key} does not exist in canonical graph input")
        if strict["resolutionStatus"] != "not_located":
            fail(
                row,
                f"source reference must remain strict not_located, got {strict['resolutionStatus']}",
            )
        if row["canonicalStrictStatus"] != strict["resolutionStatus"]:
            fail(row, "canonicalStrictStatus disagrees with regenerated strict graph")
        if row["targetRaw"] != strict["targetRaw"]:
            fail(row, "targetRaw disagrees with canonical historical cross-reference")
        if row.get("targetNormalized") != strict["targetNormalized"]:
            fail(row, "targetNormalized disagrees with regenerated strict graph")
        if row.get("sourceGuideRaw") != strict.get("sourceGuideRaw"):
            fail(row, "sourceGuideRaw disagrees with canonical article")
        if row.get("sourcePageDigital") != strict.get("sourcePageDigital"):
            fail(row, "sourcePageDigital disagrees with canonical article")
        if row.get("sourceColumn") != strict.get("sourceColumn"):
            fail(row, "sourceColumn disagrees with canonical article")

        diagnostic = diagnostic_index.get(key)
        if diagnostic is None:
            fail(row, "strict-not-located reference is absent from deterministic diagnostics")
        if row["priorityTier"] != diagnostic["priorityTier"]:
            fail(
                row,
                f"priorityTier drift: review={row['priorityTier']} diagnostic={diagnostic['priorityTier']}",
            )

        regenerated_candidates = {
            candidate["articleId"]: candidate for candidate in diagnostic["candidates"]
        }
        declared_candidate_ids: set[str] = set()
        for candidate in row["diagnosticCandidates"]:
            candidate_id = candidate["candidateArticleId"]
            if candidate_id in declared_candidate_ids:
                fail(row, f"duplicate diagnostic candidate {candidate_id}")
            declared_candidate_ids.add(candidate_id)
            regenerated = regenerated_candidates.get(candidate_id)
            if regenerated is None:
                fail(row, f"declared candidate {candidate_id} is absent from regenerated diagnostics")
            expected_pairs = {
                "candidatePageDigital": regenerated.get("sourcePageDigital"),
                "candidateColumn": regenerated.get("column"),
                "candidateGuideRaw": regenerated.get("spanishGuideRaw"),
                "diagnosticClass": regenerated.get("diagnosticClass"),
                "diagnosticScore": regenerated.get("diagnosticScore"),
            }
            for field, expected in expected_pairs.items():
                if candidate.get(field) != expected:
                    fail(
                        row,
                        f"candidate {candidate_id} field {field} drifted: {candidate.get(field)!r} != {expected!r}",
                    )

        selected = row.get("selectedTargetArticleId")
        positive_evidence = [item for item in row["evidence"] if item["supportsDecision"]]
        if selected is not None:
            selected_target_count += 1
            if selected not in article_ids:
                fail(row, f"selected target article does not exist: {selected}")
            if selected not in declared_candidate_ids:
                same_witness = any(
                    item["evidenceKind"] in {"same_witness_facsimile", "same_witness_ocr_control"}
                    for item in positive_evidence
                )
                canonical_structure = any(
                    item["evidenceKind"] == "canonical_article_structure"
                    for item in positive_evidence
                )
                if row["priorityTier"] != "C_no_strong":
                    fail(row, "selectedTargetArticleId outside diagnosticCandidates is permitted only for Tier C")
                if row["decisionStatus"] != "source_supports_unique_target":
                    fail(row, "Tier-C target outside diagnosticCandidates requires source_supports_unique_target")
                if not (same_witness and canonical_structure):
                    fail(
                        row,
                        "Tier-C target outside diagnosticCandidates requires positive same-witness and canonical-structure evidence",
                    )
                selected_outside_diagnostics_count += 1

        if row["decisionStatus"] == "source_supports_unique_target":
            if not selected:
                fail(row, "source_supports_unique_target requires selectedTargetArticleId")
            if not positive_evidence:
                fail(row, "source_supports_unique_target requires positive evidence")
            if not any(
                item["evidenceKind"] in {"same_witness_facsimile", "same_witness_ocr_control"}
                for item in positive_evidence
            ):
                fail(row, "source_supports_unique_target requires same-witness source evidence")

        if row["humanVerified"] is not False:
            fail(row, "AI-assisted source-review overlays must keep humanVerified=false")
        if row["reviewStatus"] == "human_verified":
            fail(row, "human_verified is not permitted in the current AI-assisted review layer")

        decision_counts[row["decisionStatus"]] += 1
        tier_counts[row["priorityTier"]] += 1

    print(
        "cross-reference source-review QA OK: "
        f"{len(reviews)} records across {len(review_files)} file(s); "
        f"tiers={dict(sorted(tier_counts.items()))}; "
        f"decisions={dict(sorted(decision_counts.items()))}; "
        f"selectedTargets={selected_target_count}; "
        f"selectedOutsideDiagnostics={selected_outside_diagnostics_count}; "
        "canonical strict graph modified=0; humanVerified=0"
    )


if __name__ == "__main__":
    main()
