from pathlib import Path
import re


def sub1(text, pattern, repl, label, flags=0):
    out, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f"{label}: expected 1 replacement, got {n}")
    return out

p = Path('README.md')
text = p.read_text(encoding='utf-8')
text = sub1(text,
    r'- las páginas \*\*155–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **155** tiene sus **49 candidatos canónicos reconciliados**: 45 `article` y 4 `continuation`; se documentan 2 falsos negativos conocidos, los 15 artículos seleccionados `ALC1737-art-000329`–`000343` quedaron enlazados, permanecen 32 fronteras `pending_promotion` y el censo visible sigue no exhaustivo;\n- las páginas **156–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 155\*\*, con 49 candidatos canónicos —23 izquierda y 26 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; en **p.154** quedan 41 `pending_promotion`; y en **p.155** quedan 32 `pending_promotion`. Las páginas 145–155 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 156**, con 52 candidatos canónicos —26 izquierda y 26 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–154 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–155 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 155 — reconciliación de candidatos completada

La página digital **155** contiene **49 candidatos canónicos: 23 izquierda y 26 derecha**. La reconciliación machine-only clasifica **45 `article`** y **4 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **39 `exact`**, 3 `oversegmented`, 2 `undersegmented`, 1 `merged_articles` y 4 `not_applicable`.

La página comienza con una continuidad material ya demostrada: **L-001 (`nuc. bibuatua.`) continúa p.154 R-029 (`Durar mucho tiempo`)** y no constituye un comienzo nuevo. Después, el extractor omite el artículo seleccionado `ALC1737-art-000329` (`Dar de beber à otro. Abitua.`), registrado como falso negativo conocido antes de L-002. **L-002** inicia `000330` (`Dar de veſtir à otro`) y absorbe además el comienzo de `000331` (`Echar, ò vaciar`), por lo que se conserva como `merged_articles`; `000331` se registra también como inicio interno omitido en `p155_missed_visible_starts.jsonl`.

En la parte superior derecha, R-001 proporciona la frontera geométrica del artículo seleccionado `000343` (`Encender candela, ò tea`), aunque el OCR pierde gran parte del lema; R-002 conserva sólo su forma `Abetia.` y se clasifica `continuation`. De modo equivalente, R-003→R-004 y R-006→R-007 forman dos pares artículo/continuación. R-024 absorbe material final dañado antes de `Enredar` y R-026 arrastra material `Eafar-...` de borde/reclamo que anticipa el inicio fresco `Enſeñar` en p.156 L-001; ambos se marcan `undersegmented` sin inventar nuevas voces.

Los **15 artículos seleccionados `ALC1737-art-000329`–`000343`** quedaron enlazados a evidencia estructural. Quedan **32 candidatos de artículo `pending_promotion`**; no hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 45 candidatos de artículo, el inicio adicional absorbido dentro de L-002 y el falso negativo `000329` establecen al menos **47 comienzos**. Como la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 155\*\*, con \*\*49 candidatos canónicos: 23 izquierda y 26 derecha\*\*\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; y en p.155, **32 `pending_promotion`**. Las páginas 145–155 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 156**, con **52 candidatos canónicos: 26 izquierda y 26 derecha**. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
