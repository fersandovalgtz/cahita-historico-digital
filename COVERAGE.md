# Cobertura

Estado de cobertura de Cahíta Histórico Digital para la fuente `ALC1737`.

## Estado actual — 2026-08-15

| Dimensión | Cobertura | Estado |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Segmentación macro por secciones | **182 / 182** | fronteras cotejadas visualmente |
| Páginas impresas numeradas mapeadas | **118 / 118** | digital 15–132 ↔ impresa 1–118 |
| Checksums de archivos fuente de trabajo | **2 / 2** | SHA-256 registrado |
| Extracción OCR paginada reproducible | **182 / 182** | derivado reproducible, no transcripción |
| Diagnóstico estratificado de OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Líneas OCR/layout del vocabulario | **3,899** | pp. 133–177; 61 líneas `other` por fusiones/ambigüedad |
| Candidatos v0.1 | **1,680** | método histórico preservado en Git/hashes |
| Candidatos v0.2 vigentes | **2,072** | 45 páginas; 2,072/2,072 válidos por JSON Schema |
| Muestra de evaluación v0.2 | **4 páginas / 188 comienzos visibles** | diagnóstica, IA-asistida |
| Precisión / recall / F1 v0.2 | **97.13% / 89.89% / 93.37%** | inicios de artículo, muestra no probabilística |
| Transcripciones diplomáticas completas | **1 página** | p. 3, `machine_corrected_unverified` |
| Extractos diplomáticos | **1 página** | p. 134, piloto |
| Entradas lexicográficas piloto estructuradas | **12** | JSON Schema válido; `machine_corrected_unverified` |
| Entradas lexicográficas de producción | **0** | ninguna promovida todavía |
| Revisión humana independiente | **0** | no iniciada |

## Segmentación confirmada a nivel macro

| Sección | Páginas digitales | Páginas impresas |
|---|---:|---:|
| Preliminares | 1–14 | no paginadas |
| Parte I | 15–50 | 1–36 |
| Parte II | 51–68 | 37–54 |
| Parte III | 69–104 | 55–90 |
| Parte IV | 105–132 | 91–118 |
| Vocabulario | 133–177 | no paginado |
| Numerales | 178–180 | no paginados |
| Cubierta posterior / finales materiales | 181–182 | no paginados |

La segmentación máquina-legible se encuentra en [`data/source/alc1737/sections.json`](data/source/alc1737/sections.json), y el inventario página por página en [`data/source/alc1737/page_manifest.csv`](data/source/alc1737/page_manifest.csv).

## Calidad OCR

La muestra inicial de seis estratos confirma que el OCR de entrada debe tratarse como evidencia no validada. El micro-CER normalizado es **25.66%** y el micro-WER **51.96%**. La evaluación, referencias y método están versionados y son reproducibles.

→ [`docs/OCR_QUALITY.md`](docs/OCR_QUALITY.md)

## Candidatos lexicográficos v0.2

`hybrid_margin_mode_v0.2` es el método vigente de generación de candidatos. La corrida completa sobre pp. 133–177 produjo **2,072 candidatos**, frente a 1,680 en v0.1. El aumento se interpreta como mejora de recuperación de fronteras, no como incremento del número de entradas históricas.

Sobre las mismas páginas de evaluación 133, 134, 150 y 177, v0.2 registra TP=169, FP=5 y FN=19: precisión **97.13%**, recall **89.89%**, F1 **93.37%**. v0.1 había obtenido 95.32%, 86.70% y 90.81%, respectivamente.

La muestra es diagnóstica e intencional; sus referencias son cotejos visuales IA-asistidos sin revisión humana independiente.

→ [`docs/VOCAB_BOUNDARY_V02.md`](docs/VOCAB_BOUNDARY_V02.md) · [`data/lexicon/review/boundary_algorithm_comparison.json`](data/lexicon/review/boundary_algorithm_comparison.json)

## Transcripción

La Fase 2 usa una unidad JSON por página y un manifiesto de 182 filas en [`data/transcription/status.csv`](data/transcription/status.csv). La portada, p. digital 3, ya tiene cobertura `full_page` del texto impreso; p. 134 conserva un extracto piloto. Ninguna de estas unidades está declarada `human_verified`.

→ [`docs/TRANSCRIPTION_MODEL.md`](docs/TRANSCRIPTION_MODEL.md)

## Interpretación de métricas

`OCR extraído` significa recuperación automática de una capa textual, no exactitud filológica. `Candidato de límites de artículo` significa una propuesta geométrica que requiere revisión. `Entrada piloto estructurada` significa que el contrato de datos funciona; no equivale a entrada publicada o validada.

Las cifras de cobertura deben leerse siempre junto con el **estado de autoridad** de la capa que describen.
