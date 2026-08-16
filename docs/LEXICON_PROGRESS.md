# Progreso del corpus lexicográfico

## Estado — 2026-08-15

El Vocabulario de `ALC1737` ocupa las páginas digitales 133–177. El extractor `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera sobre 45 páginas, pero los candidatos no se cuentan como artículos históricos publicados.

La secuencia curatorial principal contiene ahora **538 artículos históricos estructurados**: piloto p.134 + avance continuo pp.138–168 dentro del material efectivamente conservado. Todos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

## Lotes estructurados

| Lote | Página | Artículos |
|---|---:|---:|
| `p134_pilot_articles.jsonl` | 134 | 12 |
| `p138_selected_articles.jsonl` | 138 | 33 |
| `p139_selected_articles.jsonl` | 139 | 39 |
| `p140_selected_articles.jsonl` | 140 | 36 |
| `p141_selected_articles.jsonl` | 141 | 10 |
| `p142_botanical_pilot.jsonl` | 142 | 10 |
| `p141_p142_cross_page_article.jsonl` | 141–142 | 1 |
| `p143_selected_articles.jsonl` | 143 | 14 |
| `p144_selected_articles.jsonl` | 144 | 14 |
| `p145_selected_articles.jsonl` | 145 | 14 |
| `p146_selected_articles.jsonl` | 146 | 25 |
| `p147_selected_articles.jsonl` | 147 | 15 |
| `p148_selected_articles.jsonl` | 148 | 15 |
| `p149_selected_articles.jsonl` | 149 | 15 |
| `p150_selected_articles.jsonl` | 150 | 15 |
| `p151_selected_articles.jsonl` | 151 | 15 |
| `p152_selected_articles.jsonl` | 152 | 15 |
| `p153_selected_articles.jsonl` | 153 | 15 |
| `p154_selected_articles.jsonl` | 154 | 15 |
| `p155_selected_articles.jsonl` | 155 | 15 |
| `p156_selected_articles.jsonl` | 156 | 15 |
| `p157_selected_articles.jsonl` | 157 | 15 |
| `p158_selected_articles.jsonl` | 158 | 15 |
| `p159_selected_articles.jsonl` | 159 | 15 |
| `p160_selected_articles.jsonl` | 160 | 15 |
| `p161_selected_articles.jsonl` | 161 | 15 |
| `p162_selected_articles.jsonl` | 162 | 15 |
| `p163_selected_articles.jsonl` | 163 | 15 |
| `p164_selected_articles.jsonl` | 164 | 15 |
| `p165_selected_articles.jsonl` | 165 | 15 |
| `p166_selected_articles.jsonl` | 166 | 15 |
| `p167_selected_articles.jsonl` | 167 | 15 |
| `p168_selected_articles.jsonl` | 168 | 15 |
| **Total principal** | — | **538** |

## Reconciliación del piloto de p.165

La p.165 ya no mantiene un lote piloto separado. Durante la reconciliación se detectó que `p165_cross_reference_pilot.jsonl` reutilizaba los identificadores `ALC1737-art-000013`–`000016`, ya ocupados por la secuencia principal iniciada en p.138. El problema era de **identidad de objeto**, no de lectura histórica.

Los cuatro artículos piloto (`Orejear`, `Orina`, `Orinar`, `Oſado ſer`) fueron preservados, reasignados a `ALC1737-art-000490`–`000493` e integrados en `p165_selected_articles.jsonl`. El archivo piloto obsoleto fue eliminado. La trazabilidad del cambio se conserva en:

`data/lexicon/provenance/p165_pilot_id_reconciliation.json`

Para reducir el riesgo de regresión se añadió `scripts/validate_lexicon_ids.py`, que comprueba JSONL, unicidad global de `articleId` y coherencia entre `reviewStatus` y `humanVerified`.

## Regla de autoridad

Una estructura válida no equivale a una lectura filológicamente cerrada. `machine_corrected_unverified`, `unresolved` y `human_verified` son estados diferentes; CHD no promueve automáticamente una lectura IA-asistida a validación humana.

## Remisiones internas `Buſca`

Las remisiones se modelan como relaciones documentales, no como sustitución del artículo remitente por el contenido de su destino. La p.165 consolida `Ofender → pecar`, `Ofenſa → pecado`, `Ofenſor → pecador`, `Orejear → menear las orejas`, `Orina → meados`, `Orinar → mear` y `Oſado ſer → atrevido`. La p.166 añade `Palo para eſcarbar tierra → coa`; la p.167 incorpora la serie recíproca `Pecado → ofenſa`, `Pecador → ofenſor` y `Pecar → ofender`.

Esto amplía el grafo documental de remisiones y muestra que algunas relaciones forman pares o ciclos semánticos explícitos dentro del propio vocabulario.

## Anáforas `Lo miſmo`

`Lo miſmo` se mantiene separado de `Buſca`. Los casos ya detectados permanecen `unresolved` hasta que su antecedente pueda identificarse mediante una operación editorial explícita; no se copia automáticamente la forma de la entrada precedente.

## Agrupaciones, spans y microestructura

`sourceGroupingRaw` conserva agrupaciones históricas; `sourceSpans` representa artículos que cruzan página o columna. Ya están comprobados el artículo botánico pp.141–142 y `Camarón. Cecobi, grande del Rio. Bacauri.` en p.149.

## Catchwords y control de fronteras

Los reclamos de pie de página se conservan como paratexto, no como artículos. La capa `data/lexicon/boundary_markers/` documenta ahora, entre otros:

- p.161 `Lucer-` → anomalía de frontera: p.162 comienza con `Tohuopo, l, aioa.` sin lema visible;
- p.164 `Obr-` → `Obra aſſi, hechura. Chupari.` en p.165, continuidad ya resuelta;
- p.165 `Paga-` → `Paga tal. Bebeti.` en p.166;
- p.166 `Paſſo` → `Paſſo de las beſtias. Arabuerama.` en p.167;
- p.167 `Pena-` → `Penacho` en p.168;
- p.168 `Pie-` → pendiente de cotejo en p.169.

El caso p.161→162 **no se reconstruye por conjetura**. El reclamo `Pie-` permanece igualmente `unresolved` hasta procesar la página siguiente.

## Discontinuidad del testimonio entre F y H

La p.157 termina la secuencia visible con `Flecha. Huihua.` y presenta al pie un reclamo `Fle...`. La digital 158 comienza directamente con voces de H. El HTML guardado reproduce el mismo salto.

CHD registra el punto como `ALC1737-gap-0001` en `data/source/alc1737/gaps.jsonl` y lo documenta en `docs/SOURCE_GAPS.md`. **No se reconstruye la sección faltante ni se afirma todavía cuántas páginas o folios se perdieron.**

## Consecuencia metodológica

La unidad maestra continúa siendo el **artículo histórico**:

`página/columna → spans físicos → agrupación opcional → artículo → formas/remisiones/anáforas/notas → autoridad editorial`.

A esta arquitectura se añade ahora una capa explícita de QA de **identificadores persistentes**, además de catchwords, anomalías de frontera y lagunas documentales. La normalización, resolución de anáforas, equivalencias modernas y proyección TEI Lex-0 pertenecen a capas posteriores.

## Siguiente lote

Continuar desde **digital 169**, resolver el reclamo `Pie-` de p.168 y mantener la sincronización GitHub ↔ Notion por cada lote sustantivo.
