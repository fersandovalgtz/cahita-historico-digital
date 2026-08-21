# Hoja de ruta

Estado de planificación de Cahíta Histórico Digital (`ALC1737`) — actualización **21 de agosto de 2026**.

## Principio rector

CHD no avanza por acumulación indiscriminada de archivos. Cada fase debe cerrar una capa de evidencia con procedencia, estados de autoridad y criterios de salida explícitos antes de que los productos posteriores dependan de ella. El cierre técnico nunca se presenta como validación filológica humana.

## Fase 0 — Infraestructura científica

**Estado:** completada para la etapa de investigación activa; mantenimiento continuo.

Se establecieron registro de fuente y procedencia, política de autoría, criterios editoriales, metadatos de citación, licencias, contratos de datos, documentación de riesgos, esquemas JSON y una arquitectura explícita de evidencia. El repositorio dispone de QA automatizado para reconstrucción del inventario canónico, validación de identificadores, esquemas, reconciliaciones y resumen canónico de Phase II.

**Criterio de salida alcanzado:** el repositorio es auditable y puede procesar `ALC1737` sin confundir fuente, OCR, transcripción, estructuración e inferencia.

**Mantenimiento:** impedir deriva entre datos, resúmenes, README, ROADMAP y documentación de release; continuar ampliando QA para artefactos derivados.

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
- scripts de ingestión reproducible;
- política de separación entre datos curatoriales y derivados reconstruibles.

**Criterio de salida alcanzado:** toda unidad procesada puede remontarse a una página digital concreta y, en el cuerpo paginado, a una referencia impresa estable.

## Fase 2 — Transcripción histórico-digital

**Estado:** activa; el cuerpo gramatical está cubierto en superficie, pero la edición textual completa no está congelada.

Estado alcanzado:

- **128 páginas `full_page`**;
- preliminares textuales representados;
- Partes I–IV del Arte representadas de forma continua en capa IA-asistida hasta `FIN DEL ARTE`;
- fronteras intra-página 69 (II→III) y 105 (III→IV) preservadas;
- estados `machine_corrected_unverified`, `unresolved` y material no textual diferenciados;
- **0** páginas `human_verified`.

Pendientes:

- consolidar `status.csv` y lotes posteriores en una única vista canónica coherente;
- decidir el alcance de transcripción diplomática página-a-página para vocabulario y numerales, separándolo de sus capas estructuradas;
- mantener una cola explícita de lecturas inciertas y anomalías;
- ampliar control textual independiente sin convertir resultados automáticos en validación humana.

**Criterio de salida:** cobertura textual definida para todas las zonas incluidas en la futura edición científica, con métricas transparentes y sin falsas declaraciones de validación humana.

## Fase 3 — Corpus lexicográfico

**Estado:** **cierre técnico alcanzado para fronteras, censo visible y promoción/enlace del vocabulario completo; consolidación post-cierre activa.**

Hito alcanzado el 21 de agosto de 2026:

- **2,072 / 2,072 candidatos canónicos** `hybrid_margin_mode_v0.2` persistidos de forma lossless, reconstruible y verificable;
- **2,302 artículos históricos estructurados** en la capa curatorial;
- **45 / 45 páginas** del vocabulario p.133–177 con reconciliación candidate-level completa y cierre técnico IA-asistido;
- tramo p.145–177: **33 / 33 páginas** con censo visible exhaustivo y **33 / 33** con cierre técnico;
- `pendingPromotionTotal = 0` en Phase II;
- `unresolvedCandidateTotal = 0` en Phase II;
- `ambiguousBoundaryTotal = 0` en Phase II;
- p.177 establece el final material del vocabulario antes de la sección de numerales p.178–180;
- **0** artículos `human_verified`.

La fuente computacional vigente es `data/lexicon/reconciliation/phase2_open_work_summary.json`, regenerable mediante `scripts/summarize_open_lexicon_work.py`. El cierre se documenta en `docs/PHASE2_COMPLETION_2026-08-21.md`.

El cierre técnico no elimina incertidumbres internas de microlectura, remisiones o anáforas ya modeladas. Tampoco convierte la capa curatorial en edición crítica humana.

### Trabajo post-cierre

1. generar exportaciones canónicas JSON/CSV de los 2,302 artículos con hashes y controles de unicidad;
2. construir el grafo de remisiones `Buſca` y distinguir destinos resolubles, no resolubles y referencias circulares;
3. inventariar las anáforas `Lo miſmo` y conservarlas sin resolución automática;
4. detectar sistemáticamente atribuciones históricas explícitas Hiaqui/Mayo/Thehueco y otras etiquetas de variedad;
5. auditar `sourceSpans`, continuidades transcolumna/transpágina y anomalías materiales;
6. separar con claridad artículo histórico, lexema normalizado futuro y cualquier análisis lingüístico moderno;
7. preparar exportaciones interoperables sin hacer depender el dato canónico de un único formato externo.

**Criterio de salida de la consolidación post-cierre:** inventario histórico exportable y auditable, remisiones y metadatos de variedad explícitos, derivados reproducibles y documentación sincronizada.

## Fase 4 — Gramática, ejemplos y variación histórica

**Estado:** activa y avanzada.

Capas ya estructuradas:

- 3 paradigmas históricos;
- 9 construcciones modales, reglas 207–234;
- 5 construcciones no finitas, reglas 237–256;
- 3 construcciones participiales, reglas 257–265;
- 6 construcciones predicativas/modales, reglas 266–284;
- 6 grupos de verbos irregulares, reglas 286–291;
- 43 preposiciones/grupos, reglas 293–340;
- 11 grupos de adverbios, reglas 341–359;
- 6 grupos de conjunciones/metacategorías, reglas 360–373 e interjecciones;
- sistema numeral histórico, digitales 178–180;
- 17+ observaciones de variación histórica identificadas.

Pendientes:

- índice exhaustivo de denominaciones históricas en las 182 páginas;
- regenerar la exportación combinada de variación e incorporar todas las entidades modulares;
- integrar observaciones `Hiaqui` / `Hiaquis` / `Naciones` de los numerales;
- segunda pasada de cantidades mayores y variantes numéricas;
- extender sistemáticamente las reglas tempranas de Partes I–II a objetos gramaticales derivados;
- construir concordancia **forma ↔ regla ↔ paradigma/construcción ↔ ejemplo ↔ página**;
- producir exportaciones JSON/CSV reproducibles;
- formalizar el estudio de irregularidades editoriales y fronteras materiales.

**Criterio de salida:** corpus gramatical histórico suficientemente exhaustivo para permitir búsquedas y análisis sin regresar continuamente a una segmentación ad hoc del impreso.

## Fase 5 — Control textual, interoperabilidad y reproducibilidad avanzada

**Estado:** preparación avanzada; QA de corpus implantado, interoperabilidad y control textual no cerrados.

Estado alcanzado:

- workflow de QA sobre `main` y pull requests;
- reconstrucción automática del inventario canónico de candidatos;
- validación de IDs, estados de autoridad, JSON Schema, capas de reconciliación y metadatos centrales;
- resumen reproducible de Phase II con conteo independiente de `articleId` curatoriales;
- vocabulario p.133–177 estructuralmente cerrado, lo que permite diseñar derivados sin seguir moviendo fronteras de artículo.

Prioridades:

- impedir por CI la deriva entre la fuente canónica de métricas y la documentación central;
- generar y validar exportaciones derivadas del corpus lexicográfico;
- localizar e incorporar, con procedencia separada, testimonios independientes útiles para control textual si están disponibles;
- cotejar lagunas y anomalías sin rellenar silenciosamente el testimonio `ALC1737`;
- estabilizar esquemas JSON de producción;
- definir perfil TEI para la edición;
- proyectar el vocabulario a TEI Lex-0 sólo cuando su microestructura de salida esté suficientemente estabilizada;
- evaluar CLDF para vistas lexicográficas derivadas, sin presentar automáticamente el vocabulario histórico como corpus paralelo moderno;
- evaluar IIIF para enlazar unidades editoriales con facsímiles cuando derechos y disponibilidad lo permitan;
- formalizar metadatos FAIR y evaluación de reproducibilidad;
- generar artefactos derivados desde scripts versionados.

**Criterio de salida:** un checkout limpio puede validar y reconstruir automáticamente los principales derivados y los datos de producción disponen de perfiles interoperables estables.

## Fase 6 — Investigación comparativa

**Estado:** bloqueada hasta estabilizar las capas post-cierre y la autoridad editorial.

- comparar formas históricas con recursos modernos de yaqui y mayo;
- modelar correspondencias como **candidatos**, no como equivalencias automáticas;
- separar continuidad léxica, semejanza gráfica, traducción y cognación;
- incorporar bibliografía lingüística contemporánea y, cuando proceda, colaboración especializada;
- distinguir siempre descripción histórica, propuesta filológica y análisis moderno.

## Fase 7 — Release científica y preservación

**Estado:** pendiente. El cierre de Phase II no equivale a una release estable.

Secuencia recomendada:

1. `0.2.x-dev`: sincronización documental, consolidación post-cierre, QA y exportaciones;
2. `0.5.0` o equivalente: snapshot científico con corpus lexicográfico estable y derivados reproducibles;
3. `0.9.0`: candidata a release, con interoperabilidad, control textual y metadatos ampliados;
4. `v1.0.0`: release científica cerrada del alcance declarado.

Para `v1.0.0` deberán existir:

- metadatos finales de versión;
- cobertura y limitaciones publicadas;
- checksums y artefactos verificables;
- `CITATION.cff` y `codemeta.json` sincronizados;
- paquete de datos canónico;
- archivo en Zenodo;
- DOI específico de versión y Concept DOI cuando corresponda;
- documentación clara de autoridad y estado de revisión;
- changelog y protocolo de preservación.

## Productos científicos previstos

Los productos se diseñarán después de estabilizar suficientemente los insumos, no como sustituto del trabajo de corpus:

1. edición histórico-digital del *Arte* de 1737;
2. dataset lexicográfico abierto;
3. corpus gramatical y de ejemplos;
4. dataset de variación histórica descrita como Hiaqui/Mayo/Thehueco;
5. artículo de datos/metodología;
6. estudios lingüísticos e historiográficos especializados;
7. concordancias, visualizaciones y herramientas de consulta;
8. estudios comparativos diacrónicos posteriores;
9. modelo replicable para otras fuentes cahítas históricas.

## Prioridad inmediata

Después del cierre de Phase II, CHD debe concentrarse en:

1. **sincronización documental y QA de métricas**;
2. **exportación canónica JSON/CSV de los 2,302 artículos**;
3. **grafo de remisiones `Buſca` y registro de anáforas `Lo miſmo`**;
4. **auditoría de etiquetas históricas de variedad y `sourceSpans`**;
5. **consolidación de variación y concordancias gramaticales**;
6. **perfil TEI / evaluación Lex-0 y CLDF como derivados**;
7. **control textual, preservación y preparación gradual de release**, manteniendo `0.2.0-dev` hasta que los criterios de congelamiento estén realmente cumplidos.
