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
    r'- las páginas \*\*157–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **157** tiene sus **42 candidatos canónicos reconciliados**: 38 `article`, 2 `continuation` y 2 `unresolved`; se documentan 4 falsos negativos internos dentro de regiones `merged_articles`, los 15 artículos seleccionados `ALC1737-art-000359`–`000373` quedaron enlazados, permanecen 27 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; el salto p.157→158 se conserva como `ALC1737-gap-0001`, sin reconstruir el material F/G ausente;\n- las páginas **158–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(
    text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 157\*\*, con 42 candidatos canónicos —19 izquierda y 23 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; en **p.154** quedan 41 `pending_promotion`; en **p.155** quedan 32 `pending_promotion`; en **p.156** quedan 38 `pending_promotion`; y en **p.157** quedan 27 `pending_promotion` y 2 candidatos `unresolved`. Las páginas 145–157 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 158**, con 53 candidatos canónicos —28 izquierda y 25 derecha—, que inicia ya en H después del `ALC1737-gap-0001`; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial, discontinuidad material e incertidumbre textual.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–156 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–157 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 157 — reconciliación conservadora de candidatos completada

La página digital **157** contiene **42 candidatos canónicos: 19 izquierda y 23 derecha**. La reconciliación machine-only clasifica **38 `article`**, **2 `continuation`** y **2 `unresolved`**, sin `paratext` ni `false_positive`. La calidad de frontera se distribuye en **31 `exact`**, 2 `oversegmented`, 1 `undersegmented`, 4 `merged_articles`, 2 `ambiguous` y 2 `not_applicable`.

La columna izquierda está materialmente recortada y el OCR pierde sistemáticamente glifos iniciales y altera el orden de algunas formas. La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000359`–`000373`** y los quince quedaron enlazados mediante 11 candidatos de artículo. Cuatro candidatos contienen dos comienzos seleccionados cada uno y sus segundos inicios quedan registrados en `p157_missed_visible_starts.jsonl`: `000361` (`Eſtomago`) dentro de L-007, `000364` (`Eſtrella`) dentro de L-010, `000368` (`Eſtremecerſe`) dentro de L-014 y `000372` (`Facil coſa`) dentro de L-019.

L-004 inicia un artículo tipo `Eſtera` que continúa en L-005; L-012 (`Eſtrella las tres Marias`) continúa en L-013. **L-003 y L-006 permanecen `unresolved`**: el primero es un fragmento recortado cuya función no puede fijarse y el segundo mezcla la cola del artículo anterior con un probable comienzo fresco que no puede aislarse responsablemente. No se fuerza ninguna lectura para cerrar artificialmente la página.

El borde inferior exige una política distinta de una continuidad ordinaria. `ALC1737-gap-0001` documenta que el testimonio digital termina la secuencia visible con **`Flecha. Huihua.`** y un reclamo `Fle...`, mientras la página digital 158 comienza directamente con **`Hallarſe bien en vn lugar`**. El salto F→H se conserva como **material fuente presumiblemente faltante, de extensión no resuelta**. No se sintetizan voces F/G a partir de diccionarios modernos, reimpresiones u otras inferencias; cualquier recuperación futura requerirá un testimonio independiente y una capa de procedencia separada.

Quedan **27 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 38 candidatos de artículo y cuatro inicios seleccionados absorbidos en regiones fusionadas establecen al menos **42 comienzos visibles conocidos**, pero dos candidatos recortados permanecen irresueltos y la capa seleccionada no es exhaustiva; no se calculan TP/FP/FN, precisión, recall ni F1.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(
    text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 157\*\*, con \*\*42 candidatos canónicos: 19 izquierda y 23 derecha\*\*\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; en p.155, **32 `pending_promotion`**; en p.156, **38 `pending_promotion`**; y en p.157, **27 `pending_promotion`** y 2 candidatos `unresolved`. Las páginas 145–157 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 158**, con **53 candidatos canónicos: 28 izquierda y 25 derecha**. Esta página comienza ya en H después del `ALC1737-gap-0001`; el material F/G ausente no forma parte de la cobertura reconstruible con el testimonio actual. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
