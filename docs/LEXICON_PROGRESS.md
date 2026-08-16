# Progreso del corpus lexicográfico

## Estado — 2026-08-15

El Vocabulario de `ALC1737` ocupa las páginas digitales 133–177. El extractor `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera sobre 45 páginas, pero los candidatos no se cuentan como artículos históricos publicados.

La secuencia curatorial principal contiene ahora **388 artículos históricos estructurados**: piloto p.134 + avance continuo pp.138–158 dentro del material efectivamente conservado. Todos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

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
| **Total principal** | — | **388** |

Existen además **4 artículos de remisión piloto** en p.165, mantenidos fuera del conteo principal mientras no se consolide el tramo intermedio.

## Regla de autoridad

Una estructura válida no equivale a una lectura filológicamente cerrada. `machine_corrected_unverified`, `unresolved` y `human_verified` son estados diferentes; CHD no promueve automáticamente una lectura IA-asistida a validación humana.

## Remisiones internas `Buſca`

Las remisiones se modelan como relaciones documentales, no como sustitución del artículo remitente por el contenido de su destino. Entre los casos ya estructurados se encuentran `Apercibirſe → aparejarſe`, `Barbo → Bagre`, `Borracho → beodo`, `Compaſſion → compadecerſe`, `Cueva → caverna`, `Dilatar → diferir`, `Embolver → doblar`, `Empacharſe → hartarſe`, `Eſcoger → entreſacar`, `Eſperar → confiar`, `Fee, ò creencia → creer`, `Henchimiento → llenar` y `Holgarſe → gozarſe`.

### Primer ciclo recíproco

Las pp.153–154 revelan el primer ciclo explícito de remisión del corpus:

`Demonio. Buſca diablo.` ↔ `Diablo. Buſca demonio.`

Se preserva en `data/lexicon/relations/reciprocal_cross_references.jsonl`. CHD no infiere cuál de las dos voces debe ser el destino canónico.

## Anáforas `Lo miſmo`

`Lo miſmo` se mantiene separado de `Buſca`. Los casos `Azero`, `Bronce`, `Cobrar lo que ſe debe` y `Cobre metal` permanecen `unresolved` mientras no se resuelva documentalmente su antecedente.

## Agrupaciones, spans y microestructura

`sourceGroupingRaw` conserva agrupaciones históricas; `sourceSpans` representa artículos que cruzan página o columna. Ya están comprobados el artículo botánico pp.141–142 y `Camarón. Cecobi, grande del Rio. Bacauri.` en p.149.

## Catchwords y control de falsas entradas

Los reclamos de pie de página se conservan como paratexto, no como artículos. `data/lexicon/boundary_markers/catchwords_p153_p154.jsonl` registra:

- p.153: `Desbaſ-` → `Desbaſtar madera` en p.154;
- p.154: `Dar` → serie `Dar de comer / Dar de beber / Dar de veſtir` en p.155.

Esta regla debe incorporarse al QA del extractor para reducir falsos positivos.

## Discontinuidad del testimonio entre F y H

La p.157 termina la secuencia visible con `Flecha. Huihua.` y presenta al pie un reclamo `Fle...`. La digital 158, sin embargo, comienza directamente con `Hallarſe bien en vn lugar` y otras voces de H. El HTML guardado reproduce el mismo salto.

CHD registra el punto como `ALC1737-gap-0001` en `data/source/alc1737/gaps.jsonl` y lo documenta en `docs/SOURCE_GAPS.md`. **No se reconstruye la sección faltante ni se afirma todavía cuántas páginas o folios se perdieron.** El tramo ausente parece incluir la continuación de F y al menos G, pero esa formulación permanece como interpretación editorial del salto observable.

## Consecuencia metodológica

La unidad maestra continúa siendo el **artículo histórico**:

`página/columna → spans físicos → agrupación opcional → artículo → formas/remisiones/anáforas/notas → autoridad editorial`.

Catchwords y lagunas del testimonio se mantienen en capas separadas de paratexto/procedencia. La normalización, resolución de anáforas, equivalencias modernas y proyección TEI Lex-0 pertenecen a capas posteriores.

## Siguiente lote

Continuar desde **digital 159**, sin ocultar la discontinuidad 157→158 y manteniendo el doble registro GitHub ↔ Notion.