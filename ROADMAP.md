# Hoja de ruta

Estado de planificación de Cahíta Histórico Digital (`ALC1737`) — actualización **21 de agosto de 2026**.

## Principio rector

CHD avanza por capas de evidencia con procedencia, autoridad y criterios de salida explícitos. El cierre técnico no se presenta como validación filológica humana y ningún derivado interoperable sustituye la representación curatorial canónica.

## Fase 0 — Infraestructura científica

**Estado:** completada para la etapa de investigación activa; mantenimiento continuo.

El repositorio dispone de procedencia, política editorial, licencias, citación, esquemas JSON, estados de autoridad, QA automatizado, exportadores deterministas, control documental y paquete científico reproducible.

## Fase 1 — Ingestión de `ALC1737`

**Estado:** completada el 15 de agosto de 2026.

Quedaron fijados el manifiesto de 182 páginas, mapeo de paginación, segmentación del volumen, fe de erratas, OCR regenerable, hashes de fuente y scripts de ingestión.

## Fase 2 — Transcripción histórico-digital

**Estado:** activa; la cobertura gramatical superficial es continua, pero la edición textual completa no está congelada.

Hay 128 páginas `full_page`, preliminares y Partes I–IV representadas y estados de autoridad diferenciados. Se mantienen **0 páginas `human_verified`**. La consolidación diplomática integral permanece como trabajo filológico posterior y no bloquea una v1.0 histórico-digital de alcance declarado.

## Fase 3 — Corpus lexicográfico

**Estado:** **cierre técnico alcanzado; control filológico post-cierre activo.**

- 2,072/2,072 candidatos canónicos reconstruibles.
- 2,302 artículos históricos en 211 JSONL.
- 45/45 páginas p.133–177 reconciliadas.
- Phase II p.145–177: **33 / 33 páginas** cerradas técnicamente.
- `pendingPromotionTotal = 0`, `unresolvedCandidateTotal = 0`, `ambiguousBoundaryTotal = 0`.
- 0 artículos `human_verified`.

### Remisiones `Buſca`

150 remisiones canónicas: 60 `exact_unique`, 90 `not_located`, 4 ciclos estrictos. Las 90 no localizadas tienen revisión explícita: 40 destinos sustentados, 22 recolaciones, 5 candidatos rechazados y 23 destinos no localizados. La vista revisada contiene 100 aristas = 60 estrictas + 40 editoriales.

Las 22 recolaciones están en una cola reproducible: **8 Tier A, 4 Tier B, 10 Tier C**. No son errores confirmados y no se resuelven por similitud aproximada.

### `Lo miſmo`

14/14 ocurrencias inventariadas y revisadas; ninguna convertida automáticamente en remisión, forma cahíta o equivalencia semántica.

## Fase 4 — Gramática, ejemplos y variación histórica

**Estado:** **cierre técnico alcanzado para la cobertura numerada; consolidación filológica activa.**

- secuencia nominal 1–373;
- 370/373 números con reclamación estructurada;
- 127, 178 y 294 son omisiones materiales del impreso;
- 129 aparece dos veces y ambas unidades se conservan;
- 371/371 unidades numeradas realmente impresas representadas;
- 302 objetos gramaticales en 24 archivos;
- 1,215 filas de evidencia;
- 0 objetos `humanVerified=true`.

## Fase 5 — Interoperabilidad, contratos y reproducibilidad

**Estado:** **cerrada técnicamente para el alcance de v1.0.**

Hitos:

- CI sobre `main` y pull requests;
- derivados lexicográficos y gramaticales reproducibles;
- paquete científico reconstruido dos veces byte-a-byte;
- TEI: 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 `@target` estrictos;
- validación externa con Jing contra TEI Lex-0 0.9.5 archivado;
- schema Lex-0 fijado por SHA-256 `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`;
- TEI Lex-0 como perfil interoperable primario de v1.0;
- CLDF diferido como derivado analítico posterior;
- **22 JSON Schema + 4 metadatos fuente congelados como 26 contratos v1.0**;
- manifiesto de contratos SHA-256 `c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56`;
- CI bloquea deriva silenciosa de esos contratos.

Los metadatos de identidad de release (`CITATION.cff`, `codemeta.json`, versión/tag y DOI) se finalizan después de resolver o congelar las recolaciones, porque deben reflejar el commit/tag definitivo.

## Fase 6 — Investigación comparativa

**Estado:** diferida hasta después de v1.0.

Las comparaciones con recursos modernos de yaqui/mayo deberán modelarse como candidatos y separar continuidad léxica, semejanza gráfica, traducción, préstamo y cognación. Ninguna comparación moderna se retroproyectará automáticamente sobre `ALC1737`.

## Fase 7 — Release científica y preservación

**Estado:** **candidata avanzada; tres gates restantes.**

1. **Recolaciones:** cotejar contra imagen verificable los 22 casos cuando sea posible o congelarlos transparentemente como incertidumbres explícitas.
2. **Tag/release:** congelar bytes finales de datos, sincronizar `CITATION.cff`/`codemeta.json`, preparar changelog, reconstruir el ZIP definitivo y registrar su hash antes del tag.
3. **Preservación:** GitHub Release, depósito archivístico y DOI de versión/Concept DOI cuando corresponda.

La infraestructura, interoperabilidad y contratos ya no son gates abiertos.

## Productos científicos previstos

1. edición histórico-digital del *Arte* de 1737;
2. dataset lexicográfico abierto;
3. corpus gramatical y de ejemplos;
4. dataset de variación histórica;
5. artículo de datos/metodología;
6. estudios lingüísticos e historiográficos especializados;
7. concordancias y herramientas de consulta;
8. estudios comparativos diacrónicos posteriores;
9. modelo replicable para otras fuentes cahítas históricas.

## Prioridad inmediata

1. **cerrar la política y, cuando exista imagen verificable, el cotejo de las 22 recolaciones**;
2. **preparar la candidata final, changelog y metadatos de identidad desde el commit definitivo**;
3. **crear tag/GitHub Release y ejecutar preservación/DOI**.

Hasta completar esos tres gates, el proyecto debe permanecer en candidata de release y no presentarse como edición filológica humana.
