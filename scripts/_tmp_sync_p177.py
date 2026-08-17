from pathlib import Path

# README: close p177 and remove stale geometric-front prose.
readme=Path('README.md')
r=readme.read_text(encoding='utf-8')
old='- la página **177** ya posee representación lexicográfica estructurada, pero su reconciliación exhaustiva sigue pendiente;'
new='- la página **177** tiene sus **57 candidatos canónicos reconciliados**: 57 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; L-008/L-029 quedan `merged_articles`, L-014/R-019 conservan frontera `ambiguous` sin lema inventado y R-008/R-028 quedan `undersegmented`; los 15 artículos seleccionados `ALC1737-art-000659`–`000673` quedan enlazados a fronteras propias, no se documentan falsos negativos seleccionados, permanecen 42 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; p.177 termina el Vocabulario y p.178–180 corresponden al sistema numeral histórico;\n- con p.177, las **45 páginas del Vocabulario (133–177)** tienen reconciliación de candidatos completa; **pp.133–144** siguen siendo el único tramo técnicamente cerrado, mientras **pp.145–177** permanecen abiertos para censo exhaustivo y promoción/enlace;'
assert old in r
r=r.replace(old,new,1)
start='## Próximo frente científico\n\n'
end='\n\n## Cita'
assert start in r and end in r
before,rest=r.split(start,1)
_,after=rest.split(end,1)
front=('La reconciliación geométrica de candidatos del Vocabulario está completa en **pp.133–177 (45/45 páginas)**. '
       'El siguiente frente científico vuelve a **p.145** para completar, página por página, el **censo exhaustivo de inicios visibles** y la **promoción/enlace** de fronteras todavía sustentadas sólo por geometría/OCR. '
       'Ese trabajo debe conservar la política vigente: no promocionar lecturas OCR-only sin evidencia suficiente, mantener `humanVerified=false`, localizar explícitamente los candidatos `unresolved` y no calcular precisión/recall/F1 en páginas cuyo denominador visible siga sin ser exhaustivo.\n\n'
       'El corpus curatorial permanece en **1,045 artículos estructurados**. La finalización de la reconciliación de candidatos no cambia por sí sola ese conteo ni convierte pp.145–177 en páginas técnicamente cerradas.')
r=before+start+front+end+after
readme.write_text(r,encoding='utf-8')

# Progress document: close candidate-reconciliation coverage but keep closure distinction explicit.
p=Path('docs/LEXICON_PROGRESS.md')
s=p.read_text(encoding='utf-8')
s=s.replace('## Estado — 2026-08-16','## Estado — 2026-08-17',1)
s=s.replace('Las páginas **145–176 tienen reconciliación completa de sus candidatos canónicos**','Las páginas **145–177 tienen reconciliación completa de sus candidatos canónicos**',1)
marker='## Próximo frente'
assert marker in s
section='''## Página 177 — reconciliación conservadora completada\n\nP.177 contiene **57 candidatos: 29 izquierda y 28 derecha**, todos clasificados **`article`**. Los 15 seleccionados `ALC1737-art-000659`–`000673` tienen frontera canónica propia: no se documentan missed-starts seleccionados ni continuaciones físicas. **L-008** (`Valor` + una voz `Vana eſtar la fruta`-like) y **L-029** (`Veneno` + `Venenoso ſer`-like) quedan `merged_articles`. **L-014** y **R-019** conservan evaluación `ambiguous`: la geometría sustenta un comienzo, pero el OCR es demasiado corrupto para recuperar responsablemente el lema. **R-008** y **R-028** quedan `undersegmented`; R-028 comienza `Vomitar` y arrastra únicamente residuo terminal `*Z`, sin continuidad léxica posterior.\n\nQuedan **42 `pending_promotion`**, no hubo promociones y el corpus permanece en **1,045 artículos**. Los **57 candidatos de artículo** establecen el mínimo conservador de comienzos visibles conocidos, pero las regiones `merged_articles`/`undersegmented` pueden ocultar unidades internas no ancladas y la capa seleccionada no es exhaustiva; por ello no se calculan TP/FP/FN, precisión, recall ni F1.\n\nP.177 constituye el **borde terminal del Vocabulario**. `export_candidate_page.py --page 178 --count-only` devuelve **0** candidatos lexicográficos, y la documentación de cobertura fija el sistema numeral histórico en **pp.178–180**. Por tanto no se afirma continuidad léxica desde R-028 hacia p.178. Con esta página queda **completa la reconciliación de candidatos de las 45 páginas del Vocabulario, pp.133–177**. Esta cobertura no equivale a cierre técnico integral: pp.133–144 siguen siendo el único tramo con censo visible exhaustivo y promoción/enlace cerrados; pp.145–177 continúan abiertos en esas dos dimensiones.\n\n'''
assert '## Página 177 — reconciliación conservadora completada' not in s
head,_=s.split(marker,1)
s=head+section+'''## Próximo frente\n\nLa **reconciliación de candidatos del Vocabulario está completa en pp.133–177 (45/45 páginas)**. El siguiente frente ya no es geométrico: debe retomar **p.145** y avanzar secuencialmente en **censo exhaustivo de inicios visibles** y **promoción/enlace** de las fronteras pendientes, preservando las incertidumbres estructurales existentes.\n\nEn p.177 quedan **42 `pending_promotion`**. En el conjunto pp.145–177 persisten fronteras pendientes y algunos candidatos estructuralmente `unresolved`; por ello esas páginas no deben describirse como técnicamente cerradas. La regla sigue siendo no promover artículos desde OCR-only sin evidencia suficiente y no calcular métricas cuando el denominador visible no sea exhaustivo.\n\nEl corpus continúa publicando **1,045 artículos históricos estructurados** y **pp.133–144** como último tramo técnicamente cerrado. La siguiente fase puede aumentar el corpus sólo cuando una promoción concreta esté suficientemente sustentada y trazada.\n'''
p.write_text(s,encoding='utf-8')
