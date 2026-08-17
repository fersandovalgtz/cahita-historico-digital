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
    r'- las páginas \*\*159–177\*\* ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    '- la página **159** tiene sus **52 candidatos canónicos reconciliados**: 49 `article` y 3 `continuation`, sin candidatos estructuralmente `unresolved`; los 15 artículos seleccionados `ALC1737-art-000389`–`000403` quedaron enlazados, permanecen 34 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; las discrepancias de columna de `000398`–`000400` quedan documentadas sin corrección silenciosa;\n- las páginas **160–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;',
    'README coverage')
text = sub1(
    text,
    r'En \*\*p\.145\*\* quedan .*?El siguiente frente geométrico es la \*\*página 159\*\*, con 52 candidatos canónicos —26 izquierda y 26 derecha—, que continúa la secuencia H desde el inicio fresco `Huevo\. Totolichaba\.`; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual\.',
    'En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; en **p.154** quedan 41 `pending_promotion`; en **p.155** quedan 32 `pending_promotion`; en **p.156** quedan 38 `pending_promotion`; en **p.157** quedan 27 `pending_promotion` y 2 candidatos `unresolved`; en **p.158** quedan 36 `pending_promotion`; y en **p.159** quedan 34 `pending_promotion`. Las páginas 145–159 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 160**, con 45 candidatos canónicos —19 izquierda y 26 derecha—; p.160 abre con `Yr derecho à alguna parte`, como inicio fresco después del borde/catchword de p.159.',
    'README next front', flags=re.S)
p.write_text(text, encoding='utf-8')

p = Path('docs/LEXICON_PROGRESS.md')
text = p.read_text(encoding='utf-8')
text = text.replace('Las páginas **145–158 tienen reconciliación completa de sus candidatos canónicos**', 'Las páginas **145–159 tienen reconciliación completa de sus candidatos canónicos**', 1)
marker = '## Próximo frente\n'
if text.count(marker) != 1:
    raise SystemExit(f'LEXICON marker count {text.count(marker)}')
section = '''## Página 159 — reconciliación conservadora de candidatos completada

La página digital **159** contiene **52 candidatos canónicos: 26 izquierda y 26 derecha**. La reconciliación machine-only clasifica **49 `article`** y **3 `continuation`**, sin candidatos `unresolved`, `paratext` o `false_positive`. La calidad de frontera se distribuye en **40 `exact`**, 3 `oversegmented`, 6 `undersegmented` y 3 `not_applicable`.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000389`–`000403`** y los quince quedaron enlazados a candidatos canónicos. La página abre con `000389` (`Huevo. Totolichaba.`), inicio fresco que no continúa el `Hueva...` dañado del borde inferior de p.158. L-001 absorbe además `Aebole`, forma del artículo siguiente `000390` (`Huerfano`); de modo semejante, L-003 absorbe `Butte`, forma del artículo siguiente `000392` (`Huirſe`). Ambas fronteras se conservan `undersegmented` sin borrar los inicios frescos L-002/L-004.

Las continuidades modeladas son **L-025→L-026** (`Yerva para quelite`), **R-001→R-002** (`Yerva de la golondrina`) y **R-003→R-004**, donde `000401` (`Yerva que ſe cria en los arboles. Chibichiam.`) continúa en R-004. L-017, R-012 y R-022 contienen material guía adicional demasiado dañado o sin ancla independiente; queda marcado como `undersegmented`, pero no se promociona ni se convierte en un censo exhaustivo de falsos negativos.

La alineación detecta además una discrepancia de metadatos que se preserva para auditoría: `ALC1737-art-000398`, `000399` y `000400` están marcados como columna derecha en la capa seleccionada, mientras los textos coinciden con los candidatos geométricos izquierdos L-017, L-023 y L-024. **No se aplicó corrección silenciosa de columna en esta pasada estructural.**

R-026 inicia un artículo/cross-reference tipo `Yſlabon. Buſca eſlabon.` y conserva un pequeño fragmento de borde/catchword. El inventario canónico de p.160 abre con **`Yr derecho à alguna parte`**, por lo que se modela una transición fresca de página y no una continuación larga desde R-026.

Quedan **34 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 49 candidatos de artículo constituyen el mínimo de comienzos visibles estructuralmente sustentados; como existen agrupamientos con material interno sin anclas independientes y la capa seleccionada no es exhaustiva, no se calculan TP/FP/FN, precisión, recall ni F1.

'''
text = text.replace(marker, section + marker, 1)
text = sub1(
    text,
    r'En p\.145 quedan \*\*20 `pending_promotion`\*\*.*?El siguiente frente geométrico es la \*\*página digital 159\*\*, con \*\*52 candidatos canónicos: 26 izquierda y 26 derecha\*\*\. La primera ancla seleccionada es `Huevo\. Totolichaba\.` y no se trata como continuación de R-025 de p\.158\. Hasta que p\.145 complete censo visible y promoción, el corpus sigue publicando \*\*1,045 artículos estructurados\*\* y \*\*pp\.133–144\*\* como último tramo técnicamente cerrado\.',
    'En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; en p.152, **37 `pending_promotion`**; en p.153, **34 `pending_promotion`** y 4 candidatos estructurales `unresolved`; en p.154, **41 `pending_promotion`**; en p.155, **32 `pending_promotion`**; en p.156, **38 `pending_promotion`**; en p.157, **27 `pending_promotion`** y 2 candidatos `unresolved`; en p.158, **36 `pending_promotion`**; y en p.159, **34 `pending_promotion`**. Las páginas 145–159 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 160**, con **45 candidatos canónicos: 19 izquierda y 26 derecha**. El inventario abre con `Yr derecho à alguna parte`, un inicio fresco después del borde de p.159. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.',
    'LEXICON next front', flags=re.S)
p.write_text(text, encoding='utf-8')
