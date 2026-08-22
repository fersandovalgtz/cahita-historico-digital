# Documentación científica de Cahíta Histórico Digital

Este índice organiza la documentación por pregunta de investigación o mantenimiento. Para una introducción general, comience en el [`README.md`](../README.md) del repositorio.

## Quiero entender qué es CHD

- [`../README.md`](../README.md) — panorama, métricas, quickstart y estado v1.0.0.
- [`../README.en.md`](../README.en.md) — overview in English.
- [`../DATASHEET.md`](../DATASHEET.md) — datasheet actualizado del corpus.
- [`ECOSYSTEM.md`](ECOSYSTEM.md) — relación metodológica con Rarámuri Digital y otros proyectos.

## Quiero saber qué puedo descargar o analizar

- [`DATA_PRODUCTS.md`](DATA_PRODUCTS.md) — JSON/JSONL/CSV, TEI, gramática, release y usos recomendados.
- [`../SCHEMA.md`](../SCHEMA.md) — modelo por capas y contratos.
- [`../project-metadata.json`](../project-metadata.json) — perfil machine-readable del proyecto.
- [`../metadata/fair-dataset.jsonld`](../metadata/fair-dataset.jsonld) — metadata JSON-LD complementaria.

## Quiero reproducir resultados

- [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) — instalación, consulta, QA, exports, Lex-0 y release.
- [`../SCIENTIFIC_REPOSITORY_STANDARD.md`](../SCIENTIFIC_REPOSITORY_STANDARD.md) — estándar interno de calidad.
- [`QA_AUTOMATION.md`](QA_AUTOMATION.md) — automatización de QA.
- [`RELEASE_PUBLICATION_2026-08-22.md`](RELEASE_PUBLICATION_2026-08-22.md) — cierre y atestación de la GitHub Release v1.0.0.

## Quiero evaluar calidad y límites

- [`../QUALITY_REPORT.md`](../QUALITY_REPORT.md) — dimensiones comprobadas, métricas y limitaciones.
- [`../FAIR_ASSESSMENT.md`](../FAIR_ASSESSMENT.md) — preauditoría FAIR, no certificación.
- [`../COVERAGE.md`](../COVERAGE.md) — cobertura detallada.
- [`OCR_QUALITY.md`](OCR_QUALITY.md) — diagnóstico OCR y límites de interpretación.
- [`GRAMMAR_COMPLETION_2026-08-21.md`](GRAMMAR_COMPLETION_2026-08-21.md) — cierre técnico gramatical.
- [`PHASE2_COMPLETION_2026-08-21.md`](PHASE2_COMPLETION_2026-08-21.md) — cierre técnico lexicográfico.

## Quiero auditar la fuente y la procedencia

- [`SOURCE_ALC1737.md`](SOURCE_ALC1737.md) — descripción de la fuente principal.
- [`AUTHORSHIP.md`](AUTHORSHIP.md) — autoría histórica y atribuciones posteriores.
- [`../SOURCES.md`](../SOURCES.md) — inventario de fuentes y testimonios de control.
- [`CONTROL_WITNESSES.md`](CONTROL_WITNESSES.md) — testigos de control y límites de uso.
- [`../PROVENANCE.md`](../PROVENANCE.md) — procedencia y capas.
- [`../references.bib`](../references.bib) — bibliografía machine-readable inicial.

## Quiero entender la edición y las incertidumbres

- [`../EDITORIAL_POLICY.md`](../EDITORIAL_POLICY.md) — política editorial general.
- [`TRANSCRIPTION_CONVENTIONS.md`](TRANSCRIPTION_CONVENTIONS.md) — convenciones de transcripción.
- [`LEXICON_RECONCILIATION_PROTOCOL.md`](LEXICON_RECONCILIATION_PROTOCOL.md) — reconciliación lexicográfica.
- [`CROSSREFERENCE_RECOLLATION_QUEUE.md`](CROSSREFERENCE_RECOLLATION_QUEUE.md) — cola de 22 recolaciones.
- [`LO_MISMO_FORMULA_REVIEW.md`](LO_MISMO_FORMULA_REVIEW.md) — revisión formal de `Lo miſmo`.
- [`LEXICON_LO_MISMO.md`](LEXICON_LO_MISMO.md) — vista lexicográfica derivada de `Lo miſmo`.
- [`V1_RECOLLATION_DISPOSITION.md`](V1_RECOLLATION_DISPOSITION.md) — disposición v1 de incertidumbres abiertas.

## Quiero reutilizar, contribuir o reportar un problema

- [`../GOVERNANCE.md`](../GOVERNANCE.md) — gobernanza, identidad histórica y reutilización responsable.
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — protocolo de contribución.
- [`../CONTRIBUTORS.md`](../CONTRIBUTORS.md) — roles CRediT.
- [`../SECURITY.md`](../SECURITY.md) — seguridad e integridad científica.
- [Issue templates](../.github/ISSUE_TEMPLATE/) — corrección textual, bug de datos/software, investigación/interoperabilidad.

## Quiero citar o revisar licencias

- [`../CITATION.cff`](../CITATION.cff) — metadata canónica de citación.
- [`../codemeta.json`](../codemeta.json) — CodeMeta.
- [`../LICENSE`](../LICENSE) — software MIT.
- [`../DATA_LICENSE.md`](../DATA_LICENSE.md) — datos/capas originales CC BY 4.0.
- [`../LICENSING.md`](../LICENSING.md) — matriz de licenciamiento por componente.

## Quiero entender releases y preservación

- [`../RELEASE_CHECKLIST_v1_0.md`](../RELEASE_CHECKLIST_v1_0.md) — checklist v1.0.0.
- [`RELEASE_READINESS_2026-08-21.md`](RELEASE_READINESS_2026-08-21.md) — preparación histórica de la release.
- [`RELEASE_PUBLICATION_2026-08-22.md`](RELEASE_PUBLICATION_2026-08-22.md) — publicación/atestación efectiva.
- [`../release/github_release_attestation_v1.0.0.json`](../release/github_release_attestation_v1.0.0.json) — evidencia machine-readable post-release.
- [Issue #169](https://github.com/fersandovalgtz/cahita-historico-digital/issues/169) — depósito archivístico y DOI pendientes.

## Regla de lectura

Los documentos de avance antiguos se preservan como historia del proyecto y pueden contener cifras que eran correctas en su fecha de corte. Para el estado actual, priorice siempre:

1. `README.md`;
2. `project-metadata.json`;
3. `DATASHEET.md`;
4. `QUALITY_REPORT.md`;
5. manifests/atestaciones de `release/`;
6. datos canónicos y validadores.

CI protege la sincronización de esta superficie pública con los hechos canónicos de v1.0.0.
