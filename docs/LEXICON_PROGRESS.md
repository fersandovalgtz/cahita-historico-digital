# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El inventario canónico `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera. La capa curatorial contiene actualmente **1,045 artículos históricos estructurados**. Las páginas **133–144** están cerradas en reconciliación de candidatos, censo de inicios visibles, promoción/enlace y control computacional IA-asistido. Las páginas **145–160 tienen reconciliación completa de sus candidatos canónicos**, pero permanecen abiertas para censo exhaustivo de inicios visibles y promoción de fronteras sin transcripción suficientemente sustentada. **Ningún objeto es `human_verified` y la política vigente no contempla intervención humana independiente.**

## Inventario canónico

Las 2,072 filas están fijadas al PDF SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`; el JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

`scripts/export_candidate_page.py` reconstruye el inventario en memoria y permite inspeccionar de manera reproducible una página/columna concreta sin modificar el objeto canónico.

## Estado por páginas cerradas

| Tramo | Candidatos | `article` | Otros candidatos | Inicios visibles | TP | FP | FN | F1 | Pendientes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pp.133–134 | 61 | 57 | 4 continuaciones | 72 | 57 | 4 | 15 | 0.857143 | 0 |
| p.135 | 43 | 35 | 8 continuaciones | 47 | 35 | 8 | 12 | 0.777778 | 0 |
| p.136 | 48 | 48 | 0 | 49 | 48 | 0 | 1 | 0.989691 | 0 |
| p.137 | 39 | 36 | 3 continuaciones | 42 | 36 | 3 | 6 | 0.888889 | 0 |
| p.138 | 47 | 47 | 0 | 48 | 47 | 0 | 1 | 0.989474 | 0 |
| p.139 | 50 | 49 | 1 continuación | 51 | 49 | 1 | 2 | 0.970297 | 0 |
| p.140 | 47 | 44 | 3 continuaciones | 48 | 44 | 3 | 4 | 0.926316 | 0 |
| p.141 | 41 | 34 | 7 continuaciones | 40 | 34 | 7 | 6 | 0.839506 | 0 |
| p.142 | 53 | 50 | 2 paratextos + 1 falso positivo | 50 | 50 | 3 | 0 | 0.970874 | 0 |
| p.143 | 46 | 44 | 2 continuaciones | 48 | 44 | 2 | 4 | 0.936170 | 0 |
| p.144 | 39 | 39 | 0 | 46 | 39 | 0 | 7 | 0.917647 | 0 |

Las métricas son diagnósticas de ingeniería editorial IA-asistida. Bajo la política vigente no existe una capa posterior de revisión humana; por ello los objetos permanecen `machine_corrected_unverified` o `unresolved` aun cuando una página alcance cierre técnico.

## Crecimiento de la capa curatorial

El cierre secuencial elevó el corpus a **898 artículos** tras p.139, **910** tras p.140, **939** tras p.141, **979** tras p.142, **1,013** tras p.143 y **1,045** tras p.144. En todas las páginas cerradas el estado de promoción es `pendingPromotion = 0` o su equivalente.

El tramo conserva incertidumbres textuales explícitas cuando la evidencia primaria no permite una lectura fuerte. Entre ellas destaca `ALC1737-art-001045` (`Atormentar`), artículo transpaginal pp.144–145 cuya microestructura cahíta permanece `unresolved`; esa incertidumbre no altera el cierre estructural de p.144.

## Autoridad y estado epistemológico

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` funciona únicamente como reimpresión histórica de control y nunca sustituye silenciosamente al testimonio de 1737. `BNF1737-REPORTED` permanece como testimonio independiente reportado pendiente de verificación directa. Las lecturas dudosas se conservan como `[ileg.]`, de baja confianza o `unresolved` en lugar de completarse por analogía.

El flujo vigente de Cahíta Histórico Digital **no contempla intervención humana independiente**. `humanVerified` permanece en `false`; `human_verified` se conserva únicamente como estado reservado del esquema. El criterio de cierre es técnico: reconciliación computacional completa, incertidumbre localizada, continuidades físicas modeladas y QA satisfactorio. Ese cierre no debe describirse como autoridad diplomática o filológica humana.

## Página 145 — reconciliación de candidatos completada

La página digital **145** tiene **39 candidatos canónicos: 22 izquierda y 17 derecha**. La clasificación actual es **33 `article`**, **3 `continuation`** y **3 `unresolved`**. Las fronteras se distribuyen en 26 `exact`, 3 `merged_articles`, 4 `undersegmented`, 4 `ambiguous` y 2 `not_applicable`.

Trece candidatos de artículo enlazan 14 objetos estructurados preexistentes y **20 candidatos de artículo permanecen `pending_promotion`**. `ALC1737-art-001045` (`Atormentar`) conserva su continuidad p.144→145 y la forma `chumtieſte` permanece de baja confianza. El censo visible no se declara exhaustivo y por ello no se calculan métricas de rendimiento para esta página.

## Página 146 — reconciliación de candidatos completada

La página digital **146** contiene **47 candidatos canónicos: 21 izquierda y 26 derecha**. La clasificación estructural es **45 `article` y 2 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`; la calidad de frontera se distribuye en 42 `exact`, 1 `merged_articles`, 2 `oversegmented` y 2 `not_applicable`.

La capa seleccionada preexistente contiene 25 artículos `ALC1737-art-000184`–`000208`. Veintitrés candidatos enlazan 24 objetos. Se demostraron dos falsos negativos del extractor: `ALC1737-art-000184` antes de L-001 y `ALC1737-art-000193` dentro de L-008. R-023→R-024 y R-025→R-026 son continuidades físicas; el `Bebida` final de R-026 funciona como reclamo hacia p.147 L-001 y no como artículo nuevo.

Quedan **22 candidatos `pending_promotion`**. El censo visible sigue siendo un mínimo conocido, no exhaustivo, y las métricas permanecen sin calcular.

## Página 147 — reconciliación de candidatos completada

La página digital **147** contiene **51 candidatos canónicos: 26 izquierda y 25 derecha**. La clasificación estructural es **51 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **49 `exact`** y **2 `undersegmented`**.

La capa seleccionada preexistente contiene **15 artículos, `ALC1737-art-000209`–`ALC1737-art-000223`**. Los quince quedaron enlazados a candidatos. R-002 inicia el artículo seleccionado `Borracho. Buſca beodo.` pero contiene material OCR adicional; R-020 inicia `Brincar de alto abajo` y su agrupamiento arrastra material asociado con R-021, `Brincar por el suelo`.

Quedan **36 candidatos de artículo `pending_promotion`**. El censo visible no se declara exhaustivo. El `Bebida` final de p.146 anticipa p.147 L-001; el material `Brum*` al final de p.147 R-025 se trata como reclamo dañado que anticipa p.148 L-001 `Bruñidor`.

## Página 148 — reconciliación de candidatos completada

La página digital **148** contiene **44 candidatos canónicos: 23 izquierda y 21 derecha**. La clasificación estructural es **44 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **41 `exact`** y **3 `undersegmented`**.

La capa seleccionada contiene 15 artículos `ALC1737-art-000224`–`000238`. Se corrigió de forma auditada la columna de `ALC1737-art-000231`–`000235` (`Cabar`→`Cabeza`) de derecha a izquierda; la transcripción léxica no cambió. `ALC1737-art-000225` (`Bronce. Lo miſmo.`) conserva su anáfora histórica como `unresolved`.

Quedan **29 candidatos `pending_promotion`**. R-021 inicia `Calabaza generalmente`; `Cala-` final funciona como reclamo hacia la entrada fresca `Calabaza pequeña tierna` de p.149.

## Página 149 — reconciliación de candidatos completada

La página digital **149** contiene **61 candidatos canónicos: 31 izquierda y 30 derecha**. La clasificación machine-only es **55 `article`**, **5 `continuation`** y **1 `unresolved`**. La calidad de frontera se distribuye en **47 `exact`**, 5 `oversegmented`, 3 `undersegmented`, 1 `ambiguous` y 5 `not_applicable`.

La capa seleccionada preexistente contiene **15 artículos, `ALC1737-art-000239`–`ALC1737-art-000253`**. Los quince quedaron enlazados. `ALC1737-art-000239` (`Calabaza pequeña tierna`) se reparte entre L-001 y la continuación L-002. Otras continuidades internas demostradas son L-005→L-006, L-007→L-008, L-009→L-010 y L-014→L-015. `ALC1737-art-000247` (`Camarón`) comienza en L-031 y continúa físicamente en la parte superior de la columna derecha antes de R-001, conforme a sus `sourceSpans` ya existentes.

El candidato **L-019 permanece `unresolved`**. El OCR intercala fragmentos de las entradas contiguas de `Calentura` —incluidos `tener*`, otra aparición de `Calentura` y texto cahíta dañado— y no existe una capa preservada suficiente para asignar de modo responsable esa microestructura. L-018 se conserva como artículo `undersegmented`, pero no se reconstruye la secuencia textual faltante.

Quedan **40 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. El censo visible no se declara exhaustivo: se conocen al menos 55 inicios de artículo, pero la capa seleccionada no permite demostrar ausencia de otros falsos negativos; no se calculan TP/FP/FN ni F1.

En el borde inferior, R-030 comienza con `Carcoma de madera` y absorbe material dañado adicional. La página 150 abre con el artículo seleccionado **`Carcel. Tequiloacari.`**, por lo que no se afirma una continuidad larga p.149→150. `p149_machine_reconciliation_status.json` conserva el detalle de estas decisiones.

## Página 150 — reconciliación de candidatos completada

La página digital **150** contiene **56 candidatos canónicos: 26 izquierda y 30 derecha**. La reconciliación machine-only clasifica **55 `article`** y **1 `unresolved`**, sin candidatos `continuation`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **54 `exact`**, **1 `undersegmented`** y **1 `ambiguous`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000254`–`ALC1737-art-000268`**; los quince quedaron enlazados a candidatos canónicos. Las dos anáforas históricas seleccionadas `ALC1737-art-000266` (`Cobrar lo que ſe debe. Lo miſmo.`) y `ALC1737-art-000267` (`Cobre metal. Lo miſmo.`) mantienen su microestructura semántica `unresolved`, aunque sus fronteras físicas estén alineadas.

El único candidato estructuralmente irresuelto es **R-023**, en la región `Colgar algo` / `Colmar`: el OCR intercala material dañado y no permite decidir de forma responsable si se trata de continuación, ruido de layout o un inicio adicional. No se impone microsegmentación. L-026 inicia un artículo al pie de la columna izquierda y continúa físicamente en material no representado de la parte superior derecha antes de R-001; permanece sin promoción. R-030 inicia un artículo `Como...` pero absorbe además un `Com-` de borde/reclamo; p.151 L-001 abre un candidato fresco `Compadecerſe`, por lo que no se afirma una continuidad larga p.150→151.

Quedan **40 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. El censo visible no se declara exhaustivo: se conocen al menos 55 inicios candidatos de artículo, pero R-023 y la ausencia de un denominador facsimilar exhaustivo impiden calcular TP/FP/FN, precisión, recall o F1. `p150_machine_reconciliation_status.json` conserva estas decisiones y sus límites de evidencia.

## Página 151 — reconciliación de candidatos completada

La página digital **151** contiene **50 candidatos canónicos: 23 izquierda y 27 derecha**. La reconciliación machine-only clasifica **47 `article`** y **3 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **43 `exact`**, **3 `oversegmented`**, **1 `merged_articles`** y **3 `not_applicable`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000269`–`ALC1737-art-000283`**. Los quince quedaron enlazados mediante 13 candidatos canónicos. El caso central es **L-002**, región OCR dañada que absorbe tres artículos ya cotejados directamente: `000269` (`Compañón, ó cojon`), `000270` (`Compaſſar, ó medir con compás`) y `000271` (`Compaſſion. Buſca compadecerſe`). La reconciliación conserva esa frontera como `merged_articles` y no reemplaza las transcripciones seleccionadas por el OCR degradado.

En la columna derecha, **R-003, R-006 y R-009 son continuaciones físicas** de R-002, R-005 y R-008 respectivamente; por ello los tres candidatos precedentes se marcan `oversegmented`. El borde inferior también queda modelado: R-027 inicia `Coronilla...` al pie de p.151 y puede continuar en material superior no representado de p.152; como p.152 L-001 abre el artículo fresco `Crecer el hombre`, no se afirma continuidad hacia ese candidato.

Quedan **34 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Se conocen al menos **49 inicios de artículo**: los 47 candidatos clasificados como `article` más dos inicios adicionales absorbidos dentro de L-002. El censo visible sigue siendo no exhaustivo y, por tanto, no se calculan TP/FP/FN, precisión, recall o F1. `p151_machine_reconciliation_status.json` conserva el detalle de estas decisiones.

## Página 152 — reconciliación de candidatos completada

La página digital **152** contiene **52 candidatos canónicos: 28 izquierda y 24 derecha**. La reconciliación machine-only clasifica los **52 como `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`; las **52 fronteras** se conservan como `exact` en el plano estructural.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000284`–`ALC1737-art-000298`** y los quince quedaron enlazados directamente a candidatos canónicos. El OCR conserva dos incidencias sin convertirlas en hechos lexicográficos nuevos. **R-002** (`Cuyo ? Abcatea. Iotuc*`) arrastra `Iotuc`, forma que pertenece al artículo izquierdo seleccionado `Crecer el hombre`; se registra como probable contaminación OCR/layout entre columnas y no como un inicio adicional. **L-006** (`Criador Dios. Itotq tehuaca-`) termina truncado por guion, pero L-007 inicia el artículo fresco `Crucificar`; no se inventa una continuación inexistente en el inventario canónico.

Los bordes de página también quedan modelados conservadoramente. El `Coronilla...` final de p.151 puede continuar en material superior no representado antes de p.152 L-001, mientras L-001 abre de forma fresca `Crecer el hombre`. En el extremo opuesto, p.152 R-024 comienza `Cuñado de muger...`, pero p.153 L-001 abre el artículo fresco `Cuñado de hombre. Mocari.`; no se afirma una continuidad larga p.152→153.

Quedan **37 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 52 candidatos establecen al menos 52 comienzos estructurales conocidos, pero la capa seleccionada no es exhaustiva y no permite demostrar ausencia de falsos negativos; por ello no se calculan TP/FP/FN, precisión, recall ni F1. `p152_machine_reconciliation_status.json` conserva el detalle y los límites de autoridad.

## Página 153 — reconciliación de candidatos completada

La página digital **153** contiene **51 candidatos canónicos: 25 izquierda y 26 derecha**. La reconciliación machine-only clasifica **46 `article`**, **1 `continuation`** y **4 `unresolved`**. La calidad de frontera se distribuye en **40 `exact`**, 4 `undersegmented`, 1 `merged_articles`, 1 `oversegmented`, 4 `ambiguous` y 1 `not_applicable`.

La capa seleccionada contiene **15 artículos `ALC1737-art-000299`–`000313`**. Todos quedaron enlazados a evidencia estructural, pero no todos mediante candidatos de artículo: **dos comienzos seleccionados son falsos negativos demostrados en el borde superior derecho**. `ALC1737-art-000309` (`Dar. Amaca.`) y `ALC1737-art-000310` (`Dar coſas largas como palo. Tebec amaca.`) comienzan antes de R-001; R-001 conserva sólo `Tebec. amaca.` y se modela como continuación de `000310`. Estos falsos negativos se registran explícitamente en `p153_missed_visible_starts.jsonl`.

En la izquierda, **L-005** absorbe dos artículos seleccionados —`000302` (`Zambullir à otro. Aroptitua.`) y `000303` (`Zarcillo. Erepa.`)— y se conserva como `merged_articles`. L-001 arrastra un `Dar.` ajeno al artículo `Cuñado de hombre`, tratado como contaminación intercolumna; L-023 absorbe material `D.` de cambio alfabético. En la derecha, R-002 inicia el artículo seleccionado `Dar coſas redondas, y mazizas`, cuya terminación ocupa el comienzo de R-003. Como R-003 además introduce material guía dañado, **R-003–R-006 permanecen `unresolved`** en lugar de imponerse una microsegmentación especulativa.

El borde inferior queda también resuelto conservadoramente: R-026 inicia `Delatar` y arrastra `Desbat-` como reclamo/material de borde. P.154 L-001 abre el artículo fresco `Desbaſtar madera. Atapetia.`, por lo que no se afirma continuidad larga p.153→154.

Quedan **34 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Se conocen al menos **49 inicios**: 46 candidatos confirmados como `article`, un inicio adicional absorbido dentro de L-005 y dos falsos negativos superiores derechos. La región R-003–R-006 y la naturaleza no exhaustiva de la capa seleccionada impiden establecer un denominador completo; no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 154 — reconciliación de candidatos completada

La página digital **154** contiene **56 candidatos canónicos: 27 izquierda y 29 derecha**. La reconciliación machine-only clasifica los **56 como `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **54 `exact`**, **1 `undersegmented`** y **1 `oversegmented`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000314`–`000328`** y los quince quedaron enlazados directamente a candidatos canónicos. El candidato R-008 conserva un OCR severamente degradado, pero su geometría independiente y posición léxica sostienen una frontera de artículo; permanece sin promoción y no se fortalece su texto. R-024 inicia `Doler la llaga` y absorbe material final no explicado antes de R-025 `Doncella`, por lo que se marca `undersegmented` sin crear un inicio adicional.

El borde p.153→154 queda confirmado por el reclamo `Desbat-` de p.153 R-026, que anticipa el artículo fresco p.154 L-001 `Desbaſtar madera. Atapetia.`. En el extremo inferior, **R-029 (`Durar mucho tiempo`) cruza físicamente de página**: p.155 L-001 conserva la continuación de forma `nuc. bibuatua.` antes de los siguientes comienzos léxicos. Por ello R-029 se marca `oversegmented` respecto de la segmentación candidata entre páginas.

Quedan **41 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 56 candidatos sostienen al menos 56 comienzos estructurales, pero la capa seleccionada no es exhaustiva y no permite demostrar ausencia de falsos negativos; no se calculan TP/FP/FN, precisión, recall ni F1. `p154_machine_reconciliation_status.json` conserva el detalle y los límites de autoridad.

## Página 155 — reconciliación de candidatos completada

La página digital **155** contiene **49 candidatos canónicos: 23 izquierda y 26 derecha**. La reconciliación machine-only clasifica **45 `article`** y **4 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **39 `exact`**, 3 `oversegmented`, 2 `undersegmented`, 1 `merged_articles` y 4 `not_applicable`.

La página comienza con una continuidad material ya demostrada: **L-001 (`nuc. bibuatua.`) continúa p.154 R-029 (`Durar mucho tiempo`)** y no constituye un comienzo nuevo. Después, el extractor omite el artículo seleccionado `ALC1737-art-000329` (`Dar de beber à otro. Abitua.`), registrado como falso negativo conocido antes de L-002. **L-002** inicia `000330` (`Dar de veſtir à otro`) y absorbe además el comienzo de `000331` (`Echar, ò vaciar`), por lo que se conserva como `merged_articles`; `000331` se registra también como inicio interno omitido en `p155_missed_visible_starts.jsonl`.

En la parte superior derecha, R-001 proporciona la frontera geométrica del artículo seleccionado `000343` (`Encender candela, ò tea`), aunque el OCR pierde gran parte del lema; R-002 conserva sólo su forma `Abetia.` y se clasifica `continuation`. De modo equivalente, R-003→R-004 y R-006→R-007 forman dos pares artículo/continuación. R-024 absorbe material final dañado antes de `Enredar` y R-026 arrastra material `Eafar-...` de borde/reclamo que anticipa el inicio fresco `Enſeñar` en p.156 L-001; ambos se marcan `undersegmented` sin inventar nuevas voces.

Los **15 artículos seleccionados `ALC1737-art-000329`–`000343`** quedaron enlazados a evidencia estructural. Quedan **32 candidatos de artículo `pending_promotion`**; no hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 45 candidatos de artículo, el inicio adicional absorbido dentro de L-002 y el falso negativo `000329` establecen al menos **47 comienzos**. Como la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 156 — reconciliación de candidatos completada

La página digital **156** contiene **52 candidatos canónicos: 26 izquierda y 26 derecha**. La reconciliación machine-only clasifica los **52 como `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **51 `exact`** y **1 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000344`–`000358`**. Los quince quedaron enlazados mediante 14 candidatos canónicos. El caso central es **L-001**, que inicia `000344` (`Enſeñar. Amaſtia.`) y absorbe además el comienzo distinto de `000345` (`Enſeñanza. Amaſtianaque.`). Por ello L-001 se conserva como `merged_articles` y `000345` se registra de manera separada en `p156_missed_visible_starts.jsonl` como falso negativo interno conocido.

El material dañado del borde inferior de p.155 anticipa el inicio fresco `Enſeñar` de p.156, por lo que L-001 no se modela como continuación transpaginal. En el otro extremo, R-026 inicia `Eſquina`; la inspección del inventario de p.157 muestra que la página siguiente abre con material fresco de la serie Eſt-, por lo que tampoco se afirma continuidad p.156→157. L-025 (`Eſcobeta para peinarſe`) termina en OCR truncado `Co-`, pero ese daño textual no modifica por sí mismo la frontera estructural ni convierte L-026 en continuación.

Quedan **38 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 52 candidatos de artículo y el inicio adicional absorbido dentro de L-001 establecen al menos **53 comienzos visibles conocidos**; como la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1. `p156_machine_reconciliation_status.json` conserva el detalle y los límites de autoridad.

## Página 157 — reconciliación conservadora de candidatos completada

La página digital **157** contiene **42 candidatos canónicos: 19 izquierda y 23 derecha**. La reconciliación machine-only clasifica **38 `article`**, **2 `continuation`** y **2 `unresolved`**, sin `paratext` ni `false_positive`. La calidad de frontera se distribuye en **31 `exact`**, 2 `oversegmented`, 1 `undersegmented`, 4 `merged_articles`, 2 `ambiguous` y 2 `not_applicable`.

La columna izquierda está materialmente recortada y el OCR pierde sistemáticamente glifos iniciales y altera el orden de algunas formas. La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000359`–`000373`** y los quince quedaron enlazados mediante 11 candidatos de artículo. Cuatro candidatos contienen dos comienzos seleccionados cada uno y sus segundos inicios quedan registrados en `p157_missed_visible_starts.jsonl`: `000361` (`Eſtomago`) dentro de L-007, `000364` (`Eſtrella`) dentro de L-010, `000368` (`Eſtremecerſe`) dentro de L-014 y `000372` (`Facil coſa`) dentro de L-019.

L-004 inicia un artículo tipo `Eſtera` que continúa en L-005; L-012 (`Eſtrella las tres Marias`) continúa en L-013. **L-003 y L-006 permanecen `unresolved`**: el primero es un fragmento recortado cuya función no puede fijarse y el segundo mezcla la cola del artículo anterior con un probable comienzo fresco que no puede aislarse responsablemente. No se fuerza ninguna lectura para cerrar artificialmente la página.

El borde inferior exige una política distinta de una continuidad ordinaria. `ALC1737-gap-0001` documenta que el testimonio digital termina la secuencia visible con **`Flecha. Huihua.`** y un reclamo `Fle...`, mientras la página digital 158 comienza directamente con **`Hallarſe bien en vn lugar`**. El salto F→H se conserva como **material fuente presumiblemente faltante, de extensión no resuelta**. No se sintetizan voces F/G a partir de diccionarios modernos, reimpresiones u otras inferencias; cualquier recuperación futura requerirá un testimonio independiente y una capa de procedencia separada.

Quedan **27 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 38 candidatos de artículo y cuatro inicios seleccionados absorbidos en regiones fusionadas establecen al menos **42 comienzos visibles conocidos**, pero dos candidatos recortados permanecen irresueltos y la capa seleccionada no es exhaustiva; no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 158 — reconciliación conservadora de candidatos completada

La página digital **158** contiene **53 candidatos canónicos: 28 izquierda y 25 derecha**. La reconciliación machine-only clasifica **50 `article`** y **3 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **45 `exact`**, 1 `oversegmented`, 3 `undersegmented`, 1 `merged_articles` y 3 `not_applicable`.

La página comienza después de la discontinuidad material `ALC1737-gap-0001`. L-001 (`Hallarſe bien en vn lugar`) constituye un **inicio fresco de la secuencia H**, no una continuación del material F que termina p.157. La pérdida F/G permanece fuera de la cobertura reconstruida y no se sintetiza por inferencia.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000374`–`000388`**. Los quince quedaron enlazados mediante 14 candidatos de artículo. **L-014** inicia `000384` (`Henchir. Atapunia.`) y absorbe además el comienzo distinto de `000385` (`Henchimiento. Buſca llenar.`); por ello se conserva como `merged_articles` y `000385` queda registrado en `p158_missed_visible_starts.jsonl` como falso negativo interno conocido.

L-019 inicia `Herrar poner el hierro` y continúa en L-020. La región inferior izquierda L-026→L-027→L-028 contiene `Hilado` y varios fragmentos adicionales de guía/forma; se modela como una frontera `undersegmented` seguida de dos continuaciones, sin promover ni convertir en censo exhaustivo los posibles inicios internos no respaldados por anclas independientes. R-004 también queda `undersegmented`: su inicio tipo `Hinchazón` es estructuralmente claro, pero absorbe material interno demasiado dañado para microsegmentarlo responsablemente.

En el borde inferior, R-025 inicia `Hueva` y conserva un fragmento `Huey...` de borde. La primera ancla seleccionada de p.159 es **`Huevo. Totolichaba.`**, por lo que no se afirma una continuidad larga p.158→159; el fragmento dañado permanece como material de borde no promovido.

Quedan **36 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 50 candidatos de artículo y el comienzo seleccionado adicional absorbido dentro de L-014 establecen al menos **51 comienzos visibles conocidos**. Como L-026 y R-004 contienen material adicional sin ancla independiente y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 159 — reconciliación conservadora de candidatos completada

La página digital **159** contiene **52 candidatos canónicos: 26 izquierda y 26 derecha**. La reconciliación machine-only clasifica **49 `article`** y **3 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **40 `exact`**, 3 `oversegmented`, 6 `undersegmented` y 3 `not_applicable`.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000389`–`000403`** y los quince quedaron enlazados a candidatos canónicos. La página abre con `000389` (`Huevo. Totolichaba.`), inicio fresco que no continúa el `Hueva...` dañado del borde inferior de p.158. L-001 absorbe además `Aebole`, forma del artículo siguiente `000390` (`Huerfano`); de modo semejante, L-003 absorbe `Butte`, forma del artículo siguiente `000392` (`Huirſe`). Ambas fronteras se conservan `undersegmented` sin borrar los inicios frescos L-002/L-004.

Las continuidades modeladas son **L-025→L-026** (`Yerva para quelite`), **R-001→R-002** (`Yerva de la golondrina`) y **R-003→R-004**, donde `000401` (`Yerva que ſe cria en los arboles. Chibichiam.`) continúa en R-004. L-017, R-012 y R-022 contienen material guía adicional demasiado dañado o sin ancla independiente; queda marcado como `undersegmented`, pero no se promociona ni se convierte en un censo exhaustivo de falsos negativos.

La alineación detectó además una discrepancia de metadatos: `ALC1737-art-000398`, `000399` y `000400` estaban marcados como columna derecha, mientras sus textos coinciden con los candidatos geométricos izquierdos L-017, L-023 y L-024. Se corrigió **right→left** de forma auditada en `data/lexicon/provenance/p159_column_metadata_corrections.jsonl`; la transcripción, el tipo de artículo y las formas históricas no cambiaron.

R-026 inicia un artículo/cross-reference tipo `Yſlabon. Buſca eſlabon.` y conserva un pequeño fragmento de borde/catchword. El inventario canónico de p.160 abre con **`Yr derecho à alguna parte`**, por lo que se modela una transición fresca de página y no una continuación larga desde R-026.

Quedan **34 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 49 candidatos de artículo constituyen el mínimo de comienzos visibles estructuralmente sustentados; como existen agrupamientos con material interno sin anclas independientes y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 160 — reconciliación conservadora de candidatos completada

La página digital **160** contiene **45 candidatos canónicos: 19 izquierda y 26 derecha**. La reconciliación machine-only clasifica **44 `article`** y **1 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **40 `exact`**, 2 `oversegmented`, 2 `undersegmented` y 1 `not_applicable`.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000404`–`000418`**. Catorce artículos tienen comienzo candidato propio y `000404` (`Yr derecho à alguna parte. Tutula hueye.`) se modela como artículo en L-001 con continuación de forma en L-002. La página abre como transición fresca después del borde de p.159: L-001 no continúa `Yſlabon`.

La reconciliación documenta un falso negativo seleccionado inequívoco: **`ALC1737-art-000416` (`Ladrona. Eet buame.`)** aparece en la secuencia histórica entre `000415` (`Ladrido`) y `000417` (`Lagaña`), pero el inventario canónico salta directamente de R-005 a R-006. Se registra en `p160_missed_visible_starts.jsonl` como inicio `between_candidates`; este hallazgo no convierte la capa seleccionada en censo exhaustivo.

L-003 (`Yr rodeando`) y R-010 (`Lagrima`) quedan `undersegmented`: sus grupos OCR contienen además fragmentos de guía claramente diferenciados (`Yr delante...` y `Lamer...`, respectivamente), pero no se promueven voces internas ni se cuentan como falsos negativos exhaustivos sin anclas independientes. En el borde inferior, **R-026 inicia `Latir la vena, ò el corazón` y continúa físicamente en p.161 L-001**, que conserva la forma `Qobobohftanhuante`; p.161 L-002 abre ya el artículo fresco `Lavar`.

Quedan **30 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 44 candidatos de artículo más el inicio seleccionado `Ladrona` fuera del inventario establecen al menos **45 comienzos visibles conocidos**. Como existen grupos internos no exhaustivamente resueltos y la capa seleccionada no es cobertura total, no se calculan TP/FP/FN, precisión, recall ni F1.

## Próximo frente

En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; en p.155, **32 `pending_promotion`**; en p.156, **38 `pending_promotion`**; en p.157, **27 `pending_promotion`** y 2 candidatos `unresolved`; en p.158, **36 `pending_promotion`**; en p.159, **34 `pending_promotion`**; y en p.160, **30 `pending_promotion`**. Las páginas 145–160 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.

El siguiente frente geométrico es la **página digital 161**, con **33 candidatos canónicos: 17 izquierda y 16 derecha**. L-001 continúa el artículo `Latir la vena, ò el corazón` iniciado en p.160 R-026; L-002 comienza fresco `Lavar`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.
