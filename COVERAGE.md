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
| Payload OCR completo versionado en GitHub | **0 / 182** | empaquetado pendiente |
| Transcripción diplomática | **0 / 182** | pendiente |
| Transcripción corregida | **0 / 182** | pendiente |
| Normalización | **0 / 182** | pendiente |
| Entradas lexicográficas estructuradas | **0** | pendiente |
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

## Evidencia visual ya cotejada

Se inspeccionaron de forma dirigida las páginas digitales 3, 11, 13, 14, 15, 51, 69, 105, 132, 133, 178, 180, 181 y 182. Este muestreo incluye todos los límites estructurales principales y las páginas sin OCR significativo.

## Interpretación de métricas

`OCR extraído` significa únicamente que se pudo recuperar la capa textual automática del PDF. No implica exactitud filológica. `Hash OCR por página` permite detectar cambios bit a bit en la extracción y volver a localizar una unidad en la cadena de procesamiento.

No se declarará cobertura de transcripción, validación o entradas lexicográficas hasta que existan archivos versionados y evidencia de cotejo contra el facsímil.
