# Changelog

Todos los cambios relevantes de Cahíta Histórico Digital se documentarán en este archivo.

## [0.1.1-dev] - 2026-08-15

### Añadido

- script de ingestión reproducible `scripts/ingest_alc1737.py`;
- checksums SHA-256 de los dos archivos de trabajo de `ALC1737`;
- manifiesto página por página para las **182 páginas digitales**, con sección y paginación impresa cuando existe;
- mapeo completo de las **118 páginas impresas numeradas** del cuerpo gramatical;
- documentación técnica de ingestión;
- convenciones explícitas para transcripción diplomática, corrección, `ſ`, abreviaturas, particiones de línea e incertidumbre;
- README específico de la fuente en `data/source/alc1737/`.

### Modificado

- la segmentación macro dejó de ser únicamente inferida por encabezados: sus fronteras principales fueron cotejadas visualmente en el facsímil;
- la documentación de la fuente incorpora ahora la descripción física del registro de Internet Archive/JCB y la discrepancia técnica entre el campo `Pages: 184` y el PDF de trabajo de 182 páginas;
- las métricas de cobertura distinguen OCR disponible, OCR extraído, payload versionado y transcripción filológica;
- las páginas 181–182 se identifican como finales materiales/cubierta posterior, no como una sección textual pendiente.

### Estado científico

- **0 / 182** páginas se declaran todavía como transcripción diplomática terminada;
- **0** entradas lexicográficas se promueven todavía al corpus estructurado;
- **0** unidades se etiquetan como `human_verified`.

La fase 0.1.1-dev consolida la trazabilidad técnica necesaria antes de comenzar la extracción lexicográfica y la transcripción.

## [0.1.0] - 2026-08-15

### Añadido

- definición inicial del proyecto **Cahíta Histórico Digital**;
- registro canónico de la fuente `ALC1737`;
- documentación de la fuente histórica de 1737 y de su procedencia digital;
- política explícita para tratar la autoría histórica como cuestión no resuelta;
- política editorial por capas: testimonio, OCR, transcripción, normalización y datos derivados;
- `CITATION.cff` y `codemeta.json`;
- datasheet inicial del corpus;
- esquema JSON inicial para entradas lexicográficas;
- política de licencias separada para código, datos y materiales de terceros;
- hoja de ruta para ingestión, extracción lexicográfica, interoperabilidad y futura preservación en Zenodo;
- integración documental con el ecosistema de repositorios científicos de Fernando Sandoval Gutierrez.

### Estado científico

Esta versión es **pre-release**. Registra la infraestructura y la fuente, pero no declara terminada ni validada una transcripción crítica, un vocabulario estructurado o una edición filológica completa.
