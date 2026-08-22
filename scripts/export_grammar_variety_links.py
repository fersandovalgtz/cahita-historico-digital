#!/usr/bin/env python3
"""Export deterministic post-v1 links between grammar objects and explicit historical-variety evidence.

Links are created only from grammar-layer records already admitted by the CHD
historical-variation derivative. No page proximity, linguistic similarity,
cognacy, or modern language identity is used to create a relation.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
GRAMMAR_DIR = ROOT / "data" / "grammar"
VARIATION_EXPORTER = ROOT / "scripts" / "export_historical_variation_index.py"

OUT_JSONL = "chd_grammar_variety_links.jsonl"
OUT_CSV = "chd_grammar_variety_links.csv"
MANIFEST = "manifest.json"
CANONICAL_VERSION = "1.0.0"
CANONICAL_TAG = "v1.0.0"
CANONICAL_TAG_COMMIT = "dbcdecf0003ac5a10ae963caf6babdcf5c22128d"

LABEL_TOKEN_PATTERNS: dict[str, re.Pattern[str]] = {
    "Hiaqui": re.compile(r"hiaquis?", re.IGNORECASE),
    "Mayo": re.compile(r"(?:mayos?|mayes)", re.IGNORECASE),
    "Thehueco": re.compile(r"(?:thehuecos?|tehuecos?|teuecos?)", re.IGNORECASE),
    "Naciones": re.compile(r"naciones?", re.IGNORECASE),
    "Cynaloa": re.compile(r"(?:cynaloas?|sinaloas?)", re.IGNORECASE),
}


def compact(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def object_identifier(obj: dict[str, Any], path: Path, object_index: int) -> str:
    for key in ("id", "objectId", "ruleId", "paradigmId", "constructionId", "articleId"):
        value = obj.get(key)
        if isinstance(value, str) and value:
            return value
    return f"{path.stem}:object:{object_index}"


def read_objects(path: Path) -> list[dict[str, Any]]:
    if path.suffix == ".json":
        parsed = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(parsed, dict):
            return [parsed]
        if isinstance(parsed, list):
            return [item for item in parsed if isinstance(item, dict)]
        return []
    objects: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            item = json.loads(line)
            if isinstance(item, dict):
                objects.append(item)
    return objects


def grammar_index() -> tuple[dict[tuple[str, str], dict[str, Any]], list[str]]:
    found: dict[tuple[str, str], dict[str, Any]] = {}
    inputs: list[str] = []
    for path in sorted(
        p for p in GRAMMAR_DIR.rglob("*") if p.is_file() and p.suffix in {".json", ".jsonl"}
    ):
        rel = path.relative_to(ROOT).as_posix()
        inputs.append(rel)
        for index, obj in enumerate(read_objects(path), start=1):
            object_id = object_identifier(obj, path, index)
            key = (rel, object_id)
            if key in found:
                raise SystemExit(f"duplicate grammar object key: {key}")
            found[key] = obj
    return found, inputs


def pages(obj: dict[str, Any], plural_key: str, singular_key: str) -> list[int]:
    value = obj.get(plural_key)
    if isinstance(value, list):
        return sorted({int(item) for item in value if isinstance(item, int)})
    singular = obj.get(singular_key)
    if isinstance(singular, int):
        return [singular]
    range_key = "pageRangeDigital" if "Digital" in plural_key else "pageRangePrinted"
    page_range = obj.get(range_key)
    if isinstance(page_range, list) and len(page_range) == 2 and all(isinstance(item, int) for item in page_range):
        return list(range(page_range[0], page_range[1] + 1))
    return []


def rule_numbers(obj: dict[str, Any]) -> list[int]:
    values: set[int] = set()
    single = obj.get("ruleNumberNumeric")
    if isinstance(single, int):
        values.add(single)
    for key in ("sourceRuleNumbers", "ruleNumbers"):
        candidate = obj.get(key)
        if isinstance(candidate, list):
            values.update(item for item in candidate if isinstance(item, int))
    start = obj.get("ruleNumberStart")
    end = obj.get("ruleNumberEnd")
    if isinstance(start, int) and isinstance(end, int) and start <= end:
        values.update(range(start, end + 1))
    return sorted(values)


def object_type(obj: dict[str, Any], source_path: str) -> str:
    object_id = str(obj.get("id") or "")
    if object_id.startswith("ALC1737-par-") or "paradigmType" in obj:
        return "paradigm"
    if isinstance(obj.get("ruleNumberNumeric"), int):
        return "rule"
    if source_path.endswith("numerals_p178_p180.json"):
        return "numeral_system"
    if obj.get("constructionId") or "constructionType" in obj:
        return "construction"
    return "grammar_object"


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", text.casefold()).strip("-")
    return value or "label"


def raw_labels_for_class(members: list[dict[str, Any]], label_class: str) -> list[str]:
    pattern = LABEL_TOKEN_PATTERNS.get(label_class)
    if pattern is None:
        raise SystemExit(f"unsupported grammar historical label class: {label_class}")
    tokens = {
        token.strip()
        for row in members
        for token in (row.get("labelsRaw") or [])
        if isinstance(token, str) and pattern.fullmatch(token.strip())
    }
    if not tokens:
        raise SystemExit(
            f"grammar-variety link {label_class} has no class-specific raw source label after filtering"
        )
    return sorted(tokens)


def run_variation(out_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(VARIATION_EXPORTER), "--out-dir", str(out_dir)],
        cwd=ROOT,
        check=True,
    )


def load_variation_grammar_evidence(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        if obj.get("sourceLayer") != "grammar":
            continue
        if obj.get("attributionExplicit") is not True:
            raise SystemExit(f"grammar variation evidence lost explicit attribution: {obj.get('evidenceId')}")
        if obj.get("modernIdentityInferred") is not False:
            raise SystemExit(f"modern identity inference detected: {obj.get('evidenceId')}")
        rows.append(obj)
    if not rows:
        raise SystemExit("historical variation derivative contains no grammar evidence")
    return rows


def build_links(evidence_rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    objects, grammar_inputs = grammar_index()
    grouped: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    unlinked: list[str] = []

    for row in evidence_rows:
        source_path = row.get("sourcePath")
        object_id = row.get("objectId")
        if not isinstance(source_path, str) or not isinstance(object_id, str):
            unlinked.append(str(row.get("evidenceId")))
            continue
        if (source_path, object_id) not in objects:
            unlinked.append(str(row.get("evidenceId")))
            continue
        classes = row.get("labelClasses") or []
        if not classes:
            unlinked.append(str(row.get("evidenceId")))
            continue
        for label_class in classes:
            grouped[(source_path, object_id, str(label_class))].append(row)

    links: list[dict[str, Any]] = []
    for (source_path, object_id, label_class), members in sorted(grouped.items()):
        obj = objects[(source_path, object_id)]
        raw_labels = raw_labels_for_class(members, label_class)
        texts = sorted({text for row in members if isinstance((text := row.get("sourceText")), str) and text})
        evidence_ids = sorted(str(row["evidenceId"]) for row in members)
        digital = pages(obj, "sourcePagesDigital", "sourcePageDigital")
        printed = pages(obj, "sourcePagesPrinted", "sourcePagePrinted")
        rules = rule_numbers(obj)
        review = obj.get("reviewStatus") if isinstance(obj.get("reviewStatus"), str) else None
        link_id = f"ALC1737-gvl-{slug(object_id)}-{slug(label_class)}"
        links.append(
            {
                "id": link_id,
                "sourceId": "ALC1737",
                "grammarObjectId": object_id,
                "grammarObjectType": object_type(obj, source_path),
                "grammarSourcePath": source_path,
                "ruleNumbers": rules,
                "sourcePagesDigital": digital,
                "sourcePagesPrinted": printed,
                "section": obj.get("part") or obj.get("section"),
                "labelClass": label_class,
                "labelsRaw": raw_labels,
                "relationType": "explicit_source_attribution_in_same_grammar_object",
                "historicalVariationEvidenceIds": evidence_ids,
                "evidenceTexts": texts,
                "sourceAttributionExplicit": True,
                "pageProximityUsed": False,
                "linguisticSimilarityUsed": False,
                "modernIdentityInferred": False,
                "dialectTaxonomyInferred": False,
                "reviewStatus": review,
                "humanVerified": False,
            }
        )

    ids = [row["id"] for row in links]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate grammar-variety link IDs")

    linked_evidence = {eid for link in links for eid in link["historicalVariationEvidenceIds"]}
    all_evidence = {str(row["evidenceId"]) for row in evidence_rows}
    missing = sorted(all_evidence - linked_evidence)
    if unlinked or missing:
        raise SystemExit(
            "not all explicit grammar historical-variation evidence was linked; "
            f"unlinked={sorted(set(unlinked))}; missing={missing}"
        )

    summary = {
        "historicalVariationGrammarEvidenceCount": len(evidence_rows),
        "linkedHistoricalVariationGrammarEvidenceCount": len(linked_evidence),
        "unlinkedHistoricalVariationGrammarEvidenceCount": 0,
        "grammarInputCount": len(grammar_inputs),
        "grammarInputs": grammar_inputs,
    }
    return links, summary


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact(row) for row in rows) + ("\n" if rows else "")).encode("utf-8")
    path.write_bytes(data)
    return data


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    fields = [
        "id", "grammarObjectId", "grammarObjectType", "grammarSourcePath", "ruleNumbers",
        "sourcePagesDigital", "sourcePagesPrinted", "section", "labelClass", "labelsRaw",
        "relationType", "historicalVariationEvidenceIds", "evidenceTexts", "reviewStatus", "humanVerified",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            flat = {key: row.get(key, "") for key in fields}
            for key in (
                "ruleNumbers", "sourcePagesDigital", "sourcePagesPrinted", "labelsRaw",
                "historicalVariationEvidenceIds", "evidenceTexts",
            ):
                flat[key] = ";".join(str(value) for value in row.get(key, []))
            flat["humanVerified"] = "true" if row.get("humanVerified") else "false"
            writer.writerow(flat)
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=ROOT / "build" / "grammar-variety-links")
    args = parser.parse_args()
    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="chd-gvl-variation-") as temp:
        variation_dir = Path(temp)
        run_variation(variation_dir)
        evidence = load_variation_grammar_evidence(variation_dir / "chd_historical_variation_index.jsonl")
        links, summary = build_links(evidence)

    payloads = {
        OUT_JSONL: write_jsonl(out_dir / OUT_JSONL, links),
        OUT_CSV: write_csv(out_dir / OUT_CSV, links),
    }
    type_counts = Counter(row["grammarObjectType"] for row in links)
    label_counts = Counter(row["labelClass"] for row in links)
    linked_objects = sorted({row["grammarObjectId"] for row in links})
    linked_rule_numbers = sorted({number for row in links for number in row["ruleNumbers"]})
    manifest = {
        "sourceId": "ALC1737",
        "dataset": "post_v1_explicit_grammar_variety_links",
        "canonicalDatasetVersion": CANONICAL_VERSION,
        "canonicalTag": CANONICAL_TAG,
        "canonicalTagCommit": CANONICAL_TAG_COMMIT,
        "derivation": (
            "Exact object-level join from explicit grammar evidence already admitted by the CHD historical-variation derivative; "
            "no page-proximity or linguistic-similarity linking."
        ),
        "linkRecordCount": len(links),
        "linkedGrammarObjectCount": len(linked_objects),
        "linkedGrammarObjectIds": linked_objects,
        "linkedRuleNumbers": linked_rule_numbers,
        "grammarObjectTypeCounts": dict(sorted(type_counts.items())),
        "labelClassCounts": dict(sorted(label_counts.items())),
        **summary,
        "authorityPolicy": {
            "sourceAttributionRequired": True,
            "sameGrammarObjectEvidenceRequired": True,
            "pageProximityUsed": False,
            "linguisticSimilarityUsed": False,
            "modernIdentityInferred": False,
            "dialectTaxonomyInferred": False,
            "humanVerificationElevatedByDerivative": False,
        },
        "deterministic": True,
        "formats": {name: {"bytes": len(data), "sha256": sha256(data)} for name, data in sorted(payloads.items())},
    }
    (out_dir / MANIFEST).write_text(
        json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        "grammar-variety links generated: "
        f"links={len(links)}; objects={len(linked_objects)}; "
        f"grammarEvidence={summary['historicalVariationGrammarEvidenceCount']}; "
        f"labels={dict(sorted(label_counts.items()))}; unlinked=0"
    )
    print(f"output: {out_dir}")


if __name__ == "__main__":
    main()
