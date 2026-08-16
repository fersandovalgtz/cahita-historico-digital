# Modelo de paradigmas históricos — ALC1737

## Propósito

Cahíta Histórico Digital representa las tablas y secuencias paradigmáticas de *Arte de la lengua cahita* (1737) como objetos históricos trazables, no como paradigmas modernos reconstruidos.

El esquema maestro es [`schemas/grammatical-paradigm.schema.json`](../schemas/grammatical-paradigm.schema.json). Los primeros objetos se encuentran en [`data/grammar/paradigms_part_iii_p070_p071.jsonl`](../data/grammar/paradigms_part_iii_p070_p071.jsonl).

## Unidad de análisis

Un paradigma conserva como mínimo:

- páginas digitales e impresas;
- etiqueta o encabezado tal como lo organiza la fuente;
- lema histórico cuando existe;
- tipo de paradigma;
- celdas con etiquetas gramaticales históricas;
- forma documental;
- denominación histórica de variedad, cuando la fuente la proporciona;
- estado de lectura de cada celda;
- procedencia y autoridad editorial.

La celda es la unidad mínima de una tabla o secuencia paradigmática. No se promueve una forma a `readable` cuando el facsímil no permite una lectura suficientemente segura.

## Separación de capas

CHD distingue:

1. **estructura documental de 1737**: encabezados, voces, tiempos, personas, números y denominaciones tal como aparecen;
2. **estructuración CHD**: transformación de esa evidencia en celdas y relaciones máquina-legibles;
3. **análisis lingüístico moderno**: interpretación posterior, siempre separada.

Por ello, etiquetas como `preterito imperfecto`, `pluſquam perfecto`, `voz passiva`, `Tehuecos`, `Hiaquis` o `Mayos` se preservan primero como categorías de la fuente.

## Primeros paradigmas

### ALC1737-par-0001

Página digital 70 / impresa 56. Conjugación de `Eria` en presente de indicativo, voz activa y voz passiva. La tabla histórica distribuye formas mediante relativos o semipronombres y contiene doce celdas modeladas.

### ALC1737-par-0002

Páginas digitales 70–71 / impresas 56–57. Comparación explícita entre `Tehuecos`, `Hiaquis` y `Mayos` en terminaciones temporales. La fuente declara:

- imperfecto: `e / n / i`;
- perfecto: `c` para todos;
- pluscuamperfecto: `cat / can / cai`;
- futuro imperfecto: `naque` para todos.

El registro incluye además celdas paradigmáticas concretas que son legibles con suficiente confianza. Las demás permanecen fuera del conjunto seguro hasta una segunda colación.

## Regla de publicación

Un paradigma puede existir con estado `machine_corrected_unverified` o `unresolved`. `human_verified` exige cotejo independiente contra el facsímil por una persona identificable. Ningún paradigma de CHD debe presentarse como reconstrucción de una variedad moderna mientras permanezca en la capa histórica.
