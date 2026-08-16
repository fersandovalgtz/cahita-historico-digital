# Cobertura

Estado de cobertura de Cahíta Histórico Digital para `ALC1737` — 2026-08-15.

## Métricas vigentes

| Dimensión | Cobertura | Autoridad / nota |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digital 15–132 ↔ impresa 1–118 |
| OCR paginado reproducible | **182 / 182** | derivado; no transcripción |
| Diagnóstico OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Transcripciones `full_page` | **112 páginas** | hasta digital 116 / impresa 102 |
| Parte I | **completa** | digitales 15–50 / impresas 1–36 |
| Parte II | **completa** | 51–69 parcial / 37–55 parcial |
| Parte III | **completa** | 69 parcial–105 parcial / 55 parcial–91 parcial; reglas 189–291 |
| Parte IV | **en curso** | 105 parcial–116 / 91 parcial–102; reglas 292–324, regla 324 continúa |
| Paradigmas históricos | **3** | estructurados |
| Construcciones modales | **9** | reglas 207–234 |
| Construcciones no finitas | **5** | reglas 237–256 |
| Construcciones participiales | **3** | reglas 257–265 |
| Construcciones predicativas/modales | **6** | reglas 266–284 |
| Verbos irregulares | **6 grupos** | reglas 286–291 |
| Preposiciones/grupos | **27** | reglas 293–324; última entrada abierta |
| Observaciones de variación histórica | **15 entidades** | `0014–0015` añadidas desde Parte IV |
| Candidatos lexicográficos v0.2 | **2,072** | 45 páginas; no equivalen a entradas publicadas |
| Entradas lexicográficas piloto | **12** | no producción |
| Revisión humana independiente | **0** | no iniciada |

## Fronteras materiales

La división en partes no coincide siempre con el salto de página. Se han comprobado dos páginas `mixed`:

- **digital 69 / impresa 55:** regla 188 cierra Parte II y después comienza `PARTE III`;
- **digital 105 / impresa 91:** reglas 290–291 cierran Parte III y después comienza `IV. ULT. PARTE` con la regla 292.

Las dos fronteras están modeladas en [`data/source/alc1737/sections.json`](data/source/alc1737/sections.json) y en las unidades de página correspondientes mediante `sectionSegments`.

## Lotes de transcripción posteriores al manifiesto consolidado

`data/transcription/status.csv` permanece consolidado hasta digital 91. La cobertura posterior está versionada mediante deltas documentados en [`data/transcription/batches/README.md`](data/transcription/batches/README.md):

- `part_iii_p092_p096.csv`
- `part_iii_p097_p101.csv`
- `part_iii_iv_p102_p106.csv`
- `part_iv_p107_p111.csv`
- `part_iv_p112_p116.csv`

Una futura tarea de QA regenerará el manifiesto maestro a partir de las unidades JSON y lotes, comprobando faltantes, duplicados y regresiones de estado.

## Capas derivadas de Parte III

- [`modal_constructions_part_iii_p077_p086.jsonl`](data/grammar/modal_constructions_part_iii_p077_p086.jsonl) → [`docs/MODAL_CONSTRUCTIONS.md`](docs/MODAL_CONSTRUCTIONS.md)
- [`nonfinite_constructions_part_iii_p087_p093.jsonl`](data/grammar/nonfinite_constructions_part_iii_p087_p093.jsonl) → [`docs/NONFINITE_CONSTRUCTIONS.md`](docs/NONFINITE_CONSTRUCTIONS.md)
- [`participles_part_iii_p094_p097.jsonl`](data/grammar/participles_part_iii_p094_p097.jsonl) → [`docs/PARTICIPLES.md`](docs/PARTICIPLES.md)
- [`predicative_modal_part_iii_p097_p103.jsonl`](data/grammar/predicative_modal_part_iii_p097_p103.jsonl) → [`docs/PREDICATIVE_MODAL_CONSTRUCTIONS.md`](docs/PREDICATIVE_MODAL_CONSTRUCTIONS.md)
- [`irregular_verbs_part_iii_p103_p105.jsonl`](data/grammar/irregular_verbs_part_iii_p103_p105.jsonl) → [`docs/IRREGULAR_VERBS.md`](docs/IRREGULAR_VERBS.md)

## Parte IV: preposiciones

La regla 292 describe históricamente las “preposiciones” como elementos que se posponen al nombre. Después de observar múltiples entradas, CHD adoptó [`schemas/preposition-entry.schema.json`](schemas/preposition-entry.schema.json), que separa forma, régimen, alternancias, sentidos, comparación latina, ejemplos, juicios de uso y autoridad.

Los lotes [`prepositions_part_iv_p105_p111.jsonl`](data/grammar/prepositions_part_iv_p105_p111.jsonl) y [`prepositions_part_iv_p112_p116.jsonl`](data/grammar/prepositions_part_iv_p112_p116.jsonl) contienen **27 entradas/grupos**. El tratamiento llega a `HIPITCU` (regla 324), que continúa en la página siguiente. → [`docs/PREPOSITIONS_PART_IV.md`](docs/PREPOSITIONS_PART_IV.md)

Parte IV añadió además dos atribuciones explícitas a Hiaqui:

- `ALC1737-var-0014`: `Eſte vebuili es mui vſado en Hiaqui` (regla 314);
- `ALC1737-var-0015`: `tutiua, dice el Hiaqui` en la regla 318.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica del número 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- dos fronteras intra-página (69 y 105);
- posible ausencia visible de **294** entre el cierre de `ui` y `TZI 295`.

Ninguna de estas incidencias se corrige silenciosamente.

## Lexicografía y autoridad

El vocabulario mantiene **2,072 candidatos v0.2** sobre 45 páginas. Son propuestas geométricas de frontera, no artículos históricos publicados. La promoción requiere revisión de frontera, microestructura, procedencia y estado explícito.

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados diferentes. CHD no convierte una lectura IA-asistida en validación humana ni una categoría del gramático de 1737 en una descripción moderna sin una capa analítica separada.
