# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El extractor `hybrid_margin_mode_v0.2` produce **2,072 candidatos** de frontera sobre 45 páginas; esos candidatos no equivalen automáticamente a artículos históricos.

La secuencia curatorial contiene ahora **770 artículos históricos estructurados**. Las **45/45 páginas del vocabulario cuentan ya con representación lexicográfica estructurada**. Todos los objetos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

El inventario canónico de 2,072 candidatos está persistido de forma fila-a-fila reconstruible y verificable. El tramo de control **pp.133–134** quedó cerrado en dos sentidos distintos:

- **61/61 candidatos** tienen reconciliación editorial;
- los **57 candidatos clasificados `article` enlazan ya objetos históricos**, por lo que `pending_promotion = 0`.

Esto todavía **no** equivale a cerrar todos los inicios visibles de ambas páginas, porque existe una capa separada de falsos negativos.

## Cobertura curatorial vigente

| Tramo | Artículos |
|---|---:|
| p.133 selección inicial | 15 |
| p.134 piloto histórico | 12 |
| artículo trans-página 133–134 | 1 |
| promociones de candidatos p.133 | 11 |
| promociones de candidatos p.134 | 25 |
| pp.135–137 | 45 |
| p.138 | 33 |
| p.139 | 39 |
| p.140 | 36 |
| p.141 | 10 |
| p.142 | 10 |
| artículo trans-página 141–142 | 1 |
| pp.143–145 | 42 |
| p.146 | 25 |
| pp.147–177 | 465 |
| **Total principal** | **770** |

## Apertura y materialidad — pp.133–134

La frontera 133→134 confirmó un artículo materialmente partido entre páginas:

`Ablandar lo que eſtá duro como barro. Namacae-buaruna.`

Se representa mediante `sourceSpans`; el salto físico no genera dos entradas.

El cierre de promociones añadió además un caso intra-página de continuidad entre columnas en p.133:

`Abeja monteza de color blanco. Pochocu--mumu--toſali.`

El comienzo queda al pie de la columna izquierda y el segmento final `ſali` aparece al inicio de la columna derecha. El artículo se conserva como una unidad histórica con `sourceSpans` izquierda→derecha.

## Inventario candidato canónico v0.2

La cifra **2,072** corresponde a un inventario canónico reproducible, no sólo a una métrica de ejecución. Fue generado con la revisión fijada `f175b4bc455ff40a066d092a94e0a89a0ca2ae10`, usando:

- `scripts/extract_vocab_candidates.py`, blob `0ac729164895b0b4afd462350892426aca6e5f3d`;
- `scripts/extract_vocab_layout.py`, blob `e0bee9ddaad0c114405f13d456cc2a00317d7107`;
- PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`.

El JSONL canónico tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

Para persistirlo mediante archivos UTF-8 se usa una representación **lossless**: JSONL → gzip determinista → base64 → 12 partes ordenadas. `data/lexicon/candidates/candidate_inventory_manifest.json` registra hashes y tamaños; `scripts/reconstruct_candidate_inventory.py` verifica partes, base64, gzip, JSONL, parseo y conteo.

`data/lexicon/candidates/inventory_status.json` marca `canonical_inventory_persisted_lossless_sharded`, `reconciliationPrecondition: satisfied` y `exhaustiveReconciliationAllowed: true`.

El archivo histórico `p134_candidates.jsonl` corresponde a `indentation_margin_v0.1`; permanece como artefacto de procedencia/comparación y **no** forma parte del inventario canónico v0.2.

## Reconciliación candidata — pp.133–134

El cierre del tramo se registra en `data/lexicon/reconciliation/p133_p134_reconciliation_status.json`.

Los **61/61 candidatos** tienen decisión editorial:

- 57 `article`;
- 3 `continuation`;
- 1 `unresolved` (`ALC1737-vcand-p133-L-002`).

La calidad geométrica es:

- 52 `exact`;
- 5 `merged_articles`;
- 2 `oversegmented`;
- 1 `undersegmented`;
- 1 `ambiguous`.

### Cierre de promoción

Antes de este ciclo, 36 fronteras `article` estaban `pending_promotion`. Se promovieron de forma facsimilar y se enlazaron:

- `p133_pending_promotions_batch01.jsonl`: **11** artículos, `ALC1737-art-000735`–`000745`;
- `p134_pending_promotions_batch01.jsonl`: **25** artículos, `ALC1737-art-000746`–`000770`.

El estado actual es:

- candidatos `article` enlazados: **57 / 57**;
- artículos históricos únicos enlazados desde esos candidatos: **64**;
- candidatos `article` `pending_promotion`: **0**.

El cierre de promoción no convierte lecturas IA-asistidas en revisión humana y tampoco resuelve los falsos negativos del extractor.

## Falsos negativos visibles

Completar todos los candidatos de una página no equivale a capturar todos sus artículos visibles. `schemas/lexicon-missed-start.schema.json` y `data/lexicon/reconciliation/missed_visible_starts_p133_p134.jsonl` mantienen una capa específica para inicios omitidos.

El conjunto registra por ahora **14 inicios visibles omitidos observados** en pp.133–134. Incluye artículos absorbidos dentro de candidatos fusionados y comienzos sin candidato propio.

Este conjunto se marca expresamente como **observado, no todavía exhaustivo**. El siguiente trabajo debe reconciliar cada uno de esos 14 inicios contra objetos históricos existentes o crear, cuando corresponda, nuevos artículos; después debe hacerse una pasada página-a-página para poder declarar cerrado el inventario visible.

## QA diagnóstico

La comparación canónica en `data/lexicon/review/boundary_algorithm_comparison.json` utiliza una muestra intencional de pp.133, 134, 150 y 177:

| Método | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| `indentation_margin_v0.1` | 163 | 8 | 25 | 95.32% | 86.70% | 90.81% |
| `hybrid_margin_mode_v0.2` | 169 | 5 | 19 | **97.13%** | **89.89%** | **93.37%** |

La muestra es `purposive_stratified_diagnostic`, no probabilística, y su referencia visual es IA-asistida. Las métricas describen comportamiento de ingeniería editorial; no constituyen estimadores filológicos poblacionales.

## QA automatizado

`.github/workflows/qa.yml` valida automáticamente, entre otros controles:

- reconstrucción íntegra de las 2,072 filas canónicas;
- unicidad de `articleId` y coherencia de autoridad;
- artículos históricos contra `schemas/lexical-article.schema.json`;
- lotes de reconciliación contra `schemas/lexicon-candidate-review.schema.json`;
- capa de inicios omitidos contra su schema;
- JSON de control seleccionados.

El alcance y límites se documentan en `docs/QA_AUTOMATION.md`. Una corrida verde es **QA computacional**, no validación filológica humana.

## Identificadores y procedencia

La reconciliación de p.165 eliminó la colisión del antiguo piloto `000013`–`000016`; las cuatro remisiones fueron migradas a `000490`–`000493` y la operación quedó documentada en `data/lexicon/provenance/p165_pilot_id_reconciliation.json`.

La secuencia curatorial alcanza ahora `ALC1737-art-000770`. `scripts/validate_lexicon_ids.py` controla unicidad global, parseo JSONL y coherencia entre `reviewStatus` y `humanVerified`.

## Remisiones y anáforas

Las remisiones `Buſca` se modelan como relaciones documentales. `Lo miſmo` permanece como anáfora distinta y no se resuelve automáticamente.

## Catchwords, continuidades y lagunas

Los reclamos tipográficos y las continuidades físicas se mantienen fuera del conteo de entradas. Siguen activos:

- `ALC1737-gap-0001`: discontinuidad F→H entre digitales 157–158;
- p.161 `Lucer-` → p.162 sin lema visible correspondiente, `unresolved`.

## Final material del vocabulario

La p.177 concluye la serie alfabética visible. La p.178 termina X/Z y abre `NOMBRES NUMERALES`; las pp.178–180 se modelan como **capa gramatical de numerales**.

## Próximo frente

1. Reconciliar los **14 inicios visibles omitidos observados** de pp.133–134 contra la capa histórica.
2. Cerrar el inventario página-a-página de inicios visibles y producir métricas finales del tramo de control.
3. Mantener `ALC1737-vcand-p133-L-002` `unresolved` salvo que un cotejo específico permita resolverlo.
4. Escalar la reconciliación candidata a p.135 en adelante sólo después de cerrar el QA de apertura.
5. Continuar después con anáforas `Lo miſmo`, grafo `Buſca`, menciones históricas de variedades, exportación canónica y TEI Lex-0.
