# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El extractor `hybrid_margin_mode_v0.2` produce **2,072 candidatos** de frontera sobre 45 páginas; esos candidatos no equivalen automáticamente a artículos históricos publicados.

La secuencia curatorial contiene **734 artículos históricos estructurados**. Las **45/45 páginas del vocabulario cuentan ya con representación lexicográfica estructurada**: p.134 conserva un piloto de 12 artículos, las demás páginas disponen de lotes selectivos, y se han modelado además artículos que cruzan páginas/columnas. Todos los objetos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

Este hito cierra la **cobertura selectiva inicial por página**. La precondición técnica para la fase siguiente también está satisfecha: los **2,072 candidatos v0.2 están persistidos canónicamente en una representación fila-a-fila reconstruible y verificable**.

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

Se añadieron:

- `p133_selected_articles.jsonl` — 15;
- `p133_p134_cross_page_article.jsonl` — 1;
- `p135_selected_articles.jsonl` — 15;
- `p136_selected_articles.jsonl` — 15;
- `p137_selected_articles.jsonl` — 15.

La frontera 133→134 confirmó un artículo materialmente partido entre páginas:

`Ablandar lo que eſtá duro / como barro. Namacae-buaruna.`

Se representa mediante `sourceSpans`; el fragmento de continuidad no se transforma en entrada independiente.

## Inventario candidato canónico v0.2

La cifra **2,072** ya no es sólo una métrica de ejecución. El inventario completo fue generado con la revisión fijada `f175b4bc455ff40a066d092a94e0a89a0ca2ae10`, usando:

- `scripts/extract_vocab_candidates.py`, blob `0ac729164895b0b4afd462350892426aca6e5f3d`;
- `scripts/extract_vocab_layout.py`, blob `e0bee9ddaad0c114405f13d456cc2a00317d7107`;
- PDF fuente SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`.

El JSONL resultante contiene exactamente **2,072 filas** y tiene SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

Para persistirlo mediante archivos UTF-8 se usa una representación **lossless**: JSONL → gzip determinista → base64 → 12 partes ordenadas. `data/lexicon/candidates/candidate_inventory_manifest.json` registra hashes y tamaños de cada parte, además de los hashes agregados. `scripts/reconstruct_candidate_inventory.py` verifica partes, base64, gzip, JSONL, parseo de cada fila y conteo total antes de reconstruir opcionalmente el archivo JSONL.

`data/lexicon/candidates/inventory_status.json` marca ahora `canonical_inventory_persisted_lossless_sharded`, `reconciliationPrecondition: satisfied` y `exhaustiveReconciliationAllowed: true`.

El archivo histórico `p134_candidates.jsonl` corresponde a `indentation_margin_v0.1`; permanece como artefacto de procedencia/comparación y **no** forma parte del inventario canónico v0.2.

## Protocolo de reconciliación

Existen:

- `schemas/lexicon-candidate-review.schema.json`;
- `docs/LEXICON_RECONCILIATION_PROTOCOL.md`.

Cada candidato canónico deberá clasificarse como `article`, `paratext`, `continuation`, `false_positive` o `unresolved`, con una evaluación de frontera independiente (`exact`, `oversegmented`, `undersegmented`, `merged_articles`, `ambiguous`, `not_applicable`).

No se presupone correspondencia 1:1 entre candidato y artículo histórico: el OCR puede fragmentar o fusionar entradas y las unidades pueden cruzar columnas/páginas.

## QA diagnóstico disponible

`data/lexicon/review/stratified_boundary_evaluation.json` evalúa intencionalmente pp.133, 134, 150 y 177. Registra:

- candidatos: 171;
- inicios de artículo visibles: 188;
- verdaderos positivos: 163;
- falsos positivos: 8;
- falsos negativos: 25;
- precisión: **0.9532**;
- recobrado: **0.8670**;
- F1: **0.9081**.

El propio archivo declara el diseño `purposive_stratified_diagnostic`. Estas cifras son útiles para diagnóstico del algoritmo, pero **no constituyen estimadores probabilísticos del vocabulario completo**.

## Identificadores y procedencia

La reconciliación de p.165 eliminó la colisión del antiguo piloto `000013`–`000016`; las cuatro remisiones fueron migradas a `000490`–`000493` y la operación quedó documentada en `data/lexicon/provenance/p165_pilot_id_reconciliation.json`.

Los objetos de apertura ocupan `ALC1737-art-000674`–`000734`. `scripts/validate_lexicon_ids.py` permanece como control de unicidad de `articleId`, parseo JSONL y coherencia entre `reviewStatus` y `humanVerified`. Su incorporación al repositorio **no equivale todavía a una ejecución CI verificada**.

## Remisiones y anáforas

Las remisiones `Buſca` se modelan como relaciones documentales. `Lo miſmo` sigue tratado como anáfora distinta y permanece sin resolución automática. La reconciliación candidata deberá enlazar estas estructuras con artículos curados sin sustituir el texto histórico por destinos normalizados.

## Catchwords, continuidades y lagunas

Los reclamos tipográficos y las continuidades físicas se mantienen fuera del conteo de entradas. Siguen activos:

- `ALC1737-gap-0001`: discontinuidad F→H entre digitales 157–158;
- p.161 `Lucer-` → p.162 sin lema visible correspondiente, `unresolved`.

## Final material del vocabulario

La p.177 concluye la serie alfabética visible. La p.178 termina X/Z y abre `NOMBRES NUMERALES`; las pp.178–180 se modelan como **capa gramatical de numerales**.

## Próximo frente

1. Reconciliar exhaustivamente los **2,072 candidatos canónicos**, comenzando por pp.133–134.
2. Clasificar cada registro contra `article`, `paratext`, `continuation`, `false_positive` o `unresolved` y documentar calidad de frontera.
3. Ampliar la evaluación estratificada y publicar métricas por estrato/página.
4. Resolver anáforas `Lo miſmo` y el grafo de `Buſca` mediante operaciones editoriales explícitas.
5. Generar exportación canónica de producción y posteriormente TEI Lex-0.
