# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El extractor `hybrid_margin_mode_v0.2` produce **2,072 candidatos** de frontera sobre 45 páginas; esos candidatos no equivalen automáticamente a artículos históricos publicados.

La secuencia curatorial contiene **734 artículos históricos estructurados**. Las **45/45 páginas del vocabulario cuentan ya con representación lexicográfica estructurada**. Todos los objetos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

El inventario canónico de 2,072 candidatos está persistido de forma fila-a-fila reconstruible y verificable. El primer tramo de reconciliación candidata, **pp.133–134, quedó cerrado en 61/61 candidatos**.

## Cobertura curatorial vigente

| Tramo | Artículos |
|---|---:|
| p.133 | 15 |
| p.134 piloto | 12 |
| artículo trans-página 133–134 | 1 |
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
| **Total principal** | **734** |

## Retroprocesamiento de apertura — pp.133 y 135–137

La frontera 133→134 confirmó un artículo materialmente partido entre páginas:

`Ablandar lo que eſtá duro / como barro. Namacae-buaruna.`

Se representa mediante `sourceSpans`; el fragmento de continuidad no se transforma en entrada independiente.

## Inventario candidato canónico v0.2

La cifra **2,072** ya no es sólo una métrica de ejecución. El inventario completo fue generado con la revisión fijada `f175b4bc455ff40a066d092a94e0a89a0ca2ae10`, usando:

- `scripts/extract_vocab_candidates.py`, blob `0ac729164895b0b4afd462350892426aca6e5f3d`;
- `scripts/extract_vocab_layout.py`, blob `e0bee9ddaad0c114405f13d456cc2a00317d7107`;
- PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`.

El JSONL resultante contiene exactamente **2,072 filas** y tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

Para persistirlo mediante archivos UTF-8 se usa una representación **lossless**: JSONL → gzip determinista → base64 → 12 partes ordenadas. `data/lexicon/candidates/candidate_inventory_manifest.json` registra hashes y tamaños de cada parte, además de los hashes agregados. `scripts/reconstruct_candidate_inventory.py` verifica partes, base64, gzip, JSONL, parseo de cada fila y conteo total.

`data/lexicon/candidates/inventory_status.json` marca `canonical_inventory_persisted_lossless_sharded`, `reconciliationPrecondition: satisfied` y `exhaustiveReconciliationAllowed: true`.

El archivo histórico `p134_candidates.jsonl` corresponde a `indentation_margin_v0.1`; permanece como artefacto de procedencia/comparación y **no** forma parte del inventario canónico v0.2.

## Reconciliación candidata — pp.133–134

El cierre del tramo se registra en `data/lexicon/reconciliation/p133_p134_reconciliation_status.json`.

Los **61/61 candidatos** tienen ya decisión editorial:

- 57 `article`;
- 3 `continuation`;
- 1 `unresolved` (`ALC1737-vcand-p133-L-002`).

La calidad geométrica resultó:

- 52 `exact`;
- 5 `merged_articles`;
- 2 `oversegmented`;
- 1 `undersegmented`;
- 1 `ambiguous`.

De los 57 candidatos `article`, 21 ya pueden enlazarse a objetos históricos existentes —28 artículos únicos por la presencia de candidatos fusionados— y **36** quedan con `articleLinkStatus: pending_promotion`. Esta categoría significa que la frontera está materialmente resuelta, pero el artículo todavía no se ha promovido con transcripción/estructura suficiente. No se usa `unresolved` para esconder un simple estado pendiente del pipeline.

`schemas/lexicon-candidate-review.schema.json` y `docs/LEXICON_RECONCILIATION_PROTOCOL.md` fueron ampliados para separar estas dos dimensiones.

## Falsos negativos visibles

Completar todos los candidatos de una página no equivale a capturar todos sus artículos visibles. Se añadió `schemas/lexicon-missed-start.schema.json` y el dataset `data/lexicon/reconciliation/missed_visible_starts_p133_p134.jsonl`.

El conjunto registra por ahora **14 inicios visibles omitidos** por el extractor en pp.133–134. Incluye casos absorbidos dentro de candidatos fusionados —por ejemplo `Abajar la cabeza`, `Abiſmo agua profunda`, `Abiſpa, que haze ſu caſa de lodo`, `Abivar à otro` y el comienzo trans-página `Ablandar lo que eſtá duro como barro`— y comienzos sin candidato propio como `Abotonarſe la flor`, `Abrigarſe para defenderſe del viento`, `Abuela paterna` y `Abuela tercera`.

Este conjunto se marca expresamente como **observado, no todavía exhaustivo**. La completitud de candidatos (61/61) y la completitud de inicios visibles son métricas diferentes.

## QA diagnóstico disponible

`data/lexicon/review/stratified_boundary_evaluation.json` evalúa intencionalmente pp.133, 134, 150 y 177. Registra 171 candidatos, 188 inicios visibles, 163 verdaderos positivos, 8 falsos positivos y 25 falsos negativos: precisión **0.9532**, recobrado **0.8670** y F1 **0.9081**.

El propio archivo declara el diseño `purposive_stratified_diagnostic`. Estas cifras son útiles para diagnóstico del algoritmo, pero **no constituyen estimadores probabilísticos del vocabulario completo**.

## Identificadores y procedencia

La reconciliación de p.165 eliminó la colisión del antiguo piloto `000013`–`000016`; las cuatro remisiones fueron migradas a `000490`–`000493` y la operación quedó documentada en `data/lexicon/provenance/p165_pilot_id_reconciliation.json`.

Los objetos de apertura ocupan `ALC1737-art-000674`–`000734`. `scripts/validate_lexicon_ids.py` permanece como control de unicidad de `articleId`, parseo JSONL y coherencia entre `reviewStatus` y `humanVerified`.

## Remisiones y anáforas

Las remisiones `Buſca` se modelan como relaciones documentales. `Lo miſmo` sigue tratado como anáfora distinta y permanece sin resolución automática.

## Catchwords, continuidades y lagunas

Los reclamos tipográficos y las continuidades físicas se mantienen fuera del conteo de entradas. Siguen activos:

- `ALC1737-gap-0001`: discontinuidad F→H entre digitales 157–158;
- p.161 `Lucer-` → p.162 sin lema visible correspondiente, `unresolved`.

## Final material del vocabulario

La p.177 concluye la serie alfabética visible. La p.178 termina X/Z y abre `NOMBRES NUMERALES`; las pp.178–180 se modelan como **capa gramatical de numerales**.

## Próximo frente

1. Promover los **36 artículos pendientes** de pp.133–134 mediante lectura facsimilar y microestructura histórica.
2. Cerrar el inventario de inicios visibles/falsos negativos del tramo y producir métricas de página.
3. Mantener `ALC1737-vcand-p133-L-002` `unresolved` salvo que un cotejo específico permita resolverlo.
4. Escalar la reconciliación candidata al siguiente lote de páginas sólo después de cerrar ese QA de apertura.
5. Continuar después con anáforas `Lo miſmo`, grafo `Buſca`, exportación canónica y TEI Lex-0.
