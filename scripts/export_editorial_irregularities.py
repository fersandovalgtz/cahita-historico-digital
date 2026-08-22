#!/usr/bin/env python3
"""Export a deterministic post-v1 inventory of documented editorial irregularities in ALC1737."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_JSONL = "chd_editorial_irregularities.jsonl"
OUT_CSV = "chd_editorial_irregularities.csv"
MANIFEST = "manifest.json"
CANONICAL_VERSION = "1.0.0"
CANONICAL_TAG = "v1.0.0"
CANONICAL_TAG_COMMIT = "dbcdecf0003ac5a10ae963caf6babdcf5c22128d"

INPUTS = {
    "rule_closure": ROOT / "data/grammar/metadata/rule_numbering_closure.json",
    "rule_p052": ROOT / "data/grammar/metadata/rule_numbering_anomalies_p052.json",
    "rule_p066": ROOT / "data/grammar/metadata/rule_numbering_anomalies_p066.json",
    "rule_p107": ROOT / "data/grammar/metadata/rule_numbering_anomalies_p107.json",
    "sections": ROOT / "data/source/alc1737/sections.json",
    "p011": ROOT / "data/transcription/pages/ALC1737_p011.json",
    "p015": ROOT / "data/transcription/pages/ALC1737_p015.json",
    "p089": ROOT / "data/transcription/pages/ALC1737_p089.json",
    "p102": ROOT / "data/transcription/pages/ALC1737_p102.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def compact(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def authority() -> dict[str, bool]:
    return {
        "sourceDescriptionPreserved": True,
        "silentNormalizationPerformed": False,
        "silentRenumberingPerformed": False,
        "modernLinguisticInferencePerformed": False,
    }


def record(
    *,
    rid: str,
    category: str,
    title: str,
    digital: list[int],
    printed: list[int],
    evidence_files: list[str],
    source_text: list[str],
    evidence: str,
    treatment: str,
    structured: dict[str, Any] | None = None,
    review_status: str = "machine_corrected_unverified",
) -> dict[str, Any]:
    return {
        "id": rid,
        "sourceId": "ALC1737",
        "category": category,
        "title": title,
        "sourcePagesDigital": digital,
        "sourcePagesPrinted": printed,
        "evidenceFiles": evidence_files,
        "sourceText": source_text,
        "evidence": evidence,
        "editorialTreatment": treatment,
        "structuredData": structured or {},
        "authority": authority(),
        "reviewStatus": review_status,
        "humanVerified": False,
    }


def build_structural_conflict() -> dict[str, Any]:
    p11 = load(INPUTS["p011"])
    p15 = load(INPUTS["p015"])
    phrase_a = "obra tripartita"
    phrase_b = "quatro partes"
    if phrase_a not in p11.get("text", ""):
        raise SystemExit(f"expected phrase {phrase_a!r} not found in p011")
    if phrase_b not in p15.get("text", ""):
        raise SystemExit(f"expected phrase {phrase_b!r} not found in p015")
    return record(
        rid="ALC1737-irreg-structural-part-count",
        category="structural_self_description_conflict",
        title="Autodescripción tripartita frente a división en quatro partes",
        digital=[11, 15],
        printed=[1],
        evidence_files=[
            "data/transcription/pages/ALC1737_p011.json",
            "data/transcription/pages/ALC1737_p015.json",
        ],
        source_text=[phrase_a, phrase_b],
        evidence="Los preliminares describen la obra como tripartita, mientras el PROHEMIO declara que se dividirá en quatro partes.",
        treatment="Conservar ambas declaraciones como evidencia histórica; no armonizar retrospectivamente la arquitectura declarada de la obra.",
        structured={"declaredPartCounts": [3, 4]},
    )


def build_numbering_records() -> list[dict[str, Any]]:
    closure = load(INPUTS["rule_closure"])
    if closure.get("omittedPrintedNumbers") != [127, 178, 294]:
        raise SystemExit("rule-number closure no longer records expected omissions 127, 178, 294")
    if closure.get("duplicatedPrintedNumbers") != [129]:
        raise SystemExit("rule-number closure no longer records expected repetition 129")

    rows: list[dict[str, Any]] = []
    p52 = load(INPUTS["rule_p052"])
    for anomaly in p52.get("anomalies", []):
        kind = anomaly.get("type")
        number = anomaly.get("number")
        if kind == "printed_number_omission" and number == 127:
            rows.append(record(
                rid="ALC1737-irreg-rule-0127-omission",
                category="printed_number_omission",
                title="Omisión material del número de regla 127",
                digital=[52], printed=[38],
                evidence_files=["data/grammar/metadata/rule_numbering_anomalies_p052.json"],
                source_text=["126 → 128"], evidence=anomaly["evidence"],
                treatment=anomaly["editorialAction"],
                structured={"omittedRuleNumber": 127, "sourceRuleExistenceInferred": False},
            ))
        elif kind == "printed_number_repetition" and number == 129:
            rows.append(record(
                rid="ALC1737-irreg-rule-0129-repetition",
                category="printed_number_repetition",
                title="Duplicación material del número de regla 129",
                digital=[52, 53], printed=[38, 39],
                evidence_files=["data/grammar/metadata/rule_numbering_anomalies_p052.json"],
                source_text=["129", "129"], evidence=anomaly["evidence"],
                treatment=anomaly["editorialAction"],
                structured={"printedRuleNumber": 129, "occurrenceCount": 2, "objectIds": ["ALC1737-gr-0129a", "ALC1737-gr-0129b"]},
            ))

    p66 = load(INPUTS["rule_p066"])
    anomaly_178 = next((a for a in p66.get("anomalies", []) if a.get("number") == 178), None)
    if not anomaly_178:
        raise SystemExit("expected omission 178 not found in p066 anomaly metadata")
    rows.append(record(
        rid="ALC1737-irreg-rule-0178-omission",
        category="printed_number_omission",
        title="Omisión material del número de regla 178",
        digital=[65, 66], printed=[51, 52],
        evidence_files=["data/grammar/metadata/rule_numbering_anomalies_p066.json"],
        source_text=["177 → 179"], evidence=anomaly_178["evidence"],
        treatment=anomaly_178["editorialAction"],
        structured={"omittedRuleNumber": 178, "sourceRuleExistenceInferred": False},
    ))

    p107 = load(INPUTS["rule_p107"])
    if p107.get("omittedRuleNumber") != 294 or p107.get("observedSequence") != [293, 295]:
        raise SystemExit("expected omission 294 / sequence 293→295 not found in p107 metadata")
    rows.append(record(
        rid="ALC1737-irreg-rule-0294-omission",
        category="printed_number_omission",
        title="Omisión material del número de regla 294",
        digital=[106, 107], printed=[92, 93],
        evidence_files=["data/grammar/metadata/rule_numbering_anomalies_p107.json"],
        source_text=["293 → 295"], evidence=p107["evidence"]["interpretation"],
        treatment="Conservar el hueco material; no crear una regla 294 ni renumerar unidades vecinas.",
        structured={"omittedRuleNumber": 294, "observedSequence": [293, 295], "sourceRuleExistenceInferred": False},
    ))

    ids = {row["id"] for row in rows}
    expected = {
        "ALC1737-irreg-rule-0127-omission",
        "ALC1737-irreg-rule-0129-repetition",
        "ALC1737-irreg-rule-0178-omission",
        "ALC1737-irreg-rule-0294-omission",
    }
    if ids != expected:
        raise SystemExit(f"numbering irregularity set drift: got={sorted(ids)}")
    return rows


def build_boundary_records() -> list[dict[str, Any]]:
    sections = load(INPUTS["sections"])
    notes = sections.get("boundaryNotes", [])
    by_page = {item.get("digitalPage"): item for item in notes}
    rows: list[dict[str, Any]] = []
    for page, printed, before, after in ((69, 55, "part_ii", "part_iii"), (105, 91, "part_iii", "part_iv")):
        item = by_page.get(page)
        if not item or item.get("from") != before or item.get("to") != after:
            raise SystemExit(f"expected intra-page boundary missing or changed on digital page {page}")
        rows.append(record(
            rid=f"ALC1737-irreg-boundary-p{page:03d}",
            category="intra_page_section_boundary",
            title=f"Frontera de sección dentro de la página digital {page}",
            digital=[page], printed=[printed],
            evidence_files=["data/source/alc1737/sections.json"],
            source_text=[f"{before} → {after}"], evidence=item["evidence"],
            treatment="Representar ambas secciones dentro de la misma página y evitar asignación exclusiva de la página completa a una sola parte.",
            structured={"from": before, "to": after, "boundaryWithinPage": True},
        ))
    return rows


def find_uncertainty(page: dict[str, Any], token: str) -> dict[str, Any]:
    for item in page.get("uncertainties", []):
        if item.get("token") == token:
            return item
    raise SystemExit(f"expected uncertainty token {token!r} not found")


def build_ocr_disagreement_records() -> list[dict[str, Any]]:
    p89 = load(INPUTS["p089"])
    u242 = find_uncertainty(p89, "rule 242 numbering")
    if "242." not in p89.get("text", "") or "SEGUNDO MODO DE INFINITIVO" not in p89.get("text", ""):
        raise SystemExit("p089 no longer contains the visually collated rule 242 context")

    p102 = load(INPUTS["p102"])
    u282 = find_uncertainty(p102, "282")
    if "282." not in p102.get("text", ""):
        raise SystemExit("p102 no longer contains the visually collated rule 282")

    return [
        record(
            rid="ALC1737-irreg-ocr-rule-p089-0242",
            category="ocr_facsimile_disagreement",
            title="OCR 241 frente a cotejo visual 242",
            digital=[89], printed=[75],
            evidence_files=["data/transcription/pages/ALC1737_p089.json"],
            source_text=["SEGUNDO MODO DE INFINITIVO", "242."], evidence=u242["note"],
            treatment="Mantener 242 como lectura visual documentada y conservar el desacuerdo OCR como procedencia explícita.",
            structured={"ocrReading": 241, "facsimileReading": 242}, review_status="unresolved",
        ),
        record(
            rid="ALC1737-irreg-ocr-rule-p102-0282",
            category="ocr_facsimile_disagreement",
            title="OCR repite 281 frente a cotejo visual 282",
            digital=[102], printed=[88],
            evidence_files=["data/transcription/pages/ALC1737_p102.json"],
            source_text=["281.", "282."], evidence=u282["note"],
            treatment="Mantener 282 como lectura visual documentada y conservar la repetición 281 del OCR únicamente como discrepancia de capa.",
            structured={"ocrReading": 281, "facsimileReading": 282}, review_status="unresolved",
        ),
    ]


def build_records() -> list[dict[str, Any]]:
    rows = [build_structural_conflict()]
    rows.extend(build_numbering_records())
    rows.extend(build_boundary_records())
    rows.extend(build_ocr_disagreement_records())
    rows.sort(key=lambda row: row["id"])
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate irregularity IDs")
    if len(rows) != 9:
        raise SystemExit(f"expected 9 documented irregularities, got {len(rows)}")
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> bytes:
    data = ("\n".join(compact(row) for row in rows) + "\n").encode("utf-8")
    path.write_bytes(data)
    return data


def write_csv(path: Path, rows: list[dict[str, Any]]) -> bytes:
    fields = [
        "id", "sourceId", "category", "title", "sourcePagesDigital", "sourcePagesPrinted",
        "evidenceFiles", "sourceText", "evidence", "editorialTreatment", "reviewStatus", "humanVerified",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            flat = {key: row.get(key, "") for key in fields}
            for key in ("sourcePagesDigital", "sourcePagesPrinted", "evidenceFiles", "sourceText"):
                flat[key] = ";".join(str(value) for value in row.get(key, []))
            flat["humanVerified"] = "true" if row["humanVerified"] else "false"
            writer.writerow(flat)
    return path.read_bytes()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=ROOT / "build" / "editorial-irregularities")
    args = parser.parse_args()
    out_dir = args.out_dir if args.out_dir.is_absolute() else ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = build_records()
    payloads = {
        OUT_JSONL: write_jsonl(out_dir / OUT_JSONL, rows),
        OUT_CSV: write_csv(out_dir / OUT_CSV, rows),
    }
    category_counts = Counter(row["category"] for row in rows)
    pages = sorted({page for row in rows for page in row["sourcePagesDigital"]})
    human_verified = sum(1 for row in rows if row["humanVerified"] is True)
    canonical_inputs = sorted(path.relative_to(ROOT).as_posix() for path in INPUTS.values())
    manifest = {
        "sourceId": "ALC1737",
        "dataset": "post_v1_editorial_irregularities",
        "canonicalDatasetVersion": CANONICAL_VERSION,
        "canonicalTag": CANONICAL_TAG,
        "canonicalTagCommit": CANONICAL_TAG_COMMIT,
        "scope": "Derived inventory of documented editorial, numbering, structural-boundary and OCR/facsimile irregularities; it does not alter the diplomatic transcription or immutable v1 release.",
        "recordCount": len(rows),
        "categoryCounts": dict(sorted(category_counts.items())),
        "digitalPagesWithIrregularities": pages,
        "humanVerifiedRecordCount": human_verified,
        "authorityPolicy": {
            "sourceDescriptionPreserved": True,
            "silentNormalizationPerformed": False,
            "silentRenumberingPerformed": False,
            "modernLinguisticInferencePerformed": False,
            "humanVerificationElevatedByDerivative": False,
        },
        "canonicalInputCount": len(canonical_inputs),
        "canonicalInputs": canonical_inputs,
        "deterministic": True,
        "formats": {name: {"bytes": len(data), "sha256": sha256(data)} for name, data in sorted(payloads.items())},
    }
    manifest_bytes = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    (out_dir / MANIFEST).write_bytes(manifest_bytes)

    print(
        "editorial irregularities generated: "
        f"records={len(rows)}; categories={dict(sorted(category_counts.items()))}; "
        f"pages={pages}; humanVerified={human_verified}"
    )
    print(f"output: {out_dir}")


if __name__ == "__main__":
    main()
