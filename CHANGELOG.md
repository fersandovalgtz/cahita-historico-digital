# Changelog

Todos los cambios relevantes de Cahíta Histórico Digital se documentarán en este archivo.

## [0.1.4-dev] - 2026-08-15

### Añadido

- `scripts/extract_vocab_candidates.py`, extractor conservador de candidatos de límites de artículo basado en indentación y layout;
- `schemas/vocabulary-candidate.schema.json`, contrato que separa formalmente un candidato OCR de una entrada lexicográfica;
- muestra auditable de 38 candidatos de la página digital 134 en `data/lexicon/candidates/p134_candidates.jsonl`;
- documentación metodológica y limitaciones en `docs/VOCAB_CANDIDATES.md`.

### Resultado

La corrida completa sobre páginas digitales 133–177 produjo **1,680 candidatos**: 903 en columna izquierda y 777 en derecha, con una media de 37.33 candidatos por página. Los **1,680 / 1,680** objetos pasaron validación estructural contra su JSON Schema. El JSONL completo derivado tiene SHA-256 `f00318329c1116254388aac0ffe978fea330c8466f3863e318df1f01fd010b59`.

### Salvaguardas

La cifra 1,680 **no se presenta como número de entradas históricas**. El algoritmo conserva falsos comienzos y posibles continuaciones como candidatos revisables; no divide automáticamente lema castellano y forma cahíta, y no promueve ningún objeto a `lexical_entry`.

## [0.1.3-dev] - 2026-08-15

### Añadido

- diagnóstico estratificado y reproducible de calidad OCR en seis zonas del volumen;
- `scripts/evaluate_ocr_sample.py`;
- referencias de evaluación en `data/validation/ocr_sample_references.json`;
- resultados versionados en `data/validation/ocr_sample_results.json`;
- documentación metodológica en `docs/OCR_QUALITY.md`.

### Resultado

La muestra diagnóstica arroja **micro-CER 25.66%** y **micro-WER 51.96%** después de una normalización que mapea `ſ → s`, elimina marcas diacríticas combinantes, minúsculiza y neutraliza puntuación/espaciado. El resultado confirma que el OCR bruto no debe promoverse directamente a corpus científico.

La muestra del vocabulario (p. 134) usa reconstrucción de columna mediante `-bbox-layout` y obtiene CER 9.68% en el fragmento seleccionado; este valor se interpreta como indicio de que la geometría de dos columnas constituye una parte importante del problema, no como tasa global del vocabulario.

### Salvaguardas

Las transcripciones de referencia de la evaluación son cotejos visuales IA-asistidos sin revisión humana independiente. Por tanto, el diagnóstico es una métrica de ingeniería editorial y no una evaluación filológica definitiva.

## [0.1.2-dev] - 2026-08-15

### Añadido

- extractor reproducible de disposición a dos columnas para el vocabulario: `scripts/extract_vocab_layout.py`;
- esquema `schemas/vocabulary-layout-line.schema.json` para conservar líneas OCR con página, columna, coordenadas y estado de evidencia;
- `scripts/validate_jsonl.py` y `requirements-dev.txt` para validación reproducible de JSONL;
- primer extracto diplomático IA-asistido del vocabulario, página digital 134;
- **12 entradas lexicográficas piloto** estructuradas y validadas contra `schemas/lexical-entry.schema.json`;
- documentación metodológica del piloto en `docs/PILOT_LEXICON_P134.md`.

### Resultados de extracción

Una corrida local de `extract_vocab_layout.py` sobre las páginas digitales 133–177 produjo **3,899 líneas OCR/layout**: 1,731 clasificadas en columna izquierda, 2,107 en derecha y 61 retenidas como `other` por fusiones o ambigüedad de layout. El JSONL completo derivado tiene SHA-256 `9b5eb47fc7d93a63e8345a33da844863d8228fe7149a303ee35a1c2c00cb1871`.

### Salvaguardas

Las 12 entradas del piloto están marcadas `machine_corrected_unverified`; ninguna se presenta como `human_verified`. La extracción de líneas no se interpreta como recuento de artículos lexicográficos.

## [0.1.1-dev] - 2026-08-15

### Añadido

- script de ingestión reproducible `scripts/ingest_alc1737.py`;
- checksums SHA-256 de los dos archivos de trabajo de `ALC1737`;
- manifiesto página por página para las **182 páginas digitales**, con sección y paginación impresa cuando existe;
- mapeo completo de las **118 páginas impresas numeradas** del cuerpo gramatical;
- documentación técnica de ingestión;
- convenciones explícitas para transcripción diplomática, corrección, `ſ`, abreviaturas, particiones de línea e incertidumbre;
- README específico de la fuente en `data/source/alc1737/`.

### Modificado

- la segmentación macro dejó de ser únicamente inferida por encabezados: sus fronteras principales fueron cotejadas visualmente en el facsímil;
- la documentación de la fuente incorpora ahora la descripción física del registro de Internet Archive/JCB y la discrepancia técnica entre el campo `Pages: 184` y el PDF de trabajo de 182 páginas;
- las métricas de cobertura distinguen OCR disponible, OCR extraído, payload versionado y transcripción filológica;
- las páginas 181–182 se identifican como finales materiales/cubierta posterior, no como una sección textual pendiente.

### Estado científico

- **0 / 182** páginas se declaran todavía como transcripción diplomática terminada;
- **0** entradas lexicográficas se promueven todavía al corpus estructurado de producción;
- **0** unidades se etiquetan como `human_verified`.

La fase 0.1.1-dev consolida la trazabilidad técnica necesaria antes de comenzar la extracción lexicográfica y la transcripción.

## [0.1.0] - 2026-08-15

### Añadido

- definición inicial del proyecto **Cahíta Histórico Digital**;
- registro canónico de la fuente `ALC1737`;
- documentación de la fuente histórica de 1737 y de su procedencia digital;
- política explícita para tratar la autoría histórica como cuestión no resuelta;
- política editorial por capas: testimonio, OCR, transcripción, normalización y datos derivados;
- `CITATION.cff` y `codemeta.json`;
- datasheet inicial del corpus;
- esquema JSON inicial para entradas lexicográficas;
- política de licencias separada para código, datos y materiales de terceros;
- hoja de ruta para ingestión, extracción lexicográfica, interoperabilidad y futura preservación en Zenodo;
- integración documental con el ecosistema de repositorios científicos de Fernando Sandoval Gutierrez.

### Estado científico

Esta versión es **pre-release**. Registra la infraestructura y la fuente, pero no declara terminada ni validada una transcripción crítica, un vocabulario estructurado o una edición filológica completa.
