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
    r'- las páginas \*\*160–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **160** tiene sus **45 candidatos canónicos reconciliados**: 44 `article` y 1 `continuation`, sin candidatos estructuralmente `unresolved`; se documenta 1 falso negativo seleccionado (`Ladrona. Eet buame.`), los 15 artículos `ALC1737-art-000404`–`000418` quedaron enlazados a evidencia estructural, permanecen 30 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-026 (`Latir la vena, ò el corazón`) continúa físicamente en p.161 L-001;\n- las páginas **161–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(
    text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 160\*\*, con 45 candidatos canónicos —19 izquierda y 26 derecha—; p\.160 abre con `Yr derecho à alguna parte`, como inicio fresco después del borde/catchword de p\.159\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; en **p.154** quedan 41 `pending_promotion`; en **p.155** quedan 32 `pending_promotion`; en **p.156** quedan 38 `pending_promotion`; en **p.157** quedan 27 `pending_promotion` y 2 candidatos `unresolved`; en **p.158** quedan 36 `pending_promotion`; en **p.159** quedan 34 `pending_promotion`; y en **p.160** quedan 30 `pending_promotion`. Las páginas 145–160 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 161**, con 33 candidatos canónicos —17 izquierda y 16 derecha—; L-001 continúa `Latir la vena, ò el corazón` desde p.160 y L-002 abre fresco `Lavar`.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–159 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–160 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 160 — reconciliación conservadora de candidatos completada

La página digital **160** contiene **45 candidatos canónicos: 19 izquierda y 26 derecha**. La reconciliación machine-only clasifica **44 `article`** y **1 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **40 `exact`**, 2 `oversegmented`, 2 `undersegmented` y 1 `not_applicable`.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000404`–`000418`**. Catorce artículos tienen comienzo candidato propio y `000404` (`Yr derecho à alguna parte. Tutula hueye.`) se modela como artículo en L-001 con continuación de forma en L-002. La página abre como transición fresca después del borde de p.159: L-001 no continúa `Yſlabon`.

La reconciliación documenta un falso negativo seleccionado inequívoco: **`ALC1737-art-000416` (`Ladrona. Eet buame.`)** aparece en la secuencia histórica entre `000415` (`Ladrido`) y `000417` (`Lagaña`), pero el inventario canónico salta directamente de R-005 a R-006. Se registra en `p160_missed_visible_starts.jsonl` como inicio `between_candidates`; este hallazgo no convierte la capa seleccionada en censo exhaustivo.

L-003 (`Yr rodeando`) y R-010 (`Lagrima`) quedan `undersegmented`: sus grupos OCR contienen además fragmentos de guía claramente diferenciados (`Yr delante...` y `Lamer...`, respectivamente), pero no se promueven voces internas ni se cuentan como falsos negativos exhaustivos sin anclas independientes. En el borde inferior, **R-026 inicia `Latir la vena, ò el corazón` y continúa físicamente en p.161 L-001**, que conserva la forma `Qobobohftanhuante`; p.161 L-002 abre ya el artículo fresco `Lavar`.

Quedan **30 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 44 candidatos de artículo más el inicio seleccionado `Ladrona` fuera del inventario establecen al menos **45 comienzos visibles conocidos**. Como existen grupos internos no exhaustivamente resueltos y la capa seleccionada no es cobertura total, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(
    text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 160\*\*, con \*\*45 candidatos canónicos: 19 izquierda y 26 derecha\*\*\. El inventario abre con `Yr derecho à alguna parte`, un inicio fresco después del borde de p\.159\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; en p.155, **32 `pending_promotion`**; en p.156, **38 `pending_promotion`**; en p.157, **27 `pending_promotion`** y 2 candidatos `unresolved`; en p.158, **36 `pending_promotion`**; en p.159, **34 `pending_promotion`**; y en p.160, **30 `pending_promotion`**. Las páginas 145–160 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 161**, con **33 candidatos canónicos: 17 izquierda y 16 derecha**. L-001 continúa el artículo `Latir la vena, ò el corazón` iniciado en p.160 R-026; L-002 comienza fresco `Lavar`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
