# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El extractor `hybrid_margin_mode_v0.2` tiene documentado un resultado de **2,072 candidatos** de frontera sobre 45 páginas; esos candidatos no equivalen automáticamente a artículos históricos publicados.

La secuencia curatorial contiene ahora **734 artículos históricos estructurados**. Las **45/45 páginas del vocabulario cuentan ya con representación lexicográfica estructurada**: p.134 conserva un piloto de 12 artículos, las demás páginas disponen de lotes selectivos, y se han modelado además artículos que cruzan páginas/columnas. Todos los objetos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

Este hito cierra la **cobertura selectiva inicial por página**, no la extracción exhaustiva del vocabulario.

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

## Auditoría del inventario candidato

La cifra **2,072** debe leerse con precisión: es una **métrica documentada de ejecución del extractor**, no la prueba de que 2,072 registros candidatos estén actualmente persistidos fila-a-fila en GitHub.

La auditoría del árbol de `data/lexicon/candidates/` muestra por ahora un único artefacto candidato explícito: `p134_candidates.jsonl`. El estado se conserva en `data/lexicon/candidates/inventory_status.json`, que marca `canonicalInventoryStatus: incomplete_in_repository` y bloquea cualquier afirmación de reconciliación exhaustiva.

La precondición siguiente es regenerar reproduciblemente las pp.133–177 con `scripts/extract_vocab_candidates.py`, verificar el total esperado o documentar la divergencia y persistir el inventario canónico con versión del extractor y procedencia del PDF.

## Protocolo de reconciliación

Ya existen:

- `schemas/lexicon-candidate-review.schema.json`;
- `docs/LEXICON_RECONCILIATION_PROTOCOL.md`.

Cada candidato persistido deberá clasificarse como `article`, `paratext`, `continuation`, `false_positive` o `unresolved`, con una evaluación de frontera independiente (`exact`, `oversegmented`, `undersegmented`, `merged_articles`, `ambiguous`, `not_applicable`).

No se presupone correspondencia 1:1 entre candidato y artículo histórico: el OCR puede fragmentar o fusionar entradas y las unidades pueden cruzar columnas/páginas.

## QA diagnóstico disponible

`data/lexicon/review/stratified_boundary_evaluation.json` ya evalúa intencionalmente pp.133, 134, 150 y 177. Registra:

- candidatos: 171;
- inicios de artículo visibles: 188;
- verdaderos positivos: 163;
- falsos positivos: 8;
- falsos negativos: 25;
- precisión: **0.9532**;
- recobrado: **0.8670**;
- F1: **0.9081**.

El propio archivo declara el diseño `purposive_stratified_diagnostic`. Por tanto estas cifras son útiles para localizar comportamiento algorítmico, pero **no constituyen estimadores probabilísticos del vocabulario completo**.

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

1. Persistir el inventario canónico reproducible de candidatos para las 45 páginas.
2. Reconciliar cada registro contra `article`, `paratext`, `continuation`, `false_positive` o `unresolved`.
3. Ampliar la evaluación estratificada y publicar métricas por estrato/página.
4. Resolver anáforas `Lo miſmo` y el grafo de `Buſca` mediante operaciones editoriales explícitas.
5. Generar exportación canónica de producción y posteriormente TEI Lex-0.
