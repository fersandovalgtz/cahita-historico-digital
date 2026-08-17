from pathlib import Path

p=Path('README.md')
s=p.read_text(encoding='utf-8')
old='- las páginas **168–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **168** tiene sus **32 candidatos canónicos reconciliados**: 32 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; se documentan 4 falsos negativos seleccionados (`Pepita generalmente`, `Perder generalmente`, `Perderſe en el camino`, `Perdonar la injuria`), L-007/L-013/R-009 quedan `merged_articles`, L-006/L-012/L-014/R-011/R-018 quedan `undersegmented`, los 15 artículos seleccionados `ALC1737-art-000524`–`000538` quedaron enlazados a evidencia estructural, permanecen 21 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; p.169 tiene 35 candidatos y su primer candidato comienza en la cola de `Piedra de que ſe ſacan navajas`, después del `Pie-` de borde/catchword en p.168;\n- las páginas **169–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in s
s=s.replace(old,new,1)
old='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; en **p.165** quedan 38 `pending_promotion`; en **p.166** quedan 36 `pending_promotion`; y en **p.167** quedan 40 `pending_promotion`. Las páginas 145–167 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 168**, con 32 candidatos canónicos —14 izquierda y 18 derecha—; el primer candidato conserva `Penacho`, mientras la capa seleccionada `ALC1737-art-000524`–`000538` comienza con `Penca de miſcal. Cuumaicoa.`.'
new='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; en **p.165** quedan 38 `pending_promotion`; en **p.166** quedan 36 `pending_promotion`; en **p.167** quedan 40 `pending_promotion`; y en **p.168** quedan 21 `pending_promotion`. Las páginas 145–168 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 169**, con 35 candidatos canónicos —19 izquierda y 16 derecha—; la capa seleccionada `ALC1737-art-000539`–`000553` comienza con `Piedra de que ſe ſacan navajas. Buſca pedernal prieto.`, cuyo candidato L-001 arranca ya en la cola `...bajas`.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
marker='## Próximo frente\n'
assert marker in s
section='''## Página 168 — reconciliación conservadora de candidatos completada

La página digital **168** contiene **32 candidatos canónicos: 14 izquierda y 18 derecha**. La reconciliación machine-only clasifica **32 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **24 `exact`**, **5 `undersegmented`** y **3 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000524`–`000538`**. Once candidatos enlazan doce objetos seleccionados y cuatro comienzos seleccionados carecen de frontera canónica independiente. Tres se registran conservadoramente `between_candidates`: **`000528` (`Pepita generalmente. Tepſia.`)**, **`000530` (`Perder generalmente. Ataru.`)** y **`000531` (`Perderſe en el camino. Chituc-bochi.`)**. El cuarto, **`000533` (`Perdonar la injuria. Ahiocore.`)**, está absorbido dentro de L-007 después de `000532` (`Perdon. Nehiocore.`); L-007 queda por ello `merged_articles`.

La microsecuencia de pérdida se conserva sin imponer una geometría que el extractor no sustenta. L-006 comienza el seleccionado `000529` (`Pequeño. Ilichi.`) y contiene un fragmento `...tuc-bochi` compatible con la cola de `000531`; por ello queda `undersegmented`, pero el comienzo de `000531` se registra entre candidatos y no se fuerza dentro de L-006. De manera semejante, L-013 comienza `000537` (`Perſona. Ioreme.`) y contiene una segunda unidad `Pertenecer...`-like no seleccionada, por lo que queda `merged_articles`; L-014 comienza `000538` (`Peſada coſa. Beete.`) y conserva material `Buſca penar`-like adyacente como `undersegmented`.

En la columna derecha, **R-009** contiene al menos dos unidades `Pescado` diferenciables y queda `merged_articles`, pero el inicio interno no seleccionado no se promociona ni se añade al censo sin ancla independiente. **R-011** conserva una voz `Pescuezo`/`cerviz`-like junto con fuga de orden `Calulute` procedente de la izquierda y queda `undersegmented`. **R-018** inicia `Pie de animal` y termina con `Pie-` de borde/catchword, también `undersegmented`.

El borde inferior se mantiene fresco. P.169 tiene **35 candidatos: 19 izquierda y 16 derecha**. Su primer seleccionado es **`000539` (`Piedra de que ſe ſacan navajas. Buſca pedernal prieto.`)**; el candidato p.169 L-001 comienza ya en su cola `...bajas. Buſca pedernal prieto.` y después absorbe varias voces siguientes. El `Pie-` de p.168 se trata como material de borde/catchword, no como continuidad léxica larga.

Quedan **21 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 32 candidatos de artículo más los cuatro comienzos seleccionados perdidos establecen al menos **36 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y persisten grupos `merged_articles`/`undersegmented` sin anclas independientes, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
s=s.replace(marker,section+marker,1)
old='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; en p.165, **38 `pending_promotion`**; en p.166, **36 `pending_promotion`**; y en p.167, **40 `pending_promotion`**. Las páginas 145–167 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 168**, con **32 candidatos canónicos: 14 izquierda y 18 derecha**. El primer candidato conserva un artículo fresco `Penacho...`; la capa seleccionada contiene `ALC1737-art-000524`–`000538` y comienza en L-002 con `Penca de miſcal. Cuumaicoa.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
new='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; en p.165, **38 `pending_promotion`**; en p.166, **36 `pending_promotion`**; en p.167, **40 `pending_promotion`**; y en p.168, **21 `pending_promotion`**. Las páginas 145–168 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 169**, con **35 candidatos canónicos: 19 izquierda y 16 derecha**. La capa seleccionada contiene `ALC1737-art-000539`–`000553` y comienza con `Piedra de que ſe ſacan navajas. Buſca pedernal prieto.`; el candidato L-001 comienza ya en la cola de esa voz y contiene además varias voces siguientes. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
