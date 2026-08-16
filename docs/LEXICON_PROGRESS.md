# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera y la capa curatorial contiene **898 artículos históricos estructurados**. Las páginas **133–139** están cerradas en reconciliación, censo visible, promoción/enlace y QA computacional IA-asistidos. **Ningún objeto es `human_verified`.**

## Inventario canónico

Las 2,072 filas están fijadas al PDF SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`; el JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

`scripts/export_candidate_page.py` reconstruye el inventario en memoria y permite inspeccionar de manera reproducible una página/columna concreta sin modificar el objeto canónico.

## Estado por páginas cerradas

| Tramo | Candidatos | `article` | `continuation` | Inicios visibles | TP | FP | FN | F1 | Pendientes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pp.133–134 | 61 | 57 | 4 | 72 | 57 | 4 | 15 | 0.857143 | 0 |
| p.135 | 43 | 35 | 8 | 47 | 35 | 8 | 12 | 0.777778 | 0 |
| p.136 | 48 | 48 | 0 | 49 | 48 | 0 | 1 | 0.989691 | 0 |
| p.137 | 39 | 36 | 3 | 42 | 36 | 3 | 6 | 0.888889 | 0 |
| p.138 | 47 | 47 | 0 | 48 | 47 | 0 | 1 | 0.989474 | 0 |
| p.139 | 50 | 49 | 1 | 51 | 49 | 1 | 2 | 0.970297 | 0 |

Las métricas son diagnósticas de ingeniería editorial IA-asistida y no sustituyen la colación filológica humana.

## Página 139 — ciclo cerrado

`data/lexicon/reconciliation/p139_reconciliation_status.json` documenta los **50/50 candidatos**: 25 por columna. Cuarenta y nueve corresponden a inicios de artículo y uno, `ALC1737-vcand-p139-R-002`, es una continuación sobregenerada de `A man izquierda`. La geometría queda en 47 `exact`, 2 `merged_articles` y 1 `oversegmented`.

El censo registra **51 inicios históricos visibles**, TP49 / FP1 / FN2, precisión **0.980000**, recall **0.960784** y F1 **0.970297**. Los dos falsos negativos son `A limpiar algo` dentro de L-003 y `A man derecha` dentro de L-025. Ambos ya enlazan sus artículos históricos.

Se promovieron **12 artículos nuevos**, `ALC1737-art-000887`–`000898`, elevando el corpus a **898**. Siete promociones conservan `unresolved` por ilegibilidad o microestructura histórica no resuelta: `000889`, `000891`, `000892`, `000894`, `000895`, `000897` y `000898`. `pending_promotion = 0`.

### Fronteras físicas y reclamos

`A man derecha` (`ALC1737-art-000068`) comienza al final de la columna izquierda y su forma continúa al inicio de la derecha. La continuidad está identificada en la reconciliación; queda pendiente actualizar el objeto histórico con `sourceSpans` explícitos.

Los reclamos `Algun` p.138 → `Algun tanto de tiempo` p.139 y `Ancia-` p.139 → `Anciano. Oola.` p.140 están registrados en `data/lexicon/boundary_markers/catchwords_p138_p140.jsonl` como paratexto, no como artículos.

### Incidencias de recollación detectadas

La revisión de p.139 detectó dos lecturas antiguas que requieren corrección versionada específica antes de considerarlas cerradas a nivel textual: `ALC1737-art-000073`, cuya evidencia apunta a `Sahualic`, y `ALC1737-art-000074`, cuyo lema visible es `Amaſar` frente a la lectura previa `Amalar`. Se mantienen como tareas puntuales y no se silencian dentro de la reconciliación.

## QA automático

**CHD QA run #92** concluyó en `success`. Reconstruyó las 2,072 filas canónicas y verificó **898 objetos en 62 JSONL / 898 `articleId` únicos**, además de los 25+25 registros de reconciliación de p.139, sus dos falsos negativos y el JSON de estado. Una corrida verde es QA computacional, no revisión filológica humana.

## Fuentes y autoridad

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` permanece como reimpresión histórica de control y `BNF1737-REPORTED` como testimonio independiente reportado, aún pendiente de verificación directa. Las lecturas dudosas se conservan como `[ileg.]` o `unresolved` y no se completan por inferencia silenciosa.

## Próximo frente

La siguiente página es la **digital 140**, con **47 candidatos canónicos (24 izquierda + 23 derecha)**. Debe procesarse con el mismo ciclo candidato → censo visible → promoción/enlace → QA, sin perder las tareas puntuales de p.139 (`000068`, `000073`, `000074`).
