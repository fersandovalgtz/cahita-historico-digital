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
| Transcripciones diplomáticas `full_page` | **21 páginas** | pp. 3, 5–13 y 15–25; algunas conservan incertidumbres explícitas |
| Parte I transcrita | **11 / 36 páginas** | digitales 15–25 = impresas 1–11; **30.56%** de Parte I |
| Extractos diplomáticos | **1 página** | p. 134, piloto |
| Observaciones de variación histórica estructuradas | **5** | Hiaqui/Mayo/Thehueco; dataset inicial |
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

La Fase 2 usa una unidad JSON por página y un manifiesto de 182 filas en [`data/transcription/status.csv`](data/transcription/status.csv). Ya existen **21 unidades `full_page`** del texto impreso: portada (p. 3), dedicatoria y preliminares textuales (pp. 5–13) y las primeras once páginas impresas de la Parte I (digitales 15–25).

La Parte I ha alcanzado **30.56% de cobertura por página**: 11 de sus 36 páginas. Las páginas 16–25 fueron cotejadas contra renders de 300 dpi; las formas que no permiten lectura segura se conservan mediante marcadores de incertidumbre y no se elevan a `human_verified`.

Los lotes de trabajo están registrados en [`data/transcription/batches/part_i_p015_p020.csv`](data/transcription/batches/part_i_p015_p020.csv) y [`data/transcription/batches/part_i_p021_p025.csv`](data/transcription/batches/part_i_p021_p025.csv).

→ [`docs/TRANSCRIPTION_MODEL.md`](docs/TRANSCRIPTION_MODEL.md)

## Variación histórica explícita

Se inauguró una capa independiente para pasajes en los que el impreso atribuye contrastes a `Hiaqui`, `Mayo` o `Thehueco`. El dataset inicial contiene cinco observaciones ancladas en las páginas digitales 11, 19, 53, 70 y 71, incluyendo una regla de futuro atribuida a los Mayos, una nota léxica con la etiqueta histórica `Hiaqui ſuaue` y las terminaciones comparadas `cat / can / cai` del pluscuamperfecto.

→ [`docs/HISTORICAL_VARIATION_EVIDENCE.md`](docs/HISTORICAL_VARIATION_EVIDENCE.md) · [`data/linguistic/variety_observations.jsonl`](data/linguistic/variety_observations.jsonl)

## Interpretación de métricas

`OCR extraído` significa recuperación automática de una capa textual, no exactitud filológica. `Candidato de límites de artículo` significa una propuesta geométrica que requiere revisión. `Entrada piloto estructurada` significa que el contrato de datos funciona; no equivale a entrada publicada o validada.

`Transcripción full_page` significa que el texto impreso visible de una página está representado en la unidad editorial, pero **no implica revisión humana independiente**. Una unidad puede ser completa y conservar lecturas `unresolved`.

Las cifras de cobertura deben leerse siempre junto con el **estado de autoridad** de la capa que describen.
