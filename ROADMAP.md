# Hoja de ruta

## Fase 0 — Infraestructura científica

**Estado:** completada para la etapa inicial.

Se establecieron registro de fuente y procedencia, política de autoría, criterios editoriales, metadatos de citación, licencias, contratos de datos, documentación de riesgos y una arquitectura explícita de evidencia.

**Criterio de salida alcanzado:** el repositorio es auditable y dispone de infraestructura suficiente para procesar `ALC1737` sin confundir fuente, OCR, transcripción e inferencia.

## Fase 1 — Ingestión de `ALC1737`

**Estado:** completada el 15 de agosto de 2026.

Resultados fijados:

- SHA-256 de los dos archivos de trabajo;
- manifiesto de las 182 páginas digitales;
- segmentación macro del volumen;
- mapeo completo digital 15–132 ↔ impresa 1–118;
- identificación de preliminares, cuatro partes gramaticales, vocabulario, numerales y finales materiales;
- registro de la fe de erratas histórica;
- OCR bruto regenerable y verificable por hash;
- scripts de ingestión reproducible;
- política de empaquetado para diferenciar datos curatoriales y derivados reconstruibles.

**Criterio de salida alcanzado:** las unidades procesadas pueden remontarse a una página digital concreta y el cuerpo paginado dispone además de referencia impresa estable.

## Fase 2 — Transcripción histórico-digital

**Estado:** activa.

Objetivos:

- producir transcripción diplomática por página;
- corregir OCR contra facsímil sin modernizar ortografía;
- marcar lecturas inciertas;
- cuantificar cobertura y estados de revisión;
- mantener cola explícita de casos no resueltos;
- distinguir transcripción IA-asistida, corrección editorial y eventual revisión humana independiente.

Trabajo ya iniciado:

- convenciones de transcripción fijadas;
- piloto diplomático IA-asistido sobre página digital 134;
- diagnóstico OCR estratificado en seis zonas del volumen.

**Criterio de salida:** cobertura completa de la fuente con métricas transparentes y sin falsas declaraciones de validación humana.

## Fase 3 — Corpus lexicográfico

**Estado:** piloto iniciado en paralelo; no existe todavía corpus de producción.

Trabajo ya realizado:

- reconstrucción reproducible de las dos columnas del vocabulario;
- 3,899 líneas OCR/layout extraídas localmente en pp. 133–177;
- 1,680 candidatos conservadores de límites de artículo;
- muestra auditable de 38 candidatos de p. 134;
- 12 entradas piloto estructuradas y validadas por JSON Schema, todas `machine_corrected_unverified`.

Pendientes:

- revisar y corregir fronteras de candidatos;
- asignar identificadores persistentes sólo a entradas promovidas;
- extraer lema castellano, forma(s) cahíta(s), notas y referencias de página;
- modelar remisiones como `Busca`, abreviaturas y artículos multilínea;
- distinguir variantes explícitamente atribuidas a Hiaqui, Mayo o Thehueco;
- conservar relaciones uno-a-muchos y muchos-a-uno;
- publicar CSV y JSON reproducibles del corpus ya curado.

**Criterio de salida:** vocabulario estructurado reconstruible desde la transcripción y la procedencia, con cobertura y estados de revisión explícitos.

## Fase 4 — Gramática y ejemplos

**Estado:** pendiente.

- segmentar reglas y ejemplos;
- identificar formas lingüísticas y traducciones;
- indexar fenómenos descritos por el impreso;
- estudiar la organización interna de las partes;
- documentar la discrepancia `tripartita` / `cuatro partes`;
- preparar concordancias y búsquedas de formas.

## Fase 5 — Interoperabilidad

**Estado:** pendiente.

- definir perfil TEI para la edición;
- evaluar TEI Lex-0 para la proyección del vocabulario;
- construir esquema JSON estable;
- preparar IIIF si las condiciones del facsímil lo permiten;
- añadir metadatos FAIR y evaluación de reproducibilidad;
- generar artefactos derivados desde scripts versionados.

## Fase 6 — Investigación comparativa

**Estado:** bloqueada hasta estabilizar el corpus histórico.

- comparar formas históricas con recursos modernos de yaqui y mayo;
- modelar correspondencias como **candidatos**, no como equivalencias automáticas;
- separar continuidad léxica, semejanza gráfica, traducción y cognación;
- incorporar bibliografía lingüística contemporánea y, cuando proceda, colaboración especializada.

## Fase 7 — Publicación y preservación

**Estado:** pendiente.

- cerrar una release científica `v1.0.0`;
- generar metadatos finales de versión;
- conectar GitHub con Zenodo;
- acuñar DOI específico de versión y Concept DOI;
- publicar documentación de cobertura, limitaciones y procedencia;
- empaquetar derivados seleccionados como assets verificables;
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
