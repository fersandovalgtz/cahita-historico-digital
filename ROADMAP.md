# Hoja de ruta

Estado de planificación de Cahíta Histórico Digital (`ALC1737`) — actualización 2026-08-17.

## Principio rector

CHD no avanza por acumulación indiscriminada de archivos. Cada fase debe cerrar una capa de evidencia con procedencia, estados de autoridad y criterios de salida explícitos antes de que los productos finales dependan de ella.

## Fase 0 — Infraestructura científica

**Estado:** completada para la etapa de investigación activa; mantenimiento continuo.

Se establecieron registro de fuente y procedencia, política de autoría, criterios editoriales, metadatos de citación, licencias, contratos de datos, documentación de riesgos, esquemas JSON y una arquitectura explícita de evidencia. El repositorio dispone además de QA automatizado para reconstrucción del inventario canónico, validación de identificadores, esquemas y metadatos; la línea de fase II cuenta con un resumen computacional regenerable de trabajo abierto.

**Criterio de salida alcanzado:** el repositorio es auditable y puede procesar `ALC1737` sin confundir fuente, OCR, transcripción, estructuración e inferencia.

**Mantenimiento pendiente:** ampliar CI/QA para impedir deriva entre datos, resúmenes y documentación; continuar sincronizando métricas, esquemas y artefactos derivados.

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

**Estado:** activa, con el cuerpo gramatical ya cubierto en superficie.

Estado alcanzado:

- **128 páginas `full_page`**;
- preliminares textuales representados;
- Partes I–IV del Arte representadas de forma continua en capa IA-asistida hasta `FIN DEL ARTE`;
- fronteras intra-página 69 (II→III) y 105 (III→IV) preservadas;
- estados `machine_corrected_unverified`, `unresolved` y material no textual diferenciados;
- **0** páginas `human_verified`.

Pendientes antes de cerrar la fase:

- consolidar `status.csv` y lotes posteriores en una única vista canónica coherente;
- completar, si se decide necesario para la edición final, transcripción diplomática página-a-página del vocabulario y numerales además de sus capas estructuradas;
- mantener una cola explícita de lecturas inciertas y anomalías;
- ampliar cotejo independiente sin convertir resultados automáticos en validación humana.

**Criterio de salida:** cobertura textual definida para todas las zonas que vayan a formar parte de la edición científica, con métricas transparentes y sin falsas declaraciones de validación humana.

## Fase 3 — Corpus lexicográfico

**Estado:** activa y avanzada; la reconciliación estructural ya cubre el vocabulario, pero el corpus lexicográfico exhaustivo todavía no está cerrado.

Estado computacional vigente al 17 de agosto de 2026:

- 3,899 líneas OCR/layout documentadas para digitales 133–177;
- extractor vigente `hybrid_margin_mode_v0.2`;
- **2,072 / 2,072 candidatos canónicos** persistidos de forma lossless, reconstruible y verificable;
- comparación diagnóstica v0.2 sobre pp. 133, 134, 150 y 177: precisión 97.13%, recall 89.89%, F1 93.37%;
- **1,049 artículos históricos estructurados** en la capa curatorial actual;
- **45 / 45 páginas** del vocabulario con representación lexicográfica estructurada;
- páginas **133–144** cerradas técnicamente en reconciliación, censo visible y promoción/enlace IA-asistidos dentro del alcance declarado;
- páginas **145–177** con reconciliación completa de sus candidatos canónicos y abiertas en fase II para promoción/enlace, censo exhaustivo de inicios visibles y cierre técnico;
- **1,047 candidatos de artículo `pending_promotion`** en el alcance de fase II p.145–177;
- **1 candidato estructuralmente `unresolved`** y **9 fronteras `ambiguous`** en ese mismo alcance;
- **0 / 33 páginas** p.145–177 con censo visible exhaustivo y **0 / 33** con cierre técnico;
- primera promoción conservadora de fase II en p.145: **4 artículos nuevos**, elevando el corpus de 1,045 a 1,049 y dejando **17** candidatos `pending_promotion` en esa página;
- modelado de `Buſca`, `Lo miſmo`, agrupaciones, catchwords, spans trans-columna/trans-página y anomalías documentales;
- `ALC1737-gap-0001` (157→158) y anomalía `Lucer-` (161→162) preservadas sin reconstrucción silenciosa;
- **0** artículos `human_verified`; la autoridad sigue siendo `machine_corrected_unverified` cuando corresponde.

La fuente computacional de los totales de trabajo abierto es `data/lexicon/reconciliation/phase2_open_work_summary.json`, regenerable mediante `scripts/summarize_open_lexicon_work.py`. Los totales históricos almacenados en estados de página se tratan como instantáneas de cada pasada y no sustituyen el conteo actual de `articleId` únicos.

Pendientes:

- continuar promociones conservadoras candidato→artículo únicamente cuando el propio testimonio `ALC1737` sustente guía y forma con evidencia suficiente;
- mantener explícitamente como pendientes las lecturas materialmente divergentes, sin sustituirlas con formas de testigos secundarios;
- completar el censo exhaustivo de inicios visibles en p.145–177 y registrar falsos negativos con denominador facsimilar explícito;
- reducir la única incertidumbre estructural todavía abierta sin inventar una resolución;
- construir el inventario final de artículos históricos, separado del conteo de candidatos;
- resolver editorialmente, sin automatismos, anáforas `Lo miſmo`;
- cerrar el grafo de remisiones `Buſca`;
- detectar sistemáticamente atribuciones explícitas Hiaqui/Mayo/Thehueco dentro del vocabulario;
- generar exportaciones canónicas JSON/CSV sin duplicados;
- ampliar QA y revisión independiente.

**Criterio de salida:** corpus lexicográfico exhaustivo respecto del testimonio disponible, reconstruible desde su procedencia, con fronteras, falsos negativos, incertidumbre y estado de revisión explícitos.

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

**Estado:** preparación avanzada; QA básico ya implantado, interoperabilidad y control textual no cerrados.

Estado alcanzado:

- workflow de QA sobre `main` y pull requests;
- reconstrucción automática del inventario canónico de candidatos;
- validación de IDs, estados de autoridad, JSON Schema, capas de reconciliación y metadatos centrales;
- resumen reproducible del trabajo abierto de fase II con conteo independiente de `articleId` curatoriales.

Prioridades:

- impedir por CI que el resumen de fase II quede desincronizado respecto de datos y estados de página;
- localizar e incorporar, con procedencia separada, uno o más testimonios independientes útiles para control textual si están disponibles;
- cotejar lagunas y anomalías sin rellenar silenciosamente el testimonio `ALC1737`;
- estabilizar esquemas JSON de producción;
- definir perfil TEI para la edición;
- proyectar el vocabulario a TEI Lex-0 sólo cuando su microestructura esté estabilizada;
- evaluar IIIF para enlazar unidades editoriales con facsímiles cuando derechos y disponibilidad lo permitan;
- formalizar metadatos FAIR y evaluación de reproducibilidad;
- generar artefactos derivados desde scripts versionados.

**Criterio de salida:** un checkout limpio puede validar y reconstruir automáticamente los principales derivados, y los datos de producción disponen de perfiles interoperables estables.

## Fase 6 — Investigación comparativa

**Estado:** bloqueada hasta estabilizar el corpus histórico y la autoridad editorial.

- comparar formas históricas con recursos modernos de yaqui y mayo;
- modelar correspondencias como **candidatos**, no como equivalencias automáticas;
- separar continuidad léxica, semejanza gráfica, traducción y cognación;
- incorporar bibliografía lingüística contemporánea y, cuando proceda, colaboración especializada;
- distinguir siempre descripción histórica, propuesta filológica y análisis moderno.

## Fase 7 — Release científica y preservación

**Estado:** pendiente.

Antes de productos finales se recomienda una secuencia de congelamiento:

1. `0.2.x-dev`: estabilización de repositorio, reconciliación y QA;
2. `0.5.0` o equivalente: snapshot científico con corpus sustancialmente reconciliado;
3. `0.9.0`: candidata a release, con interoperabilidad y validación ampliada;
4. `v1.0.0`: release científica cerrada del alcance declarado.

Para `v1.0.0` deberán existir:

- metadatos finales de versión;
- cobertura y limitaciones publicadas;
- checksums y artefactos verificables;
- `CITATION.cff` y `codemeta.json` sincronizados;
- paquete de datos canónico;
- archivo en Zenodo;
- DOI específico de versión y Concept DOI cuando corresponda;
- documentación de autoridad/revisión humana;
- changelog y protocolo de preservación.

## Productos científicos previstos

Los productos se diseñarán **después de estabilizar suficientemente los insumos**, no como sustituto del trabajo de corpus. Entre los productos posibles:

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

Antes de ampliar productos, CHD debe:

1. mantener sincronizados README, ROADMAP, `phase2_open_work_summary.json`, Issues, métricas y metadatos;
2. continuar fase II con promociones conservadoras desde p.145–177, sin convertir OCR divergente ni control secundario en transcripción de `ALC1737`;
3. completar progresivamente el censo exhaustivo de inicios visibles y falsos negativos de p.145–177;
4. cerrar la incertidumbre estructural restante y mantener separadas las incertidumbres semánticas/anafóricas;
5. consolidar variación y concordancias gramaticales;
6. ampliar CI, control textual independiente e interoperabilidad antes de una release científica estable.
