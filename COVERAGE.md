# Cobertura

Estado de cobertura de Cahíta Histórico Digital para la fuente `ALC1737`.

## Estado actual — 2026-08-15

| Dimensión | Cobertura | Estado |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digital 15–132 ↔ impresa 1–118 |
| Checksums de archivos fuente de trabajo | **2 / 2** | SHA-256 registrado |
| Extracción OCR paginada reproducible | **182 / 182** | derivado reproducible; no transcripción |
| Diagnóstico estratificado de OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Líneas OCR/layout del vocabulario | **3,899** | pp. 133–177 |
| Candidatos lexicográficos v0.2 | **2,072** | 2,072/2,072 estructuralmente válidos |
| Precisión / recall / F1 v0.2 | **97.13% / 89.89% / 93.37%** | muestra diagnóstica |
| Transcripciones diplomáticas `full_page` | **107 páginas** | preliminares textuales + Partes I–III + Parte IV hasta p. 111 |
| **Parte I** | **completa** | digitales 15–50 / impresas 1–36 |
| **Parte II** | **completa** | digitales 51–69 parcial / impresas 37–55 parcial |
| **Parte III** | **completa en continuidad textual** | digital 69 parcial–105 parcial / impresa 55 parcial–91 parcial; reglas 189–291 |
| Parte IV | **en curso** | digital 105 parcial–111 / impresa 91 parcial–97; reglas 292–309, regla 309 continúa |
| Paradigmas gramaticales estructurados | **3** | corpus inicial |
| Construcciones modales estructuradas | **9** | reglas 207–234 |
| Construcciones no finitas estructuradas | **5** | reglas 237–256 |
| Construcciones participiales estructuradas | **3** | reglas 257–265 |
| Construcciones predicativas/modales estructuradas | **6** | reglas 266–284 |
| Verbos irregulares estructurados | **6** | reglas 286–291 |
| Preposiciones/grupos estructurados | **12** | Parte IV, reglas 293–309 |
| Observaciones de variación histórica | **13 entidades** | 10 en exportación JSONL + 3 modulares (`0011`–`0013`) |
| Extractos diplomáticos del vocabulario | **1 página** | p. 134, piloto |
| Entradas lexicográficas piloto | **12** | esquema válido; no producción |
| Revisión humana independiente | **0** | no iniciada |

## Segmentación refinada: dos fronteras intra-página

La fuente contiene dos fronteras de partes comprobadas que no coinciden con un salto de página digital:

1. **digital 69 / impresa 55**: la parte superior concluye Parte II con la regla 188; debajo comienza `PARTE III`.
2. **digital 105 / impresa 91**: la parte superior conserva `CAHITA. PARTE III.`, concluye las reglas 290–291; debajo aparece `IV. ULT. PARTE` y comienza la regla 292.

[`data/source/alc1737/sections.json`](data/source/alc1737/sections.json) representa ambas fronteras y [`schemas/page-transcription.schema.json`](schemas/page-transcription.schema.json) admite páginas `mixed` mediante `sectionSegments`.

| Sección | Páginas digitales | Páginas impresas |
|---|---:|---:|
| Preliminares | 1–14 | no paginadas |
| Parte I | 15–50 | 1–36 |
| Parte II | 51–69 parcial | 37–55 parcial |
| Parte III | 69 parcial–105 parcial | 55 parcial–91 parcial |
| Parte IV | 105 parcial–132 | 91 parcial–118 |
| Vocabulario | 133–177 | no paginado |
| Numerales | 178–180 | no paginados |
| Finales materiales | 181–182 | no paginados |

## Transcripción y lotes

`data/transcription/status.csv` permanece consolidado hasta digital 91 / impresa 77. Los avances posteriores se conservan como deltas versionados y se documentan en [`data/transcription/batches/README.md`](data/transcription/batches/README.md):

- `part_iii_p092_p096.csv`
- `part_iii_p097_p101.csv`
- `part_iii_iv_p102_p106.csv`
- `part_iv_p107_p111.csv`

La cobertura efectiva combinada alcanza **107 páginas `full_page`**. Una futura tarea de QA regenerará el manifiesto maestro desde las unidades JSON y lotes, con comparación de regresiones y duplicados.

## Parte III: capas derivadas consolidadas

- **Modalidad 207–234:** [`data/grammar/modal_constructions_part_iii_p077_p086.jsonl`](data/grammar/modal_constructions_part_iii_p077_p086.jsonl) — 9 construcciones. → [`docs/MODAL_CONSTRUCTIONS.md`](docs/MODAL_CONSTRUCTIONS.md)
- **Infinitivos y gerundios 237–256:** [`data/grammar/nonfinite_constructions_part_iii_p087_p093.jsonl`](data/grammar/nonfinite_constructions_part_iii_p087_p093.jsonl) — 5 objetos. → [`docs/NONFINITE_CONSTRUCTIONS.md`](docs/NONFINITE_CONSTRUCTIONS.md)
- **Participios 257–265:** [`data/grammar/participles_part_iii_p094_p097.jsonl`](data/grammar/participles_part_iii_p094_p097.jsonl) — 3 objetos. → [`docs/PARTICIPLES.md`](docs/PARTICIPLES.md)
- **Predicación y poder 266–284:** [`data/grammar/predicative_modal_part_iii_p097_p103.jsonl`](data/grammar/predicative_modal_part_iii_p097_p103.jsonl) — 6 objetos. → [`docs/PREDICATIVE_MODAL_CONSTRUCTIONS.md`](docs/PREDICATIVE_MODAL_CONSTRUCTIONS.md)
- **Verbos irregulares 286–291:** [`data/grammar/irregular_verbs_part_iii_p103_p105.jsonl`](data/grammar/irregular_verbs_part_iii_p103_p105.jsonl) — 6 grupos. → [`docs/IRREGULAR_VERBS.md`](docs/IRREGULAR_VERBS.md)

Incidencias preservadas: OCR 241 vs visual 242; OCR 281 vs visual 282; duplicación histórica de 129; `obra tripartita` / `quatro partes`; fronteras intra-página 69 y 105.

## Parte IV: preposiciones

La regla 292 abre el sistema y describe históricamente las llamadas preposiciones como elementos que se posponen al nombre. Después de observar varias entradas, CHD fijó una microestructura que separa forma, régimen histórico, alternancias, sentidos numerados, comparación latina, ejemplos, juicios de uso y estado editorial.

[`data/grammar/prepositions_part_iv_p105_p111.jsonl`](data/grammar/prepositions_part_iv_p105_p111.jsonl) contiene **12 entradas/grupos**: `ui`, `tzi`, `ye`, `maque`, `patzi/vepatzi`, `veuatzi`, `veuitzi`, `uaam`, `uaasi`, `velecana`, `vinavo/vinatzaua` y `uaitana/uanavo`. El esquema es [`schemas/preposition-entry.schema.json`](schemas/preposition-entry.schema.json).

El tratamiento preserva la polisemia y la arquitectura del impreso en vez de reducir cada forma a una traducción única. También conserva juicios históricos como `no es pulido lenguaje` en el tratamiento de `maque` exclusivamente como evidencia metalingüística del autor.

Una nueva incidencia queda abierta: después de la continuación de `ui`, el siguiente número visible antes de `TZI` es **295**; no se ha localizado todavía un **294** inequívoco. No se inventa ni reconstruye silenciosamente.

→ [`docs/PREPOSITIONS_PART_IV.md`](docs/PREPOSITIONS_PART_IV.md)

## Variación histórica y lexicografía

La exportación combinada de variación contiene aún 10 entidades iniciales; `0011`–`0013` permanecen modulares hasta una regeneración reproducible. El vocabulario mantiene **2,072 candidatos v0.2** sobre 45 páginas; son propuestas de frontera, no entradas históricas publicadas.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana, ni una categoría del gramático de 1737 en una descripción moderna sin una capa analítica separada.
