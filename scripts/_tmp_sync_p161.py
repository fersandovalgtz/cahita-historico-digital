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
    r'- las páginas \*\*161–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **161** tiene sus **33 candidatos canónicos reconciliados**: 31 `article`, 1 `continuation` y 1 `unresolved`; se documentan 3 falsos negativos seleccionados (`Lengua de buey`, `Libro`, `Limon`), los 15 artículos `ALC1737-art-000419`–`000433` quedaron enlazados a evidencia estructural, permanecen 19 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; L-001 continúa `Latir la vena, ò el corazón` desde p.160 y p.162 abre fresco en `Media coſa la mitad`;\n- las páginas **162–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(
    text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 161\*\*, con 33 candidatos canónicos —17 izquierda y 16 derecha—; L-001 continúa `Latir la vena, ò el corazón` desde p\.160 y L-002 abre fresco `Lavar`\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; en **p.154** quedan 41 `pending_promotion`; en **p.155** quedan 32 `pending_promotion`; en **p.156** quedan 38 `pending_promotion`; en **p.157** quedan 27 `pending_promotion` y 2 candidatos `unresolved`; en **p.158** quedan 36 `pending_promotion`; en **p.159** quedan 34 `pending_promotion`; en **p.160** quedan 30 `pending_promotion`; y en **p.161** quedan 19 `pending_promotion` y 1 candidato `unresolved`. Las páginas 145–161 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 162**, con 39 candidatos canónicos —20 izquierda y 19 derecha—; abre fresco con `Media coſa la mitad. Najucu.`.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–160 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–161 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 161 — reconciliación conservadora de candidatos completada

La página digital **161** contiene **33 candidatos canónicos: 17 izquierda y 16 derecha**. La reconciliación machine-only clasifica **31 `article`**, **1 `continuation`** y **1 `unresolved`**, sin `paratext` ni `false_positive`. La calidad de frontera se distribuye en **29 `exact`**, 1 `merged_articles`, 2 `ambiguous` y 1 `not_applicable`.

La página abre con **L-001 (`Qobobohftanhuante`) como continuación de p.160 R-026 (`Latir la vena, ò el corazón`)**. L-002 comienza ya el artículo fresco seleccionado `000419` (`Lavar. Hipacſia, 1, baſona.`). La capa seleccionada contiene **15 artículos `ALC1737-art-000419`–`000433`**; doce tienen comienzo candidato propio y tres quedan documentados como falsos negativos seleccionados.

El primer falso negativo es **`000429` (`Lengua de buey. Buabuaſo.`)**, absorbido dentro de L-014 después de un artículo fresco `Levantar algo del suelo`; por ello L-014 se marca `merged_articles`. Los otros dos son **`000430` (`Libro. Lo miſmo.`)** y **`000431` (`Limon. Lo miſmo.`)**, ubicados en la transición de columna después de L-017 (`Liar`) y antes de R-001, sin candidato canónico propio. Ambos conservan su fórmula anafórica sin intentar resolverla por inferencia.

La parte inferior derecha mantiene incertidumbre explícita. **R-015** conserva una frontera geométrica compatible con un comienzo nuevo, pero el OCR perdió el lema; se clasifica `article` con evaluación `ambiguous` y queda sin promoción. **R-016** es un fragmento mínimo que no permite decidir responsablemente entre artículo, continuación, paratexto o falso positivo, por lo que permanece `unresolved`. La página 162 abre fresco con `Media coſa la mitad. Najucu.`, así que no se afirma continuidad transpaginal desde R-016.

Quedan **19 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 31 candidatos de artículo más los tres comienzos seleccionados sin candidato propio establecen al menos **34 comienzos visibles conocidos**. Como R-016 sigue irresuelto y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(
    text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 161\*\*, con \*\*33 candidatos canónicos: 17 izquierda y 16 derecha\*\*\. L-001 continúa el artículo `Latir la vena, ò el corazón` iniciado en p\.160 R-026; L-002 comienza fresco `Lavar`\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; en p.155, **32 `pending_promotion`**; en p.156, **38 `pending_promotion`**; en p.157, **27 `pending_promotion`** y 2 candidatos `unresolved`; en p.158, **36 `pending_promotion`**; en p.159, **34 `pending_promotion`**; en p.160, **30 `pending_promotion`**; y en p.161, **19 `pending_promotion`** y 1 candidato `unresolved`. Las páginas 145–161 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 162**, con **39 candidatos canónicos: 20 izquierda y 19 derecha**. La primera ancla seleccionada es `Media coſa la mitad. Najucu.`. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
