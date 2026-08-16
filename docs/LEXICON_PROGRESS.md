# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El extractor canónico `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera sobre 45 páginas. La capa curatorial contiene ahora **871 artículos históricos estructurados**. Las páginas **133–137** están cerradas en reconciliación de candidatos, censo visible, promoción/enlace y QA computacional IA-asistidos. **Ningún objeto es `human_verified`.**

## Inventario candidato canónico

Las 2,072 filas están fijadas al PDF SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37` y a la revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10`. El JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3` y es reconstruible mediante `scripts/reconstruct_candidate_inventory.py`.

## Estado por páginas cerradas

| Tramo | Candidatos | `article` | `continuation` | Inicios visibles | TP | FP | FN | F1 | Pendientes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| pp.133–134 | 61 | 57 | 4 | 72 | 57 | 4 | 15 | 0.857143 | 0 |
| p.135 | 43 | 35 | 8 | 47 | 35 | 8 | 12 | 0.777778 | 0 |
| p.136 | 48 | 48 | 0 | 49 | 48 | 0 | 1 | 0.989691 | 0 |
| p.137 | 39 | 36 | 3 | 42 | 36 | 3 | 6 | 0.888889 | 0 |

Las cifras de la tabla son diagnósticas de ingeniería editorial en la capa IA-asistida; no son sustituto de colación filológica humana.

## Página 137 — ciclo cerrado

`data/lexicon/reconciliation/p137_reconciliation_status.json` documenta el cierre completo de p.137. Los **39/39 candidatos** fueron reconciliados: 36 son inicios de artículo y 3 son continuaciones OCR sobregeneradas. La calidad geométrica resultante es 33 `exact`, 3 `merged_articles` y 3 `oversegmented`.

El censo visual registra **42 inicios históricos**. El extractor captura 36, produce 3 falsos positivos de frontera y omite 6 inicios, todos representados en `p137_missed_visible_starts.jsonl`. La precisión local es **0.923077**, recall **0.857143** y F1 **0.888889**.

Se promovieron **27 artículos nuevos**, `ALC1737-art-000845`–`000871`, elevando el corpus de 844 a **871 artículos históricos estructurados**. Los 36 candidatos `article` y los 6 falsos negativos enlazan ya objetos históricos; `pending_promotion = 0`.

### Apertura y cierre materiales

La primera línea de p.137, `ca, l, chunti iauetua.`, es la continuación física de `ALC1737-art-000844`, iniciado en p.136 como `Afligirſe, ò apurarſe. Chuntia-`. No se cuenta como nuevo artículo.

El reclamo `buo-` al pie de p.137 se mantiene como catchword y queda fuera del conteo lexicográfico.

### Correcciones facsimilares versionadas

La recollación de alta resolución corrigió dos objetos existentes:

- `ALC1737-art-000729`: `Vaaſuſume` → **`Baaſuſume`**;
- `ALC1737-art-000731`: `Aguacero` → **`Aguazero`**.

Las decisiones quedan trazadas en `data/lexicon/provenance/p137_art000729_correction.json` y `p137_art000731_correction.json`. Son correcciones IA-asistidas contra el facsímil primario, no revisión humana.

### Microestructura deliberadamente no resuelta

`ALC1737-art-000856`, `000867`, `000868` y `000869` conservan estado `unresolved` cuando la puntuación histórica o la relación interna de sus secuencias cahítas no permite una segmentación responsable. No se sustituyó esa incertidumbre por OCR, analogía ni una edición posterior.

## Continuidades y relaciones

La arquitectura sigue separando continuidad material, remisión y anáfora. `sourceSpans` preserva artículos partidos entre columnas o páginas; `Buſca` se modela como remisión documental; `Lo miſmo` permanece como anáfora no resuelta automáticamente.

## QA automático

El workflow **CHD QA run #68** concluyó en `success`. Reconstruyó las 2,072 filas con el hash esperado y verificó **871 objetos en 59 JSONL / 871 `articleId` únicos**. También pasaron los schemas de artículos, los 22 registros de reconciliación izquierda + 17 derecha de p.137, los 6 falsos negativos y los JSON de estado/procedencia.

Una corrida verde sigue siendo QA computacional, no validación filológica humana.

## Fuentes de control textual

`ALC1737` sigue siendo la autoridad primaria. `BUE1890` es una reimpresión histórica de control. `BNF1737-REPORTED` conserva la noticia bibliográfica de un ejemplar independiente de 1737 en la BnF, aún pendiente de verificación directa e ingestión separada.

## Incidencias abiertas

Permanecen activas `ALC1737-gap-0001` entre pp.157–158, el reclamo `Lucer-` de p.161 sin lema visible correspondiente en p.162 y otras lecturas de baja legibilidad que continúan explícitas como `[ileg.]` o `unresolved`.

## Próximo frente

El siguiente ciclo es la **página digital 138**: reconciliar sus candidatos canónicos, censar todos los inicios visibles, enlazar los artículos ya existentes, promover faltantes y cerrar QA antes de avanzar a p.139.
