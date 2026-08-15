# Hoja de ruta

## Fase 0 — Infraestructura científica

**Estado:** en curso.

Objetivos:

- registrar la fuente y su procedencia;
- fijar política de autoría y criterios editoriales;
- establecer metadatos de citación y licencias;
- definir contratos de datos;
- documentar límites y riesgos del proyecto.

Criterio de salida: repositorio auditable y preparado para ingestión reproducible.

## Fase 1 — Ingestión de `ALC1737`

- registrar checksums de los archivos de trabajo;
- construir manifiesto de 182 páginas digitales;
- conservar OCR bruto;
- separar preliminares, gramática, vocabulario y numerales;
- mapear páginas digitales con la paginación impresa cuando sea posible;
- registrar erratas declaradas por el propio impreso.

Criterio de salida: cada fragmento textual debe poder remontarse a una página concreta del testimonio.

## Fase 2 — Transcripción histórico-digital

- producir transcripción diplomática por página;
- corregir OCR contra facsímil sin modernizar ortografía;
- marcar lecturas inciertas;
- cuantificar cobertura y estados de revisión;
- mantener cola explícita de casos no resueltos.

Criterio de salida: cobertura completa de la fuente con métricas transparentes y sin falsas declaraciones de validación humana.

## Fase 3 — Corpus lexicográfico

- segmentar el vocabulario castellano–cahíta;
- asignar identificadores persistentes a entradas;
- extraer lema castellano, forma(s) cahíta(s), notas y referencias de página;
- distinguir variantes explícitamente atribuidas a Hiaqui, Mayo o Thehueco;
- conservar relaciones uno-a-muchos y muchos-a-uno;
- publicar CSV y JSON reproducibles.

Criterio de salida: vocabulario estructurado que pueda reconstruirse desde la transcripción y el manifiesto de procedencia.

## Fase 4 — Gramática y ejemplos

- segmentar reglas y ejemplos;
- identificar formas lingüísticas y traducciones;
- indexar fenómenos descritos por el impreso;
- estudiar la organización interna de las partes;
- documentar la discrepancia `tripartita` / `cuatro partes`;
- preparar concordancias y búsquedas de formas.

## Fase 5 — Interoperabilidad

- definir perfil TEI para la edición;
- evaluar TEI Lex-0 para la proyección del vocabulario;
- construir esquema JSON estable;
- preparar IIIF si las condiciones del facsímil lo permiten;
- añadir metadatos FAIR y evaluación de reproducibilidad;
- generar artefactos derivados desde scripts versionados.

## Fase 6 — Investigación comparativa

Solo después de estabilizar el corpus histórico:

- comparar formas históricas con recursos modernos de yaqui y mayo;
- modelar correspondencias como **candidatos**, no como equivalencias automáticas;
- separar continuidad léxica, semejanza gráfica, traducción y cognación;
- incorporar bibliografía lingüística contemporánea y, cuando proceda, colaboración especializada.

## Fase 7 — Publicación y preservación

- cerrar una release científica `v1.0.0`;
- generar `CITATION.cff` y metadatos finales de versión;
- conectar GitHub con Zenodo;
- acuñar DOI específico de versión y Concept DOI;
- publicar documentación de cobertura, limitaciones y procedencia;
- preparar un artículo de datos/metodología y productos derivados.

## Productos científicos previstos

CHD está diseñado para permitir, de forma acumulativa y trazable:

1. edición histórico-digital del *Arte* de 1737;
2. dataset lexicográfico abierto;
3. corpus gramatical y de ejemplos;
4. estudio de la variación histórica descrita como Hiaqui/Mayo/Thehueco;
5. artículo metodológico sobre edición computacional de lingüística misionera;
6. estudios comparativos diacrónicos posteriores;
7. modelo replicable para otras fuentes cahítas históricas.
