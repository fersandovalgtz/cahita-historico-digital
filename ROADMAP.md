# Hoja de ruta

Estado de planificación de Cahíta Histórico Digital (`ALC1737`) — actualización 2026-08-16.

## Principio rector

CHD no avanza por acumulación indiscriminada de archivos. Cada fase debe cerrar una capa de evidencia con procedencia, estados de autoridad y criterios de salida explícitos antes de que los productos finales dependan de ella.

## Fase 0 — Infraestructura científica

**Estado:** completada para la etapa de investigación activa; mantenimiento continuo.

Se establecieron registro de fuente y procedencia, política de autoría, criterios editoriales, metadatos de citación, licencias, contratos de datos, documentación de riesgos, esquemas JSON y una arquitectura explícita de evidencia.

**Criterio de salida alcanzado:** el repositorio es auditable y puede procesar `ALC1737` sin confundir fuente, OCR, transcripción, estructuración e inferencia.

**Mantenimiento pendiente:** incorporar CI/QA automático y continuar sincronizando documentación, métricas y esquemas.

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
- ampliar cotejo humano independiente.

**Criterio de salida:** cobertura textual definida para todas las zonas que vayan a formar parte de la edición científica, con métricas transparentes y sin falsas declaraciones de validación humana.

## Fase 3 — Corpus lexicográfico

**Estado:** activa; ya existe una capa curatorial amplia, pero aún no un corpus lexicográfico exhaustivo cerrado.

Estado alcanzado:

- 3,899 líneas OCR/layout documentadas para digitales 133–177;
- extractor vigente `hybrid_margin_mode_v0.2`;
- **2,072 / 2,072 candidatos canónicos** persistidos de forma lossless, reconstruible y verificable;
- comparación diagnóstica v0.2 sobre pp. 133, 134, 150 y 177: precisión 97.13%, recall 89.89%, F1 93.37%;
- **734 artículos históricos estructurados**;
- **45 / 45 páginas** del vocabulario con representación lexicográfica estructurada;
- modelado de `Buſca`, `Lo miſmo`, agrupaciones, catchwords, spans trans-columna/trans-página y anomalías documentales;
- pp. 133–134: **61 / 61 candidatos reconciliados**;
- 14 inicios visibles omitidos observados en pp. 133–134;
- 36 candidatos `article` de ese tramo todavía `pending_promotion`;
- `ALC1737-gap-0001` (157→158) y anomalía `Lucer-` (161→162) registradas;
- **0** artículos `human_verified`.

Pendientes:

- promover los artículos históricos pendientes de pp. 133–134;
- cerrar el inventario de inicios visibles/falsos negativos de esas páginas;
- escalar reconciliación candidato→resultado editorial a pp. 135–177;
- construir el inventario final de artículos históricos, separado del conteo de candidatos;
- resolver editorialmente, sin automatismos, anáforas `Lo miſmo`;
- cerrar el grafo de remisiones `Buſca`;
- detectar sistemáticamente atribuciones explícitas Hiaqui/Mayo/Thehueco dentro del vocabulario;
- generar exportaciones canónicas JSON/CSV sin duplicados;
- ampliar QA y revisión humana.

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

**Estado:** preparación; no cerrada.

Prioridades:

- localizar e incorporar, con procedencia separada, uno o más testimonios independientes útiles para control textual si están disponibles;
- cotejar lagunas y anomalías sin rellenar silenciosamente el testimonio `ALC1737`;
- implantar integración continua para validar JSON Schema, unicidad de IDs, hashes, reconstrucción de candidatos, referencias y exports;
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

1. mantener sincronizados README, ROADMAP, Issues, métricas y metadatos;
2. cerrar QA de apertura lexicográfica y promover los 36 artículos pendientes de pp. 133–134;
3. escalar la reconciliación al resto del vocabulario;
4. consolidar variación y concordancias gramaticales;
5. incorporar CI y control textual independiente cuando sea posible.
