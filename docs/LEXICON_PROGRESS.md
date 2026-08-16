# Progreso del corpus lexicográfico

## Estado — 2026-08-15

El Vocabulario de `ALC1737` ocupa las páginas digitales 133–177. El extractor `hybrid_margin_mode_v0.2` conserva **2,072 candidatos** de frontera sobre 45 páginas, pero los candidatos no se cuentan como artículos históricos publicados.

La promoción curatorial ha comenzado con artículos visualmente cotejados y estructurados conforme a `schemas/lexical-article.schema.json`.

| Lote | Página | Artículos estructurados | Nota |
|---|---:|---:|---|
| `p134_pilot_articles.jsonl` | 134 | 12 | piloto inicial |
| `p138_selected_articles.jsonl` | 138 | 33 | selección de alta legibilidad |
| `p139_selected_articles.jsonl` | 139 | 39 | selección de alta legibilidad |
| `p140_selected_articles.jsonl` | 140 | 36 | selección de alta legibilidad |
| `p141_selected_articles.jsonl` | 141 | 10 | incluye remisión explícita `Buſca` |
| `p142_botanical_pilot.jsonl` | 142 | 10 | artículos descriptivos y agrupaciones botánicas |
| `p141_p142_cross_page_article.jsonl` | 141–142 | 1 | primer artículo reconstruido a través de salto de página |
| **Total** | — | **141** | todos sin revisión humana independiente |

## Regla de autoridad

Los 141 objetos están estructurados, pero permanecen `machine_corrected_unverified`. Una estructura válida no equivale a una lectura filológicamente cerrada ni a `human_verified`.

## Hallazgo de p. 141: la remisión forma parte del artículo

La página 141 confirma dentro de la secuencia productiva una remisión explícita:

`Apercibirſe para hazer algo. Buſca aparejarſe.`

Se representa como `articleType: cross_reference`, conservando `markerRaw = Buſca`, `targetRaw = aparejarſe` y la relación mínima `see`. No se sustituye la remisión por el contenido de su destino.

## Hallazgo de pp. 141–142: artículos que cruzan página

El último artículo de la columna derecha de p.141 termina con `...que pade-` y continúa en la parte superior de p.142 con `padecen de las caderas. Bapſam.`. La unidad histórica completa se conserva como:

`Arbol, cuya leche ſirve para vilma à las mugeres, que padecen de las caderas. Bapſam.`

El schema incorpora ahora `sourceSpans`, una secuencia ordenada de página y columna, para representar un único artículo que ocupa más de un segmento físico. El objeto `ALC1737-art-000141` registra dos spans: p.141 derecha → p.142 izquierda. La reconstrucción se limita a unir fragmentos tipográficamente contiguos; no introduce texto externo ni normalización moderna.

## Hallazgo de p. 142: microestructura botánica jerárquica

La página 142 contiene dos fenómenos que una simple pareja español–cahíta no puede representar adecuadamente.

Primero, aparecen artículos descriptivos extensos, por ejemplo los que atribuyen a determinados árboles usos medicinales o materiales. CHD los tipa como `descriptive` y preserva literalmente el contenido histórico. **Estas afirmaciones se documentan como evidencia de la fuente de 1737; no constituyen recomendaciones médicas ni identificaciones botánicas modernas.**

Segundo, el impreso organiza series bajo encabezados como `Arboles, cuyo fruto es comeſtible`, `Arboles que ſirven para madera` y `Arboles chaparros`. Para no perder esa jerarquía, `schemas/lexical-article.schema.json` incorpora el campo opcional `sourceGroupingRaw`. Cada artículo puede así conservar el encabezado histórico que lo gobierna sin convertirlo en parte artificial de la voz española.

## Consecuencia metodológica

La unidad maestra sigue siendo el **artículo histórico**, pero el modelo representa ahora explícitamente cinco dimensiones documentales:

`spans físicos → agrupación histórica opcional → artículo histórico → formas/remisiones/notas → autoridad editorial`.

La normalización léxica, la identificación de especies, las equivalencias con variedades modernas y una futura proyección TEI Lex-0 pertenecen a capas posteriores y no deben sobrescribir esta estructura documental.

## Siguiente lote

Continuar la promoción selectiva desde p. 142 hacia las páginas siguientes, manteniendo por separado:

- equivalencias simples;
- remisiones internas;
- artículos descriptivos;
- encabezados de agrupación;
- continuaciones entre páginas/columnas;
- lecturas `unresolved` cuando el facsímil no permita una lectura segura.
