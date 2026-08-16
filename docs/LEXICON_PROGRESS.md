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
| `p143_selected_articles.jsonl` | 143 | 14 | continuidad de agrupación + nueva agrupación de árboles + voces `Arco`/`Arriba` |
| `p144_selected_articles.jsonl` | 144 | 14 | equivalencias y una remisión `Buſca` |
| `p145_selected_articles.jsonl` | 145 | 14 | incluye `Lo miſmo` conservado como anáfora no resuelta |
| `p146_selected_articles.jsonl` | 146 | 25 | equivalencias y tres remisiones `Buſca` |
| **Total** | — | **208** | todos sin revisión humana independiente |

## Regla de autoridad

Los 208 objetos están estructurados, pero permanecen en estados `machine_corrected_unverified` o `unresolved`. Una estructura válida no equivale a una lectura filológicamente cerrada ni a `human_verified`.

## Remisiones internas

La p.141 confirma dentro de la secuencia productiva una remisión explícita: `Apercibirſe para hazer algo. Buſca aparejarſe.` Se representa como `articleType: cross_reference`, conservando el marcador y su destino sin sustituir el testimonio.

La p.146 muestra además una densidad mayor de remisiones internas en una sola página, entre ellas `Barbo. Buſca Bagre.`, `Barrenar. Buſca agurear con barrena.` y `Baſta, coſa ſin pulir. Buſca aſpero.`. Estas relaciones permanecen documentales: CHD no reemplaza el artículo remitente por el contenido de su destino.

## Anáforas distintas de `Buſca`

La p.145 aporta `Azero. Lo miſmo.`. CHD conserva este objeto como `unresolved`: `Lo miſmo` es una fórmula anafórica que exige resolución contextual y no autoriza a copiar automáticamente la forma del artículo precedente. Este caso confirma la necesidad de distinguir remisión explícita, anáfora y equivalencia.

## Artículos que cruzan página

El último artículo de la columna derecha de p.141 termina con `...que pade-` y continúa en la parte superior de p.142 con `padecen de las caderas. Bapſam.`. La unidad completa se conserva como `ALC1737-art-000141` y utiliza `sourceSpans` para registrar p.141 derecha → p.142 izquierda.

## Microestructura botánica jerárquica

La p.142 contiene artículos descriptivos extensos y series bajo encabezados como `Arboles, cuyo fruto es comeſtible`, `Arboles que ſirven para madera` y `Arboles chaparros`. `sourceGroupingRaw` conserva la agrupación histórica sin incorporarla artificialmente a la voz española.

Las afirmaciones de usos medicinales o materiales se registran como evidencia histórica de 1737; no constituyen recomendaciones médicas ni identificaciones botánicas modernas.

## Comprobación en p. 143: la agrupación también cruza página

La p.143 comienza con nuevas voces `Arbol. ...` que continúan materialmente la serie `Arboles chaparros` iniciada en p.142. Más adelante aparece un nuevo encabezado explícito, `Arboles de mariſmas`. El lote `p143_selected_articles.jsonl` conserva ambos contextos mediante `sourceGroupingRaw` y demuestra que un encabezado de agrupación puede gobernar artículos situados en más de una página.

El mismo lote abandona después la secuencia botánica y registra voces independientes como `Arco para tirar flecha. Huicori.`, `Arco del Cielo. Curuat.`, `Arco. Arcum.` y `Arriba. Hicachi.`, comprobando que la agrupación no se propaga más allá de su alcance material.

## Consecuencia metodológica

La unidad maestra sigue siendo el **artículo histórico**. El modelo representa ahora:

`spans físicos → agrupación histórica opcional → artículo histórico → formas/remisiones/anáforas/notas → autoridad editorial`.

La normalización léxica, resolución de anáforas, identificación de especies, equivalencias con variedades modernas y futura proyección TEI Lex-0 pertenecen a capas posteriores.

## Siguiente lote

Continuar desde **p.147**, conservando por separado equivalencias simples, remisiones, anáforas, artículos descriptivos, agrupaciones, continuaciones físicas y lecturas `unresolved`.
