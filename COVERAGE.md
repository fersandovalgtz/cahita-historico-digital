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
| Candidatos v0.2 vigentes | **2,072** | 45 páginas; 2,072/2,072 válidos por JSON Schema |
| Precisión / recall / F1 v0.2 | **97.13% / 89.89% / 93.37%** | muestra diagnóstica de inicios de artículo |
| Transcripciones diplomáticas `full_page` | **46 páginas** | p. 3, pp. 5–13 y Parte I completa pp. 15–50 |
| **Parte I transcrita** | **36 / 36 páginas** | digitales 15–50 = impresas 1–36; **100%** |
| Reglas gramaticales estructuradas | **15** | reglas históricas 46–60; corpus en expansión |
| Extractos diplomáticos | **1 página** | p. 134, piloto |
| Observaciones de variación histórica estructuradas | **9** | Hiaqui/Mayo/Tehueco/Cynaloas y otras etiquetas literales de la fuente |
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

`hybrid_margin_mode_v0.2` es el método vigente de generación de candidatos. La corrida completa sobre pp. 133–177 produjo **2,072 candidatos**. Este valor describe propuestas geométricas de frontera, no el número histórico de artículos.

Sobre las páginas diagnósticas 133, 134, 150 y 177, v0.2 registra precisión **97.13%**, recall **89.89%** y F1 **93.37%**. La muestra es intencional y el cotejo permanece IA-asistido, sin revisión humana independiente.

→ [`docs/VOCAB_BOUNDARY_V02.md`](docs/VOCAB_BOUNDARY_V02.md)

## Transcripción

La Fase 2 usa una unidad JSON por página y un manifiesto de 182 filas en [`data/transcription/status.csv`](data/transcription/status.csv). Existen ahora **46 unidades `full_page`**: portada (p. 3), bloque textual de preliminares (pp. 5–13) y **las 36 páginas de la Parte I** (digitales 15–50 / impresas 1–36).

La **Parte I ha alcanzado 100% de cobertura por página** en la capa `machine_corrected_unverified`. Esto no significa edición crítica cerrada ni revisión humana: cada JSON conserva su cola de incertidumbres y las lecturas dudosas permanecen explícitas.

Los lotes se encuentran en `data/transcription/batches/`, desde `part_i_p015_p020.csv` hasta `part_i_p046_p050.csv`.

La última página de Parte I, digital 50 / impresa 36, concluye las reglas 121–123 y conserva el catchword `PAR-`, que enlaza materialmente con el inicio de `PARTE II` en la página siguiente.

→ [`docs/TRANSCRIPTION_MODEL.md`](docs/TRANSCRIPTION_MODEL.md)

## Corpus gramatical

[`schemas/grammatical-rule.schema.json`](schemas/grammatical-rule.schema.json) representa las reglas históricas sin convertirlas en generalizaciones lingüísticas modernas. El primer lote [`data/grammar/rules_part_i_046_060.jsonl`](data/grammar/rules_part_i_046_060.jsonl) contiene 15 reglas estructuradas; la transcripción completa de Parte I permite ahora extender sistemáticamente este corpus hasta la regla 123.

La Parte I documenta, entre otros fenómenos, formación de pretéritos y futuros, voz pasiva, derivación nominal y verbal, verbales, partículas, composición, pronunciación, synalepha, orden de palabras y sintaxis.

## Variación histórica explícita

[`data/linguistic/variety_observations.jsonl`](data/linguistic/variety_observations.jsonl) contiene **9 observaciones** estructuradas. Además de Hiaqui, Mayo y Tehueco/Thehueco, la página digital 49 / impresa 35 incorpora una observación atribuida expresamente a **`los Cynaloas`** sobre el uso del acusativo `netzi` dentro de la construcción discutida en la regla 119.

Las observaciones siguen siendo declaraciones históricas de la fuente. CHD conserva sus denominaciones y análisis sin proyectarlos automáticamente sobre variedades modernas.

→ [`docs/HISTORICAL_VARIATION_EVIDENCE.md`](docs/HISTORICAL_VARIATION_EVIDENCE.md)

## Interpretación de métricas

`OCR extraído` significa recuperación automática de una capa textual, no exactitud filológica. `Transcripción full_page` significa que el texto impreso visible de una página está representado editorialmente; **no implica revisión humana independiente**. `Regla gramatical estructurada` significa que el análisis del gramático de 1737 ha sido convertido en una entidad trazable, no que CHD lo adopte sin crítica como descripción lingüística contemporánea.

Las cifras de cobertura deben leerse siempre junto con el **estado de autoridad** de la capa que describen.
