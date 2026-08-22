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

Resultados fijados:

- SHA-256 de archivos de trabajo;
- manifiesto de 182 páginas digitales;
- segmentación macro del volumen;
- mapeo digital 15–132 ↔ impresa 1–118;
- preliminares, cuatro partes gramaticales, vocabulario, numerales y finales materiales identificados;
- fe de erratas histórica registrada;
- OCR bruto regenerable y verificable por hash;
- scripts de ingestión reproducible;
- separación entre datos curatoriales y derivados reconstruibles.

## Fase 2 — Transcripción histórico-digital

**Estado:** activa; el cuerpo gramatical tiene cobertura superficial continua, pero la edición textual completa no está congelada.

Estado alcanzado:

- **128 páginas `full_page`**;
- preliminares textuales representados;
- Partes I–IV del Arte representadas hasta `FIN DEL ARTE`;
- fronteras intra-página preservadas;
- estados `machine_corrected_unverified`, `unresolved` y material no textual diferenciados;
- **0 páginas `human_verified`**.

Pendientes principales: consolidar la vista canónica de transcripción, definir el alcance diplomático del vocabulario/numerales y ampliar el control textual independiente sin promover resultados automáticos a validación humana.

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

El inventario canónico contiene **150 remisiones**, todas de clase `Buſca`:

- 60 resoluciones estrictas `exact_unique`;
- 90 `not_located` bajo igualdad normalizada estricta;
- 90/90 `not_located` con revisión editorial explícita;
- 40 `source_supports_unique_target`;
- 22 `source_or_destination_requires_recollation`;
- 5 `candidate_rejected`;
- 23 `target_not_located`;
- 100 aristas en la vista revisada = 60 estrictas + 40 editoriales;
- 0 casos pendientes en la cola inicial de revisión.

Las **22 recolaciones** están ahora materializadas como cola reproducible separada: **8 Tier A, 4 Tier B y 10 Tier C**. No son 22 errores confirmados y no deben resolverse mediante similitud aproximada. El grafo canónico estricto permanece sin modificación editorial silenciosa.

### Fórmula `Lo miſmo`

Las **14/14 ocurrencias** superficiales están inventariadas y cuentan con revisión explícita. Ninguna se transforma automáticamente en remisión, forma cahíta o equivalencia semántica; su función permanece `function_unresolved` salvo evidencia fuente-específica suficiente.

### Otros derivados post-cierre

- 76 registros de evidencia de etiquetas históricas de variedad;
- auditoría de spans físicos;
- exportaciones JSON/JSONL/CSV deterministas;
- hashes SHA-256 verificables.

**Criterio de salida post-cierre:** alcanzado para inventario, remisiones, `Lo miſmo`, derivados y trazabilidad. El remanente lexicográfico para v1.0 se concentra en la política/cotejo de las 22 recolaciones y en la declaración final de limitaciones.

## Fase 4 — Gramática, ejemplos y variación histórica

**Estado:** **cierre técnico alcanzado para las unidades gramaticales numeradas; consolidación filológica activa.**

Hitos fijados:

- secuencia nominal 1–373;
- **370 / 373 números nominales** con reclamación estructurada;
- 127, 178 y 294 documentados como omisiones materiales del impreso;
- el número 129 aparece dos veces y ambas unidades se conservan;
- **371 / 371 unidades numeradas realmente impresas** representadas;
- **302 objetos gramaticales en 24 archivos**;
- **1,215 filas de evidencia**;
- **0 objetos `humanVerified=true`**;
- concordancia y cobertura validadas mediante doble corrida determinista.

Pendientes: segunda colación de microlecturas, consolidación de variación histórica, relación explícita entre reglas y observaciones de variedad, y futura capa analítica moderna separada de la descripción histórica.

## Fase 5 — Control textual, interoperabilidad y reproducibilidad avanzada

**Estado:** **muy avanzada; TEI Lex-0 y empaquetado reproducible ya cerrados técnicamente.**

Estado alcanzado:

- CI sobre `main` y pull requests;
- validación de IDs, JSON Schema, reconciliaciones, autoridad y documentación;
- derivados lexicográficos y gramaticales reproducibles;
- paquete científico de release candidate construido dos veces byte-a-byte idéntico;
- manifiesto de release con inventario, hashes y gates abiertos;
- proyección TEI de **2,302 entradas**, **2,221 citas de traducción**, **150 remisiones** y **60 `@target` estrictos**;
- TEI validado externamente con Jing contra **TEI Lex-0 0.9.5** archivado;
- schema Relax NG fijado por SHA-256 `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`;
- XML TEI validado con SHA-256 `bad06dad39f216b8dde661b4219845c4c19db945bdfbc4478ff5e0846b72e828`;
- el perfil conserva `xml:lang="und"` para la lengua histórica etiquetada como Cahita y no infiere identidad moderna, préstamo ni equivalencia semántica.

### Prioridades restantes

1. cerrar la decisión de alcance **CLDF frente a TEI Lex-0** como derivados complementarios;
2. estabilizar/congelar schemas y metadatos de producción incluidos en v1.0;
3. mantener la cola de 22 recolaciones y resolver únicamente las que puedan cotejarse contra imagen verificable;
4. formalizar metadatos FAIR y preservación;
5. evaluar IIIF sólo si derechos y disponibilidad del facsímil permiten enlaces estables.

**Criterio de salida:** prácticamente alcanzado en reproducibilidad e interoperabilidad TEI; pendiente la decisión CLDF y el congelamiento final.

## Fase 6 — Investigación comparativa

**Estado:** diferida hasta congelar la autoridad editorial de v1.0.

La comparación con recursos modernos de yaqui/mayo deberá modelar correspondencias como candidatos y separar continuidad léxica, semejanza gráfica, traducción, préstamo y cognación. Ninguna comparación moderna debe retroproyectarse automáticamente sobre `ALC1737`.

## Fase 7 — Release científica y preservación

**Estado:** preparación avanzada; todavía no debe etiquetarse como `v1.0.0`.

El paquete científico reproducible ya existe y conserva `releaseReady=false`. Tras la validación Lex-0 quedan como gates sustantivos:

1. política/cotejo de las 22 recolaciones facsimilares;
2. decisión final de alcance CLDF/Lex-0;
3. congelamiento final de schemas, cobertura y metadatos;
4. tag/changelog y GitHub Release;
5. depósito archivístico y DOI específico de versión.

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

1. **fusionar y fijar la validación externa TEI Lex-0 0.9.5**;
2. **cerrar formalmente la decisión CLDF / Lex-0**;
3. **congelar schemas y metadatos del alcance v1.0**;
4. **resolver o congelar transparentemente las 22 recolaciones**;
5. **preparar tag/changelog, GitHub Release y preservación DOI**.

Hasta completar estos pasos, el proyecto debe permanecer en desarrollo/candidata de release y no presentarse como edición filológica humana.
