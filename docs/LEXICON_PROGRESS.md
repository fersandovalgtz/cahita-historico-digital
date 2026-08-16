# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El inventario canónico `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera. La capa curatorial contiene actualmente **1,045 artículos históricos estructurados**. Las páginas **133–144** están cerradas en reconciliación de candidatos, censo de inicios visibles, promoción/enlace y control computacional IA-asistido. **Ningún objeto es `human_verified`.**

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

Las métricas son diagnósticas de ingeniería editorial IA-asistida y no sustituyen la colación filológica humana.

## Crecimiento de la capa curatorial

El cierre secuencial elevó el corpus a **898 artículos** tras p.139, **910** tras p.140, **939** tras p.141, **979** tras p.142, **1,013** tras p.143 y **1,045** tras p.144. En todas las páginas cerradas el estado de promoción es `pendingPromotion = 0` o su equivalente.

El tramo conserva incertidumbres textuales explícitas cuando la evidencia primaria no permite una lectura fuerte. Entre ellas destaca `ALC1737-art-001045` (`Atormentar`), artículo transpaginal pp.144–145 cuya microestructura cahíta permanece `unresolved`; esa incertidumbre no altera el cierre estructural de p.144.

## Autoridad y estado epistemológico

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` funciona únicamente como reimpresión histórica de control y nunca sustituye silenciosamente al testimonio de 1737. `BNF1737-REPORTED` permanece como testimonio independiente reportado pendiente de verificación directa. Las lecturas dudosas se conservan como `[ileg.]`, de baja confianza o `unresolved` en lugar de completarse por analogía.

Todo el tramo 133–144 debe describirse como **`machine_corrected_unverified`**. Una corrida verde de QA o una reconciliación cerrada no equivalen a revisión filológica humana.

## Página 145 — preflight de reconciliación

La página digital **145** tiene **39 candidatos canónicos: 22 en la columna izquierda y 17 en la derecha**. Existe además una capa anterior de **14 artículos seleccionados de alta legibilidad** (`ALC1737-art-000170`–`000183`), pero esa selección no constituye un censo exhaustivo de la página.

`data/lexicon/reconciliation/p145_preflight.json` fija el estado previo al cierre. La página recibe en su apertura la continuación material de `ALC1737-art-001045` (`Atormentar`), iniciado al pie de p.144. La segunda forma se conserva como lectura de baja confianza `chumtieſte` y no debe promoverse como un nuevo artículo ni fortalecerse editorialmente sin colación independiente.

La consulta del texto OCR derivado de Internet Archive confirma el bloque de vocabulario alrededor de la transición p.144→145, pero también evidencia que la salida lineal mezcla el orden de las dos columnas. Por ello el OCR no se utiliza para inventar métricas de frontera, TP/FP/FN ni transcripciones diplomáticas. El preflight permanece deliberadamente **abierto** hasta inspeccionar las 39 filas canónicas con geometría y realizar cotejo directo de la página.

## Próximo frente

Cerrar exhaustivamente la **digital 145** con el protocolo ya estabilizado: exportar/inspeccionar candidatos → cotejar facsímil → clasificar fronteras → construir censo visible → enlazar/promover artículos → registrar continuidades físicas → ejecutar QA → sincronizar documentación, Issue #3 y Notion.

Hasta completar ese ciclo, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo cerrado.
