# Cobertura

Estado de cobertura de Cahíta Histórico Digital para `ALC1737` — 2026-08-15.

## Métricas vigentes

| Dimensión | Cobertura | Autoridad / nota |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digital 15–132 ↔ impresa 1–118 |
| OCR paginado reproducible | **182 / 182** | derivado; no transcripción |
| Diagnóstico OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Transcripciones diplomáticas `full_page` | **128 páginas** | portada + preliminares textuales + **todo el Arte impreso pp. 1–118** |
| Parte I | **completa** | digitales 15–50 / impresas 1–36 |
| Parte II | **completa** | 51–69 parcial / 37–55 parcial |
| Parte III | **completa** | 69 parcial–105 parcial / 55 parcial–91 parcial; reglas 189–291 |
| **Parte IV** | **completa** | 105 parcial–132 / 91 parcial–118; reglas 292–373 + nota de interjecciones + `FIN DEL ARTE` |
| Paradigmas históricos | **3** | estructurados |
| Construcciones modales | **9** | reglas 207–234 |
| Construcciones no finitas | **5** | reglas 237–256 |
| Construcciones participiales | **3** | reglas 257–265 |
| Construcciones predicativas/modales | **6** | reglas 266–284 |
| Verbos irregulares | **6 grupos** | reglas 286–291 |
| Preposiciones/grupos preposicionales-adverbiales | **43** | reglas 293–340; bloque cerrado |
| Grupos de adverbios | **11** | reglas 341–359 |
| Grupos de conjunciones / metacategorías | **6** | reglas 360–373 + interjecciones |
| Observaciones de variación histórica identificadas | **17 entidades** | `0014–0017` añadidas desde Parte IV |
| Candidatos lexicográficos v0.2 | **2,072** | 45 páginas; no equivalen a entradas publicadas |
| Artículos históricos estructurados | **253** | secuencia curatorial p.134 y pp.138–149; no revisión humana |
| Artículos de remisión piloto adicionales | **4** | p.165; fuera del conteo principal de 253 |
| Revisión humana independiente | **0** | no iniciada |

## Hito: el Arte gramatical está completamente representado

Las páginas impresas numeradas **1–118**, correspondientes a las digitales **15–132**, cuentan ya con una unidad de transcripción `full_page`. La página digital 132 / impresa 118 conserva las reglas 371–373, el encabezado `INTERJECCIONES`, la declaración `No ſe hallan en los Artes, el vſo las dará` y `FIN DEL ARTE`.

Este hito significa **cobertura completa de la superficie textual del Arte en la capa IA-asistida**, no edición crítica cerrada. Muchas páginas conservan lecturas `unresolved`; ninguna ha sido declarada `human_verified`.

## Fronteras materiales

Se han comprobado dos páginas `mixed`:

- **digital 69 / impresa 55:** regla 188 cierra Parte II y después comienza `PARTE III`;
- **digital 105 / impresa 91:** reglas 290–291 cierran Parte III y después comienza `IV. ULT. PARTE` con la regla 292.

Las dos fronteras están modeladas en [`data/source/alc1737/sections.json`](data/source/alc1737/sections.json) y en las unidades de página mediante `sectionSegments`.

## Lotes de transcripción posteriores al manifiesto consolidado

`data/transcription/status.csv` permanece consolidado hasta digital 91. La cobertura posterior está versionada mediante deltas documentados en [`data/transcription/batches/README.md`](data/transcription/batches/README.md):

- `part_iii_p092_p096.csv`
- `part_iii_p097_p101.csv`
- `part_iii_iv_p102_p106.csv`
- `part_iv_p107_p111.csv`
- `part_iv_p112_p116.csv`
- `part_iv_p117_p121.csv`
- `part_iv_p122_p126.csv`
- `part_iv_p127_p132.csv`

Una futura tarea de QA debe regenerar el manifiesto maestro desde las unidades JSON y lotes, comparando faltantes, duplicados y regresiones de estado.

## Parte III: capas derivadas

- [`modal_constructions_part_iii_p077_p086.jsonl`](data/grammar/modal_constructions_part_iii_p077_p086.jsonl) — 9 construcciones.
- [`nonfinite_constructions_part_iii_p087_p093.jsonl`](data/grammar/nonfinite_constructions_part_iii_p087_p093.jsonl) — 5 objetos.
- [`participles_part_iii_p094_p097.jsonl`](data/grammar/participles_part_iii_p094_p097.jsonl) — 3 objetos.
- [`predicative_modal_part_iii_p097_p103.jsonl`](data/grammar/predicative_modal_part_iii_p097_p103.jsonl) — 6 objetos.
- [`irregular_verbs_part_iii_p103_p105.jsonl`](data/grammar/irregular_verbs_part_iii_p103_p105.jsonl) — 6 grupos.

## Parte IV: preposiciones

El bloque preposicional, reglas 292–340, está completamente representado. Los tres lotes de datos contienen **43 entradas o grupos** y preservan polisemia, régimen histórico, comparación latina, alternancias y juicios de uso del gramático:

- [`prepositions_part_iv_p105_p111.jsonl`](data/grammar/prepositions_part_iv_p105_p111.jsonl)
- [`prepositions_part_iv_p112_p116.jsonl`](data/grammar/prepositions_part_iv_p112_p116.jsonl)
- [`prepositions_part_iv_p117_p121.jsonl`](data/grammar/prepositions_part_iv_p117_p121.jsonl)

El bloque termina explícitamente con `Hæc de præpoſitionibus ſatis.` → [`docs/PREPOSITIONS_PART_IV.md`](docs/PREPOSITIONS_PART_IV.md)

## Parte IV: adverbios y conjunciones

`§ II. ADVERBIOS DE LUGAR` comienza en digital 122 / impresa 108. CHD creó [`schemas/adverb-group.schema.json`](schemas/adverb-group.schema.json) y **11 grupos rule-level** en:

- [`adverbs_part_iv_p122_p126.jsonl`](data/grammar/adverbs_part_iv_p122_p126.jsonl)
- [`adverbs_part_iv_p127_p129.jsonl`](data/grammar/adverbs_part_iv_p127_p129.jsonl)

Los grupos preservan `Adverbia ſitus`, `Adverbia motus`, `Temporis`, `Ordinis`, `Quantitatis`, `Interrogandi, Vocandi, Reſpondendi`, `Approbantis`, `haco/hacum` y `Obſecrantis`.

`§ III. DE LAS CONJUNCIONES` comienza en digital 129 / impresa 115. [`schemas/conjunction-group.schema.json`](schemas/conjunction-group.schema.json) y [`conjunctions_part_iv_p129_p132.jsonl`](data/grammar/conjunctions_part_iv_p129_p132.jsonl) preservan **6 grupos/metacategorías**, incluyendo la reflexión del propio gramático sobre la frontera adverbio/conjunción. → [`docs/ADVERBS_CONJUNCTIONS_PART_IV.md`](docs/ADVERBS_CONJUNCTIONS_PART_IV.md)

## Variación histórica: nuevas evidencias de Parte IV

Además de `ALC1737-var-0014` (`vebuili` muy usado en Hiaqui) y `0015` (`tutiua, dice el Hiaqui`), se añadieron:

- `ALC1737-var-0016`: `Eſte ualiſi vſan mucho los Hiaquis` en el bloque temporal;
- `ALC1737-var-0017`: `En Teueco, y Mayo es mui vſado eſte modo de hablar`, vinculado a la sección `haco / hacum`.

Las formas exactas y el alcance de algunas construcciones permanecen sujetos a segunda colación; las atribuciones históricas no se proyectan automáticamente sobre variedades modernas.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica del número 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- dos fronteras intra-página (69 y 105);
- posible ausencia visible de **294** entre el cierre de `ui` y `TZI 295`.

Ninguna incidencia se corrige silenciosamente.

## Vocabulario: estado de producción

El vocabulario ocupa digitales **133–177**. El pipeline geométrico v0.2 propone **2,072 candidatos** sobre esas 45 páginas; siguen siendo candidatos de frontera y no entradas publicadas.

La secuencia curatorial principal contiene ahora **253 artículos históricos estructurados**, desde el piloto p.134 y el avance continuo pp.138–149. El modelo ya ha demostrado capacidad para representar:

- equivalencias simples y múltiples;
- remisiones `Buſca`;
- anáforas `Lo miſmo` mantenidas `unresolved`;
- agrupaciones históricas mediante `sourceGroupingRaw`;
- artículos descriptivos;
- continuidad entre páginas;
- continuidad entre columnas dentro de una misma página mediante `sourceSpans`.

La p.149 aportó el primer artículo reconstruido de izquierda a derecha en la misma página: `Camarón. Cecobi, grande del Rio. Bacauri.`. El siguiente frente comienza en digital **150**. → [`docs/LEXICON_PROGRESS.md`](docs/LEXICON_PROGRESS.md)

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados diferentes. CHD no convierte una lectura IA-asistida en validación humana ni una categoría del gramático de 1737 en una descripción moderna sin una capa analítica separada.
