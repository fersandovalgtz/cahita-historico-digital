# Hoja de ruta

Estado de planificación de Cahíta Histórico Digital (`ALC1737`) — actualización **21 de agosto de 2026**.

## Principio rector

CHD avanza por capas de evidencia con procedencia, autoridad y criterios de salida explícitos. El cierre técnico no se presenta como validación filológica humana y ningún derivado interoperable sustituye la representación curatorial canónica.

## Fase 0 — Infraestructura científica

**Estado:** completada para la etapa de investigación activa; mantenimiento continuo.

El repositorio dispone de registro de fuente y procedencia, política de autoría, criterios editoriales, licencias, citación, contratos de datos, esquemas JSON, estados de autoridad, QA automatizado, exportadores deterministas, control de documentación y un paquete científico reproducible de release candidate.

**Criterio de salida alcanzado:** un checkout limpio puede validar el corpus y reconstruir los principales derivados sin confundir fuente, OCR, transcripción, estructuración e inferencia.

## Fase 1 — Ingestión de `ALC1737`

**Estado:** completada el 15 de agosto de 2026.

Resultados fijados: manifiesto de 182 páginas digitales, mapeo de paginación, segmentación macro, fe de erratas, OCR regenerable, hashes de fuente y scripts de ingestión reproducible.

## Fase 2 — Transcripción histórico-digital

**Estado:** activa; el cuerpo gramatical tiene cobertura superficial continua, pero la edición textual completa no está congelada.

Estado alcanzado: 128 páginas `full_page`, preliminares y Partes I–IV representadas, fronteras intra-página preservadas y estados de autoridad diferenciados. Se mantienen **0 páginas `human_verified`**.

Pendientes principales: consolidar la vista canónica de transcripción, definir el alcance diplomático del vocabulario/numerales y ampliar control textual independiente sin promover resultados automáticos a validación humana.

## Fase 3 — Corpus lexicográfico

**Estado:** **cierre técnico alcanzado; consolidación filológica post-cierre activa.**

Hitos fijados:

- **2,072 / 2,072 candidatos canónicos** reconstruibles;
- **2,302 artículos históricos** en **211 JSONL** canónicos;
- **45 / 45 páginas** del vocabulario p.133–177 reconciliadas candidate-level;
- Phase II p.145–177: **33 / 33 páginas** cerradas técnicamente;
- `pendingPromotionTotal = 0`;
- `unresolvedCandidateTotal = 0`;
- `ambiguousBoundaryTotal = 0`;
- **0 artículos `human_verified`**.

### Remisiones `Buſca`

El inventario canónico contiene **150 remisiones**, todas de clase `Buſca`: 60 `exact_unique`, 90 `not_located`, 90/90 con revisión editorial explícita, 40 destinos sustentados, 22 recolaciones, 5 candidatos rechazados y 23 destinos no localizados. La vista revisada contiene 100 aristas = 60 estrictas + 40 editoriales.

Las **22 recolaciones** están materializadas como cola reproducible separada: **8 Tier A, 4 Tier B y 10 Tier C**. No son errores confirmados y no deben resolverse mediante similitud aproximada.

### Fórmula `Lo miſmo`

Las **14/14 ocurrencias** superficiales están inventariadas y revisadas. Ninguna se transforma automáticamente en remisión, forma cahíta o equivalencia semántica.

## Fase 4 — Gramática, ejemplos y variación histórica

**Estado:** **cierre técnico alcanzado para las unidades gramaticales numeradas; consolidación filológica activa.**

Hitos fijados:

- secuencia nominal 1–373;
- **370 / 373 números nominales** con reclamación estructurada;
- 127, 178 y 294 documentados como omisiones materiales del impreso;
- 129 aparece dos veces y ambas unidades se conservan;
- **371 / 371 unidades numeradas realmente impresas** representadas;
- **302 objetos gramaticales en 24 archivos**;
- **1,215 filas de evidencia**;
- **0 objetos `humanVerified=true`**;
- concordancia y cobertura validadas mediante doble corrida determinista.

## Fase 5 — Control textual, interoperabilidad y reproducibilidad avanzada

**Estado:** **interoperabilidad de v1.0 cerrada técnicamente; control textual y congelamiento final activos.**

Estado alcanzado:

- CI sobre `main` y pull requests;
- derivados lexicográficos y gramaticales reproducibles;
- paquete científico de release candidate construido dos veces byte-a-byte idéntico;
- proyección TEI de **2,302 entradas**, **2,221 citas de traducción**, **150 remisiones** y **60 `@target` estrictos**;
- TEI validado externamente con Jing contra **TEI Lex-0 0.9.5** archivado;
- schema Relax NG fijado por SHA-256 `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`;
- XML TEI validado con SHA-256 `bad06dad39f216b8dde661b4219845c4c19db945bdfbc4478ff5e0846b72e828`;
- `xml:lang="und"` conserva la indeterminación de identidad moderna de la lengua histórica etiquetada como Cahita;
- **decisión CLDF cerrada:** TEI Lex-0 0.9.5 es el perfil lexicográfico interoperable primario de v1.0; CLDF no es requisito de v1.0 y se difiere como derivado analítico futuro.

La decisión se registra en `docs/CLDF_SCOPE_DECISION_V1_0.md`. Una futura vista CLDF deberá preservar trazabilidad a `articleId`, no inferir identidad moderna, cognación, préstamo o equivalencia, y validarse con `pycldf`.

### Prioridades restantes

1. estabilizar y congelar schemas/contratos y metadatos de producción incluidos en v1.0;
2. mantener la cola de 22 recolaciones y resolver sólo las que puedan cotejarse contra imagen verificable;
3. formalizar metadatos finales y changelog;
4. preparar preservación y DOI;
5. evaluar IIIF sólo si derechos y disponibilidad del facsímil permiten enlaces estables.

## Fase 6 — Investigación comparativa

**Estado:** diferida hasta congelar la autoridad editorial de v1.0.

La comparación con recursos modernos de yaqui/mayo deberá modelar correspondencias como candidatos y separar continuidad léxica, semejanza gráfica, traducción, préstamo y cognación. Ninguna comparación moderna debe retroproyectarse automáticamente sobre `ALC1737`.

## Fase 7 — Release científica y preservación

**Estado:** preparación avanzada; todavía no debe etiquetarse como `v1.0.0`.

El paquete científico reproducible ya existe y conserva `releaseReady=false`. Tras cerrar TEI Lex-0 y la decisión CLDF quedan **cuatro gates sustantivos**:

1. política/cotejo final de las 22 recolaciones facsimilares;
2. congelamiento final de schemas, cobertura y metadatos;
3. tag/changelog y GitHub Release;
4. depósito archivístico y DOI específico de versión.

Para `v1.0.0` deberán existir metadatos finales sincronizados, limitaciones publicadas, checksums del paquete congelado, `CITATION.cff` y `codemeta.json` alineados con el tag, changelog, release GitHub y depósito preservado con DOI.

## Productos científicos previstos

1. edición histórico-digital del *Arte* de 1737;
2. dataset lexicográfico abierto;
3. corpus gramatical y de ejemplos;
4. dataset de variación histórica;
5. artículo de datos/metodología;
6. estudios lingüísticos e historiográficos especializados;
7. concordancias, visualizaciones y herramientas de consulta;
8. estudios comparativos diacrónicos posteriores;
9. modelo replicable para otras fuentes cahítas históricas.

## Prioridad inmediata

1. **congelar schemas, contratos y metadatos del alcance v1.0**;
2. **resolver por imagen o congelar transparentemente las 22 recolaciones**;
3. **preparar changelog y candidata final desde commit limpio**;
4. **crear tag/GitHub Release y ejecutar preservación/DOI**.

Hasta completar estos pasos, el proyecto debe permanecer en candidata de release y no presentarse como edición filológica humana.
