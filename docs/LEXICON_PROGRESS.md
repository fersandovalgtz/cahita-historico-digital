# Progreso del corpus lexicográfico

## Estado — 2026-08-15

El Vocabulario de `ALC1737` ocupa las páginas digitales 133–177. El extractor `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera sobre 45 páginas, pero los candidatos no se cuentan como artículos históricos publicados.

La secuencia curatorial principal contiene ahora **343 artículos históricos estructurados**: piloto p.134 + avance continuo pp.138–155. Todos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

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
| **Total principal** | — | **343** |

Existen además **4 artículos de remisión piloto** en p.165, mantenidos fuera del conteo principal mientras no se consolide el tramo intermedio.

## Regla de autoridad

Una estructura válida no equivale a una lectura filológicamente cerrada. `machine_corrected_unverified`, `unresolved` y `human_verified` son estados diferentes; CHD no promueve automáticamente una lectura IA-asistida a validación humana.

## Remisiones internas `Buſca`

Las remisiones se modelan como relaciones documentales, no como sustitución del artículo remitente por el contenido de su destino. Entre los casos ya estructurados se encuentran:

- `Apercibirſe para hazer algo → aparejarſe`;
- `Barbo → Bagre`;
- `Barrenar → agurear con barrena`;
- `Baſta, coſa ſin pulir → aſpero`;
- `Borracho → beodo`;
- `Caro venderſe → cara coſa`;
- `Carrizo → caña hueca`;
- `Compaſſion → compadecerſe`;
- `Comulgar → comunion`;
- `Cueva → caverna`;
- `Culpar à otro → acuſar`;
- `Dilatar → diferir`;
- `Embolver → doblar`;
- `Empacharſe → hartarſe`.

### Primer ciclo recíproco

Las pp.153–154 revelan el primer ciclo explícito de remisión del corpus:

`Demonio. Buſca diablo.` ↔ `Diablo. Buſca demonio.`

Se preserva como una propiedad documental en `data/lexicon/relations/reciprocal_cross_references.jsonl`. CHD no infiere cuál de las dos voces debe ser el destino canónico.

## Anáforas `Lo miſmo`

`Lo miſmo` se mantiene separado de `Buſca`. Los casos `Azero`, `Bronce`, `Cobrar lo que ſe debe` y `Cobre metal` permanecen `unresolved` mientras no se resuelva documentalmente su antecedente. No se copia de forma automática la equivalencia anterior.

## Agrupaciones históricas y artículos descriptivos

`sourceGroupingRaw` conserva encabezados como `Arboles, cuyo fruto es comeſtible`, `Arboles que ſirven para madera`, `Arboles chaparros` y `Arboles de mariſmas`. Las afirmaciones históricas de usos medicinales o materiales se documentan como contenido de 1737 y no se convierten en recomendaciones modernas.

## Continuidades físicas

`sourceSpans` representa artículos que ocupan más de un segmento material. Dos casos ya comprobados son:

1. p.141 derecha → p.142 izquierda: `Arbol, cuya leche ſirve para vilma à las mugeres, que padecen de las caderas. Bapſam.`;
2. p.149 izquierda → p.149 derecha: `Camarón. Cecobi, grande del Rio. Bacauri.`.

## Catchwords y control de falsas entradas

Las pp.153–155 confirman que los reclamos tipográficos de pie de página deben excluirse del conteo de artículos. Se documentaron dos ejemplos en `data/lexicon/boundary_markers/catchwords_p153_p154.jsonl`:

- p.153: `Desbaſ-` anticipa `Desbaſtar madera` en p.154;
- p.154: `Dar` anticipa la breve serie `Dar de comer / Dar de beber / Dar de veſtir` que abre p.155.

Estos marcadores son evidencia material para reconstruir continuidad, pero **no son artículos lexicográficos independientes**. Esta regla debe incorporarse al QA del extractor para evitar falsos positivos en los 2,072 candidatos.

## Consecuencia metodológica

La unidad maestra continúa siendo el **artículo histórico**. El modelo operativo ya representa:

`página/columna → spans físicos → agrupación histórica opcional → artículo → formas/remisiones/anáforas/notas → autoridad editorial`.

Los catchwords se mantienen en una capa paratextual de frontera. La normalización, resolución de anáforas, equivalencias modernas y proyección TEI Lex-0 pertenecen a capas posteriores.

## Siguiente lote

Continuar desde **digital 156**, mantener el doble registro GitHub ↔ Notion y revisar especialmente nuevos reclamos, remisiones, anáforas y posibles continuidades entre columna/página.