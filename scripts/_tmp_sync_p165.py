from pathlib import Path

p=Path('README.md')
s=p.read_text(encoding='utf-8')
old='- las páginas **165–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **165** tiene sus **56 candidatos canónicos reconciliados**: 52 `article` y 4 `continuation`, sin candidatos estructuralmente `unresolved`; L-016 queda `merged_articles` con `Oydor` + `Oyr`, se documenta `Oyr. Hicaha.` (000488) como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000479`–`000493` quedaron enlazados a evidencia estructural, permanecen 38 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-014 queda `undersegmented`, R-016 conserva frontera `ambiguous` sin lema inventado y p.166 abre fresco con `Paga tal. Bebeti.`;\n- las páginas **166–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in s
s=s.replace(old,new,1)
old='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; y en **p.164** quedan 36 `pending_promotion`. Las páginas 145–164 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 165**, con 56 candidatos canónicos —29 izquierda y 27 derecha—; la capa seleccionada `ALC1737-art-000479`–`000493` comienza con `Obra aſſi, hechura. Chupari.`.'
new='en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; y en **p.165** quedan 38 `pending_promotion`. Las páginas 145–165 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 166**, con 50 candidatos canónicos —28 izquierda y 22 derecha—; la capa seleccionada `ALC1737-art-000494`–`000508` comienza con `Paga tal. Bebeti.`.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
marker='## Próximo frente\n'
assert marker in s
section='''## Página 165 — reconciliación conservadora de candidatos completada

La página digital **165** contiene **56 candidatos canónicos: 29 izquierda y 27 derecha**. La reconciliación machine-only clasifica **52 `article`** y **4 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **45 `exact`**, **4 `oversegmented`**, **1 `undersegmented`**, **1 `merged_articles`**, **1 `ambiguous`** y **4 `not_applicable`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000479`–`000493`**. Catorce candidatos de artículo enlazan los quince objetos seleccionados: **L-016** contiene dos comienzos cotejados, `000487` (`Oydor el que oye. Hicahame.`) y `000488` (`Oyr. Hicaha.`). Por ello L-016 queda `merged_articles` y `000488` se registra de forma separada en `p165_missed_visible_starts.jsonl` como falso negativo interno conocido.

Las cuatro continuidades canónicas son **L-003→L-004**, **L-014→L-015**, **R-002→R-003** y **R-007→R-008**. La última completa el cross-reference seleccionado `000490` (`Orejear. Buſca menear las orejas.`); R-008 conserva la cola `...jas` y no es un comienzo fresco. Los candidatos que originan estas continuidades se conservan `oversegmented`; las filas de continuación son `not_applicable` como frontera fresca.

La incertidumbre queda localizada sin fortalecer el OCR. **R-014** inicia el seleccionado `000493` (`Oſado ſer. Buſca atrevido.`) y absorbe material adyacente dañado, por lo que queda `undersegmented`. **R-016** conserva una frontera geométrica propia, pero el OCR no permite recuperar responsablemente su guía española; se mantiene como `article` con evaluación `ambiguous` y `pending_promotion`, sin inventar lema. En L-012, el seleccionado `000485` (`Oficio propio del hombre`) convive con fuga de orden OCR procedente de la entrada vecina `Oy, adv. de tiempo`; la autoridad de transcripción permanece en las anclas seleccionadas.

Los bordes de página son frescos. P.165 L-001 abre `000479` (`Obra aſſi, hechura. Chupari.`) después del fragmento `Obr...` de p.164, sin continuidad larga. En el extremo inferior, R-027 abre `Padrino`, mientras p.166 L-001 comienza fresco con **`000494` (`Paga tal. Bebeti.`)**. El inventario canónico de p.166 contiene **50 candidatos: 28 izquierda y 22 derecha**.

Quedan **38 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 52 candidatos de artículo más el comienzo seleccionado `000488` absorbido en L-016 establecen al menos **53 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y las regiones dañadas pueden contener material interno sin anclas independientes, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
s=s.replace(marker,section+marker,1)
old='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; y en p.164, **36 `pending_promotion`**. Las páginas 145–164 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 165**, con **56 candidatos canónicos: 29 izquierda y 27 derecha**. La capa seleccionada contiene `ALC1737-art-000479`–`000493` y comienza con `Obra aſſi, hechura. Chupari.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
new='y en p.162, **25 `pending_promotion`**; en p.163, **28 `pending_promotion`**; en p.164, **36 `pending_promotion`**; y en p.165, **38 `pending_promotion`**. Las páginas 145–165 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 166**, con **50 candidatos canónicos: 28 izquierda y 22 derecha**. La capa seleccionada contiene `ALC1737-art-000494`–`000508` y comienza con `Paga tal. Bebeti.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
