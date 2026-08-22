# Hoja de ruta

Estado de planificación de Cahíta Histórico Digital (`ALC1737`) — actualización **22 de agosto de 2026**.

## Principio rector

CHD avanza por capas de evidencia con procedencia, autoridad y criterios de salida explícitos. El cierre técnico no se presenta como validación filológica humana y ningún derivado interoperable sustituye la representación curatorial canónica.

## Fase 0 — Infraestructura científica

**Estado:** completada para la etapa de investigación activa; mantenimiento continuo.

El repositorio dispone de procedencia, política editorial, licencias, citación, esquemas JSON, estados de autoridad, QA automatizado, exportadores deterministas, control documental y paquetes científicos reproducibles.

## Fase 1 — Ingestión de `ALC1737`

**Estado:** completada el 15 de agosto de 2026.

Quedaron fijados el manifiesto de 182 páginas, mapeo de paginación, segmentación del volumen, fe de erratas, OCR regenerable, hashes de fuente y scripts de ingestión.

## Fase 2 — Transcripción histórico-digital

**Estado:** cobertura técnica suficiente para v1.0; consolidación diplomática integral post-v1.

Hay 128 páginas `full_page`, preliminares y Partes I–IV representadas y estados de autoridad diferenciados. Se mantienen **0 páginas `human_verified`**. La consolidación diplomática integral permanece como trabajo filológico posterior y no bloqueó la v1.0 de alcance declarado.

## Fase 3 — Corpus lexicográfico

**Estado:** **cierre técnico alcanzado; control filológico post-v1 activo.**

- 2,072/2,072 candidatos canónicos reconstruibles.
- 2,302 artículos históricos en 211 JSONL.
- 45/45 páginas p.133–177 reconciliadas.
- Phase II p.145–177: **33 / 33 páginas** cerradas técnicamente.
- `pendingPromotionTotal = 0`, `unresolvedCandidateTotal = 0`, `ambiguousBoundaryTotal = 0`.
- 0 artículos `human_verified`.

### Remisiones `Buſca`

150 remisiones canónicas: 60 `exact_unique`, 90 `not_located`, 4 ciclos estrictos. Las 90 no localizadas tienen revisión explícita: 40 destinos sustentados, 22 recolaciones, 5 candidatos rechazados y 23 destinos no localizados. La vista revisada contiene 100 aristas = 60 estrictas + 40 editoriales.

Las 22 recolaciones se conservan en v1.0 como `frozen_open_uncertainty`: 8 A, 4 B y 10 C. No se selecciona destino por esta capa, no se modifica el grafo canónico y `humanVerified=false`. La resolución filológica continúa post-v1.

### `Lo miſmo`

14/14 ocurrencias inventariadas y revisadas; ninguna convertida automáticamente en remisión, forma cahíta o equivalencia semántica.

## Fase 4 — Gramática, ejemplos y variación histórica

**Estado:** **cierre técnico alcanzado para la cobertura numerada; consolidación filológica post-v1.**

- secuencia nominal 1–373;
- 370/373 números con reclamación estructurada;
- 127, 178 y 294 son omisiones materiales del impreso;
- 129 aparece dos veces y ambas unidades se conservan;
- 371/371 unidades numeradas realmente impresas representadas;
- 302 objetos gramaticales en 24 archivos;
- 1,215 filas de evidencia;
- 0 objetos `humanVerified=true`.

## Fase 5 — Interoperabilidad, contratos y reproducibilidad

**Estado:** **cerrada para v1.0.**

Hitos:

- CI sobre `main` y pull requests;
- derivados lexicográficos y gramaticales reproducibles;
- TEI: 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 `@target` estrictos;
- validación externa con Jing contra TEI Lex-0 0.9.5 archivado;
- schema Lex-0 fijado por SHA-256 `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`;
- TEI Lex-0 como perfil interoperable primario de v1.0;
- CLDF diferido como derivado analítico posterior;
- 22 JSON Schema + 4 metadatos fuente congelados como 26 contratos v1.0;
- manifiesto de contratos SHA-256 `c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56`;
- freeze byte-exacto de 267 archivos científicos / 2,698,997 bytes;
- CI bloquea deriva silenciosa de contratos y datos científicos congelados;
- disposición v1.0 de recolaciones validada 22/22, con cero cambios canónicos.

## Fase 6 — Investigación comparativa

**Estado:** diferida hasta después de v1.0.

Las comparaciones con recursos modernos de yaqui/mayo deberán modelarse como candidatos y separar continuidad léxica, semejanza gráfica, traducción, préstamo y cognación. Ninguna comparación moderna se retroproyectará automáticamente sobre `ALC1737`.

## Fase 7 — Release científica y preservación

**Estado:** **publicación GitHub v1.0.0 cerrada y atestada; preservación archivística pendiente.**

La identidad `1.0.0` quedó fijada y publicada:

- tag inmutable `v1.0.0` → `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`;
- GitHub Release estable: `https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0`;
- ZIP final: 1,076,296 bytes; SHA-256 `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`;
- `RELEASE_MANIFEST.json`: 67,757 bytes; SHA-256 `05970080840ed0cde9c4ca67b40432b492ba2f0afadade5efe2b9d0f60b8cb79`;
- `SHA256SUMS.txt` verificado;
- atestación durable en `release/github_release_attestation_v1.0.0.json`.

La atestación reconstruye v1.0.0 desde el tag inmutable y exige que ZIP y manifiesto sean byte-idénticos a los assets publicados. La metodología se documenta en `docs/RELEASE_PUBLICATION_2026-08-22.md`.

Después de la publicación GitHub queda un único gate externo:

1. **Preservación:** depósito archivístico, DOI de versión y Concept DOI cuando sean efectivamente asignados.

Hasta entonces `versionDoi=null`, `conceptDoi=null` y `doiInferred=false`. El gate se rastrea en el issue #169.

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

1. **depositar v1.0.0 en Zenodo u otro repositorio de preservación y registrar DOI reales**;
2. **sincronizar los DOI a metadatos post-release sin mover ni reescribir el tag**;
3. **retomar post-v1 el cotejo filológico de las 22 incertidumbres cuando exista evidencia admisible**;
4. **desarrollar productos académicos y analíticos derivados sin alterar retrospectivamente la evidencia de v1.0**.

La v1.0.0 se presenta como release científica técnica y reproducible dentro de su alcance documentado, no como edición filológica humana integral.
