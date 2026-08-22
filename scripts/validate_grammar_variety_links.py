#!/usr/bin/env python3
"""Validate deterministic explicit grammar-variety links and authority invariants."""
from __future__ import annotations

import filecmp
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "scripts" / "export_grammar_variety_links.py"
SCHEMA_VALIDATOR = ROOT / "scripts" / "validate_jsonl.py"
SCHEMA = ROOT / "schemas" / "post-v1" / "grammar-variety-link.schema.json"
EXPECTED_FILES = {
    "chd_grammar_variety_links.jsonl",
    "chd_grammar_variety_links.csv",
    "manifest.json",
}
REQUIRED_LINKS = {
    ("ALC1737-gr-0088", "Thehueco"),
    ("ALC1737-gr-0091", "Hiaqui"),
    ("ALC1737-gr-0091", "Mayo"),
    ("ALC1737-gr-0091", "Thehueco"),
    ("ALC1737-gr-0128", "Hiaqui"),
    ("ALC1737-gr-0128", "Mayo"),
    ("ALC1737-gr-0128", "Thehueco"),
    ("ALC1737-gr-0130", "Hiaqui"),
    ("ALC1737-gr-0130", "Mayo"),
    ("ALC1737-par-0002", "Hiaqui"),
    ("ALC1737-par-0002", "Mayo"),
    ("ALC1737-par-0002", "Thehueco"),
    ("ALC1737-par-0003", "Thehueco"),
    ("ALC1737-par-0003", "Naciones"),
}
LABEL_TOKEN_PATTERNS: dict[str, re.Pattern[str]] = {
    "Hiaqui": re.compile(r"hiaquis?", re.IGNORECASE),
    "Mayo": re.compile(r"(?:mayos?|mayes)", re.IGNORECASE),
    "Thehueco": re.compile(r"(?:thehuecos?|tehuecos?|teuecos?)", re.IGNORECASE),
    "Naciones": re.compile(r"naciones?", re.IGNORECASE),
    "Cynaloa": re.compile(r"(?:cynaloas?|sinaloas?)", re.IGNORECASE),
}


def run_export(out_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(EXPORTER), "--out-dir", str(out_dir)],
        cwd=ROOT,
        check=True,
    )


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSONL at {path}:{number}: {exc}") from exc
        if not isinstance(obj, dict):
            raise SystemExit(f"record at {path}:{number} is not an object")
        rows.append(obj)
    return rows


def compare_directories(a: Path, b: Path) -> None:
    a_files = {path.name for path in a.iterdir() if path.is_file()}
    b_files = {path.name for path in b.iterdir() if path.is_file()}
    if a_files != EXPECTED_FILES or b_files != EXPECTED_FILES:
        raise SystemExit(f"unexpected grammar-variety output set: a={sorted(a_files)} b={sorted(b_files)}")
    for name in sorted(EXPECTED_FILES):
        if not filecmp.cmp(a / name, b / name, shallow=False):
            raise SystemExit(f"grammar-variety export is not deterministic: {name}")


def validate_manifest(out_dir: Path) -> dict:
    manifest = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("canonicalDatasetVersion") != "1.0.0":
        raise SystemExit("grammar-variety manifest lost canonical v1 version")
    if manifest.get("canonicalTag") != "v1.0.0":
        raise SystemExit("grammar-variety manifest lost canonical tag")
    if manifest.get("canonicalTagCommit") != "dbcdecf0003ac5a10ae963caf6babdcf5c22128d":
        raise SystemExit("grammar-variety manifest lost immutable v1 anchor")
    if manifest.get("linkRecordCount", 0) <= 0:
        raise SystemExit("grammar-variety link layer is empty")
    if manifest.get("linkedGrammarObjectCount", 0) <= 0:
        raise SystemExit("grammar-variety layer links no grammar objects")
    evidence_count = manifest.get("historicalVariationGrammarEvidenceCount", 0)
    if evidence_count <= 0:
        raise SystemExit("grammar-variety layer reports no upstream grammar variation evidence")
    if manifest.get("linkedHistoricalVariationGrammarEvidenceCount") != evidence_count:
        raise SystemExit("not every upstream grammar historical-variation evidence row is linked")
    if manifest.get("unlinkedHistoricalVariationGrammarEvidenceCount") != 0:
        raise SystemExit("grammar-variety manifest reports unlinked explicit grammar evidence")
    if manifest.get("deterministic") is not True:
        raise SystemExit("grammar-variety manifest must declare deterministic=true")

    expected_policy = {
        "sourceAttributionRequired": True,
        "sameGrammarObjectEvidenceRequired": True,
        "pageProximityUsed": False,
        "linguisticSimilarityUsed": False,
        "modernIdentityInferred": False,
        "dialectTaxonomyInferred": False,
        "humanVerificationElevatedByDerivative": False,
    }
    if manifest.get("authorityPolicy") != expected_policy:
        raise SystemExit(f"grammar-variety authority policy drift: {manifest.get('authorityPolicy')}")
    return manifest


def validate_links(out_dir: Path, manifest: dict) -> None:
    rows = load_jsonl(out_dir / "chd_grammar_variety_links.jsonl")
    if len(rows) != manifest["linkRecordCount"]:
        raise SystemExit("link count differs from manifest")
    ids = [row.get("id") for row in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate grammar-variety link IDs")

    actual_pairs = {(row.get("grammarObjectId"), row.get("labelClass")) for row in rows}
    missing = sorted(REQUIRED_LINKS - actual_pairs)
    if missing:
        raise SystemExit(f"known explicit grammar-variety links missing: {missing}")

    evidence_ids: set[str] = set()
    for row in rows:
        if row.get("sourceAttributionExplicit") is not True:
            raise SystemExit(f"non-explicit grammar link detected: {row.get('id')}")
        for key in (
            "pageProximityUsed",
            "linguisticSimilarityUsed",
            "modernIdentityInferred",
            "dialectTaxonomyInferred",
            "humanVerified",
        ):
            if row.get(key) is not False:
                raise SystemExit(f"forbidden transition {key}=true in {row.get('id')}")

        label_class = row.get("labelClass")
        pattern = LABEL_TOKEN_PATTERNS.get(str(label_class))
        if pattern is None:
            raise SystemExit(f"unsupported labelClass in {row.get('id')}: {label_class!r}")
        raw_labels = row.get("labelsRaw") or []
        if not raw_labels:
            raise SystemExit(f"link has no raw documentary label: {row.get('id')}")
        for token in raw_labels:
            if not isinstance(token, str) or not pattern.fullmatch(token.strip()):
                raise SystemExit(
                    f"raw documentary label {token!r} does not belong to class {label_class!r} "
                    f"in {row.get('id')}"
                )

        upstream = row.get("historicalVariationEvidenceIds") or []
        if not upstream:
            raise SystemExit(f"link has no upstream historical-variation evidence: {row.get('id')}")
        evidence_ids.update(str(item) for item in upstream)

    if len(evidence_ids) != manifest["historicalVariationGrammarEvidenceCount"]:
        raise SystemExit(
            "unique upstream evidence count differs from manifest: "
            f"links={len(evidence_ids)} manifest={manifest['historicalVariationGrammarEvidenceCount']}"
        )

    paradigms = [row for row in rows if row.get("grammarObjectType") == "paradigm"]
    rules = [row for row in rows if row.get("grammarObjectType") == "rule"]
    if not paradigms:
        raise SystemExit("explicit link layer contains no paradigms")
    if not rules:
        raise SystemExit("explicit link layer contains no numbered rules")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="chd-gvl-a-") as a, tempfile.TemporaryDirectory(
        prefix="chd-gvl-b-"
    ) as b:
        first = Path(a)
        second = Path(b)
        run_export(first)
        run_export(second)
        compare_directories(first, second)
        manifest = validate_manifest(first)
        validate_links(first, manifest)
        subprocess.run(
            [
                sys.executable,
                str(SCHEMA_VALIDATOR),
                "--schema",
                str(SCHEMA),
                "--jsonl",
                str(first / "chd_grammar_variety_links.jsonl"),
            ],
            cwd=ROOT,
            check=True,
        )
        print(
            "grammar-variety link QA OK: "
            f"links={manifest['linkRecordCount']}; objects={manifest['linkedGrammarObjectCount']}; "
            f"upstreamGrammarEvidence={manifest['historicalVariationGrammarEvidenceCount']}; "
            f"types={manifest['grammarObjectTypeCounts']}; labels={manifest['labelClassCounts']}; "
            "unlinked=0; rawLabelsClassScoped=true; similarityUsed=false; humanVerified=0"
        )


if __name__ == "__main__":
    main()
