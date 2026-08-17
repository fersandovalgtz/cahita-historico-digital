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
    r'- las páginas \*\*158–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **158** tiene sus **53 candidatos canónicos reconciliados**: 50 `article` y 3 `continuation`, sin candidatos estructuralmente `unresolved`; L-014 queda `merged_articles` con `Henchir` + `Henchimiento`, se documenta 1 falso negativo interno seleccionado, los 15 artículos `ALC1737-art-000374`–`000388` quedaron enlazados, permanecen 36 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; la página inicia una secuencia H fresca después de `ALC1737-gap-0001`;\n- las páginas **159–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(
    text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 158\*\*, con 53 candidatos canónicos —28 izquierda y 25 derecha—, que inicia ya en H después del `ALC1737-gap-0001`; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial, discontinuidad material e incertidumbre textual\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; en **p.154** quedan 41 `pending_promotion`; en **p.155** quedan 32 `pending_promotion`; en **p.156** quedan 38 `pending_promotion`; en **p.157** quedan 27 `pending_promotion` y 2 candidatos `unresolved`; y en **p.158** quedan 36 `pending_promotion`. Las páginas 145–158 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 159**, con 52 candidatos canónicos —26 izquierda y 26 derecha—, que continúa la secuencia H desde el inicio fresco `Huevo. Totolichaba.`; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–157 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–158 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 158 — reconciliación conservadora de candidatos completada

La página digital **158** contiene **53 candidatos canónicos: 28 izquierda y 25 derecha**. La reconciliación machine-only clasifica **50 `article`** y **3 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **45 `exact`**, 1 `oversegmented`, 3 `undersegmented`, 1 `merged_articles` y 3 `not_applicable`.

La página comienza después de la discontinuidad material `ALC1737-gap-0001`. L-001 (`Hallarſe bien en vn lugar`) constituye un **inicio fresco de la secuencia H**, no una continuación del material F que termina p.157. La pérdida F/G permanece fuera de la cobertura reconstruida y no se sintetiza por inferencia.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000374`–`000388`**. Los quince quedaron enlazados mediante 14 candidatos de artículo. **L-014** inicia `000384` (`Henchir. Atapunia.`) y absorbe además el comienzo distinto de `000385` (`Henchimiento. Buſca llenar.`); por ello se conserva como `merged_articles` y `000385` queda registrado en `p158_missed_visible_starts.jsonl` como falso negativo interno conocido.

L-019 inicia `Herrar poner el hierro` y continúa en L-020. La región inferior izquierda L-026→L-027→L-028 contiene `Hilado` y varios fragmentos adicionales de guía/forma; se modela como una frontera `undersegmented` seguida de dos continuaciones, sin promover ni convertir en censo exhaustivo los posibles inicios internos no respaldados por anclas independientes. R-004 también queda `undersegmented`: su inicio tipo `Hinchazón` es estructuralmente claro, pero absorbe material interno demasiado dañado para microsegmentarlo responsablemente.

En el borde inferior, R-025 inicia `Hueva` y conserva un fragmento `Huey...` de borde. La primera ancla seleccionada de p.159 es **`Huevo. Totolichaba.`**, por lo que no se afirma una continuidad larga p.158→159; el fragmento dañado permanece como material de borde no promovido.

Quedan **36 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 50 candidatos de artículo y el comienzo seleccionado adicional absorbido dentro de L-014 establecen al menos **51 comienzos visibles conocidos**. Como L-026 y R-004 contienen material adicional sin ancla independiente y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(
    text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 158\*\*, con \*\*53 candidatos canónicos: 28 izquierda y 25 derecha\*\*\. Esta página comienza ya en H después del `ALC1737-gap-0001`; el material F/G ausente no forma parte de la cobertura reconstruible con el testimonio actual\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; en p.155, **32 `pending_promotion`**; en p.156, **38 `pending_promotion`**; en p.157, **27 `pending_promotion`** y 2 candidatos `unresolved`; y en p.158, **36 `pending_promotion`**. Las páginas 145–158 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 159**, con **52 candidatos canónicos: 26 izquierda y 26 derecha**. La primera ancla seleccionada es `Huevo. Totolichaba.` y no se trata como continuación de R-025 de p.158. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
