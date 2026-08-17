from pathlib import Path

p=Path('README.md')
s=p.read_text(encoding='utf-8')
old='- las páginas **170–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **170** tiene sus **48 candidatos canónicos reconciliados**: 48 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; se documentan 3 falsos negativos seleccionados (`000554` `Por donde?`, `000563` `Premiar`, `000568` `Puerco, ò puerca`), L-008/L-024 quedan `merged_articles`, L-004/R-022 quedan `undersegmented`, los 15 artículos seleccionados `ALC1737-art-000554`–`000568` quedaron enlazados a evidencia estructural, permanecen 36 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; p.171 tiene 24 candidatos y abre fresco con `Querella`, después del `Que-` de borde/catchword en R-022;\n- las páginas **171–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in s
s=s.replace(old,new,1)
old='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; en **p.165** quedan 38 `pending_promotion`; en **p.166** quedan 36 `pending_promotion`; en **p.167** quedan 40 `pending_promotion`; en **p.168** quedan 21 `pending_promotion`; y en **p.169** quedan 22 `pending_promotion`. Las páginas 145–169 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 170**, con 48 candidatos canónicos —26 izquierda y 22 derecha—; la capa seleccionada `ALC1737-art-000554`–`000568` comienza con `Por donde? Hacumbichaca?`, comienzo que no tiene frontera canónica propia antes de L-001 (`Porqué? Hita bechibuo?`).'
new='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; en **p.165** quedan 38 `pending_promotion`; en **p.166** quedan 36 `pending_promotion`; en **p.167** quedan 40 `pending_promotion`; en **p.168** quedan 21 `pending_promotion`; en **p.169** quedan 22 `pending_promotion`; y en **p.170** quedan 36 `pending_promotion`. Las páginas 145–170 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 171**, con 24 candidatos canónicos —7 izquierda y 17 derecha—; la capa seleccionada comienza con `ALC1737-art-000569` (`Querella. Natebo.`), alineable al candidato L-001 tras el `Que-` de borde/catchword de p.170.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
marker='## Próximo frente\n'
assert marker in s
section='''## Página 170 — reconciliación conservadora de candidatos completada

La página digital **170** contiene **48 candidatos canónicos: 26 izquierda y 22 derecha**. La reconciliación machine-only clasifica **48 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **44 `exact`**, **2 `undersegmented`** y **2 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000554`–`000568`**. Doce candidatos enlazan trece objetos seleccionados y se documentan tres comienzos seleccionados sin frontera independiente. **`000554` (`Por donde? Hacumbichaca?`)** es un comienzo fresco en el borde superior izquierdo antes de L-001 (`000555`, `Porqué?`). **`000568` (`Puerco, ò puerca. Cobuu.`)** aparece en el borde superior derecho antes de R-001 (`Pulga. Teput.`). Ambos se registran como missed-starts de borde.

El tercer missed-start es **`000563` (`Premiar. Buſca pagar.`)**, absorbido dentro de L-008 después de `000562` (`Pregunta. Atema.`). L-008 queda `merged_articles` y enlaza ambos artículos seleccionados. **L-024** también queda `merged_articles` porque el grupo comienza una voz `Proximo`-like y contiene una segunda unidad `Publico ſer`-like; esta última no está seleccionada/directamente cotejada en la capa disponible, por lo que no se promociona ni se añade al censo de falsos negativos.

**L-004** comienza el seleccionado `000558` (`Predicar hazer ſermon. Hinabaca.`) y conserva `Hinababacame`-like material de `000559`, cuya guía `Predicador` sí tiene frontera propia en L-005; se modela como `undersegmented` por fuga de orden, sin perder la frontera de L-005. En el borde inferior, **R-022** inicia una voz Querellarse-like y termina con `Que-` de borde/catchword, por lo que también queda `undersegmented`.

El paso p.170→171 se conserva fresco. P.171 contiene **24 candidatos: 7 izquierda y 17 derecha** y L-001 abre el seleccionado **`000569` (`Querella. Natebo.`)**. El `Que-` final de p.170 no se trata como continuidad léxica larga.

Quedan **36 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 48 candidatos de artículo más los tres comienzos seleccionados perdidos establecen al menos **51 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y persisten grupos `merged_articles`/`undersegmented` no agotados, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
s=s.replace(marker,section+marker,1)
old='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; en p.165, **38 `pending_promotion`**; en p.166, **36 `pending_promotion`**; en p.167, **40 `pending_promotion`**; en p.168, **21 `pending_promotion`**; y en p.169, **22 `pending_promotion`**. Las páginas 145–169 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 170**, con **48 candidatos canónicos: 26 izquierda y 22 derecha**. La capa seleccionada contiene `ALC1737-art-000554`–`000568` y comienza con `Por donde? Hacumbichaca?`; ese comienzo superior carece de frontera canónica propia y L-001 comienza con `Porqué? Hita bechibuo?`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
new='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; en p.165, **38 `pending_promotion`**; en p.166, **36 `pending_promotion`**; en p.167, **40 `pending_promotion`**; en p.168, **21 `pending_promotion`**; en p.169, **22 `pending_promotion`**; y en p.170, **36 `pending_promotion`**. Las páginas 145–170 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 171**, con **24 candidatos canónicos: 7 izquierda y 17 derecha**. La capa seleccionada comienza con `ALC1737-art-000569` (`Querella. Natebo.`), alineable a L-001 después del `Que-` de borde/catchword de p.170. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
