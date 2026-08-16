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
| Artículos históricos estructurados | **886** | capa curatorial actual; no conteo final del vocabulario |
| Páginas de vocabulario con representación estructurada | **45 / 45** | al menos una representación por página |
| Páginas con reconciliación + censo + promoción cerrados | **133–138** | IA-asistido; no `human_verified` |
| Reconciliación pp.133–134 | **61 / 61 candidatos** | 57 article; 4 continuation |
| Censo visible pp.133–134 | **72 inicios** | TP57 / FP4 / FN15; F1 0.857143 |
| Reconciliación p.135 | **43 / 43 candidatos** | 35 article; 8 continuation |
| Censo visible p.135 | **47 inicios** | TP35 / FP8 / FN12; F1 0.777778 |
| Reconciliación p.136 | **48 / 48 candidatos** | 48 article; 48 exact |
| Censo visible p.136 | **49 inicios** | TP48 / FP0 / FN1; F1 0.989691 |
| Reconciliación p.137 | **39 / 39 candidatos** | 36 article; 3 continuation |
| Censo visible p.137 | **42 inicios** | TP36 / FP3 / FN6; F1 0.888889 |
| Reconciliación p.138 | **47 / 47 candidatos** | 47 article; 46 exact + 1 merged_articles |
| Censo visible p.138 | **48 inicios** | TP47 / FP0 / FN1; F1 0.989474 |
| `pending_promotion` pp.133–138 | **0** | candidatos article y falsos negativos visibles enlazados |
| Lagunas/discontinuidades del testimonio | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA automatizado | **activo** | GitHub Actions valida inventario, IDs, schemas y reconciliaciones |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. Las fronteras mixtas de las digitales 69 y 105 se conservan estructuralmente. Esta cobertura de superficie textual no equivale a una edición crítica cerrada.

## Vocabulario

El vocabulario ocupa las digitales 133–177. `hybrid_margin_mode_v0.2` produce **2,072 candidatos de frontera**, mientras que la capa curatorial contiene **886 artículos históricos estructurados**. Son objetos distintos y ninguna cifra debe interpretarse como el número final de entradas de la obra.

El inventario completo está fijado a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10` y al PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`. El JSONL reconstruido tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

## Cierre pp.133–137

Las páginas 133–137 permanecen cerradas en la capa IA-asistida. El tramo 133–134 funciona como control metodológico; p.135 introdujo el ciclo completo de promoción y falsos negativos; p.136 confirmó una página de alta precisión geométrica y dos continuidades físicas; p.137 añadió 27 artículos y cerró en 871 objetos.

## Página 138

`data/lexicon/reconciliation/p138_reconciliation_status.json` registra:

- **47/47 candidatos** reconciliados: 24 izquierda + 23 derecha;
- los 47 son `article`; 46 límites son `exact` y `ALC1737-vcand-p138-L-006` es `merged_articles` porque absorbe el inicio visible siguiente;
- **48 inicios históricos visibles**;
- TP47 / FP0 / FN1;
- precisión **1.000000**, recall **0.979167**, F1 **0.989474**;
- el único falso negativo es `Ahogarſe con el bocado`, ya representado por `ALC1737-art-000017`;
- 47/47 candidatos `article` y 1/1 falso negativo enlazados;
- **15 artículos nuevos**, `ALC1737-art-000872`–`000886`;
- `pending_promotion = 0`.

La página obligó además a corregir la frontera material p.137→138. `ALC1737-art-000734`, `Aguja para trancas. Cuta. buoboi.`, comienza al final de p.137 y termina con `buoboi.` al inicio de p.138; se conserva como una sola unidad mediante `sourceSpans`. El reclamo inferior `Algun` de p.138 no se cuenta como artículo: p.139 abre con `Algun tanto de tiempo`.

La recollación de los 33 objetos seleccionados ya existentes de p.138 corrigió seis lecturas, todas versionadas en `data/lexicon/provenance/p138_selected_recollation_corrections.json`: `Hiquia arbuhuame` → `Hiquia aribuhuame`; `Ayſar à otro` → `Ayrar à otro`; `Amocta` → `Amoſa`; `Maſabuecori` → `Maſahuecori`; `Hita buneri` → `Hita huneri`; `Seſa buneri` → `Seſa huneri`.

`ALC1737-art-000884`, `Alargar algo`, conserva `Hitaric--ru-[ileg.]` y estado `unresolved`: el facsímil primario no permite completar responsablemente la continuación.

## QA diagnóstico y automático

La muestra diagnóstica del extractor conserva para `hybrid_margin_mode_v0.2` precisión 97.13%, recall 89.89% y F1 93.37% sobre pp.133, 134, 150 y 177. Es una muestra intencional, no probabilística.

**CHD QA run #81** terminó en `success`. Reconstruyó las 2,072 filas con el hash esperado y verificó **886 objetos en 61 JSONL / 886 `articleId` únicos**. También validó los 24+23 registros de reconciliación de p.138, su único falso negativo y los JSON de estado/procedencia. Una corrida verde es QA computacional, no revisión filológica humana.

## Fuentes de control textual

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` es una reimpresión histórica de control secundaria. `BNF1737-REPORTED` conserva la noticia bibliográfica de un ejemplar independiente de la edición de 1737 en la BnF; falta verificar directamente su ficha/signatura y, si es accesible, ingerirlo como testimonio separado.

## Incidencias editoriales abiertas

Permanecen, entre otras, `obra tripartita` frente a `quatro partes`, la duplicación de la regla 129, las discrepancias OCR 241/242 y 281/282, la posible ausencia visible de 294, la discontinuidad F→H p.157→158 y `Lucer-` p.161→162. Las lecturas de baja confianza se mantienen como `[ileg.]` o `unresolved`.

## Próximos criterios de cobertura

1. procesar la página digital **139** con el mismo ciclo de candidato → censo visible → promoción → QA;
2. escalar página por página hasta 177;
3. consolidar concordancias y exportaciones gramaticales/variacionales;
4. verificar directamente el ejemplar 1737 reportado en BnF;
5. incorporar revisión humana independiente suficiente para una futura release científica.
