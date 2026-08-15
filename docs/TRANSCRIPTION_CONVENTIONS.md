# Convenciones de transcripción — ALC1737

Estas convenciones rigen la futura transcripción diplomática y la transcripción corregida de `ALC1737`. Su finalidad es impedir que modernización, corrección de OCR e interpretación filológica se mezclen en una sola capa.

## 1. Unidad de referencia

Toda transcripción debe conservar como mínimo:

- `source_id = ALC1737`;
- página digital del PDF;
- página impresa cuando corresponda;
- capa editorial;
- estado de revisión;
- agente y fecha de procesamiento.

La página digital es el ancla técnica estable. Para el cuerpo impreso numerado, páginas digitales 15–132 equivalen a páginas impresas 1–118.

## 2. Transcripción diplomática

La capa diplomática reproducirá la evidencia tipográfica visible sin modernizarla intencionalmente.

### Grafía histórica

- `ſ` se conserva como `ſ` cuando la forma es legible con seguridad.
- `s` redonda se conserva como `s`.
- `u/v`, `i/j`, `x/j`, `c/ç/z` y demás oposiciones históricas no se regularizan.
- Las mayúsculas, tildes y signos se conservan según el testimonio en la medida en que la lectura sea segura.
- No se expande una abreviatura dentro del texto diplomático. Una expansión propuesta pertenece a una capa o atributo separado.

### Saltos y guiones

- El salto de línea tipográfico puede conservarse cuando sea necesario para reconstruir el impreso o resolver una lectura.
- El guion de partición al final de línea no se elimina silenciosamente.
- Una forma partida por cambio de línea podrá tener una representación continua en la capa corregida, pero la capa diplomática conservará la evidencia de la partición.

### Caracteres inciertos e ilegibles

Se usarán marcadores explícitos, por ejemplo:

- `[?]`: carácter o secuencia no resuelta;
- `[ileg.]`: porción ilegible cuya extensión no puede determinarse con seguridad;
- `[abc?]`: lectura propuesta pero incierta.

Estos marcadores son convenciones editoriales de CHD y no forman parte del impreso.

## 3. Transcripción corregida

La capa corregida puede reparar errores comprobables del OCR **contra el facsímil**, pero mantiene la ortografía histórica. Debe conservar un vínculo con la lectura OCR de la que parte y registrar el tipo de intervención.

No son correcciones admisibles en esta capa:

- modernizar ortografía;
- traducir una forma histórica a una forma contemporánea;
- inferir una equivalencia yaqui/mayo moderna;
- resolver automáticamente una abreviatura dudosa;
- sustituir una lectura por la fe de erratas sin registrar ambas.

## 4. Fe de erratas histórica

La página digital 13 contiene `ERRATA SIC CORRIGE`. Para cada corrección histórica se conservarán tres niveles potenciales:

1. `printed_reading`: forma efectivamente impresa en el lugar señalado;
2. `historical_erratum`: corrección prescrita por el propio impreso;
3. `chd_editorial_reading`: decisión de CHD, cuando exista.

La fe de erratas no autoriza a sobrescribir el testimonio. Es una fuente histórica adicional dentro del mismo volumen.

## 5. Vocabulario

Las entradas del vocabulario deben distinguir, cuando la evidencia lo permita:

- lema o frase guía castellana tal como aparece;
- forma o formas cahítas;
- abreviaturas (`L.`, `V.`, `Ibid.` y otras);
- remisiones internas como `Busca`;
- variantes o explicaciones añadidas;
- página digital;
- orden y posición de la entrada dentro de la página.

Una segmentación automática será siempre `raw_ocr` o `machine_corrected_unverified` hasta su cotejo contra el facsímil.

## 6. Normalización

La normalización será un producto derivado para recuperación y análisis. Deberá indicar reglas aplicadas y conservar la forma histórica original. No se utilizará una forma normalizada como sustituto del texto fuente en citas filológicas.

## 7. Validación humana

`human_verified` exige cotejo explícito contra la imagen del testimonio por una persona identificable. Haber pasado por un modelo de lenguaje, corrector automático u OCR adicional no constituye validación humana independiente.
