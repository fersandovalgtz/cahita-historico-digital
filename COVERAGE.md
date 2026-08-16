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
| Sistema numeral histórico | **1 bloque estructurado** | digitales 178–180 |
| Observaciones de variación histórica | **17+** | exportación combinada pendiente de consolidación |
| Candidatos lexicográficos v0.2 | **2,072 / 2,072 persistidos canónicamente** | inventario reconstruible |
| Artículos históricos estructurados | **871** | capa curatorial actual; no conteo final del vocabulario |
| Páginas de vocabulario con representación estructurada | **45 / 45** | al menos una representación por página |
| Páginas con reconciliación + censo + promoción cerrados | **133–137** | IA-asistido; no `human_verified` |
| Reconciliación pp.133–134 | **61 / 61 candidatos** | 57 article; 4 continuation; 0 unresolved |
| Censo visible pp.133–134 | **72 inicios** | TP57 / FP4 / FN15; F1 0.857143 |
| Reconciliación p.135 | **43 / 43 candidatos** | 35 article; 8 continuation |
| Censo visible p.135 | **47 inicios** | TP35 / FP8 / FN12; F1 0.777778 |
| Reconciliación p.136 | **48 / 48 candidatos** | 48 article; 48 exact |
| Censo visible p.136 | **49 inicios** | TP48 / FP0 / FN1; F1 0.989691 |
| Reconciliación p.137 | **39 / 39 candidatos** | 36 article; 3 continuation |
| Censo visible p.137 | **42 inicios** | TP36 / FP3 / FN6; F1 0.888889 |
| `pending_promotion` pp.133–137 | **0** | candidatos article y falsos negativos visibles enlazados |
| Lagunas/discontinuidades del testimonio | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA automatizado | **activo** | GitHub Actions valida inventario, IDs, schemas y reconciliaciones |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. Las fronteras mixtas de las digitales 69 y 105 se conservan estructuralmente. Esta cobertura de superficie textual no equivale a una edición crítica cerrada.

## Vocabulario

El vocabulario ocupa las digitales 133–177. `hybrid_margin_mode_v0.2` produce **2,072 candidatos de frontera**, mientras que la capa curatorial contiene **871 artículos históricos estructurados**. Son objetos distintos y ninguna cifra debe interpretarse como el número final de entradas de la obra.

El inventario completo está fijado a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10` y al PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`. El JSONL reconstruido tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

## Cierre pp.133–136

Las páginas 133–136 permanecen cerradas en la capa IA-asistida. El tramo 133–134 funciona como control metodológico; p.135 introdujo el ciclo completo de promoción y falsos negativos; p.136 confirmó una página de alta precisión geométrica y dos continuidades físicas importantes: `ALC1737-art-000821` entre columnas y `ALC1737-art-000844` entre p.136 y p.137.

## Página 137

`data/lexicon/reconciliation/p137_reconciliation_status.json` registra:

- **39/39 candidatos** reconciliados: 22 izquierda + 17 derecha;
- **36 `article`** y **3 `continuation`**;
- calidad geométrica: 33 `exact`, 3 `merged_articles`, 3 `oversegmented`;
- **42 inicios históricos visibles**;
- TP36 / FP3 / FN6;
- precisión **0.923077**, recall **0.857143**, F1 **0.888889**;
- 36/36 candidatos `article` enlazados;
- 6/6 falsos negativos enlazados;
- **27 artículos nuevos** promovidos, `ALC1737-art-000845`–`000871`;
- `pending_promotion = 0`.

La primera línea visible de p.137, `ca, l, chunti iauetua.`, no constituye entrada nueva: cierra `ALC1737-art-000844`, iniciado en p.136. El reclamo inferior `buo-` se modela como catchword y tampoco cuenta como artículo.

La colación de alta resolución produjo además dos correcciones explícitamente versionadas en la capa ya existente: `ALC1737-art-000729`, **`Vaaſuſume` → `Baaſuſume`**, y `ALC1737-art-000731`, **`Aguacero` → `Aguazero`**. Ambas derivan del facsímil primario de 1737 y no implican revisión humana.

Las microestructuras de `ALC1737-art-000856`, `000867`, `000868` y `000869` permanecen `unresolved` donde la puntuación o relación interna de las formas no permite una interpretación responsable.

## QA diagnóstico y automático

La muestra diagnóstica del extractor conserva para `hybrid_margin_mode_v0.2` precisión 97.13%, recall 89.89% y F1 93.37% sobre pp.133, 134, 150 y 177. Es una muestra intencional, no probabilística.

El workflow `CHD QA` run #68 terminó en `success`: reconstruyó las 2,072 filas con el hash esperado y verificó **871 objetos / 871 `articleId` únicos**, además de validar schemas de artículos, los 22+17 registros de reconciliación de p.137, los 6 falsos negativos y los JSON de estado/procedencia. Una corrida verde es QA computacional, no revisión filológica humana.

## Fuentes de control textual

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` es una reimpresión histórica de control secundaria. `BNF1737-REPORTED` conserva la noticia bibliográfica de un ejemplar independiente de la edición de 1737 en la BnF; falta verificar directamente su ficha/signatura y, si es accesible, ingerirlo como testimonio separado.

## Incidencias editoriales abiertas

Permanecen, entre otras, `obra tripartita` frente a `quatro partes`, la duplicación de la regla 129, las discrepancias OCR 241/242 y 281/282, la posible ausencia visible de 294, la discontinuidad F→H p.157→158 y `Lucer-` p.161→162. Las lecturas de baja confianza se mantienen como `[ileg.]` o `unresolved`.

## Próximos criterios de cobertura

1. procesar la página digital **138** con el mismo ciclo de candidato → censo visible → promoción → QA;
2. escalar página por página hasta 177;
3. consolidar concordancias y exportaciones gramaticales/variacionales;
4. verificar directamente el ejemplar 1737 reportado en BnF;
5. incorporar revisión humana independiente suficiente para una futura release científica.
