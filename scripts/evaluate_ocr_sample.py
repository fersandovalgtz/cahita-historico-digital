#!/usr/bin/env python3
"""Evaluate OCR on a small stratified ALC1737 sample.

This is a process-quality diagnostic, not philological validation. References are
visual transcriptions selected for the evaluation file. The default
normalization maps long-s to s, removes combining marks, lowercases, replaces
punctuation by spaces, and collapses whitespace.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import unicodedata
from pathlib import Path

from extract_vocab_layout import extract_page


def normalize(text: str) -> str:
    text = text.replace("ſ", "s")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def levenshtein(a, b) -> int:
    prev = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(cur[-1] + 1, prev[j] + 1, prev[j - 1] + (x != y)))
        prev = cur
    return prev[-1]


def best_token_window(reference_words: list[str], ocr_words: list[str]):
    n = len(reference_words)
    best = None
    for size in range(max(1, n - 8), n + 13):
        if size > len(ocr_words):
            continue
        for start in range(0, len(ocr_words) - size + 1):
            window = ocr_words[start : start + size]
            distance = levenshtein(reference_words, window)
            score = distance / max(1, n)
            if best is None or score < best[0]:
                best = (score, distance, start, window)
    if best is None:
        return 1.0, n, 0, []
    return best


def raw_ocr(pdf: Path, page: int, source: str) -> str:
    if source == "pdftotext_layout":
        return subprocess.check_output(
            ["pdftotext", "-f", str(page), "-l", str(page), "-layout", str(pdf), "-"]
        ).decode("utf-8", "replace")
    if source == "bbox_left_column":
        records = extract_page(pdf, page)
        return " ".join(r["text_raw"] for r in records if r["column"] == "left")
    raise ValueError(f"unsupported ocrSource: {source}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True, type=Path)
    ap.add_argument("--references", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    spec = json.loads(args.references.read_text(encoding="utf-8"))
    results = []

    for sample in spec["samples"]:
        page = int(sample["page"])
        reference_norm = normalize(sample["reference"])
        ocr_norm = normalize(raw_ocr(args.pdf, page, sample["ocrSource"]))
        ref_words, ocr_words = reference_norm.split(), ocr_norm.split()
        _, word_edits, _, window = best_token_window(ref_words, ocr_words)
        ocr_window = " ".join(window)
        char_edits = levenshtein(list(reference_norm), list(ocr_window))
        results.append(
            {
                "id": sample["id"],
                "page": page,
                "ocrSource": sample["ocrSource"],
                "referenceWords": len(ref_words),
                "referenceChars": len(reference_norm),
                "wordEdits": word_edits,
                "charEdits": char_edits,
                "wer": word_edits / max(1, len(ref_words)),
                "cer": char_edits / max(1, len(reference_norm)),
                "referenceNormalized": reference_norm,
                "ocrWindowNormalized": ocr_window,
            }
        )

    summary = {
        "sampleCount": len(results),
        "macroWER": sum(r["wer"] for r in results) / len(results),
        "macroCER": sum(r["cer"] for r in results) / len(results),
        "microWER": sum(r["wordEdits"] for r in results)
        / sum(r["referenceWords"] for r in results),
        "microCER": sum(r["charEdits"] for r in results)
        / sum(r["referenceChars"] for r in results),
    }
    payload = {
        "sourceId": spec.get("sourceId", "ALC1737"),
        "normalization": spec.get("normalization"),
        "summary": summary,
        "results": results,
        "caveat": "Diagnostic sample only; reference transcription is AI-assisted visual collation and has no independent human verification.",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
