#!/usr/bin/env python3
"""Validate CHD's deterministic experimental TEI lexical projection.

This validator checks well-formed XML and CHD project invariants. It does not
claim external TEI Lex-0 schema validation.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEI_NS = "http://www.tei-c.org/ns/1.0"
XML_NS = "http://www.w3.org/XML/1998/namespace"
NS = {"tei": TEI_NS}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_export(out_dir: Path) -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/export_lexicon_tei.py"), "--out-dir", str(out_dir)],
        cwd=ROOT,
        check=True,
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        first = base / "run1"
        second = base / "run2"
        run_export(first)
        run_export(second)

        names1 = sorted(p.name for p in first.iterdir() if p.is_file())
        names2 = sorted(p.name for p in second.iterdir() if p.is_file())
        if names1 != names2:
            raise SystemExit("TEI export file-set mismatch across deterministic runs")
        for name in names1:
            if (first / name).read_bytes() != (second / name).read_bytes():
                raise SystemExit(f"TEI export is not deterministic for {name}")

        manifest = json.loads((first / "manifest.json").read_text(encoding="utf-8"))
        xml_path = first / "chd_lexicon_tei.xml"
        tree = ET.parse(xml_path)
        root = tree.getroot()

        if root.tag != f"{{{TEI_NS}}}TEI":
            raise SystemExit("TEI export root is not TEI in the TEI namespace")
        if root.get("type") != "dictionary":
            raise SystemExit("TEI export must declare TEI/@type=dictionary")
        if root.get(f"{{{XML_NS}}}lang") != "es":
            raise SystemExit("TEI export root must declare xml:lang=es")

        entries = root.findall(".//tei:entry", NS)
        if len(entries) != manifest["articleCount"]:
            raise SystemExit("TEI entry count disagrees with manifest")
        if manifest["articleCount"] != 2302:
            raise SystemExit(f"unexpected canonical TEI article count: {manifest['articleCount']}")

        ids = [entry.get(f"{{{XML_NS}}}id") for entry in entries]
        if any(not value for value in ids):
            raise SystemExit("TEI entry missing xml:id")
        if len(set(ids)) != len(ids):
            raise SystemExit("duplicate TEI entry xml:id")
        if any(entry.get("type") != "mainEntry" for entry in entries):
            raise SystemExit("all CHD TEI lexical entries must use type=mainEntry")
        if any(entry.get(f"{{{XML_NS}}}lang") != "es" for entry in entries):
            raise SystemExit("all CHD TEI lexical entries must preserve Spanish guide language")

        orths = root.findall(".//tei:entry/tei:form[@type='lemma']/tei:orth", NS)
        if len(orths) != len(entries):
            raise SystemExit("every TEI entry must contain exactly one lemma orthography")

        citations = root.findall(".//tei:cit[@type='translation']", NS)
        if len(citations) != manifest["translationCitationCount"]:
            raise SystemExit("TEI translation citation count disagrees with manifest")
        quotes = root.findall(".//tei:cit[@type='translation']/tei:quote", NS)
        if len(quotes) != len(citations):
            raise SystemExit("each translation citation must contain one quote")
        if any(quote.get(f"{{{XML_NS}}}lang") != "und" for quote in quotes):
            raise SystemExit("historical Cahita forms must remain xml:lang=und in this profile")

        xrs = root.findall(".//tei:xr", NS)
        refs = root.findall(".//tei:xr/tei:ref", NS)
        if len(xrs) != manifest["crossReferenceCount"] or len(refs) != len(xrs):
            raise SystemExit("TEI cross-reference count disagrees with manifest")
        if manifest["crossReferenceCount"] != 150:
            raise SystemExit("canonical TEI projection must contain 150 Buſca cross-references")

        targeted = [ref for ref in refs if ref.get("target")]
        if len(targeted) != manifest["strictTargetedCrossReferenceCount"]:
            raise SystemExit("TEI strict target count disagrees with manifest")
        if len(targeted) != 60:
            raise SystemExit("TEI projection must expose exactly 60 strict exact @target pointers")
        valid_ids = set(ids)
        for ref in targeted:
            target = ref.get("target")
            if not target or not target.startswith("#") or target[1:] not in valid_ids:
                raise SystemExit(f"TEI @target does not resolve to an exported entry: {target}")

        for key in (
            "teiLex0ConformanceClaimed",
            "externalLex0SchemaValidationPerformed",
            "modernLanguageIdentityInferred",
            "editorialCrossReferenceEdgesIncluded",
            "fuzzyCrossReferenceTargetsIncluded",
            "semanticEquivalenceInferred",
            "borrowingInferred",
        ):
            if manifest[key] is not False:
                raise SystemExit(f"TEI non-inference/conformance guard must remain false: {key}")
        if manifest["strictExactTargetsIncluded"] is not True:
            raise SystemExit("TEI strictExactTargetsIncluded must be true")
        if manifest["sourceTranscriptionPreserved"] is not True:
            raise SystemExit("TEI sourceTranscriptionPreserved must be true")
        if manifest["deterministic"] is not True:
            raise SystemExit("TEI export manifest must declare deterministic=true")

        print(
            "TEI lexical projection QA OK: "
            f"entries={len(entries)}; translations={len(citations)}; "
            f"crossRefs={len(refs)}; strictTargets={len(targeted)}; "
            f"xmlSha256={sha256(xml_path)}; Lex0ConformanceClaimed=false"
        )


if __name__ == "__main__":
    main()
