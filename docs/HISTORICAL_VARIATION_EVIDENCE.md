# Evidencia explícita de variación histórica en ALC1737

## Propósito

Este documento reúne pasajes en los que *Arte de la lengua cahita* (1737) atribuye de manera explícita una forma, terminación, contraste o modo de hablar a denominaciones históricas como `Hiaqui`, `Mayo` y `Thehueco`. Su objetivo no es modernizar la clasificación ni resolver por anticipado relaciones dialectales contemporáneas, sino construir una capa de evidencia trazable que pueda explotarse después en estudios diacrónicos y comparativos.

Los registros máquina-legibles correspondientes se conservan en [`data/linguistic/variety_observations.jsonl`](../data/linguistic/variety_observations.jsonl) y se validarán contra [`schemas/historical-variety-observation.schema.json`](../schemas/historical-variety-observation.schema.json).

## Principio de autoridad

CHD diferencia cuatro niveles:

1. **denominación literal de la fuente**;
2. **fenómeno lingüístico tal como lo formula el gramático de 1737**;
3. **estructuración editorial de CHD**;
4. **comparación histórica o moderna posterior**.

Los niveles 3 y 4 nunca sustituyen los dos primeros. Las etiquetas históricas no se convierten automáticamente en taxones modernos, y una semejanza entre una forma de 1737 y una forma contemporánea no se registra como continuidad genética o identidad sin evidencia adicional.

## Evidencias iniciales

### Página digital 11 — `Al lector`

La fuente agrupa a `Hiaquis`, `Mayes` y `Thehuecos` dentro de lo que llama un mismo idioma y, en la misma secuencia, afirma que se diferencian en el modo de hablar. A continuación proporciona ejemplos paralelos. CHD registra esta formulación como una afirmación metalingüística histórica doble: **unidad declarada + diferencia de uso**.

Esta evidencia es especialmente importante porque impide reducir la posición del impreso a una sola categoría moderna. El propio texto sostiene simultáneamente semejanza y diversidad.

### Página digital 19 / impresa 5 — formación del futuro

En la regla 20 de la Parte I, después de describir que los verbos acabados en `ſe` mudan `ſe` en `h` para recibir `naque`, el texto introduce una excepción atribuida expresamente a `los Mayos`: indica que en algunas partes no se usa `h` en lugar de `ſe` y ejemplifica con formas como `Buaſe → buaſnaque` y `tuſe → tuſnaque`.

CHD tipa este pasaje como **variación morfofonológica atribuida por la fuente**. No se interpreta todavía como regla del mayo moderno.

### Página digital 53 / impresa 39 — `Hiaqui ſuaue`

En la Segunda Declinación aparece el ejemplo `paros la liebre`, seguido de la nota parentética `aſſi la llaman los Mayos, y el Hiaqui ſuaue`.

Este pasaje es doblemente relevante. Registra una atribución léxica explícita y, además, conserva una etiqueta interna —`Hiaqui ſuaue`— que deberá estudiarse como categoría histórica del propio testimonio. CHD no presupone qué entidad dialectal contemporánea, si alguna, corresponde exactamente a esa denominación.

### Página digital 70 / impresa 56 — terminaciones temporales comparadas

El *Arte* proporciona una regla comparativa particularmente explícita:

- pretérito imperfecto: `Tehuecos = e`, `Hiaquis = n`, `Mayos = i`;
- perfecto: todos en `c`;
- pluscuamperfecto: `Tehuecos = cat`, `Hiaquis = can`, `Mayos = cai`;
- futuro imperfecto: todos en `naque`.

Estas relaciones se conservan como valores atribuidos por el gramático, no como normalización de CHD. Constituyen uno de los núcleos principales para un futuro dataset de variación morfológica histórica.

### Página digital 71 / impresa 57 — paradigma por variedad

La página siguiente lleva la comparación a un paradigma concreto. Se distinguen formas para `El Hiaqui`, `El Mayo` y `el Tehueco`, y una nota reitera que los verbos acabados en `e` presentan `cat` para los Tehuecos, `can` para los Hiaquis y `cai` para los Mayos.

Antes de promover todas las formas paradigmáticas a datos de producción, CHD exige transcripción completa de la página y revisión de cada forma. El registro actual conserva la existencia y estructura del contraste sin fingir una validación lingüística independiente.

## Valor científico inmediato

Esta capa cambia la naturaleza del proyecto: CHD no será únicamente una edición digital y un vocabulario estructurado. La fuente contiene un **sistema interno de observaciones comparativas sobre variedades históricas**, susceptible de convertirse en un corpus independiente de evidencia dialectal de comienzos del siglo XVIII.

Un futuro producto derivado podrá organizar las observaciones por:

- nivel lingüístico: léxico, fonología/morfofonología, morfología, paradigma, sintaxis;
- denominación histórica;
- página y regla;
- forma fuente;
- glosa castellana;
- contraste explícito;
- grado de revisión;
- posible correspondencia moderna, siempre en una capa separada.

## Siguiente etapa

La búsqueda de menciones de `Hiaqui`, `Mayo`, `Mayes`, `Thehueco`, `Tehueco` y variantes gráficas deberá realizarse sobre la obra completa. Cada aparición relevante se cotejará contra facsímil antes de incorporarse al dataset. La ausencia de una coincidencia OCR no se considerará evidencia de ausencia en el impreso.

**Estado:** dataset inicial, `machine_corrected_unverified`; sin revisión humana independiente.
