from pathlib import Path

readme=Path('README.md')
r=readme.read_text(encoding='utf-8')
old='- las páginas **176–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;'
new='- la página **176** tiene sus **49 candidatos canónicos reconciliados**: 49 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; se documenta `000653` (`Traer coſas largas como palo`) como falso negativo interno de L-010, L-010/R-004/R-009 quedan `merged_articles`, L-009/R-023 quedan `undersegmented`, los 15 artículos seleccionados `ALC1737-art-000644`–`000658` quedan enlazados a evidencia estructural, permanecen 34 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-023 termina con `Vn par` como reclamo y p.177 abre fresco con `Vn par. Huipalai.`;\n- la página **177** ya posee representación lexicográfica estructurada, pero su reconciliación exhaustiva sigue pendiente;'
assert old in r
r=r.replace(old,new,1)
readme.write_text(r,encoding='utf-8')

p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
s=s.replace('Las páginas **145–175 tienen reconciliación completa de sus candidatos canónicos**','Las páginas **145–176 tienen reconciliación completa de sus candidatos canónicos**',1)
marker='## Próximo frente'
assert marker in s
section='''## Página 176 — reconciliación conservadora completada\n\nP.176 contiene **49 candidatos: 26 izquierda y 23 derecha**, todos clasificados **`article`**. La inspección dirigida demuestra un missed-start seleccionado: `000653` (`Traer coſas largas como palo. Tetebe.`) está absorbido dentro de L-010 después de una voz `Trabarse`-like; su cola `...palo. Tetebe.` conserva el anclaje. L-010, R-004 (`Tuétano` + `Tuna generalmente`) y R-009 (dos voces de `Tuna`) quedan `merged_articles`; L-009 y R-023 quedan `undersegmented`, este último porque añade el reclamo `Vn par` hacia la página siguiente.\n\nLos 15 seleccionados `ALC1737-art-000644`–`000658` quedan enlazados a evidencia estructural mediante 15 candidatos. Quedan **34 `pending_promotion`**, no hubo promociones y el corpus sigue en **1,045 artículos**. El mínimo sustentado es **50 comienzos visibles conocidos** y no se calculan métricas por falta de censo exhaustivo. P.177 tiene **57 candidatos: 29 izquierda y 28 derecha** y abre fresco con `ALC1737-art-000659` (`Vn par. Huipalai.`) alineado a L-001; el `Vn par` final de p.176 se conserva como reclamo y no como inicio transpaginal.\n\n'''
assert '## Página 176 — reconciliación conservadora completada' not in s
s=s.replace(marker,section+marker,1)
s=s.replace('y en p.175, **21 `pending_promotion`**. Las páginas 145–175 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.','y en p.175, **21 `pending_promotion`**; y en p.176, **34 `pending_promotion`**. Las páginas 145–176 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.',1)
oldfront='El siguiente frente geométrico es la **página digital 176**, con **49 candidatos canónicos: 26 izquierda y 23 derecha**. La capa seleccionada comienza con `ALC1737-art-000644` (`Tortuga. Mochic.`), alineado al primer candidato L-001; el `Tor-` final de p.175 se conserva como reclamo y el borde p.175→176 es fresco. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
newfront='El siguiente y último frente geométrico del Vocabulario es la **página digital 177**, con **57 candidatos canónicos: 29 izquierda y 28 derecha**. La capa seleccionada comienza con `ALC1737-art-000659` (`Vn par. Huipalai.`), alineado al primer candidato L-001; el `Vn par` final de p.176 se conserva como reclamo y el borde p.176→177 es fresco. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.'
assert oldfront in s
s=s.replace(oldfront,newfront,1)
p.write_text(s,encoding='utf-8')
