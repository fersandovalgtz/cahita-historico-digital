# Hoja de ruta

Estado de planificación de Cahíta Histórico Digital (`ALC1737`) — actualización **2026-08-21**.

## Principio rector

CHD no avanza por acumulación indiscriminada de archivos. Cada fase debe cerrar una capa de evidencia con procedencia, estados de autoridad y criterios de salida explícitos antes de que los productos finales dependan de ella.

## Fase 0 — Infraestructura científica

**Estado:** completada para la etapa de investigación activa; mantenimiento continuo.

Se establecieron registro de fuente y procedencia, política de autoría, criterios editoriales, metadatos de citación, licencias, contratos de datos, esquemas JSON, documentación de riesgos y una arquitectura explícita de evidencia. GitHub Actions valida inventarios, IDs, esquemas, reconciliaciones y resúmenes derivados.

**Mantenimiento pendiente:** ampliar CI/QA para impedir deriva entre datos, documentación y exportaciones nuevas.

## Fase 1 — Ingestión de `ALC1737`

**Estado:** completada el 15 de agosto de 2026.

Resultados fijados:

- SHA-256 de los archivos de trabajo;
- manifiesto de las 182 páginas digitales;
- segmentación macro del volumen;
- mapeo completo digital 15–132 ↔ impresa 1–118;
- preliminares, cuatro partes gramaticales, vocabulario, numerales y finales materiales identificados;
- fe de erratas histórica registrada;
- OCR bruto regenerable y verificable por hash;
- scripts de ingestión reproducible.

## Fase 2 — Transcripción histórico-digital

**Estado:** activa; el cuerpo gramatical está cubierto en superficie, pero la fase no se declara cerrada.

Estado alcanzado:

- **128 páginas `full_page`**;
- preliminares textuales representados;
- Partes I–IV del Arte representadas de forma continua hasta `FIN DEL ARTE`;
- fronteras intra-página 69 (II→III) y 105 (III→IV) preservadas;
- estados `machine_corrected_unverified`, `unresolved` y material no textual diferenciados;
- **0** páginas `human_verified`.

Pendientes:

- consolidar `status.csv` y lotes posteriores en una única vista canónica;
- definir y ejecutar el alcance final de transcripción diplomática página-a-página para vocabulario y numerales si formarán parte de la edición científica;
- mantener una cola explícita de lecturas inciertas y anomalías;
- ampliar control independiente sin convertir resultados automáticos en validación humana.

## Fase 3 — Corpus lexicográfico

**Estado:** **estructuralmente cerrado en pp.133–177; fase activa de consolidación, interenlace y exportación**.

Estado computacional vigente al **21 de agosto de 2026**:

- **2,072 / 2,072 candidatos canónicos** `hybrid_margin_mode_v0.2` persistidos de forma lossless, reconstruible y verificable;
- **2,302 artículos históricos estructurados** en la capa curatorial;
- **45 / 45 páginas** del Vocabulario con reconciliación candidate-level completa;
- **45 / 45 páginas** con censo exhaustivo de inicios visibles, promoción/enlace completo y cierre técnico IA-asistido;
- la subfase p.145–177 terminó con **33 / 33 páginas** cerradas;
- **0 candidatos `pending_promotion`**;
- **0 candidatos estructuralmente `unresolved`** en el resumen de cierre;
- **0 fronteras `ambiguous`**;
- p.177 fija el final material del Vocabulario; pp.178–180 contienen el sistema numeral;
- agrupaciones, reclamos, continuidades trans-columna/trans-página y falsos negativos permanecen modelados como capas explícitas;
- `ALC1737-gap-0001` (157→158) y otras incertidumbres materiales siguen visibles sin reconstrucción silenciosa;
- **0 artículos `human_verified`**.

La fuente computacional de estos totales es `data/lexicon/reconciliation/phase2_open_work_summary.json`, regenerable mediante `scripts/summarize_open_lexicon_work.py`. Los estados de página conservan snapshots históricos de cada pasada y no sustituyen el conteo actual de `articleId` únicos.

El cierre estructural no resuelve automáticamente incertidumbres semánticas o microtextuales dentro de artículos ya estructurados. Anáforas `Lo miſmo`, remisiones `Buſca`, lecturas parcialmente `unresolved` y atribuciones históricas requieren capas editoriales separadas.

### Próximo bloque de Fase 3

1. construir un **inventario maestro final de artículos históricos**, explícitamente separado del inventario de candidatos;
2. cerrar el **grafo de remisiones `Buſca`** con destinos resueltos cuando la evidencia lo permita y estado explícito cuando no;
3. inventariar y modelar las **anáforas `Lo miſmo`** sin inferencia silenciosa;
4. detectar sistemáticamente atribuciones históricas `Hiaqui`, `Mayo`, `Thehueco` y variantes dentro del vocabulario;
5. producir exportaciones canónicas **JSONL / JSON / CSV** reproducibles y sin duplicados;
6. estabilizar la microestructura necesaria para una proyección posterior **TEI Lex-0**;
7. ampliar QA para validar que exportaciones y grafos se regeneren desde datos canónicos.

**Criterio de salida de Fase 3:** corpus lexicográfico exhaustivo respecto del testimonio disponible, reconstruible desde su procedencia y apto para exportación estable, con remisiones, anáforas, etiquetas históricas, incertidumbre y estado de revisión explícitos.

## Fase 4 — Gramática, ejemplos y variación histórica

**Estado:** activa y avanzada.

Capas ya estructuradas incluyen paradigmas históricos, construcciones modales/no finitas/participiales/predicativas, verbos irregulares, preposiciones, adverbios, conjunciones, interjecciones, el sistema numeral histórico de pp.178–180 y 17+ observaciones de variación histórica.

Pendientes prioritarios:

- índice exhaustivo de denominaciones históricas en las 182 páginas;
- integrar observaciones `Hiaqui` / `Hiaquis` / `Naciones` de los numerales;
- segunda pasada de cantidades mayores y variantes numéricas;
- extender sistemáticamente reglas tempranas de Partes I–II a objetos gramaticales derivados;
- construir concordancia **forma ↔ regla ↔ paradigma/construcción ↔ ejemplo ↔ página**;
- producir exportaciones JSON/CSV reproducibles;
- formalizar irregularidades editoriales y fronteras materiales.

## Fase 5 — Control textual, interoperabilidad y reproducibilidad avanzada

**Estado:** preparación avanzada; QA básico implantado, interoperabilidad y control textual no cerrados.

Prioridades:

- ampliar CI a nuevos derivados y documentación de estado;
- localizar e incorporar, con procedencia separada, testimonios independientes útiles para control textual;
- cotejar lagunas y anomalías sin rellenar silenciosamente `ALC1737`;
- estabilizar esquemas JSON de producción;
- definir perfil TEI para la edición;
- proyectar el vocabulario a TEI Lex-0 sólo sobre microestructura estabilizada;
- evaluar IIIF cuando derechos y disponibilidad lo permitan;
- formalizar metadatos FAIR y evaluación de reproducibilidad;
- generar artefactos derivados exclusivamente desde scripts versionados.

## Fase 6 — Investigación comparativa

**Estado:** bloqueada hasta estabilizar el corpus histórico y la autoridad editorial.

La comparación futura con recursos modernos de yaqui y mayo deberá modelar correspondencias como candidatos, no como equivalencias automáticas, y distinguir continuidad léxica, semejanza gráfica, traducción y cognación.

## Fase 7 — Release científica y preservación

**Estado:** pendiente.

Secuencia recomendada:

1. `0.2.x-dev`: estabilización de repositorio, corpus maestro y QA;
2. `0.5.0`: snapshot científico con exportaciones reproducibles;
3. `0.9.0`: candidata a release con interoperabilidad y validación ampliada;
4. `v1.0.0`: release científica cerrada del alcance declarado.

Para una release estable deberán existir metadatos finales de versión, cobertura y limitaciones publicadas, checksums, `CITATION.cff` y `codemeta.json` sincronizados, paquete de datos canónico, archivo en Zenodo, DOI de versión, changelog y protocolo de preservación.

## Productos científicos previstos

1. edición histórico-digital del _Arte_ de 1737;
2. dataset lexicográfico abierto;
3. corpus gramatical y de ejemplos;
4. dataset de variación histórica;
5. artículo de datos/metodología;
6. estudios lingüísticos e historiográficos especializados;
7. concordancias, visualizaciones y herramientas de consulta;
8. estudios comparativos diacrónicos posteriores;
9. modelo replicable para otras fuentes cahítas históricas.

## Prioridad inmediata

Tras el cierre estructural del Vocabulario, CHD debe:

1. sincronizar README, ROADMAP, COVERAGE, `LEXICON_PROGRESS`, Issues y métricas con el estado de 2,302 artículos y 0 pendientes;
2. construir el **corpus maestro reproducible** y exportaciones JSONL/JSON/CSV;
3. cerrar el grafo `Buſca` y el inventario de `Lo miſmo`;
4. estructurar atribuciones históricas dentro del vocabulario;
5. consolidar variación y concordancias gramaticales;
6. ampliar CI, control textual e interoperabilidad antes de una release científica estable.
