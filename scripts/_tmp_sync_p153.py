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
    r'- las páginas \*\*153–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **153** tiene sus **51 candidatos canónicos reconciliados**: 46 `article`, 1 `continuation` y 4 `unresolved`; se documentan además 2 falsos negativos conocidos en el borde superior derecho, 34 fronteras `pending_promotion` y un censo visible no exhaustivo;\n- las páginas **154–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(
    text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 153\*\*, con 51 candidatos canónicos —25 izquierda y 26 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; y en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`. Las páginas 145–153 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 154**, con 56 candidatos canónicos —27 izquierda y 29 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

# LEXICON_PROGRESS
p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–152 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–153 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 153 — reconciliación de candidatos completada

La página digital **153** contiene **51 candidatos canónicos: 25 izquierda y 26 derecha**. La reconciliación machine-only clasifica **46 `article`**, **1 `continuation`** y **4 `unresolved`**. La calidad de frontera se distribuye en **40 `exact`**, 4 `undersegmented`, 1 `merged_articles`, 1 `oversegmented`, 4 `ambiguous` y 1 `not_applicable`.

La capa seleccionada contiene **15 artículos `ALC1737-art-000299`–`000313`**. Todos quedaron enlazados a evidencia estructural, pero no todos mediante candidatos de artículo: **dos comienzos seleccionados son falsos negativos demostrados en el borde superior derecho**. `ALC1737-art-000309` (`Dar. Amaca.`) y `ALC1737-art-000310` (`Dar coſas largas como palo. Tebec amaca.`) comienzan antes de R-001; R-001 conserva sólo `Tebec. amaca.` y se modela como continuación de `000310`. Estos falsos negativos se registran explícitamente en `p153_missed_visible_starts.jsonl`.

En la izquierda, **L-005** absorbe dos artículos seleccionados —`000302` (`Zambullir à otro. Aroptitua.`) y `000303` (`Zarcillo. Erepa.`)— y se conserva como `merged_articles`. L-001 arrastra un `Dar.` ajeno al artículo `Cuñado de hombre`, tratado como contaminación intercolumna; L-023 absorbe material `D.` de cambio alfabético. En la derecha, R-002 inicia el artículo seleccionado `Dar coſas redondas, y mazizas`, cuya terminación ocupa el comienzo de R-003. Como R-003 además introduce material guía dañado, **R-003–R-006 permanecen `unresolved`** en lugar de imponerse una microsegmentación especulativa.

El borde inferior queda también resuelto conservadoramente: R-026 inicia `Delatar` y arrastra `Desbat-` como reclamo/material de borde. P.154 L-001 abre el artículo fresco `Desbaſtar madera. Atapetia.`, por lo que no se afirma continuidad larga p.153→154.

Quedan **34 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Se conocen al menos **49 inicios**: 46 candidatos confirmados como `article`, un inicio adicional absorbido dentro de L-005 y dos falsos negativos superiores derechos. La región R-003–R-006 y la naturaleza no exhaustiva de la capa seleccionada impiden establecer un denominador completo; no se calculan TP/FP/FN, precisión, recall ni F1.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(
    text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 153\*\*, con \*\*51 candidatos canónicos: 25 izquierda y 26 derecha\*\*\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; y en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`. Las páginas 145–153 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 154**, con **56 candidatos canónicos: 27 izquierda y 29 derecha**. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
