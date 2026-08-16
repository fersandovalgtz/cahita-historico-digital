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
| Artículos históricos estructurados | **1,013** | capa curatorial actual; no conteo final del vocabulario |
| Páginas de vocabulario con representación estructurada | **45 / 45** | al menos una representación por página |
| Páginas con reconciliación + censo + promoción cerrados | **133–143** | IA-asistido; no `human_verified` |
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
| Reconciliación p.139 | **50 / 50 candidatos** | 49 article; 1 continuation |
| Censo visible p.139 | **51 inicios** | TP49 / FP1 / FN2; F1 0.970297 |
| Reconciliación p.140 | **47 / 47 candidatos** | 44 article; 3 continuation |
| Censo visible p.140 | **48 inicios** | TP44 / FP3 / FN4; F1 0.926316 |
| Reconciliación p.141 | **41 / 41 candidatos** | 34 article; 7 continuation |
| Censo visible p.141 | **40 inicios** | TP34 / FP7 / FN6; F1 0.839506 |
| Reconciliación p.142 | **53 / 53 candidatos** | 50 article; 2 paratext; 1 false_positive |
| Censo visible p.142 | **50 inicios** | TP50 / FP3 / FN0; F1 0.970874 |
| Reconciliación p.143 | **46 / 46 candidatos** | 44 article; 2 continuation |
| Censo visible p.143 | **48 inicios** | TP44 / FP2 / FN4; F1 0.936170 |
| Agregado pp.133–143 | **475 candidatos / 495 inicios visibles** | TP444 / FP31 / FN51; F1 0.915464 |
| `pending_promotion` pp.133–143 | **0** | candidatos article y falsos negativos visibles enlazados |
| Lagunas/discontinuidades del testimonio | **1** | `ALC1737-gap-0001`, digital 157→158 |
| Anomalías de frontera adicionales | **1 abierta** | p.161 `Lucer-` → p.162 sin lema visible |
| QA automatizado | **activo** | GitHub Actions valida inventario, IDs, schemas y reconciliaciones hasta p.143 |
| Revisión humana independiente | **0** | no iniciada |

## Arte gramatical

Las páginas impresas 1–118, digitales 15–132, están representadas de forma continua en la capa de transcripción IA-asistida. Las fronteras mixtas de las digitales 69 y 105 se conservan estructuralmente. Esta cobertura de superficie textual no equivale a una edición crítica cerrada.

## Vocabulario

El vocabulario ocupa las digitales 133–177. `hybrid_margin_mode_v0.2` produce **2,072 candidatos de frontera**, mientras que la capa curatorial contiene **1,013 artículos históricos estructurados**. Son objetos distintos y ninguna cifra debe interpretarse como el número final de entradas de la obra.

El inventario completo está fijado a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10` y al PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`. El JSONL reconstruido tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

La utilidad `scripts/export_candidate_page.py` permite inspeccionar de forma reproducible una página concreta del inventario canónico sin alterar su representación persistida.

## Página 139 — ciclo cerrado

`data/lexicon/reconciliation/p139_reconciliation_status.json` registra:

- **50/50 candidatos** reconciliados: 25 izquierda + 25 derecha;
- **49 `article`** y **1 `continuation`**;
- calidad geométrica: **47 `exact`**, 2 `merged_articles` y 1 `oversegmented`;
- **51 inicios históricos visibles**;
- TP49 / FP1 / FN2;
- precisión **0.980000**, recall **0.960784**, F1 **0.970297**;
- 49/49 candidatos `article` enlazados;
- 2/2 falsos negativos enlazados;
- **12 artículos nuevos**, `ALC1737-art-000887`–`000898`;
- `pending_promotion = 0`.

Los dos falsos negativos son `A limpiar algo`, absorbido dentro del candidato que comienza `Aliento, ó huelgo`, y `A man derecha`, absorbido dentro del candidato de `Amancebarſe hurtando à la muger`. `ALC1737-vcand-p139-R-002` contiene sólo la continuación `bichaca.` del artículo `A man izquierda`, por lo que no se contabiliza como entrada nueva.

Siete de las doce promociones de p.139 permanecen `unresolved` en su microestructura o en segmentos de baja legibilidad (`000889`, `000891`, `000892`, `000894`, `000895`, `000897`, `000898`). No se completaron por OCR ni por analogía.

La continuidad material de `ALC1737-art-000068` (`A man derecha`) entre el final de la columna izquierda y el inicio de la derecha quedó identificada durante el cierre; la normalización de sus `sourceSpans` en el objeto histórico es una tarea puntual pendiente. La recollación también señaló dos objetos seleccionados antiguos para corrección versionada posterior: `000073` (la evidencia apunta a `Sahualic`) y `000074` (el lema visible es `Amaſar`, no la lectura previa `Amalar`).

Los reclamos se mantienen como paratexto: `Algun` al pie de p.138 conduce a `Algun tanto de tiempo. Me quiſu.` en p.139, y `Ancia-` al pie de p.139 conduce a `Anciano. Oola.` en p.140. Se documentan en `data/lexicon/boundary_markers/catchwords_p138_p140.jsonl` y no inflan el conteo lexicográfico.

## Página 140 — ciclo cerrado

`data/lexicon/reconciliation/p140_reconciliation_status.json` registra:

- **47/47 candidatos** reconciliados: 24 izquierda + 23 derecha;
- **44 `article`** y **3 `continuation`**;
- calidad geométrica: **40 `exact`**, 4 `merged_articles` y 3 `oversegmented`;
- **48 inicios históricos visibles**;
- TP44 / FP3 / FN4;
- precisión **0.936170**, recall **0.916667**, F1 **0.926316**;
- 44/44 candidatos `article` enlazados;
- 4/4 falsos negativos enlazados;
- **12 artículos nuevos**, `ALC1737-art-000899`–`000910`;
- `pending_promotion = 0`.

Los cuatro falsos negativos visibles son `Andar ſobre vno de los pies`, `Andas de muertos`, `Anteceder, ò guiar` y `Añublado eſtár en partes el Cielo`, todos absorbidos dentro de grupos candidatos mayores. Sólo `Andas de muertos` requería promoción nueva; los otros tres ya tenían objeto histórico estructurado.

Las tres falsas fronteras R-019, R-021 y R-023 son continuaciones físicas de artículos iniciados en el candidato precedente. R-023 contiene además el reclamo inferior `Apar-`, que se conserva como paratexto y se excluye del censo de artículos. Las remisiones `Buſca` de `Anguſtiarſe`, `Anguſtia` y `Anguſtiar á otro` se modelaron explícitamente como `cross_reference`, no como equivalencias cahítas.

## Página 141 — ciclo cerrado

`data/lexicon/reconciliation/p141_reconciliation_status.json` registra:

- **41/41 candidatos** reconciliados: 20 izquierda + 21 derecha;
- **34 `article`** y **7 `continuation`**;
- calidad geométrica: **31 `exact`**, 3 `merged_articles` y 7 `oversegmented`;
- **40 inicios históricos visibles**;
- TP34 / FP7 / FN6;
- precisión **0.829268**, recall **0.850000**, F1 **0.839506**;
- 34/34 candidatos `article` enlazados;
- 6/6 falsos negativos enlazados;
- **29 artículos nuevos**, `ALC1737-art-000911`–`000939`;
- `pending_promotion = 0`.

Los seis falsos negativos visibles son `Apercibirſe para hazer algo`, `Apetecer algo`, `Aplacar á alguno`, `Aprenſar`, `Apiopriarſe alguna coſa` y `A qué tiempo?`. Cinco están absorbidos dentro de grupos candidatos mayores y `Apiopriarſe alguna coſa` comienza antes del primer límite candidato de la columna derecha; R-001 arranca ya en su continuación `ta auhoria.`.

Dos promociones se mantienen explícitamente `unresolved` en su microestructura, no en la existencia del artículo: `ALC1737-art-000930` (`Apretarla por detrás, ò delante de la mula`) conserva sin interpretar los separadores históricos entre formas, y `ALC1737-art-000936` (`Apuntar con el dedo à alguna parte`) conserva un separador gráfico ambiguo. La lectura de `Apreſuramiento` fue recotejada y corregida a `Taaubamiria` antes del cierre.

El artículo `ALC1737-art-000141` comienza al pie de p.141 y continúa en p.142; su representación trans-página con `sourceSpans` se conserva separadamente y está enlazada al candidato R-021.

## Página 142 — ciclo cerrado

`data/lexicon/reconciliation/p142_reconciliation_status.json` registra:

- **53/53 candidatos** reconciliados: 20 izquierda + 33 derecha;
- **50 `article`**, **2 `paratext`** y **1 `false_positive`**;
- calidad geométrica: **50 `exact`** y 3 `not_applicable`;
- **50 inicios históricos visibles**;
- TP50 / FP3 / FN0;
- precisión **0.943396**, recall **1.000000**, F1 **0.970874**;
- 50/50 candidatos `article` enlazados;
- ningún falso negativo visible;
- **40 artículos nuevos**, `ALC1737-art-000940`–`000979`;
- corpus acumulado **979**;
- `pending_promotion = 0`.

La continuación de `ALC1737-art-000141` al comienzo de la columna izquierda (`padecen de las caderas. Bapſam.`) no se contó como nuevo inicio. Los candidatos L-006 y R-004 son encabezados históricos de agrupación —`Arboles, cuyo fruto es comeſtible` y `Arboles que ſirven para madera`— y L-020 es un artefacto OCR/layout sin frontera visible correspondiente. R-022 contiene `Arbol. Hocona.` y absorbe además el encabezado `Arboles chaparros`; R-033 contiene `Arbol. Sañia.` y el reclamo inferior `Arbol.` para p.143. Encabezados y reclamos se excluyen del conteo lexicográfico.

El antiguo piloto botánico de p.142 fue recotejado a 600 dpi antes del cierre. Se corrigieron, conservando IDs y trazabilidad, `ALC1737-art-000131` de `Hohuno` a **`Hohuo`** y `ALC1737-art-000135` de `Maccchua` a **`Maccehua`**. Las afirmaciones terapéuticas o botánicas históricas siguen representándose exclusivamente como contenido de la fuente, sin identificación taxonómica moderna ni validación de eficacia.

## Página 143 — ciclo cerrado

`data/lexicon/reconciliation/p143_reconciliation_status.json` registra:

- **46/46 candidatos** reconciliados: 30 izquierda + 16 derecha;
- **44 `article`** y **2 `continuation`**;
- calidad geométrica: **40 `exact`**, 4 `merged_articles` y 2 `oversegmented`;
- **48 inicios históricos visibles**;
- TP44 / FP2 / FN4;
- precisión **0.956522**, recall **0.916667**, F1 **0.936170**;
- 44/44 candidatos `article` enlazados;
- 4/4 falsos negativos enlazados;
- **34 artículos nuevos**, `ALC1737-art-000980`–`001013`;
- corpus acumulado **1,013**;
- `pending_promotion = 0`.

Los cuatro inicios visibles omitidos por el extractor son `Arbol. Sapo.`, `Arenal. Sepai.`, `Armarſe para la batalla. Emo anahuſacana bechibuo.` y `Arriba como en la ſotea. Catabepa.`. El primero ya tenía objeto seleccionado (`000147`); los otros tres fueron promovidos en el cierre. Los candidatos L-021 (`cori.`) y L-027 (`betec.`) son continuaciones físicas, no entradas nuevas.

La recollación a 600 dpi corrigió dos lecturas antiguas conservando sus IDs: `ALC1737-art-000143` de `Hilobue` a **`Hiolhue`** y `ALC1737-art-000153` de `Curuat` a **`Curuas`**. La trazabilidad quedó registrada en `data/lexicon/provenance/p143_selected_recollation_corrections.json`.

En `Arrendar dar algo à renta` se conserva literalmente el separador histórico `l` de `Hitare urec, l, reureuri`; no se le asignó una función lingüística moderna. Del mismo modo, guiones y separadores de `Namacari --- buecamta popona`, `Hitaric -- huique` y formas afines se conservaron cuando eran visibles, eliminando sólo particiones tipográficas inequívocas de fin de línea.

## QA diagnóstico y automático

La muestra diagnóstica del extractor conserva para `hybrid_margin_mode_v0.2` precisión 97.13%, recall 89.89% y F1 93.37% sobre pp.133, 134, 150 y 177. Es una muestra intencional, no probabilística.

**CHD QA run #135** concluyó en `success` después del cierre de p.143 y de ampliar nuevamente el workflow. Verificó el inventario canónico, unicidad/estados de IDs, todos los artículos históricos contra schema, reconciliaciones hasta p.143, capas de falsos negativos hasta p.143 y sintaxis JSON de los estados/proveniencias incluidos. Una corrida verde es QA computacional, no revisión filológica humana.

## Fuentes de control textual

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` es una reimpresión histórica de control secundaria. `BNF1737-REPORTED` conserva la noticia bibliográfica de un ejemplar independiente de la edición de 1737 en la BnF; falta verificar directamente su ficha/signatura y, si es accesible, ingerirlo como testimonio separado.

## Incidencias editoriales abiertas

Permanecen, entre otras, `obra tripartita` frente a `quatro partes`, la duplicación de la regla 129, las discrepancias OCR 241/242 y 281/282, la posible ausencia visible de 294, la discontinuidad F→H p.157→158, `Lucer-` p.161→162, la normalización de `sourceSpans` de `000068` y la recollación versionada de `000073`/`000074`. Las lecturas de baja confianza se mantienen como `[ileg.]` o `unresolved`.

## Próximos criterios de cobertura

1. procesar la página digital **144** mediante candidato → censo visible → promoción → QA;
2. escalar página por página hasta 177;
3. resolver las tareas puntuales de metadatos/corrección detectadas en p.139;
4. consolidar concordancias y exportaciones gramaticales/variacionales;
5. verificar directamente el ejemplar 1737 reportado en BnF;
6. incorporar revisión humana independiente suficiente para una futura release científica.
