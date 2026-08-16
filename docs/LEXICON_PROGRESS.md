# Progreso del corpus lexicográfico

## Estado — 2026-08-16

El Vocabulario de `ALC1737` ocupa las páginas digitales **133–177**. El extractor `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera sobre 45 páginas; esos candidatos no equivalen automáticamente a artículos históricos publicados.

La secuencia curatorial contiene ahora **734 artículos históricos estructurados**. Las **45/45 páginas del vocabulario cuentan ya con representación lexicográfica estructurada**: p.134 conserva un piloto de 12 artículos, las demás páginas disponen de lotes selectivos, y se han modelado además artículos que cruzan páginas/columnas. Todos los objetos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

Este hito cierra la **cobertura selectiva inicial por página**, no la extracción exhaustiva del vocabulario. La siguiente fase consiste en reconciliar los 2,072 candidatos con artículos históricos, paratexto, continuidades y falsos positivos.

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

Se representa mediante `sourceSpans`; el fragmento inferior `como` no se transforma en entrada independiente.

Entre las voces de apertura estructuradas aparecen `Abajar`, diversas `Abeja`, `Abertura`, `Abiſmo`, `Acaudalarſe`, `Azedo/agrio`, `Azechar`, `Acepillar`, `Azequia`, `Acompañar`, `Adarga`, `Adelante`, `Aderezar`, `Adornar → aderezar`, `Aflojar`, `Agarrar`, `Agua`, `Aguacero`, `Agujero` y `Aguila`.

## Identificadores y procedencia

La reconciliación de p.165 eliminó la colisión del antiguo piloto `000013`–`000016`; las cuatro remisiones fueron migradas a `000490`–`000493` y la operación quedó documentada en `data/lexicon/provenance/p165_pilot_id_reconciliation.json`.

Los nuevos objetos de apertura ocupan `ALC1737-art-000674`–`000734`. `scripts/validate_lexicon_ids.py` permanece como control de unicidad de `articleId`, parseo JSONL y coherencia entre `reviewStatus` y `humanVerified`. Su incorporación al repositorio **no equivale todavía a una ejecución CI verificada**.

## Remisiones y anáforas

Las remisiones `Buſca` se modelan como relaciones documentales. El retroprocesamiento añade, entre otras, `Adornar → aderezar`; los lotes posteriores conservan el grafo amplio ya identificado (`Piel → pelo`, `Platicar → parlar`, `Premiar → pagar`, `Reñir → regañar`, `Tocar → palpar`, `Viejo → anciano`, etc.).

`Lo miſmo` sigue tratado como anáfora distinta de `Buſca` y permanece sin resolución automática.

## Catchwords, continuidades y lagunas

Los reclamos tipográficos y las continuidades físicas se mantienen fuera del conteo de entradas. Están ya modeladas continuidades normales desde la apertura hasta el final del vocabulario, junto con dos problemas que siguen activos:

- `ALC1737-gap-0001`: discontinuidad F→H entre digitales 157–158;
- p.161 `Lucer-` → p.162 sin lema visible correspondiente, `unresolved`.

La frontera 133→134 aporta un nuevo caso explícito de artículo trans-página y refuerza la necesidad de no identificar automáticamente cada línea o reclamo con un artículo.

## Final material del vocabulario

La p.177 concluye la serie alfabética visible. La p.178 termina X/Z y abre `NOMBRES NUMERALES`; las pp.178–180 se modelan como **capa gramatical de numerales**, no como prolongación indiferenciada del corpus lexicográfico.

## Próximo frente

1. Reconciliar sistemáticamente los **2,072 candidatos** con `article`, `paratext`, `continuation` o `false_positive`.
2. Crear métricas reproducibles de precisión/recobrado del extractor a partir de una muestra estratificada.
3. Resolver anáforas `Lo miſmo` y el grafo completo de `Buſca` mediante operaciones editoriales explícitas.
4. Generar una exportación canónica de producción sin duplicar los lotes fuente.
5. Proyectar TEI Lex-0 sólo después de estabilizar esas reconciliaciones.
