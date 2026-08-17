from pathlib import Path
import re


def sub1(text, pattern, repl, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f"{label}: expected 1 replacement, got {n}")
    return out

# README
p = Path('README.md')
text = p.read_text(encoding='utf-8')
text = sub1(
    text,
    r'- las páginas \*\*154–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **154** tiene sus **56 candidatos canónicos reconciliados**: 56 `article`, con 54 fronteras `exact`, 1 `undersegmented` y 1 `oversegmented`; los 15 artículos seleccionados `ALC1737-art-000314`–`000328` quedaron enlazados, permanecen 41 fronteras `pending_promotion` y el censo visible sigue no exhaustivo;\n- las páginas **155–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(
    text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 154\*\*, con 56 candidatos canónicos —27 izquierda y 29 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; y en **p.154** quedan 41 `pending_promotion`. Las páginas 145–154 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 155**, con 49 candidatos canónicos —23 izquierda y 26 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

# LEXICON_PROGRESS
p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–153 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–154 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 154 — reconciliación de candidatos completada

La página digital **154** contiene **56 candidatos canónicos: 27 izquierda y 29 derecha**. La reconciliación machine-only clasifica los **56 como `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **54 `exact`**, **1 `undersegmented`** y **1 `oversegmented`**.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000314`–`000328`** y los quince quedaron enlazados directamente a candidatos canónicos. El candidato R-008 conserva un OCR severamente degradado, pero su geometría independiente y posición léxica sostienen una frontera de artículo; permanece sin promoción y no se fortalece su texto. R-024 inicia `Doler la llaga` y absorbe material final no explicado antes de R-025 `Doncella`, por lo que se marca `undersegmented` sin crear un inicio adicional.

El borde p.153→154 queda confirmado por el reclamo `Desbat-` de p.153 R-026, que anticipa el artículo fresco p.154 L-001 `Desbaſtar madera. Atapetia.`. En el extremo inferior, **R-029 (`Durar mucho tiempo`) cruza físicamente de página**: p.155 L-001 conserva la continuación de forma `nuc. bibuatua.` antes de los siguientes comienzos léxicos. Por ello R-029 se marca `oversegmented` respecto de la segmentación candidata entre páginas.

Quedan **41 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 56 candidatos sostienen al menos 56 comienzos estructurales, pero la capa seleccionada no es exhaustiva y no permite demostrar ausencia de falsos negativos; no se calculan TP/FP/FN, precisión, recall ni F1. `p154_machine_reconciliation_status.json` conserva el detalle y los límites de autoridad.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(
    text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 154\*\*, con \*\*56 candidatos canónicos: 27 izquierda y 29 derecha\*\*\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; y en p.154, **41 `pending_promotion`**. Las páginas 145–154 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 155**, con **49 candidatos canónicos: 23 izquierda y 26 derecha**. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
