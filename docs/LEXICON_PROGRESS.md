# Progreso del corpus lexicográfico

## Estado — 2026-08-15

El Vocabulario de `ALC1737` ocupa las páginas digitales 133–177. El extractor `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera sobre 45 páginas, pero los candidatos no se cuentan como artículos históricos publicados.

La secuencia curatorial principal contiene ahora **478 artículos históricos estructurados**: piloto p.134 + avance continuo pp.138–164 dentro del material efectivamente conservado. Todos permanecen `machine_corrected_unverified` o `unresolved`; **ninguno** ha sido declarado `human_verified`.

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
| **Total principal** | — | **478** |

Existen además **4 artículos de remisión piloto** en p.165, mantenidos fuera del conteo principal mientras no se reconcilie esa página con la secuencia productiva.

## Regla de autoridad

Una estructura válida no equivale a una lectura filológicamente cerrada. `machine_corrected_unverified`, `unresolved` y `human_verified` son estados diferentes; CHD no promueve automáticamente una lectura IA-asistida a validación humana.

## Remisiones internas `Buſca`

Las remisiones se modelan como relaciones documentales, no como sustitución del artículo remitente por el contenido de su destino. Los nuevos lotes añaden, entre otras, `Yr por agua → agua traer`, `Jubilo → gozo`, `Legumbres → frixol, habas, &c.`, `Loco bolverſe → enloquecer`, `Loma → ladera`, `Mentar à alguno → mencionar`, `Mozo de edad → mancebo`, `Mofar, eſcarnecer → menoſpreciar`, `Montear → caçar`, `Neceſſidad tener de alguna coſa → meneſter ſer`, `Ninguna coſa → nada` y `Nombrar, poner nombre → llamar`.

### Primer ciclo recíproco

Las pp.153–154 conservan el primer ciclo explícito de remisión del corpus:

`Demonio. Buſca diablo.` ↔ `Diablo. Buſca demonio.`

Se preserva en `data/lexicon/relations/reciprocal_cross_references.jsonl`. CHD no infiere cuál de las dos voces debe ser el destino canónico.

## Anáforas `Lo miſmo`

`Lo miſmo` se mantiene separado de `Buſca`. Además de los casos anteriores, los nuevos lotes conservan como `unresolved` `Yerva buena`, `Libro`, `Limon` y `Noez, y nogal`. No se copia automáticamente la forma de la entrada precedente.

## Agrupaciones, spans y microestructura

`sourceGroupingRaw` conserva agrupaciones históricas; `sourceSpans` representa artículos que cruzan página o columna. Ya están comprobados el artículo botánico pp.141–142 y `Camarón. Cecobi, grande del Rio. Bacauri.` en p.149.

## Catchwords y control de fronteras

Los reclamos de pie de página se conservan como paratexto, no como artículos. La capa `data/lexicon/boundary_markers/` registra ahora también:

- p.159 `Yr` → inicio normal de p.160;
- p.160 `Que-` → continuación en la parte superior de p.161 de un artículo cuyo lema comienza en la página anterior;
- p.161 `Lucer-` → anomalía de frontera: p.162 comienza con la forma visible `Tohuopo, l, aioa.` sin que el lema anunciado por el reclamo sea visible en el escaneo;
- p.163 `Naci-` → `Nacido...` en p.164;
- p.164 `Obr-` → pendiente de cotejo al reconciliar p.165.

El caso p.161→162 **no se reconstruye por conjetura**: puede responder a recorte, pérdida de una línea o comportamiento material del testimonio, y queda `unresolved` hasta contar con evidencia adicional.

## Discontinuidad del testimonio entre F y H

La p.157 termina la secuencia visible con `Flecha. Huihua.` y presenta al pie un reclamo `Fle...`. La digital 158 comienza directamente con voces de H. El HTML guardado reproduce el mismo salto.

CHD registra el punto como `ALC1737-gap-0001` en `data/source/alc1737/gaps.jsonl` y lo documenta en `docs/SOURCE_GAPS.md`. **No se reconstruye la sección faltante ni se afirma todavía cuántas páginas o folios se perdieron.**

## Consecuencia metodológica

La unidad maestra continúa siendo el **artículo histórico**:

`página/columna → spans físicos → agrupación opcional → artículo → formas/remisiones/anáforas/notas → autoridad editorial`.

Catchwords, anomalías de frontera y lagunas del testimonio se mantienen en capas separadas de paratexto/procedencia. La normalización, resolución de anáforas, equivalencias modernas y proyección TEI Lex-0 pertenecen a capas posteriores.

## Siguiente lote

Reconciliar **digital 165** con los cuatro artículos piloto ya existentes, evitar duplicados y continuar después la secuencia productiva hacia p.166.