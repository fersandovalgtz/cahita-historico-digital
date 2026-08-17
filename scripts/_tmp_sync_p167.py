from pathlib import Path

p=Path('README.md')
s=p.read_text(encoding='utf-8')
old='- las páginas **167–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **167** tiene sus **55 candidatos canónicos reconciliados**: 54 `article` y 1 `continuation`, sin candidatos estructuralmente `unresolved`; L-010 queda `merged_articles` con `Pato. Tepciabiri.` + `Paxaro generalmente. Moel.`, se documenta `Paxaro generalmente. Moel.` (000519) como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000509`–`000523` quedaron enlazados a evidencia estructural, permanecen 40 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-002→R-003 modela la única continuidad, L-030 conserva frontera `ambiguous`, R-011/R-013/R-025 quedan `undersegmented`, R-020 queda `merged_articles` sin inflar el censo y p.168 abre fresco con `Penacho`;\n- las páginas **168–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in s
s=s.replace(old,new,1)
old='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; en **p.165** quedan 38 `pending_promotion`; y en **p.166** quedan 36 `pending_promotion`. Las páginas 145–166 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 167**, con 55 candidatos canónicos —30 izquierda y 25 derecha—; la capa seleccionada `ALC1737-art-000509`–`000523` comienza con `Paſſo de las beſtias. Arabuerama.`.'
new='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; en **p.165** quedan 38 `pending_promotion`; en **p.166** quedan 36 `pending_promotion`; y en **p.167** quedan 40 `pending_promotion`. Las páginas 145–167 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 168**, con 32 candidatos canónicos —14 izquierda y 18 derecha—; el primer candidato conserva `Penacho`, mientras la capa seleccionada `ALC1737-art-000524`–`000538` comienza con `Penca de miſcal. Cuumaicoa.`.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
marker='## Próximo frente\n'
assert marker in s
section='''## Página 167 — reconciliación conservadora de candidatos completada

La página digital **167** contiene **55 candidatos canónicos: 30 izquierda y 25 derecha**. La reconciliación machine-only clasifica **54 `article`** y **1 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **47 `exact`**, **1 `oversegmented`**, **3 `undersegmented`**, **2 `merged_articles`**, **1 `ambiguous`** y **1 `not_applicable`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000509`–`000523`**. Catorce candidatos de artículo enlazan los quince objetos seleccionados: **L-010** contiene `000518` (`Pato. Tepciabiri.`) y `000519` (`Paxaro generalmente. Moel.`). Por ello L-010 queda `merged_articles` y `000519` se registra en `p167_missed_visible_starts.jsonl` como falso negativo interno conocido.

La única continuidad canónica inequívoca es **R-002→R-003**: `Pedernal prieto para flechas` comienza en R-002 y su forma `Bicam` continúa en R-003. R-002 queda `oversegmented` y R-003 `not_applicable` como frontera fresca. **L-030** se conserva como `article` con evaluación `ambiguous`: la geometría sustenta un comienzo entre `Pecar` y `Pedazo`, pero el OCR no permite recuperar responsablemente su guía española y no se promueve.

Las mezclas internas se conservan sin convertir OCR en edición. **R-011** contiene `Peine` más material `Apea`-like de la región siguiente y **R-013** termina con un fragmento `limpi-` procedente de material adyacente; ambos quedan `undersegmented`. **R-020** comienza `Pelo interior. Huiboa.` y contiene una segunda unidad guía `pelo... Caita chona`-like, por lo que queda `merged_articles`; ese inicio interno no seleccionado no se promociona ni se registra como falso negativo sin ancla directa independiente.

El borde inferior es fresco. **R-025** comienza `Pena generalmente` y absorbe `Pena-` como material de borde/catchword, por lo que queda `undersegmented`. P.168 L-001 comienza un artículo fresco `Penacho...`; el primer seleccionado de p.168 es `000524` (`Penca de miſcal. Cuumaicoa.`) en L-002. El inventario canónico de p.168 contiene **32 candidatos: 14 izquierda y 18 derecha**.

Quedan **40 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 54 candidatos de artículo más el comienzo seleccionado `000519` absorbido en L-010 establecen al menos **55 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y persisten grupos `merged_articles`/`undersegmented` sin anclas independientes, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
s=s.replace(marker,section+marker,1)
old='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; en p.165, **38 `pending_promotion`**; y en p.166, **36 `pending_promotion`**. Las páginas 145–166 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 167**, con **55 candidatos canónicos: 30 izquierda y 25 derecha**. La capa seleccionada contiene `ALC1737-art-000509`–`000523` y comienza con `Paſſo de las beſtias. Arabuerama.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
new='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; en p.165, **38 `pending_promotion`**; en p.166, **36 `pending_promotion`**; y en p.167, **40 `pending_promotion`**. Las páginas 145–167 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 168**, con **32 candidatos canónicos: 14 izquierda y 18 derecha**. El primer candidato conserva un artículo fresco `Penacho...`; la capa seleccionada contiene `ALC1737-art-000524`–`000538` y comienza en L-002 con `Penca de miſcal. Cuumaicoa.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
