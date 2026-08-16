# Evidencia explícita de variación histórica en ALC1737

## Propósito

Este documento reúne pasajes en los que *Arte de la lengua cahita* (1737) atribuye explícitamente una forma, terminación, contraste, preferencia o modo de hablar a denominaciones históricas. CHD conserva esas categorías como **datos del impreso**, no como clasificación lingüística moderna.

Los registros máquina-legibles están en [`data/linguistic/variety_observations.jsonl`](../data/linguistic/variety_observations.jsonl) y su contrato en [`schemas/historical-variety-observation.schema.json`](../schemas/historical-variety-observation.schema.json).

## Principio de autoridad

CHD diferencia cuatro niveles:

1. denominación literal de la fuente;
2. fenómeno tal como lo formula el gramático de 1737;
3. estructuración editorial de CHD;
4. comparación histórica o moderna posterior.

Los niveles 3 y 4 nunca sustituyen los dos primeros. Una etiqueta histórica no se convierte automáticamente en taxón moderno, y una semejanza formal no se registra como cognación, continuidad o identidad sin evidencia adicional.

## Diez observaciones estructuradas actualmente

### 1. Página 11 — Hiaquis, Mayes y Thehuecos

`Al lector` agrupa a `Hiaquis`, `Mayes` y `Thehuecos` dentro de lo que denomina un mismo `Idioma`, pero afirma simultáneamente que se diferencian en el `modo de hablar`. CHD conserva ambas afirmaciones: **unidad declarada + diferencia de uso**.

### 2. Página 19 / impresa 5 — futuro atribuido a los Mayos

La regla 20 señala que, frente a la sustitución general de `ſe` por `h` antes de `naque`, `los Mayos` no usan esa `h` y pierden la `e`. El texto ejemplifica con `Buaſe → buaſnaque` y `tuſe → tuſnaque`.

### 3. Página 37 / impresa 23 — `Teueco` y la alternancia ſ/h

La regla 79 afirma que en muchos partidos se convierte `ſ` en `h` en determinado contexto medial. Dentro de esa explicación contrasta expresamente `tuſi → tuſta` en `Teueco` con otras realizaciones, y ofrece además `hioſte, vel hiohte`.

### 4. Página 39 / impresa 25 — inserción de `i` más usada en Teueco

La regla 88 describe la interposición de una `i` entre vocales y añade de manera explícita: `Eſto es mas vſado en Teueco`. CHD registra la atribución de frecuencia, sin convertirla todavía en regla fonológica moderna.

### 5. Página 40 / impresa 26 — Hiaquis, Teuecos y Mayos en el `accento`

Al tratar las synalephas, la fuente declara que no puede darse una regla única porque los mismos vocablos son pronunciados por `los Hiaquis breves`, `los Teuecos largos` y por `los Mayos vnos breves, y otros largos`. `Breve`, `largo` y `accento` permanecen como categorías metalingüísticas del impreso.

### 6. Página 49 / impresa 35 — `los Cynaloas`

La regla 119 afirma que `Los Cynaloas vſan mucho del accuſativo netzi` y advierte que quien escucha puede confundirlo con dativo. El ejemplo `netzavuriac` se conserva como forma documental. `Cynaloas` se incorpora así al inventario de denominaciones históricas relevantes para la variación descrita por el *Arte*.

### 7. Página 52 / impresa 38 — Tehuecos frente a Hiaqui y Mayo

La regla 128 contrasta la formación del oblicuo de nombres terminados en `ſi` y `ſo`. El impreso atribuye a `Tehuecos` formas como `tuſta` y `maſta`, mientras que para `Hiaqui, y Mayo` presenta `tuhta` y `mahta`, explicándolo como sustitución por `h` antes de `ta`.

### 8. Página 53 / impresa 39 — `Hiaqui ſuaue`

En la Segunda Declinación aparece `paros la liebre`, acompañado de la nota `aſſi la llaman los Mayos, y el Hiaqui ſuaue`. Además de la atribución léxica, la etiqueta histórica `Hiaqui ſuaue` se conserva literalmente como objeto de estudio; CHD no presupone qué entidad dialectal moderna le corresponde.

### 9. Página 70 / impresa 56 — terminaciones temporales comparadas

El *Arte* distribuye terminaciones entre tres denominaciones:

- pretérito imperfecto: `Tehuecos = e`, `Hiaquis = n`, `Mayos = i`;
- perfecto: todos en `c`;
- pluscuamperfecto: `Tehuecos = cat`, `Hiaquis = can`, `Mayos = cai`;
- futuro imperfecto: todos en `naque`.

Es uno de los pasajes comparativos más densos del volumen.

### 10. Página 71 / impresa 57 — paradigma por variedad

La página siguiente lleva el contraste a un paradigma concreto, con formas identificadas como `El Hiaqui`, `El Mayo` y `el Tehueco`, y vuelve a declarar `cat / can / cai` para Tehuecos, Hiaquis y Mayos respectivamente.

## Consecuencia científica

La capa ya no puede considerarse una colección incidental de notas. El impreso contiene un **sistema distribuido de observaciones comparativas históricas** que abarca al menos:

- agrupación metalingüística;
- variación léxica;
- morfología y formación de caso;
- morfofonología;
- realización descrita en términos de `accento`, `breve` y `largo`;
- preferencias de uso atribuidas a grupos o regiones;
- paradigmas verbales comparados.

Esto justifica un producto científico independiente: un **corpus de evidencia de variación cahíta histórica**, siempre anclado en página, regla, forma fuente, denominación literal, estado de revisión y procedencia.

## Próxima etapa

La búsqueda deberá extenderse a todas las variantes gráficas de `Hiaqui`, `Mayo/Mayes`, `Thehueco/Tehueco`, `Cynaloa/Cynaloas` y cualquier otra denominación que el volumen utilice comparativamente. Cada coincidencia se cotejará contra facsímil; la ausencia en OCR nunca se considerará evidencia suficiente de ausencia en el impreso.

**Estado:** 10 observaciones estructuradas, `machine_corrected_unverified`; sin revisión humana independiente.
