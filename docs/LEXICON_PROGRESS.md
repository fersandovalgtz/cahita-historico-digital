# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El inventario canónico `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera. La capa curatorial contiene actualmente **1,045 artículos históricos estructurados**. Las páginas **133–144** están cerradas en reconciliación de candidatos, censo de inicios visibles, promoción/enlace y control computacional IA-asistido. Las páginas **145–147 tienen reconciliación completa de sus candidatos canónicos**, pero permanecen abiertas para censo exhaustivo de inicios visibles y promoción de fronteras sin transcripción suficientemente sustentada. **Ningún objeto es `human_verified` y la política vigente no contempla intervención humana independiente.**

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

La página digital **147** contiene **51 candidatos canónicos: 26 izquierda y 25 derecha**. Los 51 quedaron clasificados en `p147_left_reconciliation.jsonl` y `p147_right_reconciliation.jsonl`.

La clasificación estructural es **51 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **49 `exact`** y **2 `undersegmented`**. R-002 inicia el artículo seleccionado `Borracho. Buſca beodo.` pero contiene material OCR adicional; R-020 inicia `Brincar de alto abajo` y su agrupamiento arrastra material asociado con el siguiente candidato R-021, `Brincar por el suelo`.

La capa seleccionada preexistente contiene **15 artículos, `ALC1737-art-000209`–`ALC1737-art-000223`**. Los quince quedaron enlazados a candidatos: 14 en la columna izquierda y uno en la derecha. No se observó un falso negativo demostrable dentro de esta capa de anclaje, pero su cobertura —en especial un solo artículo seleccionado en la columna derecha— es demasiado escasa para afirmar que no existan otros inicios omitidos.

Quedan **36 candidatos de artículo `pending_promotion`**. Sus fronteras son suficientemente claras para reconciliación estructural, pero no se promueven desde OCR sin una transcripción más fuerte. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**.

El borde entre páginas también quedó modelado. El `Bebida` final de p.146 anticipa p.147 L-001, `Bebida de chía, y maíz toſtado`, que es una entrada nueva. En el borde p.147→148, el material `Brum*` al final de R-025 se trata como reclamo dañado que anticipa p.148 L-001, `Bruñidor`, y no como un segundo artículo de p.147.

El censo visible **no se declara exhaustivo**. Se conocen al menos 51 inicios, pero la ausencia de un censo facsimilar completo impide demostrar que ese mínimo sea el denominador real. Por ello TP/FP/FN, precisión, recobrado y F1 permanecen sin calcular. `p147_machine_reconciliation_status.json` registra esta distinción.

## Próximo frente

En p.145 continúa la reducción de **20 `pending_promotion`** y 3 `unresolved`; en p.146 quedan **22 `pending_promotion`**; y en p.147 quedan **36 `pending_promotion`**. Las tres páginas tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.

El siguiente frente geométrico es la **página digital 148**, con **44 candidatos canónicos**. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.
