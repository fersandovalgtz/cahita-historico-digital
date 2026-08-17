from pathlib import Path

readme=Path('README.md')
r=readme.read_text(encoding='utf-8')
old='- las páginas **174–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **174** tiene sus **48 candidatos canónicos reconciliados**: 48 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; se documentan 3 falsos negativos seleccionados (`000614` `Si, adv. para afirmar`, `000623` `Socorrer`, `000628` `Soplar`), L-013/L-024/R-001/R-006/R-011/R-012 quedan `merged_articles`, los 15 artículos seleccionados `ALC1737-art-000614`–`000628` quedan enlazados a evidencia estructural, permanecen 34 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; p.175 tiene 35 candidatos (20 izquierda, 15 derecha) y abre fresco con `Tarde. Cuſte.`;\n- las páginas **175–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in r
r=r.replace(old,new,1)
readme.write_text(r,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
s=s.replace('Las páginas **145–162 tienen reconciliación completa de sus candidatos canónicos**','Las páginas **145–174 tienen reconciliación completa de sus candidatos canónicos**',1)
marker='## Próximo frente'
assert marker in s
section='''## Página 174 — reconciliación conservadora completada\n\nP.174 contiene **48 candidatos: 26 izquierda y 22 derecha**, todos clasificados **`article`**. Se documentan tres missed-starts seleccionados: `000614` (`Si, adv. para afirmar. Hebui.`) en el borde superior antes de L-001, `000623` (`Socorrer. Buſca ayudar.`) dentro de L-013 y `000628` (`Soplar. Apuña.`) dentro de L-024. L-013 y L-024 quedan `merged_articles` por esos comienzos internos seleccionados; R-001, R-006, R-011 y R-012 quedan también `merged_articles` por múltiples unidades guía visibles en el OCR, pero las unidades internas no seleccionadas no se promocionan ni se añaden al censo sin ancla independiente.\n\nLos 15 seleccionados `ALC1737-art-000614`–`000628` quedan enlazados a evidencia estructural mediante 14 candidatos más el missed-start superior. Quedan **34 `pending_promotion`**, no hubo promociones y el corpus sigue en **1,045 artículos**. El mínimo sustentado es **51 comienzos visibles conocidos** y no se calculan métricas por falta de censo exhaustivo. P.175 tiene **35 candidatos: 20 izquierda y 15 derecha** y abre fresco con `ALC1737-art-000629` (`Tarde. Cuſte.`) alineado a L-001; no se afirma continuidad p.174→175.\n\n'''
assert '## Página 174 — reconciliación conservadora completada' not in s
s=s.replace(marker,section+marker,1)
s=s.replace('y en p.173, **29 `pending_promotion`**. Las páginas 145–173 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.','y en p.173, **29 `pending_promotion`**; y en p.174, **34 `pending_promotion`**. Las páginas 145–174 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.',1)
oldfront='El siguiente frente geométrico es la **página digital 174**, con **48 candidatos canónicos: 26 izquierda y 22 derecha**. La capa seleccionada comienza con `ALC1737-art-000614` (`Si, adv. para afirmar. Hebui.`), comienzo superior sin frontera propia antes de L-001 (`Si, conj. Soc.`). Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
newfront='El siguiente frente geométrico es la **página digital 175**, con **35 candidatos canónicos: 20 izquierda y 15 derecha**. La capa seleccionada comienza con `ALC1737-art-000629` (`Tarde. Cuſte.`), alineado al primer candidato L-001; el borde p.174→175 es fresco. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert oldfront in s
s=s.replace(oldfront,newfront,1)
p.write_text(s,encoding='utf-8')
