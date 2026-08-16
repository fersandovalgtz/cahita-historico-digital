# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El inventario canónico `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera. La capa curatorial contiene actualmente **1,045 artículos históricos estructurados**. Las páginas **133–144** están cerradas en reconciliación de candidatos, censo de inicios visibles, promoción/enlace y control computacional IA-asistido. Las páginas **145–146 tienen ya reconciliación completa de sus candidatos canónicos**, pero permanecen abiertas para censo exhaustivo de inicios visibles y promoción de fronteras sin transcripción suficientemente sustentada. La **p.147 tiene preflight reproducible abierto sobre 51 candidatos y 15 artículos seleccionados preexistentes**. **Ningún objeto es `human_verified` y la política vigente no contempla intervención humana independiente.**

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

La página digital **145** tiene **39 candidatos canónicos: 22 en la columna izquierda y 17 en la derecha**. Los 39 están persistidos en `p145_left_reconciliation.jsonl` y `p145_right_reconciliation.jsonl`.

La clasificación de máquina actual es **33 `article`**, **3 `continuation`** y **3 `unresolved`**. Las fronteras se distribuyen en **26 `exact`**, 3 `merged_articles`, 4 `undersegmented`, 4 `ambiguous` y 2 `not_applicable`. Trece candidatos de artículo enlazan **14 objetos estructurados preexistentes** de la capa seleccionada; **20 candidatos de artículo quedan `pending_promotion`** porque la frontera puede sostenerse pero la lectura textual disponible no justifica todavía crear un objeto curatorial confiable.

La apertura de p.145 conserva la continuación material de `ALC1737-art-001045` (`Atormentar`), iniciado al pie de p.144. La segunda forma sigue como lectura de baja confianza `chumtieſte`; no se duplica como entrada nueva ni se fortalece por analogía.

El censo de inicios visibles **no se declara exhaustivo**. La evidencia preservada demuestra que algunos candidatos absorben inicios internos —por ejemplo el primer candidato derecho contiene las entradas seleccionadas `Aventarſe el vientre` y `Axi, ò pimienta`— y existen otros inicios probables cuyo texto es demasiado dañado para promoción responsable. Por esa razón TP/FP/FN, precisión, recobrado y F1 se mantienen deliberadamente sin calcular para p.145.

`data/lexicon/reconciliation/p145_machine_reconciliation_status.json` documenta el estado completo de este pase.

## Página 146 — reconciliación de candidatos completada

La página digital **146** contiene **47 candidatos canónicos: 21 en la columna izquierda y 26 en la derecha**. Los 47 quedaron clasificados en `p146_left_reconciliation.jsonl` y `p146_right_reconciliation.jsonl`.

La clasificación estructural es **45 `article` y 2 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **42 `exact`**, 1 `merged_articles`, 2 `oversegmented` y 2 `not_applicable`.

La capa seleccionada preexistente contiene **25 artículos, `ALC1737-art-000184`–`ALC1737-art-000208`**. Veintitrés candidatos enlazan 24 de esos objetos; `ALC1737-art-000184`, `Baho, q ſale de la boca`, es un falso negativo de borde superior sin candidato contenedor. L-008 enlaza simultáneamente `000192` (`Bañarſe`) y `000193` (`Barata darſe la coſa`), por lo que `000193` constituye un segundo inicio visible omitido por el detector de fronteras.

La inspección de toda la geometría confirma además dos continuidades en el pie derecho. R-023 inicia `Beber agua con la mano arrojándola à la boca` y R-024 conserva su continuación. R-025 inicia `Bebida de maíz toſtado`; R-026 comienza con material de continuidad y termina en el reclamo **`Bebida`**, que anticipa la apertura de p.147: `Bebida de chía, y maíz toſtado`. Ese reclamo no se cuenta como nuevo artículo de p.146.

Quedan **22 candidatos de artículo `pending_promotion`**. Sus fronteras estructurales son suficientemente claras, pero carecen de una lectura facsimilar/seleccionada suficientemente fuerte para convertir el OCR dañado en transcripción curatorial. No se promovió ninguno durante este pase y el corpus permanece en **1,045 artículos**.

`p146_missed_visible_starts.jsonl` registra los **dos falsos negativos ya demostrados**, pero el censo visible todavía se considera un **mínimo conocido, no exhaustivo**. Por ello no se calculan TP/FP/FN agregados ni precisión, recobrado o F1 para p.146. `p146_machine_reconciliation_status.json` conserva esta distinción explícita.

## Página 147 — preflight reproducible

La página digital **147** contiene **51 candidatos canónicos: 26 izquierda y 25 derecha**. La capa seleccionada preexistente es más escasa que en p.146: **15 artículos `ALC1737-art-000209`–`ALC1737-art-000223`**, 14 en la columna izquierda y sólo 1 en la derecha. Por ello se trata explícitamente como capa de anclaje, no como expectativa de cobertura.

El borde p.146→147 queda físicamente aclarado: el `Bebida` final de p.146 R-026 es un reclamo que anticipa p.147 L-001, **`Bebida de chía, y maíz toſtado`**, alineado con `ALC1737-art-000209`. L-002 (`Bebida otra de maíz`) aparece como un inicio distinto fuera de la capa seleccionada; L-003 y L-004 se alinean con `000210` (`Beſtia`) y `000211` (`Bibora`), mientras L-005 contiene otra entrada `Bibora...` no seleccionada.

En la columna derecha, R-001 (`Bordón`) no tiene ancla seleccionada; R-002 inicia el único artículo derecho seleccionado, `ALC1737-art-000223` (`Borracho. Buſca beodo.`), aunque contiene material OCR adicional que deberá resolverse al reconciliar la página completa. R-003–R-005 son también inicios probables fuera de la capa seleccionada.

`data/lexicon/reconciliation/p147_preflight.json` fija estos hechos sin declarar todavía clasificación completa, promociones ni métricas.

## Próximo frente

En p.145 continúa la reducción de **20 `pending_promotion`** y 3 `unresolved`; en p.146 quedan **22 `pending_promotion`** y el censo visible exhaustivo. El frente geométrico activo es ahora **p.147**: exportar los 51 candidatos completos, alinear los 15 anclajes seleccionados, clasificar cada frontera y detectar falsos negativos adicionales.

Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.
