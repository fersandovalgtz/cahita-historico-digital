# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El inventario canónico `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera. La capa curatorial contiene actualmente **1,045 artículos históricos estructurados**. Las páginas **133–144** están cerradas en reconciliación de candidatos, censo de inicios visibles, promoción/enlace y control computacional IA-asistido. Las páginas **145–174 tienen reconciliación completa de sus candidatos canónicos**, pero permanecen abiertas para censo exhaustivo de inicios visibles y promoción de fronteras sin transcripción suficientemente sustentada. **Ningún objeto es `human_verified` y la política vigente no contempla intervención humana independiente.**

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

## Página 161 — reconciliación conservadora de candidatos completada

La página digital **161** contiene **33 candidatos canónicos: 17 izquierda y 16 derecha**. La reconciliación machine-only clasifica **31 `article`**, **1 `continuation`** y **1 `unresolved`**, sin `paratext` ni `false_positive`. La calidad de frontera se distribuye en **29 `exact`**, 1 `merged_articles`, 2 `ambiguous` y 1 `not_applicable`.

La página abre con **L-001 (`Qobobohftanhuante`) como continuación de p.160 R-026 (`Latir la vena, ò el corazón`)**. L-002 comienza ya el artículo fresco seleccionado `000419` (`Lavar. Hipacſia, 1, baſona.`). La capa seleccionada contiene **15 artículos `ALC1737-art-000419`–`000433`**; doce tienen comienzo candidato propio y tres quedan documentados como falsos negativos seleccionados.

El primer falso negativo es **`000429` (`Lengua de buey. Buabuaſo.`)**, absorbido dentro de L-014 después de un artículo fresco `Levantar algo del suelo`; por ello L-014 se marca `merged_articles`. Los otros dos son **`000430` (`Libro. Lo miſmo.`)** y **`000431` (`Limon. Lo miſmo.`)**, ubicados en la transición de columna después de L-017 (`Liar`) y antes de R-001, sin candidato canónico propio. Ambos conservan su fórmula anafórica sin intentar resolverla por inferencia.

La parte inferior derecha mantiene incertidumbre explícita. **R-015** conserva una frontera geométrica compatible con un comienzo nuevo, pero el OCR perdió el lema; se clasifica `article` con evaluación `ambiguous` y queda sin promoción. **R-016** es un fragmento mínimo que no permite decidir responsablemente entre artículo, continuación, paratexto o falso positivo, por lo que permanece `unresolved`. La página 162 abre fresco con `Media coſa la mitad. Najucu.`, así que no se afirma continuidad transpaginal desde R-016.

Quedan **19 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 31 candidatos de artículo más los tres comienzos seleccionados sin candidato propio establecen al menos **34 comienzos visibles conocidos**. Como R-016 sigue irresuelto y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 162 — reconciliación conservadora de candidatos completada

La página digital **162** contiene **39 candidatos canónicos: 20 izquierda y 19 derecha**. La reconciliación machine-only clasifica **39 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **36 `exact`**, **2 `undersegmented`** y **1 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000434`–`000448`**. Catorce comienzan en candidato canónico propio y **`000439` (`Memoria. Aubuate.`)** queda absorbido dentro de L-006 después de `000438` (`Melon. Manari.`). Por ello L-006 se conserva como `merged_articles` y `000439` se registra de forma separada en `p162_missed_visible_starts.jsonl` como falso negativo interno conocido.

La auditoría contra el export canónico corrigió varias lecturas provisionales antes del cierre. **L-020** conserva de forma recuperable `Merecer. Hkamabare`, de modo que su frontera es `exact`. **R-011** conserva `Miedo tener. Mahabuené` y se clasifica como artículo, no como fragmento irresuelto. El seleccionado **`000448` (`Mirar. Abicha.`) se alinea a R-016**, mientras R-014 corresponde al artículo distinto `Miembro del hombre` y permanece `pending_promotion`. R-006 queda `undersegmented` porque su grupo `Meter como en la caxa` absorbe material adicional sin anclas seleccionadas independientes.

Los bordes de página permanecen frescos. P.162 L-001 inicia `000434` (`Media coſa la mitad. Najucu.`) después del fragmento irresuelto R-016 de p.161, sin continuidad transpaginal. En el extremo inferior, **R-019 inicia un artículo `Mirar saliendo de lo obscuro`-like y absorbe el reclamo `Mozo`**, por lo que también queda `undersegmented`. Ese reclamo anticipa el artículo fresco seleccionado de p.163 **`000449` (`Mozo de edad. Buſca mancebo.`)**; el primer candidato canónico p.163 L-001 comienza ya en su cola `...cebo.` y contiene después `Mofar, eſcarnecer`. No se afirma continuidad léxica p.162→163.

Quedan **25 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 39 candidatos de artículo más el inicio seleccionado `Memoria` absorbido en L-006 establecen al menos **40 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y los grupos subsegmentados pueden contener material interno sin anclas independientes, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 163 — reconciliación conservadora de candidatos completada

La página digital **163** contiene **49 candidatos canónicos: 26 izquierda y 23 derecha**. La reconciliación machine-only clasifica **42 `article`** y **7 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **31 `exact`**, **6 `oversegmented`**, **5 `undersegmented`** y **7 `not_applicable`**.

El arranque de página conserva una pérdida de frontera explícita. El reclamo `Mozo` al final de p.162 anticipa el artículo fresco seleccionado **`000449` (`Mozo de edad. Buſca mancebo.`)**, pero el inventario canónico de p.163 no le asigna frontera propia: L-001 comienza ya en la cola `...cebo.` y después abre el seleccionado **`000450` (`Mofar, eſcarnecer. Buſca menoſpreciar.`)**. `000449` se registra por ello como falso negativo de borde superior; no se interpreta el reclamo de p.162 como continuidad léxica.

La microestructura del comienzo se conserva sin reconstrucción silenciosa. L-001 queda `undersegmented` por mezclar la cola de `000449` con el inicio de `000450`; L-002 comienza con la continuación/cross-reference `menoſpreciar` de `000450` y después abre un artículo fresco `Moho como de pan`; L-003 empieza con la cola de ese artículo y abre `Moho como de hierro`, que continúa físicamente en L-004. L-007 también queda `undersegmented`: recibe material de la voz previa antes de abrir el seleccionado `000452` (`Moler. Tuſe.`).

Las siete continuidades canónicas son **L-003→L-004**, **L-010→L-011** (`000455`, `Molendero el que muele. Tuſeme.`), **L-012→L-013** (`Mondar algo...`), **L-022→L-023** (`Morirſe de frío`-like), **L-026→R-001** (`Mosquito, que llaman gegen`, a través de columnas), **R-004→R-005** (`Mostrar con el dedo. Buſca apuntar`) y **R-006→R-007** (`Moverſe, menearſe`). Los candidatos que originan una continuación se conservan `oversegmented`; las filas de continuación son `not_applicable` como frontera fresca.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000449`–`000463`**. Catorce comienzan dentro de candidatos canónicos y `000449` queda documentado fuera del inventario mediante `p163_missed_visible_starts.jsonl`; los quince quedan así enlazados a evidencia estructural. R-023 inicia un artículo `Murmuyo`-like y absorbe ruido/catchword dañado al pie de página, pero p.164 L-001 abre fresco con **`000464` (`Nacimiento. Ioleria.`)**, por lo que no se afirma continuidad p.163→164.

Quedan **28 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 42 candidatos de artículo más el comienzo seleccionado `000449` fuera del inventario establecen al menos **43 comienzos visibles conocidos**. La capa seleccionada no es exhaustiva y los grupos `undersegmented` pueden contener material interno no anclado, por lo que no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 164 — reconciliación conservadora de candidatos completada

La página digital **164** contiene **51 candidatos canónicos: 29 izquierda y 22 derecha**. La reconciliación machine-only clasifica **51 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **48 `exact`** y **3 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000464`–`000478`** y los quince quedaron enlazados a candidatos canónicos propios. La página abre de forma fresca con **`000464` (`Nacimiento. Ioleria.`)** después del material inferior dañado de p.163; no se afirma continuidad léxica p.163→164. El seleccionado **`000477` (`Noez, y nogal. Lo miſmo.`)** conserva su anáfora histórica como `unresolved` semántico, pero su frontera física R-001 es `exact`; la incertidumbre de contenido y la clasificación de frontera permanecen desacopladas.

Tres grupos canónicos contienen más de una unidad guía visible en el OCR y se conservan como **`merged_articles`**. R-018 comienza `Nudo` y contiene además una unidad `O. adv. para llamar`-like; R-020 contiene `Obediente` y `Obediencia`; R-022 comienza `Obligación`, contiene un comienzo `Obrar algo`-like y termina con un fragmento `Obr...` de borde/reclamo. Esos inicios internos no poseen anclas seleccionadas/directamente cotejadas en esta pasada: por ello **no se crean artículos, no se promocionan y no se inflan como falsos negativos del censo visible**.

El borde inferior se modela como transición fresca. Aunque R-022 termina con `Obr...`, la página 165 L-001 abre el artículo seleccionado **`000479` (`Obra aſſi, hechura. Chupari.`)**; no se impone una continuidad larga p.164→165. El inventario canónico de p.165 contiene **56 candidatos: 29 izquierda y 27 derecha**.

Quedan **36 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los **51 candidatos de artículo** constituyen el mínimo conservador de comienzos visibles estructuralmente sustentados. Como R-018, R-020 y R-022 contienen unidades internas no ancladas y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 165 — reconciliación conservadora de candidatos completada

La página digital **165** contiene **56 candidatos canónicos: 29 izquierda y 27 derecha**. La reconciliación machine-only clasifica **52 `article`** y **4 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **45 `exact`**, **4 `oversegmented`**, **1 `undersegmented`**, **1 `merged_articles`**, **1 `ambiguous`** y **4 `not_applicable`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000479`–`000493`**. Catorce candidatos de artículo enlazan los quince objetos seleccionados: **L-016** contiene dos comienzos cotejados, `000487` (`Oydor el que oye. Hicahame.`) y `000488` (`Oyr. Hicaha.`). Por ello L-016 queda `merged_articles` y `000488` se registra de forma separada en `p165_missed_visible_starts.jsonl` como falso negativo interno conocido.

Las cuatro continuidades canónicas son **L-003→L-004**, **L-014→L-015**, **R-002→R-003** y **R-007→R-008**. La última completa el cross-reference seleccionado `000490` (`Orejear. Buſca menear las orejas.`); R-008 conserva la cola `...jas` y no es un comienzo fresco. Los candidatos que originan estas continuidades se conservan `oversegmented`; las filas de continuación son `not_applicable` como frontera fresca.

La incertidumbre queda localizada sin fortalecer el OCR. **R-014** inicia el seleccionado `000493` (`Oſado ſer. Buſca atrevido.`) y absorbe material adyacente dañado, por lo que queda `undersegmented`. **R-016** conserva una frontera geométrica propia, pero el OCR no permite recuperar responsablemente su guía española; se mantiene como `article` con evaluación `ambiguous` y `pending_promotion`, sin inventar lema. En L-012, el seleccionado `000485` (`Oficio propio del hombre`) convive con fuga de orden OCR procedente de la entrada vecina `Oy, adv. de tiempo`; la autoridad de transcripción permanece en las anclas seleccionadas.

Los bordes de página son frescos. P.165 L-001 abre `000479` (`Obra aſſi, hechura. Chupari.`) después del fragmento `Obr...` de p.164, sin continuidad larga. En el extremo inferior, R-027 abre `Padrino`, mientras p.166 L-001 comienza fresco con **`000494` (`Paga tal. Bebeti.`)**. El inventario canónico de p.166 contiene **50 candidatos: 28 izquierda y 22 derecha**.

Quedan **38 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 52 candidatos de artículo más el comienzo seleccionado `000488` absorbido en L-016 establecen al menos **53 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y las regiones dañadas pueden contener material interno sin anclas independientes, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 166 — reconciliación conservadora de candidatos completada

La página digital **166** contiene **50 candidatos canónicos: 28 izquierda y 22 derecha**. La reconciliación machine-only clasifica **50 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **46 `exact`**, **3 `undersegmented`** y **1 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000494`–`000508`**. Catorce candidatos enlazan los quince objetos seleccionados: **L-003** contiene `000496` (`Palabra. Noqui.`) y `000497` (`Palma arbol conocido. Taco.`). Por ello L-003 queda `merged_articles` y `000497` se registra en `p166_missed_visible_starts.jsonl` como falso negativo interno conocido.

La fuga de orden OCR se conserva sin transformarla en transcripción. **L-007** inicia el cross-reference seleccionado `000501` (`Palo para eſcarbar tierra. Buſca coa.`) y absorbe `brazo.` de la región vecina de `000502` (`Paletilla del brazo`). **R-008** inicia un artículo `Partear`-like, pero contiene además `tierra` y `Hapari`-like desplazados desde las entradas seleccionadas izquierdas `000501`/`000502`; ambos grupos quedan `undersegmented`. L-008 sigue siendo el comienzo estructural de `000502`, y la capa seleccionada de cotejo directo conserva la autoridad de su transcripción.

En el borde inferior, **R-022** inicia un artículo dañado Pesar-like y contiene además material `Paſſo`-like de borde/reclamo, por lo que queda `undersegmented`. La página 167 L-001 abre de forma fresca el seleccionado **`000509` (`Paſſo de las beſtias. Arabuerama.`)**; no se afirma continuidad léxica p.166→167. El inventario canónico de p.167 contiene **55 candidatos: 30 izquierda y 25 derecha**.

Quedan **36 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 50 candidatos de artículo más el comienzo seleccionado `000497` absorbido en L-003 establecen al menos **51 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y existe fuga de orden OCR, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 167 — reconciliación conservadora de candidatos completada

La página digital **167** contiene **55 candidatos canónicos: 30 izquierda y 25 derecha**. La reconciliación machine-only clasifica **54 `article`** y **1 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **47 `exact`**, **1 `oversegmented`**, **3 `undersegmented`**, **2 `merged_articles`**, **1 `ambiguous`** y **1 `not_applicable`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000509`–`000523`**. Catorce candidatos de artículo enlazan los quince objetos seleccionados: **L-010** contiene `000518` (`Pato. Tepciabiri.`) y `000519` (`Paxaro generalmente. Moel.`). Por ello L-010 queda `merged_articles` y `000519` se registra en `p167_missed_visible_starts.jsonl` como falso negativo interno conocido.

La única continuidad canónica inequívoca es **R-002→R-003**: `Pedernal prieto para flechas` comienza en R-002 y su forma `Bicam` continúa en R-003. R-002 queda `oversegmented` y R-003 `not_applicable` como frontera fresca. **L-030** se conserva como `article` con evaluación `ambiguous`: la geometría sustenta un comienzo entre `Pecar` y `Pedazo`, pero el OCR no permite recuperar responsablemente su guía española y no se promueve.

Las mezclas internas se conservan sin convertir OCR en edición. **R-011** contiene `Peine` más material `Apea`-like de la región siguiente y **R-013** termina con un fragmento `limpi-` procedente de material adyacente; ambos quedan `undersegmented`. **R-020** comienza `Pelo interior. Huiboa.` y contiene una segunda unidad guía `pelo... Caita chona`-like, por lo que queda `merged_articles`; ese inicio interno no seleccionado no se promociona ni se registra como falso negativo sin ancla directa independiente.

El borde inferior es fresco. **R-025** comienza `Pena generalmente` y absorbe `Pena-` como material de borde/catchword, por lo que queda `undersegmented`. P.168 L-001 comienza un artículo fresco `Penacho...`; el primer seleccionado de p.168 es `000524` (`Penca de miſcal. Cuumaicoa.`) en L-002. El inventario canónico de p.168 contiene **32 candidatos: 14 izquierda y 18 derecha**.

Quedan **40 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 54 candidatos de artículo más el comienzo seleccionado `000519` absorbido en L-010 establecen al menos **55 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y persisten grupos `merged_articles`/`undersegmented` sin anclas independientes, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 168 — reconciliación conservadora de candidatos completada

La página digital **168** contiene **32 candidatos canónicos: 14 izquierda y 18 derecha**. La reconciliación machine-only clasifica **32 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **24 `exact`**, **5 `undersegmented`** y **3 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000524`–`000538`**. Once candidatos enlazan doce objetos seleccionados y cuatro comienzos seleccionados carecen de frontera canónica independiente. Tres se registran conservadoramente `between_candidates`: **`000528` (`Pepita generalmente. Tepſia.`)**, **`000530` (`Perder generalmente. Ataru.`)** y **`000531` (`Perderſe en el camino. Chituc-bochi.`)**. El cuarto, **`000533` (`Perdonar la injuria. Ahiocore.`)**, está absorbido dentro de L-007 después de `000532` (`Perdon. Nehiocore.`); L-007 queda por ello `merged_articles`.

La microsecuencia de pérdida se conserva sin imponer una geometría que el extractor no sustenta. L-006 comienza el seleccionado `000529` (`Pequeño. Ilichi.`) y contiene un fragmento `...tuc-bochi` compatible con la cola de `000531`; por ello queda `undersegmented`, pero el comienzo de `000531` se registra entre candidatos y no se fuerza dentro de L-006. De manera semejante, L-013 comienza `000537` (`Perſona. Ioreme.`) y contiene una segunda unidad `Pertenecer...`-like no seleccionada, por lo que queda `merged_articles`; L-014 comienza `000538` (`Peſada coſa. Beete.`) y conserva material `Buſca penar`-like adyacente como `undersegmented`.

En la columna derecha, **R-009** contiene al menos dos unidades `Pescado` diferenciables y queda `merged_articles`, pero el inicio interno no seleccionado no se promociona ni se añade al censo sin ancla independiente. **R-011** conserva una voz `Pescuezo`/`cerviz`-like junto con fuga de orden `Calulute` procedente de la izquierda y queda `undersegmented`. **R-018** inicia `Pie de animal` y termina con `Pie-` de borde/catchword, también `undersegmented`.

El borde inferior se mantiene fresco. P.169 tiene **35 candidatos: 19 izquierda y 16 derecha**. Su primer seleccionado es **`000539` (`Piedra de que ſe ſacan navajas. Buſca pedernal prieto.`)**; el candidato p.169 L-001 comienza ya en su cola `...bajas. Buſca pedernal prieto.` y después absorbe varias voces siguientes. El `Pie-` de p.168 se trata como material de borde/catchword, no como continuidad léxica larga.

Quedan **21 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 32 candidatos de artículo más los cuatro comienzos seleccionados perdidos establecen al menos **36 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y persisten grupos `merged_articles`/`undersegmented` sin anclas independientes, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 169 — reconciliación conservadora de candidatos completada

La página digital **169** contiene **35 candidatos canónicos: 19 izquierda y 16 derecha**. La reconciliación machine-only clasifica **34 `article`** y **1 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **28 `exact`**, **2 `undersegmented`**, **3 `merged_articles`**, **1 `ambiguous`** y **1 `not_applicable`**.

El arranque de página requiere contabilidad explícita para no inflar el censo. El seleccionado **`000539` (`Piedra de que ſe ſacan navajas. Buſca pedernal prieto.`)** comienza antes de la frontera canónica: L-001 arranca ya en su cola `...bajas. Buſca pedernal prieto.`. Dentro del mismo megagrupo aparecen además los comienzos seleccionados **`000540` (`Piel`)**, **`000541` (`Pino`)** y **`000542` (`Pinal`)**, seguidos por varias voces OCR no seleccionadas. L-001 queda `merged_articles` y se documentan cuatro missed-starts seleccionados `000539`–`000542`: uno de borde superior y tres internos.

Los cuatro missed-starts no se suman mecánicamente a los 34 candidatos de artículo. L-001 no representa una frontera fresca independiente, sino una región que abre en la cola de `000539`; por ello el mínimo conservador se calcula como **33 regiones de artículo restantes + 4 comienzos seleccionados = 37 comienzos visibles conocidos**. Las voces OCR internas no seleccionadas de L-001 no se añaden a ese mínimo sin ancla de cotejo directo.

La única continuidad canónica es **L-002→L-003**: L-002 contiene una cola previa y abre una voz `Piſar alguna coſa`-like no seleccionada cuyo material cahíta continúa en L-003 (`huotle.`). L-002 queda `undersegmented` y L-003 `continuation/not_applicable`. L-010 también queda `undersegmented` por material `huefo.` adyacente. **R-005** conserva una frontera geométrica compatible con artículo, pero su guía es irrecuperable responsablemente desde OCR y se mantiene `article/ambiguous` sin promoción.

En la derecha, **R-009** contiene `Pocas vezes` y una segunda unidad `poco`-like; **R-016** agrupa numerosas voces (`Polilla`, `Polvos`, `Pollo`, `Poner`, varios `Por...`, etc.). Ambos quedan `merged_articles`, pero sus comienzos internos OCR-only no se promocionan ni se cuentan como falsos negativos sin anclas independientes. Los quince artículos seleccionados `ALC1737-art-000539`–`000553` quedan enlazados a evidencia estructural. El seleccionado **`000548` (`Plato. Lo miſmo.`)** conserva su anáfora semántica como `unresolved`, mientras la frontera física L-018 permanece `exact`.

El borde inferior es fresco. P.170 contiene **48 candidatos: 26 izquierda y 22 derecha**. Su primer seleccionado **`000554` (`Por donde? Hacumbichaca?`)** es un comienzo de borde superior sin candidato propio; el primer candidato canónico p.170 L-001 comienza ya con **`000555` (`Porqué? Hita bechibuo?`)**. No se afirma continuidad larga desde el megagrupo R-016 de p.169.

Quedan **22 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. El censo visible sigue no exhaustivo; por tanto no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 170 — reconciliación conservadora de candidatos completada

La página digital **170** contiene **48 candidatos canónicos: 26 izquierda y 22 derecha**. La reconciliación machine-only clasifica **48 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **44 `exact`**, **2 `undersegmented`** y **2 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000554`–`000568`**. Doce candidatos enlazan trece objetos seleccionados y se documentan tres comienzos seleccionados sin frontera independiente. **`000554` (`Por donde? Hacumbichaca?`)** es un comienzo fresco en el borde superior izquierdo antes de L-001 (`000555`, `Porqué?`). **`000568` (`Puerco, ò puerca. Cobuu.`)** aparece en el borde superior derecho antes de R-001 (`Pulga. Teput.`). Ambos se registran como missed-starts de borde.

El tercer missed-start es **`000563` (`Premiar. Buſca pagar.`)**, absorbido dentro de L-008 después de `000562` (`Pregunta. Atema.`). L-008 queda `merged_articles` y enlaza ambos artículos seleccionados. **L-024** también queda `merged_articles` porque el grupo comienza una voz `Proximo`-like y contiene una segunda unidad `Publico ſer`-like; esta última no está seleccionada/directamente cotejada en la capa disponible, por lo que no se promociona ni se añade al censo de falsos negativos.

**L-004** comienza el seleccionado `000558` (`Predicar hazer ſermon. Hinabaca.`) y conserva `Hinababacame`-like material de `000559`, cuya guía `Predicador` sí tiene frontera propia en L-005; se modela como `undersegmented` por fuga de orden, sin perder la frontera de L-005. En el borde inferior, **R-022** inicia una voz Querellarse-like y termina con `Que-` de borde/catchword, por lo que también queda `undersegmented`.

El paso p.170→171 se conserva fresco. P.171 contiene **24 candidatos: 7 izquierda y 17 derecha** y L-001 abre el seleccionado **`000569` (`Querella. Natebo.`)**. El `Que-` final de p.170 no se trata como continuidad léxica larga.

Quedan **36 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 48 candidatos de artículo más los tres comienzos seleccionados perdidos establecen al menos **51 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y persisten grupos `merged_articles`/`undersegmented` no agotados, no se calculan TP/FP/FN, precisión, recall ni F1.

## Página 171 — reconciliación conservadora completada

P.171 contiene **24 candidatos: 7 izquierda y 17 derecha**: **23 `article`** y **1 `continuation`**. L-007 es un megagrupo `merged_articles` que inicia `000575` y concentra ocho comienzos seleccionados sin frontera propia (`000576`–`000583`); cuatro son visibles dentro del grupo y cuatro se registran conservadoramente `between_candidates`. R-001 es forma-only y queda `continuation/from_previous_column`. L-004/L-005 quedan `undersegmented`; R-003/R-017 `merged_articles`; R-015 `article/ambiguous`. No se corrige la columna declarada de los seleccionados.

Quedan **16 `pending_promotion`**, no hubo promociones y el corpus sigue en **1,045 artículos**. El mínimo sustentado es **31 comienzos visibles conocidos**; no se calculan métricas por falta de censo exhaustivo. P.172 tiene **55 candidatos: 27 izquierda y 28 derecha**; `000584` (`Relampago. Beroitcme.`) es un comienzo superior sin candidato propio y L-001 comienza `Redaño`.

## Página 172 — reconciliación conservadora completada

P.172 contiene **55 candidatos: 27 izquierda y 28 derecha**, todos clasificados `article`. El seleccionado **`000584` (`Relampago. Beroitcme.`)** es un comienzo fresco en el borde superior sin frontera canónica propia; los otros 14 seleccionados `000585`–`000598` se alinean con candidatos propios. R-028 queda `merged_articles`: comienza `Ruido hazer el agua` y termina con una segunda unidad `Rubio`-like, que no se promociona ni se añade al censo sin ancla independiente.

Quedan **41 `pending_promotion`**, no hubo promociones y el corpus sigue en **1,045 artículos**. El mínimo sustentado es **56 comienzos visibles conocidos** y no se calculan métricas por falta de censo exhaustivo. P.173 tiene **42 candidatos: 20 izquierda y 22 derecha**; `000599` (`Rueda. Buſca redonda coſa.`) es un comienzo superior sin candidato propio y L-001 comienza `Sabio`.

## Página 173 — reconciliación conservadora completada

P.173 contiene **42 candidatos: 20 izquierda y 22 derecha**: **40 `article`** y **2 `continuation`**. Los missed-starts seleccionados demostrados son `000599` (`Rueda`) y `000600` (`Saber generalmente`) en el borde superior, `000605` (`Sahumar`) dentro de L-010 y `000607` (`Salitral`) dentro de L-011. L-001→L-002 y R-002→R-003 son las dos continuidades. L-010, L-011 y R-015 quedan `merged_articles`; R-018 queda `undersegmented`.

Quedan **29 `pending_promotion`**, no hubo promociones y el corpus sigue en **1,045 artículos**. El mínimo sustentado es **44 comienzos visibles conocidos** y no se calculan métricas por falta de censo exhaustivo. P.174 tiene **48 candidatos: 26 izquierda y 22 derecha**; `000614` (`Si, adv. para afirmar. Hebui.`) es un comienzo superior sin candidato propio y L-001 comienza `Si, conj. Soc.`.

## Página 174 — reconciliación conservadora completada

P.174 contiene **48 candidatos: 26 izquierda y 22 derecha**, todos clasificados **`article`**. Se documentan tres missed-starts seleccionados: `000614` (`Si, adv. para afirmar. Hebui.`) en el borde superior antes de L-001, `000623` (`Socorrer. Buſca ayudar.`) dentro de L-013 y `000628` (`Soplar. Apuña.`) dentro de L-024. L-013 y L-024 quedan `merged_articles` por esos comienzos internos seleccionados; R-001, R-006, R-011 y R-012 quedan también `merged_articles` por múltiples unidades guía visibles en el OCR, pero las unidades internas no seleccionadas no se promocionan ni se añaden al censo sin ancla independiente.

Los 15 seleccionados `ALC1737-art-000614`–`000628` quedan enlazados a evidencia estructural mediante 14 candidatos más el missed-start superior. Quedan **34 `pending_promotion`**, no hubo promociones y el corpus sigue en **1,045 artículos**. El mínimo sustentado es **51 comienzos visibles conocidos** y no se calculan métricas por falta de censo exhaustivo. P.175 tiene **35 candidatos: 20 izquierda y 15 derecha** y abre fresco con `ALC1737-art-000629` (`Tarde. Cuſte.`) alineado a L-001; no se afirma continuidad p.174→175.

## Próximo frente

En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; en p.155, **32 `pending_promotion`**; en p.156, **38 `pending_promotion`**; en p.157, **27 `pending_promotion`** y 2 candidatos `unresolved`; en p.158, **36 `pending_promotion`**; en p.159, **34 `pending_promotion`**; en p.160, **30 `pending_promotion`**; en p.161, **19 `pending_promotion`** y 1 candidato `unresolved`; y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; en p.165, **38 `pending_promotion`**; en p.166, **36 `pending_promotion`**; en p.167, **40 `pending_promotion`**; en p.168, **21 `pending_promotion`**; en p.169, **22 `pending_promotion`**; y en p.170, **36 `pending_promotion`**; y en p.171, **16 `pending_promotion`**; y en p.172, **41 `pending_promotion`**; y en p.173, **29 `pending_promotion`**; y en p.174, **34 `pending_promotion`**. Las páginas 145–174 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.

El siguiente frente geométrico es la **página digital 175**, con **35 candidatos canónicos: 20 izquierda y 15 derecha**. La capa seleccionada comienza con `ALC1737-art-000629` (`Tarde. Cuſte.`), alineado al primer candidato L-001; el borde p.174→175 es fresco. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.
