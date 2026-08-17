from pathlib import Path

README_OLD = '- la página **162** tiene sus **39 candidatos canónicos reconciliados**: 38 `article` y 1 `unresolved`; L-006 queda `merged_articles` con `Melon` + `Memoria`, se documenta `Memoria. Aubuate.` como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000434`–`000448` quedaron enlazados, permanecen 24 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-011 (`Mahahuene.`) permanece irresuelto y p.163 abre fresco con `Mucho. Hibua.`;'
README_NEW = '- la página **162** tiene sus **39 candidatos canónicos reconciliados**: 39 `article`, sin candidatos estructuralmente `unresolved`; L-006 queda `merged_articles` con `Melon` + `Memoria`, se documenta `Memoria. Aubuate.` como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000434`–`000448` quedaron enlazados, permanecen 25 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-006 y R-019 quedan `undersegmented`, `Mirar` (000448) se alinea a R-016 y el `Mozo` final funciona como reclamo hacia una voz fresca de p.163;'

p=Path('README.md')
s=p.read_text(encoding='utf-8')
if README_OLD not in s:
    raise SystemExit('README p162 old line not found')
s=s.replace(README_OLD, README_NEW, 1)
s=s.replace('en **p.162** quedan 24 `pending_promotion` y 1 candidato `unresolved`.', 'en **p.162** quedan 25 `pending_promotion`.', 1)
s=s.replace('Las páginas 145–162 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 163**, con 45 candidatos canónicos —25 izquierda y 20 derecha—; la capa seleccionada `ALC1737-art-000449`–`000463` comienza en `Mozo de edad. Buſca mancebo.`.', 'Las páginas 145–162 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 163**, con 49 candidatos canónicos —26 izquierda y 23 derecha—; la capa seleccionada `ALC1737-art-000449`–`000463` comienza con `Mozo de edad. Buſca mancebo.`. El primer candidato canónico de p.163 comienza ya en la cola `...cebo.` de esa voz y contiene además `Mofar, eſcarnecer`, por lo que el arranque de p.163 requerirá reconciliación conservadora propia.', 1)
p.write_text(s, encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
old='''## Página 162 — reconciliación conservadora de candidatos completada

La página digital **162** contiene **39 candidatos canónicos: 20 izquierda y 19 derecha**. La reconciliación machine-only clasifica **38 `article`** y **1 `unresolved`**, sin candidatos `continuation`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **36 `exact`**, 1 `merged_articles` y 2 `ambiguous`.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000434`–`000448`**. Catorce comienzan en candidato canónico propio y **`000439` (`Memoria. Aubuate.`)** queda absorbido dentro de L-006 después de `000438` (`Melon. Manari.`). Por ello L-006 se conserva como `merged_articles` y `000439` se registra de forma separada en `p162_missed_visible_starts.jsonl` como falso negativo interno conocido.

La incertidumbre se mantiene localizada. **L-020** conserva una frontera geométrica compatible con un comienzo nuevo, pero el OCR no permite recuperar un lema fiable; se mantiene como `article` con evaluación `ambiguous` y sin promoción. **R-011** contiene únicamente `Mahahuene.` sin guía recuperable. Aunque esa forma podría ser compatible con material semánticamente cercano a `Miedo`, la evidencia disponible no autoriza asignarla a R-010 ni fabricar una entrada como `Miedo tener`; por ello R-011 permanece `unresolved`.

Los bordes de página son frescos. P.162 L-001 inicia `000434` (`Media coſa la mitad. Najucu.`) después del fragmento irresuelto R-016 de p.161, sin continuidad transpaginal. En el extremo inferior, R-019 inicia un artículo `Moverſe`; p.163 L-001 abre fresco con `Mucho. Hibua.`, por lo que tampoco se afirma continuación larga.

Quedan **24 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 38 candidatos de artículo más el inicio seleccionado `Memoria` absorbido en L-006 establecen al menos **39 comienzos visibles conocidos**. Como R-011 sigue irresuelto y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.
'''
new='''## Página 162 — reconciliación conservadora de candidatos completada

La página digital **162** contiene **39 candidatos canónicos: 20 izquierda y 19 derecha**. La reconciliación machine-only clasifica **39 `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **36 `exact`**, **2 `undersegmented`** y **1 `merged_articles`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000434`–`000448`**. Catorce comienzan en candidato canónico propio y **`000439` (`Memoria. Aubuate.`)** queda absorbido dentro de L-006 después de `000438` (`Melon. Manari.`). Por ello L-006 se conserva como `merged_articles` y `000439` se registra de forma separada en `p162_missed_visible_starts.jsonl` como falso negativo interno conocido.

La auditoría contra el export canónico corrigió varias lecturas provisionales antes del cierre. **L-020** conserva de forma recuperable `Merecer. Hkamabare`, de modo que su frontera es `exact`. **R-011** conserva `Miedo tener. Mahabuené` y se clasifica como artículo, no como fragmento irresuelto. El seleccionado **`000448` (`Mirar. Abicha.`) se alinea a R-016**, mientras R-014 corresponde al artículo distinto `Miembro del hombre` y permanece `pending_promotion`. R-006 queda `undersegmented` porque su grupo `Meter como en la caxa` absorbe material adicional sin anclas seleccionadas independientes.

Los bordes de página permanecen frescos. P.162 L-001 inicia `000434` (`Media coſa la mitad. Najucu.`) después del fragmento irresuelto R-016 de p.161, sin continuidad transpaginal. En el extremo inferior, **R-019 inicia un artículo `Mirar saliendo de lo obscuro`-like y absorbe el reclamo `Mozo`**, por lo que también queda `undersegmented`. Ese reclamo anticipa el artículo fresco seleccionado de p.163 **`000449` (`Mozo de edad. Buſca mancebo.`)**; el primer candidato canónico p.163 L-001 comienza ya en su cola `...cebo.` y contiene después `Mofar, eſcarnecer`. No se afirma continuidad léxica p.162→163.

Quedan **25 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 39 candidatos de artículo más el inicio seleccionado `Memoria` absorbido en L-006 establecen al menos **40 comienzos visibles conocidos**. Como la capa seleccionada no es exhaustiva y los grupos subsegmentados pueden contener material interno sin anclas independientes, no se calculan TP/FP/FN, precisión, recall ni F1.
'''
if old not in s:
    raise SystemExit('LEXICON p162 old section not found')
s=s.replace(old,new,1)
s=s.replace('y en p.162, **24 `pending_promotion`** y 1 candidato `unresolved`.', 'y en p.162, **25 `pending_promotion`**.', 1)
s=s.replace('El siguiente frente geométrico es la **página digital 163**, con **45 candidatos canónicos: 25 izquierda y 20 derecha**. La capa seleccionada contiene `ALC1737-art-000449`–`000463` y comienza con `Mozo de edad. Buſca mancebo.`.', 'El siguiente frente geométrico es la **página digital 163**, con **49 candidatos canónicos: 26 izquierda y 23 derecha**. La capa seleccionada contiene `ALC1737-art-000449`–`000463` y comienza con `Mozo de edad. Buſca mancebo.`; el primer candidato canónico L-001 empieza ya en la cola `...cebo.` y contiene además `Mofar, eſcarnecer`, por lo que ese arranque requerirá reconciliación conservadora propia.', 1)
p.write_text(s, encoding='utf-8')
