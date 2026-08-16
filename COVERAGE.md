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
| Transcripciones diplomáticas `full_page` | **102 páginas** | preliminares textuales + Partes I–III + inicio de Parte IV hasta p. 106 |
| **Parte I** | **completa** | digitales 15–50 / impresas 1–36 |
| **Parte II** | **completa** | digitales 51–69 parcial / impresas 37–55 parcial |
| **Parte III** | **completa en continuidad textual** | digital 69 parcial–105 parcial / impresa 55 parcial–91 parcial; reglas 189–291 |
| Parte IV | **iniciada** | digital 105 parcial–106 / impresa 91 parcial–92; reglas 292–293 |
| Reglas gramaticales estructuradas | **15** | lote inicial 46–60 |
| Paradigmas gramaticales estructurados | **3** | presente de `Eria`; comparación temporal; comparación optativa |
| Construcciones modales estructuradas | **9** | reglas 207–234 |
| Construcciones no finitas estructuradas | **5** | reglas 237–256 |
| Construcciones participiales estructuradas | **3** | reglas 257–265 |
| Construcciones predicativas/modales estructuradas | **6** | reglas 266–284 |
| Verbos irregulares estructurados | **6** | reglas 286–291 |
| Observaciones de variación histórica | **13 entidades** | 10 en exportación JSONL + 3 modulares (`0011`–`0013`) |
| Extractos diplomáticos del vocabulario | **1 página** | p. 134, piloto |
| Entradas lexicográficas piloto | **12** | esquema válido; no producción |
| Revisión humana independiente | **0** | no iniciada |

## Segmentación refinada: dos fronteras intra-página

La fuente contiene al menos dos fronteras de partes que no coinciden con el salto de página digital:

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

## Transcripción

La Fase 2 utiliza una unidad JSON por página. El manifiesto maestro [`data/transcription/status.csv`](data/transcription/status.csv) sigue consolidado hasta digital 91 / impresa 77; los avances posteriores están versionados como lotes delta y deberán incorporarse en una consolidación reproducible del manifiesto, sin perder el historial de lotes.

Lotes posteriores a la última consolidación del manifiesto:

- [`data/transcription/batches/part_iii_p092_p096.csv`](data/transcription/batches/part_iii_p092_p096.csv)
- [`data/transcription/batches/part_iii_p097_p101.csv`](data/transcription/batches/part_iii_p097_p101.csv)
- [`data/transcription/batches/part_iii_iv_p102_p106.csv`](data/transcription/batches/part_iii_iv_p102_p106.csv)

Con estos lotes, la **Parte III queda completamente representada en continuidad textual** hasta su cierre en la porción superior de p. 105. La Parte IV comienza en la misma página y ya se encuentra transcrita hasta p. 106.

`full_page` significa que la superficie textual impresa de la página está representada editorialmente. Puede contener secuencias `[ileg.]`, lecturas provisionales o incertidumbres tipadas; **no equivale a `human_verified`**.

## Parte III: capas derivadas consolidadas

### Modalidad — reglas 207–234

[`data/grammar/modal_constructions_part_iii_p077_p086.jsonl`](data/grammar/modal_constructions_part_iii_p077_p086.jsonl) contiene **9 construcciones** que preservan la oposición histórica entre `vn supuesto` y `dos supuestos` y las series asociadas a `ſi`, `antes`, `como`, `quando`, `aunque`, `deſpues`, `porque`, `para / paraque` y `como ſi`.

→ [`docs/MODAL_CONSTRUCTIONS.md`](docs/MODAL_CONSTRUCTIONS.md)

### Infinitivos y gerundios — reglas 237–256

[`data/grammar/nonfinite_constructions_part_iii_p087_p093.jsonl`](data/grammar/nonfinite_constructions_part_iii_p087_p093.jsonl) contiene **5 objetos**: primer y segundo modo de infinitivo, gerundios en `DI`, `DO` y `DVM`.

La discrepancia OCR/facsímil de la regla **242** permanece documentada: el OCR leyó 241; el cotejo visual apoya 242.

→ [`docs/NONFINITE_CONSTRUCTIONS.md`](docs/NONFINITE_CONSTRUCTIONS.md)

### Participios — reglas 257–265

[`data/grammar/participles_part_iii_p094_p097.jsonl`](data/grammar/participles_part_iii_p094_p097.jsonl) contiene **3 objetos** para participios en `me`, `u` y `ye`. Las reglas 264–265 documentan además extensiones que el gramático trata como instrumentales (`aye / ayeye`) y locativas (`aet`).

→ [`docs/PARTICIPLES.md`](docs/PARTICIPLES.md)

### Predicación y poder — reglas 266–284

[`data/grammar/predicative_modal_part_iii_p097_p103.jsonl`](data/grammar/predicative_modal_part_iii_p097_p103.jsonl) contiene **6 objetos**: `avia de / avia de aver`; `Sum, es, fui` con `tuc / iec`; poder `phyſicè` con `araue/ara`; no poder `moralitèr` con `machi`; no poder `voluntariè` con `poeta`; y querer/no querer con `vare / ca vare`.

La página 102 presenta otra incidencia entre capas: el OCR repite **281**, mientras el facsímil apoya **282** para la regla sobre verbales en `bilis`. CHD conserva el desacuerdo explícitamente.

→ [`docs/PREDICATIVE_MODAL_CONSTRUCTIONS.md`](docs/PREDICATIVE_MODAL_CONSTRUCTIONS.md)

### Verbos irregulares y cierre de Parte III — reglas 285–291

[`data/grammar/irregular_verbs_part_iii_p103_p105.jsonl`](data/grammar/irregular_verbs_part_iii_p103_p105.jsonl) contiene **6 grupos verbales** estructurados. La regla 290 cruza de p. 104 a p. 105; la regla 291 se completa antes de la aparición de `IV. ULT. PARTE` en la misma página.

→ [`docs/IRREGULAR_VERBS.md`](docs/IRREGULAR_VERBS.md)

## Inicio de Parte IV

La regla 292 formula una generalización histórica sobre las preposiciones y su colocación. La regla 293 abre el tratamiento de `ui` y enumera múltiples significaciones con ejemplos; la explicación continúa después de p. 106. Todavía no se ha promovido este material a un dataset estable de preposiciones, porque conviene observar primero varias entradas para fijar una microestructura adecuada.

## Variación histórica: estado de exportación

La exportación combinada [`data/linguistic/variety_observations.jsonl`](data/linguistic/variety_observations.jsonl) contiene todavía las **10 entidades** iniciales. Las nuevas observaciones modulares `0011`–`0013` permanecen pendientes de una regeneración reproducible de la exportación combinada.

## Corpus lexicográfico

El vocabulario mantiene **2,072 candidatos v0.2** sobre 45 páginas. Ese número representa propuestas de frontera y no entradas históricas publicadas. La promoción a entrada de producción continúa requiriendo revisión de frontera, microestructura, procedencia y estado explícito.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana, ni una categoría del gramático de 1737 en una descripción moderna sin una capa analítica separada.
