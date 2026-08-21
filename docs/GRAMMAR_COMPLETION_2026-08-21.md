# Cierre técnico de la cobertura gramatical — 21 de agosto de 2026

## Alcance del hito

El 21 de agosto de 2026, Cahíta Histórico Digital alcanzó el **cierre técnico de la cobertura de las unidades gramaticales numeradas** del _Arte de la lengua cahita_ de 1737 (`ALC1737`). Este hito significa que toda unidad numerada efectivamente impresa en la secuencia 1–373 dispone de una reclamación estructurada explícita en `data/grammar/`, con procedencia hacia las páginas del testimonio y estados de revisión visibles.

Este cierre **no equivale a validación filológica humana**, edición crítica definitiva ni release científica estable. Todos los objetos permanecen con `humanVerified=false`; las lecturas inseguras continúan marcadas como `machine_corrected_unverified` o `unresolved` según corresponda.

## Resultado cuantitativo

La auditoría reproducible ejecutada por `scripts/validate_grammar_exports.py` después del cierre produjo:

- **370 / 373 números nominales** con reclamación estructurada explícita;
- **3 números nominales sin reclamación**: 127, 178 y 294;
- **302 objetos gramaticales** distribuidos en 24 archivos;
- **1,215 filas de evidencia explícita** en la concordancia derivada;
- **0 objetos `humanVerified=true`**;
- doble ejecución determinista de la concordancia y de la auditoría de cobertura.

Los tres números sin reclamación no representan trabajo estructural pendiente: corresponden a **omisiones materiales de numeración en el impreso**.

## Anomalías de numeración preservadas

La secuencia nominal 1–373 presenta cuatro incidencias editoriales relevantes:

1. **127 omitido**: el impreso pasa de 126 a 128 en la página digital 52.
2. **129 duplicado**: la misma página imprime dos reglas sucesivas con el número 129; CHD conserva dos objetos diferenciados y no renumera silenciosamente la segunda unidad.
3. **178 omitido**: el impreso pasa de 177 a 179 en la página digital 66.
4. **294 omitido**: la regla 293 continúa de la página digital 106 a la 107 y el siguiente número visible es 295.

Por ello, la secuencia nominal contiene **370 números efectivamente impresos distintos**. Al contar las dos unidades diferentes impresas como 129, el testimonio contiene **371 unidades numeradas efectivas**. CHD representa **371 / 371** de esas unidades.

Las incidencias se registran en:

- `data/grammar/metadata/rule_numbering_anomalies_p052.json`;
- `data/grammar/metadata/rule_numbering_anomalies_p066.json`;
- `data/grammar/metadata/rule_numbering_anomalies_p107.json`;
- `data/grammar/metadata/rule_numbering_closure.json`.

## Qué significa «cierre técnico»

El cierre técnico de numeración establece que:

- no queda ninguna unidad numerada realmente impresa sin representación estructurada;
- las relaciones entre objetos y números se apoyan en localizadores explícitos, no en proximidad inferida;
- las reglas que cruzan páginas conservan todos sus `sourcePagesDigital` y `sourcePagesPrinted` pertinentes;
- las anomalías materiales se modelan como anomalías, no mediante reglas inventadas;
- los objetos temáticos que agrupan varios números siguen siendo válidos: el número de objetos gramaticales no tiene que coincidir con el número de reglas impresas;
- toda incertidumbre de lectura que no puede resolverse con seguridad permanece expuesta.

## QA y reproducibilidad

La corrida integral que confirmó el cierre informó:

- cobertura: `370/373`;
- uncovered: `3`;
- gap ranges: `3`;
- concordancia: `302 objects / 1,215 evidence rows`;
- SHA-256 del manifiesto de auditoría de cobertura: `56b33f61acb3e9429ed82d3cfdb7477e9f29edcf4c41b2b833971b8397ea2251`;
- SHA-256 del CSV de cobertura: `8b91f800e69416689f9bfd7768264db7fd8ffe0c97984698b45f5d204641270d`;
- SHA-256 del JSONL de cobertura: `bb0121fe2cf4f4d8742fa7b1ff03662285132ea81bd0c644628cc9803dea25ad`;
- SHA-256 del JSON de rangos de huecos: `82b4e329f0e7e3ea667dcbf6419cc92f133e465b28ce2c7c2734121b0bceba6e`;
- SHA-256 del CSV de concordancia: `b7076dfcdd6486bf747fd8452773c728c2d638e0803a1ccadac9086c18d7d1fb`;
- SHA-256 del JSONL de concordancia: `22e795a935eea9d4db832e96fae09ab46dd87982a1366aa616ca76d32ce33681`.

Una corrida verde certifica consistencia computacional del estado versionado. No certifica que cada forma cahíta haya sido validada independientemente por un especialista humano.

## Trabajo que permanece abierto

El cierre de cobertura desplaza el frente gramatical desde «localizar y estructurar reglas faltantes» hacia tareas de mayor resolución:

- segunda colación de formas y ejemplos actualmente `unresolved`;
- consolidación de observaciones históricas de variedad (`Hiaqui`, `Mayo`, `Thehueco`, `Naciones` y otras etiquetas explícitas);
- enlaces reproducibles entre reglas, paradigmas, ejemplos y observaciones de variedad;
- control textual con testimonios independientes cuando estén disponibles y sean metodológicamente apropiados;
- perfil TEI y otros derivados interoperables sin alterar la capa canónica;
- preparación de una futura release científica con limitaciones, autoridad y procedencia explícitas.

## Principio editorial aplicado

Este hito mantiene el principio central de CHD: **preservar primero; estructurar después; inferir sólo en capas explícitas; mantener toda incertidumbre visible y trazable**.
