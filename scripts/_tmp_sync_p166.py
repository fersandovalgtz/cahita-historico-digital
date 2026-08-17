from pathlib import Path

p=Path('README.md')
s=p.read_text(encoding='utf-8')
old='- las páginas **166–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **166** tiene sus **50 candidatos canónicos reconciliados**: 50 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; L-003 queda `merged_articles` con `Palabra` + `Palma arbol conocido`, se documenta `Palma arbol conocido. Taco.` (000497) como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000494`–`000508` quedaron enlazados a evidencia estructural, permanecen 36 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; L-007, R-008 y R-022 quedan `undersegmented` por mezcla/fuga de orden OCR o material de borde, y p.167 abre fresco con `Paſſo de las beſtias. Arabuerama.`;\n- las páginas **167–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in s
s=s.replace(old,new,1)
old='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; y en **p.165** quedan 38 `pending_promotion`. Las páginas 145–165 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 166**, con 50 candidatos canónicos —28 izquierda y 22 derecha—; la capa seleccionada `ALC1737-art-000494`–`000508` comienza con `Paga tal. Bebeti.`.'
new='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; en **p.165** quedan 38 `pending_promotion`; y en **p.166** quedan 36 `pending_promotion`. Las páginas 145–166 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 167**, con 55 candidatos canónicos —30 izquierda y 25 derecha—; la capa seleccionada `ALC1737-art-000509`–`000523` comienza con `Paſſo de las beſtias. Arabuerama.`.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
marker='## Próximo frente\n'
assert marker in s
section='''## Página 166 — reconciliación conservadora de candidatos completada

La página digital **166** contiene **50 candidatos canónicos: 28 izquierda y 22 derecha**. La reconciliación machine-only clasifica **50 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **46 `exact`**, **3 `undersegmented`** y **1 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000494`–`000508`**. Catorce candidatos enlazan los quince objetos seleccionados: **L-003** contiene `000496` (`Palabra. Noqui.`) y `000497` (`Palma arbol conocido. Taco.`). Por ello L-003 queda `merged_articles` y `000497` se registra en `p166_missed_visible_starts.jsonl` como falso negativo interno conocido.

La fuga de orden OCR se conserva sin transformarla en transcripción. **L-007** inicia el cross-reference seleccionado `000501` (`Palo para eſcarbar tierra. Buſca coa.`) y absorbe `brazo.` de la región vecina de `000502` (`Paletilla del brazo`). **R-008** inicia un artículo `Partear`-like, pero contiene además `tierra` y `Hapari`-like desplazados desde las entradas seleccionadas izquierdas `000501`/`000502`; ambos grupos quedan `undersegmented`. L-008 sigue siendo el comienzo estructural de `000502`, y la capa seleccionada de cotejo directo conserva la autoridad de su transcripción.

En el borde inferior, **R-022** inicia un artículo dañado Pesar-like y contiene además material `Paſſo`-like de borde/reclamo, por lo que queda `undersegmented`. La página 167 L-001 abre de forma fresca el seleccionado **`000509` (`Paſſo de las beſtias. Arabuerama.`)**; no se afirma continuidad léxica p.166→167. El inventario canónico de p.167 contiene **55 candidatos: 30 izquierda y 25 derecha**.

Quedan **36 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 50 candidatos de artículo más el comienzo seleccionado `000497` absorbido en L-003 establecen al menos **51 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y existe fuga de orden OCR, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
s=s.replace(marker,section+marker,1)
old='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; y en p.165, **38 `pending_promotion`**. Las páginas 145–165 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 166**, con **50 candidatos canónicos: 28 izquierda y 22 derecha**. La capa seleccionada contiene `ALC1737-art-000494`–`000508` y comienza con `Paga tal. Bebeti.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
new='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; en p.165, **38 `pending_promotion`**; y en p.166, **36 `pending_promotion`**. Las páginas 145–166 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 167**, con **55 candidatos canónicos: 30 izquierda y 25 derecha**. La capa seleccionada contiene `ALC1737-art-000509`–`000523` y comienza con `Paſſo de las beſtias. Arabuerama.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
