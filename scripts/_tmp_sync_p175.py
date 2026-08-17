from pathlib import Path

readme=Path('README.md')
r=readme.read_text(encoding='utf-8')
old='- las páginas **175–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **175** tiene sus **35 candidatos canónicos reconciliados**: 35 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; se documentan 3 falsos negativos seleccionados (`000637` `Tener con las manos`, `000640` `Tentar con las manos`, `000643` `Tocar`), L-012/L-014/L-020/R-007/R-015 quedan `merged_articles`, los 15 artículos seleccionados `ALC1737-art-000629`–`000643` quedan enlazados a evidencia estructural, permanecen 21 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-015 termina con un `Tor-` de reclamo y p.176 abre fresco con `Tortuga. Mochic.`;\n- las páginas **176–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
assert old in r
r=r.replace(old,new,1)
readme.write_text(r,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
s=s.replace('Las páginas **145–174 tienen reconciliación completa de sus candidatos canónicos**','Las páginas **145–175 tienen reconciliación completa de sus candidatos canónicos**',1)
marker='## Próximo frente'
assert marker in s
section='''## Página 175 — reconciliación conservadora completada\n\nP.175 contiene **35 candidatos: 20 izquierda y 15 derecha**, todos clasificados **`article`**. La inspección dirigida de la región dañada L-012–L-014 permite sostener tres missed-starts seleccionados: `000637` (`Tener con las manos. Buſca agarrar.`) dentro de L-012, `000640` (`Tentar con las manos. Buſca palpar.`) dentro de L-014 tras `000639` (`Tener ſed`), y `000643` (`Tocar. Buſca palpar.`) dentro de R-007 tras `Tizón`. L-012, L-014, L-020, R-007 y R-015 quedan `merged_articles`; las unidades internas OCR-only no se promocionan ni se añaden al mínimo sin ancla independiente.\n\nLos 15 seleccionados `ALC1737-art-000629`–`000643` quedan enlazados a evidencia estructural mediante 14 candidatos. Quedan **21 `pending_promotion`**, no hubo promociones y el corpus sigue en **1,045 artículos**. El mínimo sustentado es **38 comienzos visibles conocidos** y no se calculan métricas por falta de censo exhaustivo. R-015 termina con un `Tor-` de reclamo después de varias unidades Tordo/Tortuga; p.176 tiene **49 candidatos: 26 izquierda y 23 derecha** y abre fresco con `ALC1737-art-000644` (`Tortuga. Mochic.`) alineado a L-001, por lo que no se afirma continuidad p.175→176.\n\n'''
assert '## Página 175 — reconciliación conservadora completada' not in s
s=s.replace(marker,section+marker,1)
s=s.replace('y en p.174, **34 `pending_promotion`**. Las páginas 145–174 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.','y en p.174, **34 `pending_promotion`**; y en p.175, **21 `pending_promotion`**. Las páginas 145–175 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.',1)
oldfront='El siguiente frente geométrico es la **página digital 175**, con **35 candidatos canónicos: 20 izquierda y 15 derecha**. La capa seleccionada comienza con `ALC1737-art-000629` (`Tarde. Cuſte.`), alineado al primer candidato L-001; el borde p.174→175 es fresco. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
newfront='El siguiente frente geométrico es la **página digital 176**, con **49 candidatos canónicos: 26 izquierda y 23 derecha**. La capa seleccionada comienza con `ALC1737-art-000644` (`Tortuga. Mochic.`), alineado al primer candidato L-001; el `Tor-` final de p.175 se conserva como reclamo y el borde p.175→176 es fresco. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert oldfront in s
s=s.replace(oldfront,newfront,1)
p.write_text(s,encoding='utf-8')
