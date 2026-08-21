# Cobertura de Cahíta Histórico Digital

Estado canónico de cobertura de `ALC1737` — **21 de agosto de 2026**.

> El estado detallado que `COVERAGE.md` mostraba el 16 de agosto de 2026 se conserva íntegramente, sin reescritura retroactiva, en [`docs/COVERAGE_SNAPSHOT_2026-08-16.md`](docs/COVERAGE_SNAPSHOT_2026-08-16.md). Este archivo principal presenta únicamente el estado vigente y los criterios de trabajo actuales.

## Resumen ejecutivo

Cahíta Histórico Digital ha alcanzado **cierre técnico de las dos grandes capas estructurales históricas** del testimonio procesado:

- **vocabulario castellano–cahíta:** 45/45 páginas digitales, p.133–177, técnicamente cerradas en fronteras y representación de artículos;
- **gramática numerada:** 371/371 unidades numeradas efectivamente impresas representadas estructuralmente.

El cierre técnico significa que las unidades y fronteras históricas dentro del alcance declarado están modeladas y pasan QA computacional. **No significa validación filológica humana, edición crítica definitiva ni release científica estable.** Todos los objetos IA-asistidos conservan `humanVerified=false`.

## Fuente y paginación

- Fuente primaria de autoridad: `ALC1737`.
- Volumen digital procesado: **182 páginas digitales**.
- Cuerpo gramatical impreso paginado: páginas digitales **15–132**, equivalentes a impresas **1–118**.
- Vocabulario castellano–cahíta: páginas digitales **133–177**.
- Sistema numeral: páginas digitales **178–180**.
- Material final: páginas digitales **181–182**.

La procedencia bibliográfica y material se documenta en [`docs/SOURCE_ALC1737.md`](docs/SOURCE_ALC1737.md) y [`PROVENANCE.md`](PROVENANCE.md).

## Cobertura lexicográfica vigente

### Inventario y corpus

- **2,072** candidatos lexicográficos canónicos `hybrid_margin_mode_v0.2`.
- **2,302** artículos históricos estructurados.
- **211** archivos JSONL de artículos históricos en el estado post-cierre actual.
- **2,302** `articleId` únicos.
- **0** artículos `human_verified`.

El inventario canónico de candidatos es reconstruible y verificable por SHA-256 mediante `scripts/reconstruct_candidate_inventory.py`.

### Cierre de páginas

- Vocabulario p.133–177: **45/45 páginas** con reconciliación candidate-level completa y cierre técnico IA-asistido.
- Phase II p.145–177: **33/33 páginas** con censo visible exhaustivo.
- Phase II p.145–177: **33/33 páginas** con cierre técnico.
- `pendingPromotionTotal = 0`.
- `unresolvedCandidateTotal = 0` dentro del alcance estructural de Phase II.
- `ambiguousBoundaryTotal = 0`.

La fuente computacional vigente para estos totales es [`data/lexicon/reconciliation/phase2_open_work_summary.json`](data/lexicon/reconciliation/phase2_open_work_summary.json), regenerada por `scripts/summarize_open_lexicon_work.py`.

### Qué permanece abierto dentro del léxico

El cierre de fronteras y promociones no elimina problemas de microestructura. Permanecen, entre otros:

- lecturas internas marcadas como `unresolved`;
- remisiones históricas cuyo destino no se resuelve por igualdad estricta;
- anáforas superficiales `Lo miſmo` pendientes de interpretación controlada;
- continuidades transcolumna/transpágina y `sourceSpans` que merecen auditoría adicional;
- etiquetas históricas de variedad cuya interpretación moderna no debe inferirse automáticamente.

## Remisiones históricas del vocabulario

Los derivados post-cierre registran:

- **151** remisiones históricas en total;
- **150** de clase `Buſca`;
- **60** resoluciones `exact_unique` mediante igualdad normalizada estricta;
- **90** remisiones `Buſca` con estado `not_located` bajo esa política estricta;
- **1** remisión que no pertenece a la clase `Buſca`;
- **4** ciclos exactos, preservados como propiedades del grafo y no “corregidos”.

Estos números proceden de `scripts/export_lexicon_crossreferences.py` y `scripts/export_lexicon_crossreference_graph.py`. La política vigente **no ensancha automáticamente** la resolución mediante similitud gráfica, semántica o contención parcial.

## Otras capas derivadas del vocabulario

- **14** artículos candidatos con fórmula superficial `Lo miſmo`.
- **76** registros de evidencia de etiquetas históricas de variedad en **65** artículos.
- **12** artículos con metadatos físicos auditables mediante el exportador post-cierre; **0** señalados actualmente por problemas estructurales en esa auditoría.

Estas cifras son derivados reproducibles, no nuevas fuentes de verdad editorial.

## Cobertura gramatical vigente

### Resultado de cierre

La secuencia nominal del Arte va de 1 a 373, pero el impreso presenta anomalías materiales:

- **127 omitido**: secuencia visible 126 → 128;
- **129 duplicado**: dos reglas sucesivas llevan impreso el mismo número;
- **178 omitido**: secuencia visible 177 → 179;
- **294 omitido**: la regla 293 continúa y el siguiente número visible es 295.

En consecuencia:

- **370/373 números nominales** tienen reclamación estructurada explícita;
- los 3 números restantes —127, 178 y 294— son omisiones materiales documentadas, no trabajo de estructuración pendiente;
- existen **370 números distintos efectivamente impresos**;
- al conservar las dos unidades impresas como 129, el testimonio contiene **371 unidades numeradas efectivas**;
- CHD representa **371/371 unidades numeradas efectivamente impresas**.

Las anomalías se documentan en `data/grammar/metadata/` y el cierre en [`docs/GRAMMAR_COMPLETION_2026-08-21.md`](docs/GRAMMAR_COMPLETION_2026-08-21.md).

### Concordancia y evidencia

La QA gramatical post-cierre registra:

- **302 objetos gramaticales**;
- **24 archivos** de objetos gramaticales;
- **1,215 filas de evidencia explícita**;
- `humanVerified = 0`;
- auditoría de cobertura: **370/373** números nominales, con 3 huecos materiales documentados;
- doble ejecución determinista byte-a-byte de concordancia y cobertura.

Los 302 objetos no tienen por qué coincidir uno a uno con las 371 unidades impresas: algunos objetos estructurados abarcan rangos de reglas o construcciones históricas que constituyen una sola entidad analítica documentada.

## Transcripción

La capa de transcripción cubre de forma continua el cuerpo gramatical y dispone de **128 páginas `full_page`** en el estado documentado por la hoja de ruta. Las transcripciones distinguen texto, estructura, material no textual e incertidumbres. `machine_corrected_unverified` no equivale a transcripción diplomática humana.

El trabajo textual abierto se concentra ahora en:

- segunda colación de tokens y ejemplos de baja confianza;
- consolidación de una vista canónica de avance de transcripción;
- alcance diplomático final del vocabulario y numerales;
- control textual independiente cuando exista un testimonio apropiado y accesible.

## Incidencias materiales y editoriales que permanecen relevantes

Entre las incidencias que deben conservarse visibles están:

- `obra tripartita` frente a la estructura material en cuatro partes;
- las omisiones impresas 127, 178 y 294;
- la duplicación impresa de 129;
- discrepancias históricas/OCR en numeración que ya no deben confundirse con unidades inventadas;
- la discontinuidad material F→H entre p.157–158;
- continuidades y reclamos como `Lucer-` p.161→162;
- microlecturas específicas mantenidas como `unresolved`;
- correcciones versionadas de lecturas seleccionadas y metadatos físicos.

La existencia de estas incidencias es compatible con el cierre técnico: están modeladas o explícitamente abiertas, no ocultas.

## QA y reproducibilidad

El workflow `CHD QA` verifica actualmente, entre otros componentes:

- reconstrucción del inventario canónico de candidatos;
- unicidad y estados de autoridad de artículos;
- validación JSON Schema del corpus histórico;
- reconciliaciones y capas de falsos negativos;
- sintaxis de metadatos centrales;
- invariantes de Phase II y sincronía de su resumen canónico;
- sincronización documental básica;
- derivados post-cierre en doble ejecución;
- concordancia gramatical y auditoría de cobertura en doble ejecución determinista.

Una corrida verde certifica **consistencia computacional del estado versionado**, no autoridad filológica humana.

## Fuentes de control textual

- `ALC1737`: autoridad primaria.
- `BUE1890`: reimpresión histórica de control secundaria; nunca sustituye silenciosamente una lectura de 1737.
- `BNF1737-REPORTED`: noticia bibliográfica de un ejemplar independiente reportado; requiere verificación directa antes de utilizarse como testimonio de control.

## Prioridades de cobertura después del cierre técnico

El trabajo ya no debe orientarse a “encontrar más artículos” o “rellenar números de regla”. Las prioridades son:

1. revisar conservadoramente las **90 remisiones `Buſca` `not_located`**, separando candidatos diagnósticos de resoluciones aceptadas;
2. analizar las **14** fórmulas `Lo miſmo` sin resolver anáforas por automatismo;
3. consolidar y enlazar las **76** evidencias de variedad histórica;
4. ejecutar segunda colación priorizada de microlecturas `unresolved` y continuidades físicas;
5. mejorar control textual y procedencia de testimonios secundarios;
6. preparar perfiles TEI y derivados interoperables sin alterar la capa canónica;
7. mantener README, ROADMAP, COVERAGE y métricas computacionales sincronizados;
8. preparar gradualmente una futura release científica, sin adelantar `v1.0.0`, DOI o validación humana inexistentes.

## Historial de cobertura

Para conservar la evolución verificable del corpus, el snapshot completo anterior de este documento queda archivado en:

- [`docs/COVERAGE_SNAPSHOT_2026-08-16.md`](docs/COVERAGE_SNAPSHOT_2026-08-16.md).

Los cierres de las dos capas principales se documentan además en:

- [`docs/PHASE2_COMPLETION_2026-08-21.md`](docs/PHASE2_COMPLETION_2026-08-21.md);
- [`docs/GRAMMAR_COMPLETION_2026-08-21.md`](docs/GRAMMAR_COMPLETION_2026-08-21.md).

## Principio de interpretación

**Cobertura estructural completa no es sinónimo de lectura filológica completa.** CHD conserva la diferencia entre lo que está localizado y modelado, lo que está leído con incertidumbre, lo que ha sido inferido en capas explícitas y lo que todavía necesita control especializado.
