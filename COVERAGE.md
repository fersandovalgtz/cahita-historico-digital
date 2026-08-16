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
| Candidatos lexicográficos v0.2 | **2,072 / 2,072 persistidos canónicamente** | inventario fila-a-fila reconstruible |
| Artículos históricos estructurados | **844** | capa curatorial actual; no conteo final del vocabulario completo |
| Páginas de vocabulario con representación estructurada | **45 / 45** | al menos una representación por página |
| Páginas con reconciliación + censo + promoción cerrados | **133–136** | IA-asistido; no `human_verified` |
| Reconciliación pp.133–134 | **61 / 61 candidatos** | 57 article; 4 continuation; 0 unresolved |
| Censo visible pp.133–134 | **72 inicios** | TP57 / FP4 / FN15; F1 0.857143 |
| Reconciliación p.135 | **43 / 43 candidatos** | 35 article; 8 continuation; 0 unresolved |
| Censo visible p.135 | **47 inicios** | TP35 / FP8 / FN12; F1 0.777778 |
| Reconciliación p.136 | **48 / 48 candidatos** | 48 article; 48 exact |
| Censo visible p.136 | **49 inicios** | TP48 / FP0 / FN1; F1 0.989691 |
| `pending_promotion` pp.133–136 | **0** | candidatos article y falsos negativos visibles enlazados |
| Lagunas/discontinuidades del testimonio | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA automatizado | **activo** | GitHub Actions valida inventario, IDs, schemas y reconciliaciones |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. La digital 132 / impresa 118 conserva `INTERJECCIONES`, la nota `No ſe hallan en los Artes, el vſo las dará` y `FIN DEL ARTE`.

Las digitales 69 y 105 son páginas mixtas: en 69 cierra Parte II y comienza Parte III; en 105 cierra Parte III y comienza Parte IV. Ambas fronteras se conservan estructuralmente. Esta cobertura de superficie textual no equivale a una edición crítica cerrada.

## Vocabulario

El vocabulario ocupa las digitales 133–177. `hybrid_margin_mode_v0.2` produce **2,072 candidatos de frontera**, mientras que la capa curatorial contiene **844 artículos históricos estructurados**. Las dos cifras representan objetos distintos y ninguna debe interpretarse como el número final de entradas de la obra.

### Inventario candidato canónico

El inventario completo de candidatos está fijado a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10` y al PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`. El JSONL reconstruido tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

`data/lexicon/candidates/candidate_inventory_manifest.json` y `scripts/reconstruct_candidate_inventory.py` controlan la persistencia lossless, la reconstrucción y la integridad del inventario.

### QA diagnóstico del extractor

La muestra intencional de pp.133, 134, 150 y 177 conserva:

| Método | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| `indentation_margin_v0.1` | 163 | 8 | 25 | 95.32% | 86.70% | 90.81% |
| `hybrid_margin_mode_v0.2` | 169 | 5 | 19 | **97.13%** | **89.89%** | **93.37%** |

Son métricas diagnósticas, no probabilísticas, con referencia visual IA-asistida.

## Cierre pp.133–134

El tramo de control tiene 61 candidatos reconciliados: 57 `article`, 4 `continuation`, 0 `unresolved`. El censo completo registra 72 inicios visibles, con TP57 / FP4 / FN15. Todos los candidatos `article` y los 15 falsos negativos están enlazados; `pending_promotion = 0`.

La apertura del vocabulario queda representada como `A. denotando la persona que padece. A. Aa.` (`ALC1737-art-000778`).

## Página 135

La p.135 tiene 43 candidatos reconciliados: 35 `article`, 8 `continuation`; el censo registra 47 inicios visibles, TP35 / FP8 / FN12. Todos están enlazados y no quedan promociones pendientes.

En esta página se documentó la corrección `Azotar. Ahlocotua.` → **`Azofar. Ahlocotua.`** para `ALC1737-art-000704`, separando la entrada posterior `Azotar con cuero, ò ſoga. Abeba.` (`000810`). `ALC1737-art-000809` conserva `Senu[ileg.]`.

## Página 136

`data/lexicon/reconciliation/p136_reconciliation_status.json` registra:

- **48/48 candidatos** reconciliados, 24 por columna;
- 48 `article`, 0 continuaciones, 0 candidatos irresueltos;
- 48 límites `exact` en el cotejo visual IA-asistido;
- **49 inicios históricos visibles**;
- TP48 / FP0 / FN1;
- precisión **1.000000**, recall **0.979592**, F1 **0.989691**;
- el único falso negativo es el primer artículo de página, `Azotar con vara al caballo`, ya enlazado a `ALC1737-art-000705`;
- **34 artículos nuevos** promovidos, `000811`–`000844`;
- `pending_promotion = 0`.

La página añade dos continuidades físicas importantes. `ALC1737-art-000821`, `Adobar cueros. Huacabeata-buiaruna.`, cruza de la columna izquierda a la derecha. `ALC1737-art-000844`, `Afligirſe, ò apurarſe. Chuntia-ca, l, chunti iauetua.`, cruza de p.136 a p.137. Ambas se representan con `sourceSpans` y no como entradas separadas.

`ALC1737-art-000831`, `A ello, manos à la obra`, permanece `unresolved` a nivel de la expresión cahíta en tipo pequeño.

## Fuentes de control textual

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` se registra como reimpresión histórica de control secundaria. `BNF1737-REPORTED` conserva la noticia bibliográfica de un ejemplar independiente de la edición de 1737 en la BnF; falta todavía verificar directamente su ficha/signatura y, si es accesible, ingerirlo como testimonio separado.

## Sistema numeral — digitales 178–180

La capa numeral incluye esquema, dataset y documentación para cardinales de alta confianza, numerales de orden descritos por la fuente, distributivos y adverbios numerales. Las observaciones explícitas sobre `Naciones` y `Hiaqui/Hiaquis` deberán integrarse a la capa combinada de variación histórica.

## Incidencias editoriales abiertas

- `obra tripartita` frente a `quatro partes`;
- duplicación histórica de la regla 129;
- OCR 241 vs lectura visual 242;
- OCR 281 vs lectura visual 282;
- posible ausencia visible de 294;
- discontinuidad F→H entre digitales 157–158;
- reclamo `Lucer-` en p.161 sin lema visible al comienzo de p.162;
- lecturas cahítas de baja legibilidad conservadas como `[ileg.]` o `unresolved`.

## QA automatizado

`.github/workflows/qa.yml` verifica la reconstrucción de candidatos, unicidad de identificadores, schemas de artículos, reconciliaciones, falsos negativos y JSON de estado. Una corrida verde es **QA computacional**, no revisión filológica humana.

## Interpretación de autoridad

`raw_ocr`, `machine_corrected_unverified`, `unresolved`, `editorial_proposal` y `human_verified` son estados distintos. CHD no convierte una lectura IA-asistida en validación humana y no rellena lagunas mediante inferencia silenciosa.

## Próximos criterios de cobertura

1. procesar la página digital **137**, comenzando por la continuación de `ALC1737-art-000844`;
2. escalar el mismo ciclo página por página hasta 177;
3. consolidar concordancias y exportaciones gramaticales/variacionales;
4. verificar directamente el ejemplar 1737 reportado en BnF;
5. incorporar revisión humana independiente suficiente para el alcance de una futura release científica.
