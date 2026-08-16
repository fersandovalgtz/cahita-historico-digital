# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera y la capa curatorial contiene **886 artículos históricos estructurados**. Las páginas **133–138** están cerradas en reconciliación, censo visible, promoción/enlace y QA computacional IA-asistidos. **Ningún objeto es `human_verified`.**

## Inventario canónico

Las 2,072 filas están fijadas al PDF SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`; el JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

## Estado por páginas cerradas

| Tramo | Candidatos | `article` | `continuation` | Inicios visibles | TP | FP | FN | F1 | Pendientes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pp.133–134 | 61 | 57 | 4 | 72 | 57 | 4 | 15 | 0.857143 | 0 |
| p.135 | 43 | 35 | 8 | 47 | 35 | 8 | 12 | 0.777778 | 0 |
| p.136 | 48 | 48 | 0 | 49 | 48 | 0 | 1 | 0.989691 | 0 |
| p.137 | 39 | 36 | 3 | 42 | 36 | 3 | 6 | 0.888889 | 0 |
| p.138 | 47 | 47 | 0 | 48 | 47 | 0 | 1 | 0.989474 | 0 |

## Página 138 — ciclo cerrado

`data/lexicon/reconciliation/p138_reconciliation_status.json` registra **47/47 candidatos** reconciliados, 24 izquierda + 23 derecha. Todos son `article`; 46 límites son `exact` y `ALC1737-vcand-p138-L-006` es `merged_articles` porque absorbe el inicio siguiente `Ahogarſe con el bocado`.

El censo visual registra **48 inicios históricos**, TP47 / FP0 / FN1, precisión **1.000000**, recall **0.979167** y F1 **0.989474**. El único falso negativo enlaza `ALC1737-art-000017`. Se promovieron **15 artículos nuevos**, `ALC1737-art-000872`–`000886`; `pending_promotion = 0`.

### Continuidad material p.137→138

`ALC1737-art-000734` no termina en p.137: `Aguja para trancas. Cuta.` continúa al inicio de p.138 con `buoboi.`. Se conserva como una sola unidad mediante `sourceSpans` p.137 derecha → p.138 izquierda y la decisión se documenta en `data/lexicon/provenance/p137_p138_art000734_continuation.json`. El reclamo `Algun` al pie de p.138 se excluye; p.139 abre con `Algun tanto de tiempo`.

### Recollación de artículos existentes

La recollación de los 33 objetos seleccionados ya existentes corrigió seis lecturas: `Hiquia arbuhuame` → `Hiquia aribuhuame`; `Ayſar à otro` → `Ayrar à otro`; `Amocta` → `Amoſa`; `Maſabuecori` → `Maſahuecori`; `Hita buneri` → `Hita huneri`; `Seſa buneri` → `Seſa huneri`. La procedencia se conserva en `data/lexicon/provenance/p138_selected_recollation_corrections.json`.

`ALC1737-art-000884`, `Alargar algo`, permanece `unresolved` como `Hitaric--ru-[ileg.]`: el facsímil primario no permite una terminación responsable.

## QA automático

**CHD QA run #81** concluyó en `success`. Reconstruyó las 2,072 filas canónicas y verificó **886 objetos en 61 JSONL / 886 `articleId` únicos**, además de los 24+23 registros de reconciliación de p.138, su falso negativo y los JSON de estado/procedencia. Una corrida verde es QA computacional, no revisión filológica humana.

## Fuentes y autoridad

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` permanece como reimpresión histórica de control y `BNF1737-REPORTED` como testimonio independiente reportado, aún pendiente de verificación directa. Las lecturas dudosas se conservan como `[ileg.]` o `unresolved` y no se completan por inferencia silenciosa.

## Próximo frente

La siguiente página es la **digital 139**, con **50 candidatos canónicos (25+25)**. Debe procesarse con el mismo ciclo: candidato → censo visible → promoción/enlace → QA.
