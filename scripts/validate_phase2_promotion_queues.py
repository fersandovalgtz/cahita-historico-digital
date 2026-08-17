#!/usr/bin/env python3
"""Validate Phase II lexicographic promotion-triage queues.

The validator keeps candidate-level open-work queues synchronized with their
page reconciliation state and with the evidence files they cite. It does not
change or strengthen any lexical reading.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RECON = ROOT / "data" / "lexicon" / "reconciliation"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            records.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path.relative_to(ROOT)}:{line_number}: invalid JSON: {exc}") from exc
    return records


def evidence_names(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return value
    raise TypeError("evidence reference must be a string or a list of strings")


def validate_queue(path: Path) -> list[str]:
    errors: list[str] = []
    rel = path.relative_to(ROOT)
    try:
        queue = load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{rel}: cannot parse queue: {exc}"]

    page = queue.get("sourcePageDigital")
    if not isinstance(page, int):
        return [f"{rel}: sourcePageDigital must be an integer"]

    scope = queue.get("scope")
    if not isinstance(scope, dict):
        return [f"{rel}: scope must be an object"]

    candidate_ids = scope.get("candidateIds")
    expected_count = scope.get("pendingPromotionCandidates")
    if not isinstance(candidate_ids, list) or not all(isinstance(cid, str) for cid in candidate_ids):
        return [f"{rel}: scope.candidateIds must be a list of strings"]

    if expected_count != len(candidate_ids):
        errors.append(
            f"{rel}: scope.pendingPromotionCandidates={expected_count!r} "
            f"but candidateIds has {len(candidate_ids)} entries"
        )

    duplicate_scope_ids = sorted(cid for cid, count in Counter(candidate_ids).items() if count > 1)
    if duplicate_scope_ids:
        errors.append(f"{rel}: duplicate scope candidateIds: {', '.join(duplicate_scope_ids)}")

    page_marker = f"-p{page}-"
    wrong_page_ids = sorted(cid for cid in candidate_ids if page_marker not in cid)
    if wrong_page_ids:
        errors.append(
            f"{rel}: candidateIds do not match sourcePageDigital {page}: "
            + ", ".join(wrong_page_ids)
        )

    categories = queue.get("categories")
    if not isinstance(categories, dict) or not categories:
        errors.append(f"{rel}: categories must be a non-empty object")
        categories = {}

    membership: Counter[str] = Counter()
    for category_name, category in categories.items():
        if not isinstance(category, dict):
            errors.append(f"{rel}: category {category_name!r} must be an object")
            continue
        ids = category.get("candidateIds")
        if not isinstance(ids, list) or not all(isinstance(cid, str) for cid in ids):
            errors.append(f"{rel}: category {category_name!r} candidateIds must be strings")
            continue
        if category.get("count") != len(ids):
            errors.append(
                f"{rel}: category {category_name!r} count={category.get('count')!r} "
                f"but has {len(ids)} candidateIds"
            )
        local_duplicates = sorted(cid for cid, count in Counter(ids).items() if count > 1)
        if local_duplicates:
            errors.append(
                f"{rel}: category {category_name!r} has duplicate candidateIds: "
                + ", ".join(local_duplicates)
            )
        membership.update(ids)

        try:
            refs = evidence_names(category.get("evidence"))
        except TypeError as exc:
            errors.append(f"{rel}: category {category_name!r}: {exc}")
            refs = []
        for ref in refs:
            evidence_path = RECON / ref
            if not evidence_path.is_file():
                errors.append(
                    f"{rel}: category {category_name!r} references missing evidence {ref}"
                )

    scope_set = set(candidate_ids)
    categorized_set = set(membership)
    missing_from_categories = sorted(scope_set - categorized_set)
    outside_scope = sorted(categorized_set - scope_set)
    multiply_categorized = sorted(cid for cid, count in membership.items() if count != 1)
    if missing_from_categories:
        errors.append(
            f"{rel}: scope candidates missing from categories: " + ", ".join(missing_from_categories)
        )
    if outside_scope:
        errors.append(
            f"{rel}: categorized candidates outside scope: " + ", ".join(outside_scope)
        )
    if multiply_categorized:
        errors.append(
            f"{rel}: candidates must occur in exactly one category: "
            + ", ".join(multiply_categorized)
        )

    next_pass = queue.get("nextPassOrder")
    if isinstance(next_pass, list):
        ordered_categories: list[str] = []
        priorities: list[int] = []
        for index, item in enumerate(next_pass, start=1):
            if not isinstance(item, dict):
                errors.append(f"{rel}: nextPassOrder item {index} must be an object")
                continue
            category_name = item.get("category")
            priority = item.get("priority")
            if not isinstance(category_name, str):
                errors.append(f"{rel}: nextPassOrder item {index} has invalid category")
            else:
                ordered_categories.append(category_name)
            if not isinstance(priority, int):
                errors.append(f"{rel}: nextPassOrder item {index} has invalid priority")
            else:
                priorities.append(priority)
        if set(ordered_categories) != set(categories):
            errors.append(f"{rel}: nextPassOrder categories must exactly match queue categories")
        if priorities and sorted(priorities) != list(range(1, len(priorities) + 1)):
            errors.append(f"{rel}: nextPassOrder priorities must be contiguous starting at 1")
    else:
        errors.append(f"{rel}: nextPassOrder must be a list")

    triage_policy = queue.get("triagePolicy", {})
    if triage_policy.get("automaticPromotionAllowed") is not False:
        errors.append(f"{rel}: triagePolicy.automaticPromotionAllowed must remain false")
    if triage_policy.get("humanVerified") is not False:
        errors.append(f"{rel}: triagePolicy.humanVerified must remain false")
    if queue.get("humanVerified") is not False:
        errors.append(f"{rel}: humanVerified must remain false")
    if queue.get("reviewStatus") == "human_verified":
        errors.append(f"{rel}: reviewStatus cannot be human_verified while humanVerified=false")

    provenance = queue.get("provenance", {})
    derived_from = provenance.get("derivedFrom", [])
    if isinstance(derived_from, list):
        for ref in derived_from:
            if not isinstance(ref, str):
                errors.append(f"{rel}: provenance.derivedFrom entries must be strings")
                continue
            if not (RECON / ref).is_file():
                errors.append(f"{rel}: provenance references missing file {ref}")
    else:
        errors.append(f"{rel}: provenance.derivedFrom must be a list")

    status_path = RECON / f"p{page}_machine_reconciliation_status.json"
    if not status_path.is_file():
        errors.append(f"{rel}: missing page status {status_path.name}")
    else:
        status = load_json(status_path)
        status_pending = (
            status.get("promotion", {}).get("articleCandidatesPendingPromotion")
            if isinstance(status.get("promotion"), dict)
            else None
        )
        if status_pending is None:
            status_pending = status.get("linkage", {}).get("articleCandidatesPendingPromotion")
        if status_pending != len(candidate_ids):
            errors.append(
                f"{rel}: page status reports {status_pending!r} pending promotions, "
                f"queue contains {len(candidate_ids)}"
            )
        if status.get("humanVerified") is not False:
            errors.append(f"{rel}: page status humanVerified must remain false")

    reconciliation_paths = [
        RECON / f"p{page}_left_reconciliation.jsonl",
        RECON / f"p{page}_right_reconciliation.jsonl",
    ]
    pending_from_reconciliation: set[str] = set()
    for reconciliation_path in reconciliation_paths:
        if not reconciliation_path.is_file():
            errors.append(f"{rel}: missing reconciliation file {reconciliation_path.name}")
            continue
        try:
            records = load_jsonl(reconciliation_path)
        except (OSError, ValueError) as exc:
            errors.append(f"{rel}: {exc}")
            continue
        for record in records:
            if record.get("articleLinkStatus") == "pending_promotion":
                candidate_id = record.get("candidateId")
                if isinstance(candidate_id, str):
                    pending_from_reconciliation.add(candidate_id)
                else:
                    errors.append(
                        f"{rel}: pending_promotion record in {reconciliation_path.name} "
                        "has no string candidateId"
                    )

    if pending_from_reconciliation != scope_set:
        missing_in_queue = sorted(pending_from_reconciliation - scope_set)
        stale_in_queue = sorted(scope_set - pending_from_reconciliation)
        if missing_in_queue:
            errors.append(
                f"{rel}: pending reconciliation candidates missing from queue: "
                + ", ".join(missing_in_queue)
            )
        if stale_in_queue:
            errors.append(
                f"{rel}: queue candidates no longer pending in reconciliation: "
                + ", ".join(stale_in_queue)
            )

    if not errors:
        print(
            f"OK: {rel} — page {page}, {len(candidate_ids)} pending candidates, "
            f"{len(categories)} disjoint categories."
        )
    return errors


def main() -> int:
    queue_paths = sorted(RECON.glob("p*_phase2_promotion_queue_*.json"))
    if not queue_paths:
        print("ERROR: no Phase II promotion queue files found", file=sys.stderr)
        return 2

    errors: list[str] = []
    for path in queue_paths:
        errors.extend(validate_queue(path))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"FAILED: {len(errors)} Phase II queue invariant error(s).", file=sys.stderr)
        return 1

    print(f"Phase II queue QA: validated {len(queue_paths)} queue file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
