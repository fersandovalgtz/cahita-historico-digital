# Preposiciones históricas de la Parte IV

## Alcance inicial

La Parte IV comienza dentro de la página digital 105 / impresa 91. La regla 292 formula una caracterización general de las preposiciones de la lengua y afirma que se posponen al nombre con el que se juntan. Las páginas digitales 106–111 / impresas 92–97 permiten ya observar suficiente variación para fijar una primera microestructura estable de datos.

CHD representa las entradas iniciales en [`data/grammar/prepositions_part_iv_p105_p111.jsonl`](../data/grammar/prepositions_part_iv_p105_p111.jsonl), conforme a [`schemas/preposition-entry.schema.json`](../schemas/preposition-entry.schema.json).

## Microestructura adoptada

Cada entrada separa:

- forma o formas del encabezado histórico (`headwordRaw`);
- páginas y reglas de procedencia;
- modo de unión indicado por el gramático;
- régimen/caso formulado por la fuente;
- alternancias morfofonológicas descritas históricamente;
- sentidos numerados en el orden del impreso;
- comparación latina cuando aparece (`ad`, `in`, `cum`, `ante`, `erga`, `apud`, `iuxta`, `coram`, etc.);
- ejemplos históricos;
- juicios de uso del autor, cuando los hay;
- estado de autoridad y advertencias editoriales.

Esta arquitectura evita reducir cada preposición a una traducción única y conserva la polisemia y la metalengua gramatical de 1737.

## Entradas estructuradas

El primer lote contiene 12 entradas o grupos: `ui`, `tzi`, `ye`, `maque`, `patzi / vepatzi`, `veuatzi`, `veuitzi`, `uaam`, `uaasi`, `velecana`, `vinavo / vinatzaua` y `uaitana / uanavo`.

La fuente combina en estas entradas valores espaciales, instrumentales, comitativos, causales, atributivos y discursivos. CHD no reasigna todavía estos sentidos a roles semánticos modernos: conserva primero la organización y las comparaciones latinas del *Arte*.

## Juicios de uso

En la regla 299, al tratar `maque`, la fuente señala que algunos hablantes usan un caso oblicuo y califica ese uso como `no es pulido lenguaje`. CHD conserva esta valoración únicamente como evidencia sociolingüística/metalingüística histórica; no la adopta como juicio normativo propio.

## Incidencia de numeración

Tras la continuación de `ui` en la página digital 107, el siguiente número visible ante `TZI` es **295**. En la inspección actual no se ha localizado un **294** inequívoco. CHD no inventa la regla ausente: registra una posible omisión tipográfica o una segmentación todavía no identificada y mantiene la incidencia abierta para segunda colación.

## Estado

Las entradas son IA-asistidas y se mantienen en `unresolved` cuando una forma, ejemplo o frontera de sentido requiere segunda colación. `uaitana / uanavo` permanece abierta porque la regla 309 continúa en la página digital 112.
