#!/usr/bin/env python3
"""Export a deterministic audit of numbered-rule coverage in data/grammar.

The audit records which source rule numbers (comparison universe 1..373) are
explicitly claimed by structured grammar objects. A number with no claim means
only that no current structured object declares coverage; it does *not* assert
that the historical source lacks that rule.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GRAMMAR_DIR = ROOT / "data/grammar"

JSONL_NAME = "chd_grammar_rule_coverage.jsonl"
CSV_NAME = "chd_grammar_rule_coverage.csv"
GAPS_NAME = "chd_grammar_rule_gap_ranges.json"
MANIFEST_NAME = "manifest.json"

MIN_RULE = 1
MAX_RULE = 373

CSV_FIELDS = [
    "ruleNumber",
    "coverageStatus",
    "objectCount",
    "objectIds",
    "objectTypes",
    "sourceFiles",
    "sourcePagesDigital",
    "sourcePagesPrinted",
    "reviewStatuses",
]


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def object_type(path: Path, obj: dict[str, Any]) -> str:
    object_id = obj.get("id")
    if isinstance(object_id, str) and object_id.startswith("ALC1737-"):
        parts = object_id.split("-")
        if len(parts) >= 3:
            return parts[1]
    stem = path.stem
    for prefix in (
        "rules_",
        "paradigms_",
        "modal_constructions_",
        "nonfinite_constructions_",
        "participles_",
        "predicative_modal_",
        "irregular_verbs_",
        "prepositions_",
        "adverbs_",
        "conjunctions_",
    ):
        if stem.startswith(prefix):
            return prefix.rstrip("_")
    return stem


def parse_rule_locator(obj: dict[str, Any]) -> tuple[list[int], str | None, str | None]:
    """Return explicit numbered rule claims plus raw locator and source field.

    Priority is given to ruleNumberNumeric, then ruleNumberRaw, then the leading
    numeric/range token of sourceRuleRange. We intentionally ignore page numbers
    embedded later in free text such as `293; continuation to p.107`.
    """
    numeric = obj.get("ruleNumberNumeric")
    if isinstance(numeric, int):
        return [numeric], str(numeric), "ruleNumberNumeric"

    raw_number = obj.get("ruleNumberRaw")
    if isinstance(raw_number, str) and raw_number.strip():
        token = raw_number.strip()
        if token.isdigit():
            return [int(token)], raw_number, "ruleNumberRaw"

    raw_range = obj.get("sourceRuleRange")
    if isinstance(raw_range, str) and raw_range.strip():
        raw = raw_range.strip()
        leading = raw.split(";", 1)[0].split("(", 1)[0].strip()
        if leading.casefold().startswith("post-"):
            return [], raw_range, "sourceRuleRange"
        match = re.fullmatch(r"(\d{1,3})(?:\s*[-–]\s*(\d{1,3}))?", leading)
        if match:
            start = int(match.group(1))
            end = int(match.group(2) or start)
            if end < start:
                raise SystemExit(f"descending sourceRuleRange is not supported: {raw_range!r}")
            return list(range(start, end + 1)), raw_range, "sourceRuleRange"
        return [], raw_range, "sourceRuleRange"

    return [], None, None


def read_objects() -> tuple[list[dict[str, Any]], list[str]]:
    rows: list[dict[str, Any]] = []
    source_files: list[str] = []

    for path in sorted(GRAMMAR_DIR.iterdir()):
        if not path.is_file() or path.suffix not in {".json", ".jsonl"}:
            continue
        relative = path.relative_to(ROOT).as_posix()
        source_files.append(relative)
        if path.suffix == ".jsonl":
            payloads: list[tuple[int, dict[str, Any]]] = []
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise SystemExit(f"invalid JSON in {path}:{line_number}: {exc}") from exc
                if not isinstance(obj, dict):
                    raise SystemExit(f"non-object JSONL row in {path}:{line_number}")
                payloads.append((line_number, obj))
        else:
            try:
                parsed = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"invalid JSON in {path}: {exc}") from exc
            if not isinstance(parsed, dict):
                raise SystemExit(f"top-level grammar JSON must be object: {path}")
            payloads = [(1, parsed)]

        for record_number, obj in payloads:
            rules, locator_raw, locator_field = parse_rule_locator(obj)
            pages_digital = obj.get("sourcePagesDigital")
            if pages_digital is None and isinstance(obj.get("sourcePageDigital"), int):
                pages_digital = [obj["sourcePageDigital"]]
            pages_printed = obj.get("sourcePagesPrinted")
            if pages_printed is None and isinstance(obj.get("sourcePagePrinted"), int):
                pages_printed = [obj["sourcePagePrinted"]]
            rows.append(
                {
                    "objectId": obj.get("id") or f"{relative}#record-{record_number}",
                    "sourceFile": relative,
                    "sourceRecord": record_number,
                    "objectType": object_type(path, obj),
                    "ruleNumbers": rules,
                    "ruleLocatorRaw": locator_raw,
                    "ruleLocatorField": locator_field,
                    "sourcePagesDigital": pages_digital if isinstance(pages_digital, list) else [],
                    "sourcePagesPrinted": pages_printed if isinstance(pages_printed, list) else [],
                    "reviewStatus": obj.get("reviewStatus"),
                    "humanVerified": obj.get("humanVerified"),
                }
            )

    return rows, source_files


def unique_sorted(values: list[Any]) -> list[Any]:
    return sorted({value for value in values if value is not None})


def build_audit() -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    objects, source_files = read_objects()
    coverage: dict[int, list[dict[str, Any]]] = defaultdict(list)
    outside_universe: list[dict[str, Any]] = []

    for obj in objects:
        for rule in obj["ruleNumbers"]:
            if MIN_RULE <= rule <= MAX_RULE:
                coverage[rule].append(obj)
            else:
                outside_universe.append(
                    {
                        "objectId": obj["objectId"],
                        "ruleNumber": rule,
                        "sourceFile": obj["sourceFile"],
                        "ruleLocatorRaw": obj["ruleLocatorRaw"],
                    }
                )

    audit_rows: list[dict[str, Any]] = []
    for rule in range(MIN_RULE, MAX_RULE + 1):
        claims = sorted(
            coverage.get(rule, []),
            key=lambda item: (item["sourceFile"], item["sourceRecord"], item["objectId"]),
        )
        audit_rows.append(
            {
                "ruleNumber": rule,
                "coverageStatus": "structured_claim" if claims else "no_structured_object_claim",
                "objectCount": len(claims),
                "objectIds": [item["objectId"] for item in claims],
                "objectTypes": unique_sorted([item["objectType"] for item in claims]),
                "sourceFiles": unique_sorted([item["sourceFile"] for item in claims]),
                "sourcePagesDigital": unique_sorted(
                    [page for item in claims for page in item["sourcePagesDigital"]]
                ),
                "sourcePagesPrinted": unique_sorted(
                    [page for item in claims for page in item["sourcePagesPrinted"]]
                ),
                "reviewStatuses": unique_sorted([item["reviewStatus"] for item in claims]),
                "claims": [
                    {
                        "objectId": item["objectId"],
                        "objectType": item["objectType"],
                        "sourceFile": item["sourceFile"],
                        "sourceRecord": item["sourceRecord"],
                        "ruleLocatorField": item["ruleLocatorField"],
                        "ruleLocatorRaw": item["ruleLocatorRaw"],
                        "sourcePagesDigital": item["sourcePagesDigital"],
                        "sourcePagesPrinted": item["sourcePagesPrinted"],
                        "reviewStatus": item["reviewStatus"],
                        "humanVerified": item["humanVerified"],
                    }
                    for item in claims
                ],
            }
        )

    uncovered = [row["ruleNumber"] for row in audit_rows if row["objectCount"] == 0]
    gap_ranges: list[dict[str, int]] = []
    if uncovered:
        start = previous = uncovered[0]
        for rule in uncovered[1:]:
            if rule == previous + 1:
                previous = rule
                continue
            gap_ranges.append({"start": start, "end": previous, "count": previous - start + 1})
            start = previous = rule
        gap_ranges.append({"start": start, "end": previous, "count": previous - start + 1})

    objects_without_rule_claim = [obj for obj in objects if not obj["ruleNumbers"]]
    object_type_counts = Counter(obj["objectType"] for obj in objects)
    claim_object_type_counts = Counter(
        obj["objectType"] for obj in objects if obj["ruleNumbers"]
    )

    summary = {
        "sourceId": "ALC1737",
        "comparisonUniverse": {"minRule": MIN_RULE, "maxRule": MAX_RULE, "ruleCount": MAX_RULE},
        "grammarObjectCount": len(objects),
        "grammarFileCount": len(source_files),
        "rulesWithStructuredClaim": sum(row["objectCount"] > 0 for row in audit_rows),
        "rulesWithoutStructuredClaim": len(uncovered),
        "coverageFraction": sum(row["objectCount"] > 0 for row in audit_rows) / MAX_RULE,
        "gapRangeCount": len(gap_ranges),
        "objectsWithoutExplicitRuleClaim": len(objects_without_rule_claim),
        "objectTypeCounts": dict(sorted(object_type_counts.items())),
        "claimObjectTypeCounts": dict(sorted(claim_object_type_counts.items())),
        "outsideComparisonUniverseClaimCount": len(outside_universe),
    }

    gaps = {
        "sourceId": "ALC1737",
        "semantics": "Ranges where no current structured grammar object explicitly claims the numbered rule; this does not assert source omission.",
        "comparisonUniverse": summary["comparisonUniverse"],
        "gapRanges": gap_ranges,
        "objectsWithoutExplicitRuleClaim": [
            {
                "objectId": obj["objectId"],
                "objectType": obj["objectType"],
                "sourceFile": obj["sourceFile"],
                "sourceRecord": obj["sourceRecord"],
                "ruleLocatorRaw": obj["ruleLocatorRaw"],
                "ruleLocatorField": obj["ruleLocatorField"],
                "sourcePagesDigital": obj["sourcePagesDigital"],
                "sourcePagesPrinted": obj["sourcePagesPrinted"],
                "reviewStatus": obj["reviewStatus"],
            }
            for obj in objects_without_rule_claim
        ],
        "claimsOutsideComparisonUniverse": outside_universe,
    }
    return audit_rows, summary, gaps


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact_json(row) for row in rows) + "\n").encode("utf-8")
    path.write_bytes(data)
    return data


def csv_value(value: Any) -> Any:
    if isinstance(value, (list, dict)):
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
        default=ROOT / "build/grammar-rule-coverage",
        help="Directory for deterministic grammar rule-coverage audit outputs.",
    )
    args = parser.parse_args()

    rows, summary, gaps = build_audit()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    gap_bytes = (json.dumps(gaps, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    payloads = {
        JSONL_NAME: write_jsonl(args.out_dir / JSONL_NAME, rows),
        CSV_NAME: write_csv(args.out_dir / CSV_NAME, rows),
        GAPS_NAME: gap_bytes,
    }
    (args.out_dir / GAPS_NAME).write_bytes(gap_bytes)

    source_files = sorted(path.relative_to(ROOT).as_posix() for path in GRAMMAR_DIR.iterdir() if path.is_file() and path.suffix in {".json", ".jsonl"})
    manifest = {
        "sourceId": "ALC1737",
        "dataset": "grammar_numbered_rule_coverage_audit",
        "derivation": "explicit rule-number claims from canonical data/grammar objects",
        **summary,
        "absenceSemantics": "no_structured_object_claim means only that the current structured layer does not explicitly claim the rule number; it does not assert historical-source absence",
        "sourceRuleExistenceInferred": False,
        "ruleContentInferred": False,
        "implicitCoverageInferred": False,
        "canonicalGrammarModified": False,
        "deterministic": True,
        "canonicalInputs": source_files,
        "formats": {
            name: {"bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(payloads.items())
        },
    }
    (args.out_dir / MANIFEST_NAME).write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )

    for name, metadata in manifest["formats"].items():
        actual = (args.out_dir / name).read_bytes()
        if len(actual) != metadata["bytes"] or sha256_bytes(actual) != metadata["sha256"]:
            raise SystemExit(f"post-write integrity check failed for {name}")

    if len(rows) != MAX_RULE:
        raise SystemExit(f"expected {MAX_RULE} rule rows, got {len(rows)}")

    print(
        "exported grammar rule-coverage audit: "
        f"{summary['rulesWithStructuredClaim']}/{MAX_RULE} rules with explicit structured claims; "
        f"{summary['rulesWithoutStructuredClaim']} without claims; "
        f"{summary['objectsWithoutExplicitRuleClaim']} objects without explicit rule locator; "
        f"gap ranges={summary['gapRangeCount']}; outputs in {args.out_dir}"
    )
    for name, metadata in manifest["formats"].items():
        print(f"  {name}: {metadata['bytes']} bytes; sha256 {metadata['sha256']}")


if __name__ == "__main__":
    main()
