from pathlib import Path
import re


def sub1(text, pattern, repl, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f"{label}: expected 1 replacement, got {n}")
    return out

p = Path('README.md')
text = p.read_text(encoding='utf-8')
text = sub1(
    text,
    r'- las páginas \*\*162–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **162** tiene sus **39 candidatos canónicos reconciliados**: 38 `article` y 1 `unresolved`; L-006 queda `merged_articles` con `Melon` + `Memoria`, se documenta `Memoria. Aubuate.` como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000434`–`000448` quedaron enlazados, permanecen 24 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-011 (`Mahahuene.`) permanece irresuelto y p.163 abre fresco con `Mucho. Hibua.`;\n- las páginas **163–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(
    text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 162\*\*, con 39 candidatos canónicos —20 izquierda y 19 derecha—; abre fresco con `Media coſa la mitad\. Najucu\.`\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; en **p.154** quedan 41 `pending_promotion`; en **p.155** quedan 32 `pending_promotion`; en **p.156** quedan 38 `pending_promotion`; en **p.157** quedan 27 `pending_promotion` y 2 candidatos `unresolved`; en **p.158** quedan 36 `pending_promotion`; en **p.159** quedan 34 `pending_promotion`; en **p.160** quedan 30 `pending_promotion`; en **p.161** quedan 19 `pending_promotion` y 1 candidato `unresolved`; y en **p.162** quedan 24 `pending_promotion` y 1 candidato `unresolved`. Las páginas 145–162 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 163**, con 45 candidatos canónicos —25 izquierda y 20 derecha—; la capa seleccionada `ALC1737-art-000449`–`000463` comienza en `Mozo de edad. Buſca mancebo.`.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–161 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–162 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 162 — reconciliación conservadora de candidatos completada

La página digital **162** contiene **39 candidatos canónicos: 20 izquierda y 19 derecha**. La reconciliación machine-only clasifica **38 `article`** y **1 `unresolved`**, sin candidatos `continuation`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **36 `exact`**, 1 `merged_articles` y 2 `ambiguous`.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000434`–`000448`**. Catorce comienzan en candidato canónico propio y **`000439` (`Memoria. Aubuate.`)** queda absorbido dentro de L-006 después de `000438` (`Melon. Manari.`). Por ello L-006 se conserva como `merged_articles` y `000439` se registra de forma separada en `p162_missed_visible_starts.jsonl` como falso negativo interno conocido.

La incertidumbre se mantiene localizada. **L-020** conserva una frontera geométrica compatible con un comienzo nuevo, pero el OCR no permite recuperar un lema fiable; se mantiene como `article` con evaluación `ambiguous` y sin promoción. **R-011** contiene únicamente `Mahahuene.` sin guía recuperable. Aunque esa forma podría ser compatible con material semánticamente cercano a `Miedo`, la evidencia disponible no autoriza asignarla a R-010 ni fabricar una entrada como `Miedo tener`; por ello R-011 permanece `unresolved`.

Los bordes de página son frescos. P.162 L-001 inicia `000434` (`Media coſa la mitad. Najucu.`) después del fragmento irresuelto R-016 de p.161, sin continuidad transpaginal. En el extremo inferior, R-019 inicia un artículo `Moverſe`; p.163 L-001 abre fresco con `Mucho. Hibua.`, por lo que tampoco se afirma continuación larga.

Quedan **24 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 38 candidatos de artículo más el inicio seleccionado `Memoria` absorbido en L-006 establecen al menos **39 comienzos visibles conocidos**. Como R-011 sigue irresuelto y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(
    text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 162\*\*, con \*\*39 candidatos canónicos: 20 izquierda y 19 derecha\*\*\. La primera ancla seleccionada es `Media coſa la mitad\. Najucu\.`\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; en p.155, **32 `pending_promotion`**; en p.156, **38 `pending_promotion`**; en p.157, **27 `pending_promotion`** y 2 candidatos `unresolved`; en p.158, **36 `pending_promotion`**; en p.159, **34 `pending_promotion`**; en p.160, **30 `pending_promotion`**; en p.161, **19 `pending_promotion`** y 1 candidato `unresolved`; y en p.162, **24 `pending_promotion`** y 1 candidato `unresolved`. Las páginas 145–162 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 163**, con **45 candidatos canónicos: 25 izquierda y 20 derecha**. La capa seleccionada contiene `ALC1737-art-000449`–`000463` y comienza con `Mozo de edad. Buſca mancebo.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
