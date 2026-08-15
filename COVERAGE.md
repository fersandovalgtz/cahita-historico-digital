# Cobertura

Estado de cobertura de Cahíta Histórico Digital para la fuente `ALC1737`.

## Estado actual — 2026-08-15

| Dimensión | Cobertura | Estado |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Segmentación macro por secciones | **182 / 182** | fronteras cotejadas visualmente |
| Páginas impresas numeradas mapeadas | **118 / 118** | digital 15–132 ↔ impresa 1–118 |
| Checksums de archivos fuente de trabajo | **2 / 2** | SHA-256 registrado |
| Hash OCR por página | **182 / 182** | derivado local `page_manifest_full.csv` |
| Extracción OCR paginada reproducible | **182 / 182** | producida localmente; no validada filológicamente |
| Diagnóstico estratificado de OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Payload OCR completo versionado en GitHub | **0 / 182** | empaquetado pendiente |
| Líneas OCR/layout del vocabulario extraídas localmente | **3,899** | páginas 133–177; 61 fusiones de columnas retenidas como `other` |
| Candidatos de límites de artículo | **1,680** | 45 páginas; `machine_candidate`, no recuento de entradas |
| Candidatos de artículo versionados como muestra | **38** | página digital 134 |
| Extracto diplomático IA-asistido | **1 página piloto** | p. digital 134; no validación humana |
| Entradas lexicográficas piloto estructuradas | **12** | JSON Schema válido; `machine_corrected_unverified` |
| Entradas lexicográficas de producción | **0** | ninguna promovida todavía |
| Transcripción diplomática completa | **0 / 182** | pendiente |
| Transcripción corregida completa | **0 / 182** | pendiente |
| Normalización | **0 / 182** | pendiente |
| Ejemplos gramaticales estructurados | **0** | pendiente |
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

La segmentación machine-readable se encuentra en [`data/source/alc1737/sections.json`](data/source/alc1737/sections.json), y el inventario completo página por página en [`data/source/alc1737/page_manifest.csv`](data/source/alc1737/page_manifest.csv).

## Calidad OCR

La muestra inicial de seis estratos confirma que el OCR de entrada debe tratarse como evidencia no validada. El micro-CER normalizado es **25.66%** y el micro-WER **51.96%**. La evaluación, referencias y método están versionados y son reproducibles.

→ [`docs/OCR_QUALITY.md`](docs/OCR_QUALITY.md)

## Candidatos lexicográficos

El vocabulario ya cuenta con una capa reproducible entre OCR/layout y entrada estructurada. `scripts/extract_vocab_candidates.py` produjo **1,680 candidatos de límites de artículo** sobre las páginas 133–177. Esos objetos no afirman todavía lema ni forma cahíta y no deben citarse como número de entradas de la obra.

La página 134 aporta una muestra versionada de **38 candidatos** que permite auditar tanto agrupamientos plausibles como falsas fronteras. El esquema específico impide confundir formalmente esta capa con `lexical-entry`.

→ [`docs/VOCAB_CANDIDATES.md`](docs/VOCAB_CANDIDATES.md)

## Piloto lexicográfico

La página digital 134 dispone de un extracto diplomático IA-asistido y doce registros estructurados. Los doce pasaron validación local contra `schemas/lexical-entry.schema.json`, pero permanecen explícitamente en estado `machine_corrected_unverified`.

→ [`docs/PILOT_LEXICON_P134.md`](docs/PILOT_LEXICON_P134.md)

## Evidencia visual ya cotejada

Se inspeccionaron de forma dirigida las páginas digitales 3, 11, 13, 14, 15, 51, 69, 105, 132, 133, 134, 178, 180, 181 y 182. Este muestreo incluye todos los límites estructurales principales, las páginas sin OCR significativo, las zonas de evaluación OCR y la página del primer piloto lexicográfico.

## Interpretación de métricas

`OCR extraído` significa únicamente que se pudo recuperar la capa textual automática del PDF. No implica exactitud filológica. `Hash OCR por página` permite detectar cambios bit a bit en la extracción y volver a localizar una unidad en la cadena de procesamiento.

`Candidato de límites de artículo` significa una agrupación geométrica que requiere revisión. `Entrada piloto estructurada` tampoco equivale a entrada validada. Ambas capas prueban contratos de datos, trazabilidad y flujo editorial antes de escalar la edición.
