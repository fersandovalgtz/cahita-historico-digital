from pathlib import Path

# README
p=Path('README.md')
s=p.read_text(encoding='utf-8')
old='- las páginas **163–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **163** tiene sus **49 candidatos canónicos reconciliados**: 42 `article` y 7 `continuation`, sin candidatos estructuralmente `unresolved`; se documenta `Mozo de edad. Buſca mancebo.` (000449) como falso negativo de borde superior, los 15 artículos seleccionados `ALC1737-art-000449`–`000463` quedaron enlazados a evidencia estructural, permanecen 28 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; L-026→R-001 cruza columnas y p.164 abre fresco con `Nacimiento. Ioleria.`;\n- las páginas **164–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in s
s=s.replace(old,new,1)
old='en **p.162** quedan 25 `pending_promotion`. Las páginas 145–162 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 163**, con 49 candidatos canónicos —26 izquierda y 23 derecha—; la capa seleccionada `ALC1737-art-000449`–`000463` comienza con `Mozo de edad. Buſca mancebo.`. El primer candidato canónico de p.163 comienza ya en la cola `...cebo.` de esa voz y contiene además `Mofar, eſcarnecer`, por lo que el arranque de p.163 requerirá reconciliación conservadora propia.'
new='en **p.162** quedan 25 `pending_promotion`; y en **p.163** quedan 28 `pending_promotion`. Las páginas 145–163 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 164**, con 51 candidatos canónicos —29 izquierda y 22 derecha—; la capa seleccionada `ALC1737-art-000464`–`000478` comienza con `Nacimiento. Ioleria.`.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')

# LEXICON_PROGRESS
p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
marker='## Próximo frente\n'
assert marker in s
section='''## Página 163 — reconciliación conservadora de candidatos completada

La página digital **163** contiene **49 candidatos canónicos: 26 izquierda y 23 derecha**. La reconciliación machine-only clasifica **42 `article`** y **7 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **31 `exact`**, **6 `oversegmented`**, **5 `undersegmented`** y **7 `not_applicable`**.

El arranque de página conserva una pérdida de frontera explícita. El reclamo `Mozo` al final de p.162 anticipa el artículo fresco seleccionado **`000449` (`Mozo de edad. Buſca mancebo.`)**, pero el inventario canónico de p.163 no le asigna frontera propia: L-001 comienza ya en la cola `...cebo.` y después abre el seleccionado **`000450` (`Mofar, eſcarnecer. Buſca menoſpreciar.`)**. `000449` se registra por ello como falso negativo de borde superior; no se interpreta el reclamo de p.162 como continuidad léxica.

La microestructura del comienzo se conserva sin reconstrucción silenciosa. L-001 queda `undersegmented` por mezclar la cola de `000449` con el inicio de `000450`; L-002 comienza con la continuación/cross-reference `menoſpreciar` de `000450` y después abre un artículo fresco `Moho como de pan`; L-003 empieza con la cola de ese artículo y abre `Moho como de hierro`, que continúa físicamente en L-004. L-007 también queda `undersegmented`: recibe material de la voz previa antes de abrir el seleccionado `000452` (`Moler. Tuſe.`).

Las siete continuidades canónicas son **L-003→L-004**, **L-010→L-011** (`000455`, `Molendero el que muele. Tuſeme.`), **L-012→L-013** (`Mondar algo...`), **L-022→L-023** (`Morirſe de frío`-like), **L-026→R-001** (`Mosquito, que llaman gegen`, a través de columnas), **R-004→R-005** (`Mostrar con el dedo. Buſca apuntar`) y **R-006→R-007** (`Moverſe, menearſe`). Los candidatos que originan una continuación se conservan `oversegmented`; las filas de continuación son `not_applicable` como frontera fresca.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000449`–`000463`**. Catorce comienzan dentro de candidatos canónicos y `000449` queda documentado fuera del inventario mediante `p163_missed_visible_starts.jsonl`; los quince quedan así enlazados a evidencia estructural. R-023 inicia un artículo `Murmuyo`-like y absorbe ruido/catchword dañado al pie de página, pero p.164 L-001 abre fresco con **`000464` (`Nacimiento. Ioleria.`)**, por lo que no se afirma continuidad p.163→164.

Quedan **28 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 42 candidatos de artículo más el comienzo seleccionado `000449` fuera del inventario establecen al menos **43 comienzos visibles conocidos**. La capa seleccionada no es exhaustiva y los grupos `undersegmented` pueden contener material interno no anclado, por lo que no se calculan TP/FP/FN, precisión, recall ni F1.

'''
s=s.replace(marker,section+marker,1)
old='y en p.162, **25 `pending_promotion`**. Las páginas 145–162 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 163**, con **49 candidatos canónicos: 26 izquierda y 23 derecha**. La capa seleccionada contiene `ALC1737-art-000449`–`000463` y comienza con `Mozo de edad. Buſca mancebo.`; el primer candidato canónico L-001 empieza ya en la cola `...cebo.` y contiene además `Mofar, eſcarnecer`, por lo que ese arranque requerirá reconciliación conservadora propia. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
new='y en p.162, **25 `pending_promotion`**; y en p.163, **28 `pending_promotion`**. Las páginas 145–163 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 164**, con **51 candidatos canónicos: 29 izquierda y 22 derecha**. La capa seleccionada contiene `ALC1737-art-000464`–`000478` y comienza con `Nacimiento. Ioleria.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert old in s
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
