# Cahíta Histórico Digital

**Historical-digital edition, open corpus and reproducible research infrastructure for the _Arte de la lengua cahita_ printed in Mexico in 1737.**

[![Release](https://img.shields.io/github/v/release/fersandovalgtz/cahita-historico-digital?style=flat-square&label=release)](https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0)
[![CI](https://img.shields.io/github/actions/workflow/status/fersandovalgtz/cahita-historico-digital/qa.yml?branch=main&style=flat-square&label=CI)](https://github.com/fersandovalgtz/cahita-historico-digital/actions/workflows/qa.yml)
![Lexical articles](https://img.shields.io/badge/lexical%20articles-2%2C302-172033?style=flat-square)
![Grammar evidence](https://img.shields.io/badge/grammar%20evidence-1%2C215-455B55?style=flat-square)
![TEI](https://img.shields.io/badge/TEI-Lex--0%200.9.5-8A1538?style=flat-square)
[![CLDF](https://img.shields.io/badge/CLDF-Dictionary%20post--v1-5b4b8a?style=flat-square)](CLDF.md)
![Human verified](https://img.shields.io/badge/humanVerified-0-b7791f?style=flat-square)
![DOI](https://img.shields.io/badge/DOI-pending-b7791f?style=flat-square)

[Español](README.md) · [v1.0.0 release](https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0) · [Data products](docs/DATA_PRODUCTS.md) · [CLDF](CLDF.md) · [Data model](SCHEMA.md) · [Provenance](PROVENANCE.md) · [FAIR pre-assessment](FAIR_ASSESSMENT.md) · [Governance](GOVERNANCE.md) · [How to cite](CITATION.cff)

## What this repository is

Cahíta Histórico Digital (CHD) is a research infrastructure for preserving, transcribing, structuring and publishing the historical evidence contained in `ALC1737`, the 1737 _Arte de la lengua cahita_. It explicitly separates the historical witness, OCR, AI-assisted transcription, curatorial structures, derived analytical products and human verification.

The stable `v1.0.0` release is a **technical and reproducible scholarly release within its declared scope**. It is not a fully human-verified diplomatic or critical edition. The project deliberately keeps `humanVerified=0` where no independent human collation has occurred, and it publishes 22 unresolved cross-reference recollation cases as explicit open uncertainties rather than silently resolving them.

## Primary historical witness

- **Source ID:** `ALC1737`
- **Title:** _Arte de la lengua cahita conforme à las reglas de muchos peritos en ella_
- **Imprint:** Mexico, 1737, D. Francisco Xavier Sánchez
- **Title-page authorship:** anonymous Jesuit missionary; later nominal attributions are documented as cataloguing history rather than substituted for the title-page evidence
- **Working digital witness:** John Carter Brown Library / Internet Archive, identifier `artedelalenguaca00gonz`
- **Historical labels explicitly named in the source:** `Hiaqui`, `Mayo`, `Thehueco`

CHD does **not** infer a single modern ISO 639-3 code for the historical umbrella label “Cahita”, and it does not automatically map historical forms to modern Yaqui or Mayo.

## v1.0.0 at a glance

| Layer | Verified technical state |
|---|---:|
| Canonical boundary candidates | 2,072 / 2,072 reconstructible |
| Historical lexical articles | 2,302 in 211 canonical JSONL files |
| Vocabulary pages 133–177 | 45 / 45 technically reconciled |
| Printed numbered grammar units | 371 / 371 represented |
| Structured grammar objects | 302 |
| Grammar evidence rows | 1,215 |
| Historical `Buſca` references | 150 |
| `not_located` references explicitly reviewed | 90 / 90 |
| Open recollation uncertainties | 22 = 8 A / 4 B / 10 C |
| `Lo miſmo` occurrences reviewed | 14 / 14 |
| Human-verified objects | 0 |

TEI Lex-0 0.9.5 remains the primary lexical interoperability format of the immutable `v1.0.0` release and is validated against the archived Lex-0 Relax NG schema with Jing. As a **post-v1 derivative**, CHD now also provides a reproducible CLDF `Dictionary` projection: **2,221 `EntryTable` rows**, **2,221 `SenseTable` rows**, one documentary `LanguageTable` row and one bibliographic source record. Historical forms are preserved verbatim, `humanVerified` is carried through without promotion, and no ISO 639-3 or Glottocode is inferred for the historical label “Cahita”. The projection is rebuilt from the canonical JSONL, validated with `pycldf`, and checked row by row against CHD authority invariants. See [CLDF.md](CLDF.md).

## Try it in 30 seconds

Clone the repository and inspect the canonical corpus:

```bash
git clone https://github.com/fersandovalgtz/cahita-historico-digital.git
cd cahita-historico-digital
python scripts/query_lexicon.py --stats
python scripts/query_lexicon.py "Danzar" --field spanish --limit 5
```

Or download the stable release payload with the GitHub CLI:

```bash
gh release download v1.0.0 \
  -R fersandovalgtz/cahita-historico-digital \
  -p 'cahita-historico-digital-v1.0.0.zip'
```

The release contains canonical frozen data, reproducible derived views, manifests and checksums. See [Data products](docs/DATA_PRODUCTS.md).

## Reproducibility

The repository uses JSON Schema contracts, deterministic exporters, content freezes and GitHub Actions. The v1.0.0 scientific freeze covers 267 files; the contract freeze covers 22 JSON Schemas plus four source-scope metadata files. The published release has a durable post-release attestation that rebuilds the payload from the immutable tag and compares the rebuilt bytes with the published assets. A separate post-v1 workflow reconstructs and validates the CLDF Dictionary projection without adding it to the scientific freeze.

Useful entry points:

```bash
make qa-surface
make stats
make cldf-qa
python scripts/export_lexicon_corpus.py
python scripts/validate_v1_release.py
```

A green CI run establishes structural and computational consistency. It does not turn AI-assisted editorial work into human philological verification.

## Responsible reuse

Historical labels and colonial-era descriptions are source evidence, not necessarily contemporary editorial terminology. Reusers should preserve source identifiers and provenance, distinguish transcription from normalization or analysis, and avoid projecting modern linguistic identities, community consensus or normative authority onto `ALC1737` without separate evidence.

See [Governance](GOVERNANCE.md), [Editorial policy](EDITORIAL_POLICY.md), [Contributing](CONTRIBUTING.md) and [Datasheet](DATASHEET.md).

## Citation and preservation

The canonical citation metadata are in [`CITATION.cff`](CITATION.cff) and [`codemeta.json`](codemeta.json). The immutable release tag is `v1.0.0`, pointing to commit `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`.

Archival deposit and DOI assignment remain pending. No DOI is inferred or invented before an actual preservation repository assigns it. The external preservation gate is tracked in issue #169.

## Maintainer

**Fernando Sandoval Gutierrez** · Universidad Autónoma de Ciudad Juárez · ORCID [0000-0002-3168-6725](https://orcid.org/0000-0002-3168-6725)

## Licensing

Original software is MIT licensed. Original structured data, metadata and editorial layers are CC BY 4.0 unless otherwise stated. Third-party facsimiles, scans and reproductions are not relicensed by this repository. See [`LICENSE`](LICENSE) and [`DATA_LICENSE.md`](DATA_LICENSE.md).
