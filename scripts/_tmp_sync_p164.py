from pathlib import Path

p=Path('README.md')
s=p.read_text(encoding='utf-8')
old='- las páginas **164–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **164** tiene sus **51 candidatos canónicos reconciliados**: 51 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; R-018, R-020 y R-022 quedan `merged_articles`, los 15 artículos seleccionados `ALC1737-art-000464`–`000478` quedaron enlazados, permanecen 36 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; `000477` (`Noez, y nogal. Lo miſmo.`) conserva su anáfora semántica `unresolved` sin volver irresuelta su frontera física; p.165 abre fresco con `Obra aſſi, hechura. Chupari.`;\n- las páginas **165–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in s
s=s.replace(old,new,1)
old='en **p.162** quedan 25 `pending_promotion`; y en **p.163** quedan 28 `pending_promotion`. Las páginas 145–163 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 164**, con 51 candidatos canónicos —29 izquierda y 22 derecha—; la capa seleccionada `ALC1737-art-000464`–`000478` comienza con `Nacimiento. Ioleria.`.'
new='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; y en **p.164** quedan 36 `pending_promotion`. Las páginas 145–164 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 165**, con 56 candidatos canónicos —29 izquierda y 27 derecha—; la capa seleccionada `ALC1737-art-000479`–`000493` comienza con `Obra aſſi, hechura. Chupari.`.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
marker='## Próximo frente\n'
assert marker in s
section='''## Página 164 — reconciliación conservadora de candidatos completada

La página digital **164** contiene **51 candidatos canónicos: 29 izquierda y 22 derecha**. La reconciliación machine-only clasifica **51 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **48 `exact`** y **3 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000464`–`000478`** y los quince quedaron enlazados a candidatos canónicos propios. La página abre de forma fresca con **`000464` (`Nacimiento. Ioleria.`)** después del material inferior dañado de p.163; no se afirma continuidad léxica p.163→164. El seleccionado **`000477` (`Noez, y nogal. Lo miſmo.`)** conserva su anáfora histórica como `unresolved` semántico, pero su frontera física R-001 es `exact`; la incertidumbre de contenido y la clasificación de frontera permanecen desacopladas.

Tres grupos canónicos contienen más de una unidad guía visible en el OCR y se conservan como **`merged_articles`**. R-018 comienza `Nudo` y contiene además una unidad `O. adv. para llamar`-like; R-020 contiene `Obediente` y `Obediencia`; R-022 comienza `Obligación`, contiene un comienzo `Obrar algo`-like y termina con un fragmento `Obr...` de borde/reclamo. Esos inicios internos no poseen anclas seleccionadas/directamente cotejadas en esta pasada: por ello **no se crean artículos, no se promocionan y no se inflan como falsos negativos del censo visible**.

El borde inferior se modela como transición fresca. Aunque R-022 termina con `Obr...`, la página 165 L-001 abre el artículo seleccionado **`000479` (`Obra aſſi, hechura. Chupari.`)**; no se impone una continuidad larga p.164→165. El inventario canónico de p.165 contiene **56 candidatos: 29 izquierda y 27 derecha**.

Quedan **36 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los **51 candidatos de artículo** constituyen el mínimo conservador de comienzos visibles estructuralmente sustentados. Como R-018, R-020 y R-022 contienen unidades internas no ancladas y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
s=s.replace(marker,section+marker,1)
old='y en p.162, **25 `pending_promotion`**; y en p.163, **28 `pending_promotion`**. Las páginas 145–163 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 164**, con **51 candidatos canónicos: 29 izquierda y 22 derecha**. La capa seleccionada contiene `ALC1737-art-000464`–`000478` y comienza con `Nacimiento. Ioleria.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
new='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; y en p.164, **36 `pending_promotion`**. Las páginas 145–164 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 165**, con **56 candidatos canónicos: 29 izquierda y 27 derecha**. La capa seleccionada contiene `ALC1737-art-000479`–`000493` y comienza con `Obra aſſi, hechura. Chupari.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
