# Verbos irregulares y cierre de la Parte III

## Alcance

El apartado `VERBOS IRREGULARES` comienza en la página digital 103 / impresa 89 con la regla 285 y llega hasta la regla 291 en la porción superior de la página digital 105 / impresa 91. CHD representa seis grupos verbales en [`data/grammar/irregular_verbs_part_iii_p103_p105.jsonl`](../data/grammar/irregular_verbs_part_iii_p103_p105.jsonl), conforme a [`schemas/irregular-verb.schema.json`](../schemas/irregular-verb.schema.json).

## Criterio de la fuente

La regla 285 llama irregulares a estos verbos porque, en las significaciones seleccionadas por el gramático, no presentan todos los tiempos o recurren a suplencia. CHD conserva esa definición histórica y no presupone que coincida con un concepto morfológico moderno de irregularidad.

## Grupos registrados

- regla 286: `catec / to`, glosado `eſtar`, con futuro e imperativo suplidos según la fuente;
- regla 287: formas para `eſtar en pie`, distribuidas por singular/plural y con restricciones de futuro/imperativo;
- regla 288: `voca / toca`, `eſtar acoſtado`;
- regla 289: `ſime / ſica / ſaca / ſaba`, `ir`;
- regla 290: `ietſa / iſa`, `llegar`, cuyo paradigma cruza de p. 104 a p. 105 y carece de imperativo según el impreso;
- regla 291: `ueie / cate`, `ir, ó venir`, donde la propia fuente contrapone una afirmación normativa sobre ausencia de perfecto/futuro con el uso que atribuye a `los Indios`.

## Segunda frontera intra-página

La página digital **105 / impresa 91** es materialmente mixta. Su parte superior conserva el encabezado `CAHITA. PARTE III.`, termina las reglas 290–291 y cierra el bloque de verbos irregulares. Más abajo aparece `IV. ULT. PARTE`, seguido por `PREPOSICIONES, ADVERBIOS, INTERJECCIONES, y conjunciones` y el inicio de la regla 292.

Esta frontera se modela explícitamente en `data/source/alc1737/sections.json` y `data/transcription/pages/ALC1737_p105.json`. No se fuerza una división artificial entre páginas.

## Autoridad

Los paradigmas actuales son IA-asistidos. Las celdas dudosas permanecen sin reconstruir y ningún objeto está marcado como `human_verified`.
