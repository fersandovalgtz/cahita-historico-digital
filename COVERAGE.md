# Cobertura

Estado canónico de cobertura de Cahíta Histórico Digital para `ALC1737` — 2026-08-16.

## Métricas vigentes

| Dimensión | Cobertura | Autoridad / nota |
|---|---:|---|
| Páginas digitales identificadas | **182 / 182** | verificado |
| Páginas impresas numeradas mapeadas | **118 / 118** | digitales 15–132 ↔ impresas 1–118 |
| OCR paginado reproducible | **182 / 182** | derivado; no transcripción |
| Diagnóstico OCR | **6 muestras** | micro-CER 25.66%; micro-WER 51.96% |
| Transcripciones diplomáticas `full_page` | **128 páginas** | preliminares textuales + Arte completo hasta digital 132 |
| Partes I–IV del Arte | **completas en capa IA-asistida** | fronteras intra-página 69 y 105 preservadas |
| Paradigmas históricos | **3** | estructurados |
| Construcciones modales | **9** | reglas 207–234 |
| Construcciones no finitas | **5** | reglas 237–256 |
| Construcciones participiales | **3** | reglas 257–265 |
| Construcciones predicativas/modales | **6** | reglas 266–284 |
| Verbos irregulares | **6 grupos** | reglas 286–291 |
| Preposiciones/grupos | **43** | reglas 293–340 |
| Grupos de adverbios | **11** | reglas 341–359 |
| Grupos de conjunciones/metacategorías | **6** | reglas 360–373 + interjecciones |
| Sistema numeral histórico | **1 bloque estructurado** | digitales 178–180 |
| Observaciones de variación histórica | **17+** | exportación combinada aún pendiente de consolidación |
| Candidatos lexicográficos v0.2 | **2,072 / 2,072 persistidos canónicamente** | inventario fila-a-fila reconstruible y verificable |
| Artículos históricos estructurados | **810** | capa curatorial actual; no conteo final del vocabulario completo |
| Páginas de vocabulario con representación estructurada | **45 / 45** | cobertura selectiva por página completa |
| Páginas con reconciliación + censo visible cerrados | **133–135** | IA-asistido; no human_verified |
| Reconciliación pp.133–134 | **61 / 61 candidatos** | 57 article; 4 continuation; 0 unresolved |
| Censo visible pp.133–134 | **72 inicios** | TP57 / FP4 / FN15; F1 0.857143 |
| Reconciliación p.135 | **43 / 43 candidatos** | 35 article; 8 continuation; 0 unresolved |
| Censo visible p.135 | **47 inicios** | TP35 / FP8 / FN12; F1 0.777778 |
| `pending_promotion` pp.133–135 | **0** | todos los candidatos article y falsos negativos visibles enlazados |
| Lagunas/discontinuidades del testimonio | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA automatizado | **activo** | GitHub Actions valida inventario, IDs, schemas y capas de reconciliación |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. La digital 132 / impresa 118 conserva `INTERJECCIONES`, la nota `No ſe hallan en los Artes, el vſo las dará` y `FIN DEL ARTE`.

Las digitales 69 y 105 son páginas mixtas: en 69 cierra Parte II y comienza Parte III; en 105 cierra Parte III y comienza Parte IV. Ambas fronteras se conservan estructuralmente.

Este hito significa **cobertura de superficie textual**, no edición crítica cerrada. Las lecturas `unresolved` permanecen visibles y ninguna página ha sido declarada `human_verified`.

## Vocabulario

El vocabulario ocupa digitales 133–177. El pipeline vigente `hybrid_margin_mode_v0.2` produce **2,072 candidatos de frontera**. La capa curatorial contiene ahora **810 artículos históricos estructurados** y las **45 páginas** poseen al menos una representación lexicográfica estructurada.

La diferencia entre candidato computacional, frontera editorial, inicio visible omitido y artículo histórico se conserva explícitamente. **2,072 no es el número de entradas históricas y 810 tampoco es todavía el número final del vocabulario.**

### Inventario candidato canónico

El inventario fila-a-fila de los **2,072 candidatos** quedó fijado a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10` y al PDF con SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`.

El JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`. Se conserva lossless como gzip determinista → base64 → 12 partes ordenadas. `data/lexicon/candidates/candidate_inventory_manifest.json` registra hashes y tamaños; `scripts/reconstruct_candidate_inventory.py` reconstruye y verifica integridad, parseo y conteo.

El antiguo `data/lexicon/candidates/p134_candidates.jsonl` corresponde a `indentation_margin_v0.1` y se conserva únicamente como artefacto histórico/no canónico.

### QA de fronteras: v0.1 frente a v0.2

La comparación documentada en `data/lexicon/review/boundary_algorithm_comparison.json` utiliza las páginas intencionales 133, 134, 150 y 177.

| Método | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| `indentation_margin_v0.1` | 163 | 8 | 25 | 95.32% | 86.70% | 90.81% |
| `hybrid_margin_mode_v0.2` | 169 | 5 | 19 | **97.13%** | **89.89%** | **93.37%** |

Estas métricas son **diagnósticas y no probabilísticas**. Sus referencias visuales son IA-asistidas y no constituyen validación filológica humana.

## Páginas de control pp.133–134

`data/lexicon/reconciliation/p133_p134_reconciliation_status.json` y `p133_p134_visible_start_census.json` registran el cierre del primer tramo.

### Candidatos

- 61/61 candidatos reconciliados;
- 57 `article`;
- 4 `continuation`;
- 0 `unresolved`;
- 52 `exact`, 5 `merged_articles`, 3 `oversegmented`, 1 `undersegmented`.

### Censo visible

- p.133: 30 inicios; TP20 / FP4 / FN10; precisión 0.833333; recall 0.666667; F1 0.740741;
- p.134: 42 inicios; TP37 / FP0 / FN5; precisión 1.0; recall 0.880952; F1 0.936709;
- conjunto: **72 inicios**; TP57 / FP4 / FN15; precisión **0.934426**; recall **0.791667**; F1 **0.857143**.

La apertura del vocabulario quedó representada como `A. denotando la persona que padece. A. Aa.` (`ALC1737-art-000778`).

Todos los candidatos `article` y todos los falsos negativos del censo cerrado enlazan artículos históricos; `pending_promotion = 0`.

## Página 135

La página 135 se procesó con el mismo protocolo cerrado en pp.133–134.

### Candidatos

- **43/43** candidatos reconciliados: 26 izquierda + 17 derecha;
- 35 `article`;
- 8 `continuation`;
- 0 `unresolved`;
- 33 `exact`, 4 `merged_articles`, 6 `oversegmented`.

### Censo visible

- **47 inicios históricos visibles**;
- TP35 / FP8 / FN12;
- precisión **0.813953**;
- recall **0.744681**;
- F1 **0.777778**.

Todos los **35/35 candidatos `article`** y los **12/12 inicios omitidos** enlazan objetos históricos. Se promovieron 32 artículos nuevos en esta página: 26 desde candidatos y 6 desde falsos negativos, llevando la secuencia curatorial hasta `ALC1737-art-000810`.

### Corrección editorial y lectura incierta

La inspección dirigida corrigió `ALC1737-art-000704` de `Azotar. Ahlocotua.` a **`Azofar. Ahlocotua.`**. La entrada siguiente, distinta, es **`Azotar con cuero, ò ſoga. Abeba.`** (`ALC1737-art-000810`). La corrección está documentada en `data/lexicon/provenance/p135_art000704_correction.json`.

`ALC1737-art-000809`, `Acoſtar à otro`, conserva `Senu[ileg.]`: el inicio de la forma es visible, pero el resto no se completa desde OCR, analogía ni una edición posterior.

## Fuentes de control textual

CHD distingue la autoridad del testimonio `ALC1737` de materiales de control:

- `BUE1890`: reimpresión de Eustaquio Buelna, registrada como edición histórica de control secundaria;
- `BNF1737-REPORTED`: noticia bibliográfica de un ejemplar independiente de la edición de 1737 en la Réserve des Livres rares de la Bibliothèque nationale de France. Todavía no se ha verificado directamente su ficha/signatura ni se ha ingerido un facsímil.

La política se documenta en `docs/CONTROL_WITNESSES.md`.

## Sistema numeral — digitales 178–180

La capa numeral incluye esquema, dataset y documentación para cardinales de alta confianza, numerales de orden descritos por la fuente, distributivos y adverbios numerales. Las observaciones explícitas sobre `Naciones` y `Hiaqui/Hiaquis` deben integrarse todavía a la capa combinada de variación histórica.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica de la regla 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- posible ausencia visible de 294;
- discontinuidad F→H entre digitales 157–158;
- reclamo `Lucer-` en p.161 sin lema visible al comienzo de p.162;
- formas cahítas aún `[ileg.]` en algunos artículos, entre ellos `000771`, `000774` y `000809`.

## QA automatizado

`.github/workflows/qa.yml` verifica, entre otros controles:

- reconstrucción del inventario canónico de 2,072 candidatos;
- unicidad global de `articleId`;
- todos los artículos históricos contra `schemas/lexical-article.schema.json`;
- capas de reconciliación y falsos negativos contra sus schemas;
- JSON de control seleccionados.

La corrida **CHD QA #46**, commit `9e2a5b122db563447fd3df32fa020a675ba8fa11`, terminó en `success` y verificó **810 objetos lexicográficos / 810 `articleId` únicos**. Esto es QA computacional, no revisión filológica humana.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana ni rellena lagunas sin una capa de procedencia separada.

## Próximos criterios de cobertura

1. iniciar reconciliación candidata y censo visible de la página digital 136;
2. escalar después página por página hasta 177;
3. consolidar concordancias y exportaciones gramaticales/variacionales;
4. verificar directamente el ejemplar 1737 reportado en BnF y, si es accesible, ingerirlo como testimonio separado;
5. ampliar QA automatizado y revisión humana suficiente para el alcance de una futura release.
