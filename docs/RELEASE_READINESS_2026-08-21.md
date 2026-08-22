# Cahíta Histórico Digital — estado de preparación para v1.0

Fecha de corte: **21 de agosto de 2026**.

## Resumen ejecutivo

Cahíta Histórico Digital está en fase de cierre de release, no de construcción gruesa del corpus. El vocabulario y la gramática numerada tienen cierre técnico; las 90 remisiones `Buſca` inicialmente no localizadas tienen revisión editorial explícita; `Lo miſmo` está separado del grafo; los principales derivados son deterministas; existe un paquete científico reproducible; y la vista TEI pasa el schema oficial archivado de **TEI Lex-0 0.9.5** mediante Jing dentro del CI.

La decisión de interoperabilidad para v1.0 también está cerrada: **TEI Lex-0 0.9.5 es el perfil lexicográfico interoperable primario; CLDF no es requisito de v1.0 y queda diferido como derivado analítico futuro**. La justificación y condiciones de reapertura se registran en `docs/CLDF_SCOPE_DECISION_V1_0.md`.

Para una **v1.0 técnica, reproducible y científicamente publicable dentro del alcance declarado**, la preparación se estima ahora en **93–95 %**. Esta estimación no mide validación filológica humana: los estados `humanVerified=false` se conservan y una edición revisada por especialistas sigue siendo una meta distinta.

## Evidencia cerrada

### Corpus

- 2,072/2,072 candidatos canónicos reconstruibles.
- 2,302 artículos históricos en 211 archivos JSONL.
- 45/45 páginas p.133–177 reconciliadas; Phase II 33/33 técnicamente cerrada.
- 371/371 unidades gramaticales numeradas realmente impresas representadas.
- 302 objetos gramaticales y 1,215 filas de evidencia.

### Remisiones y microestructura

- 150 referencias canónicas, todas `Buſca`.
- 60 `exact_unique`, 90 `not_located`, 4 ciclos estrictos.
- 90/90 `not_located` con revisión editorial: 40 destinos sustentados, 22 recolaciones, 5 candidatos rechazados y 23 destinos no localizados.
- vista revisada: 100 aristas = 60 estrictas + 40 editoriales.
- cola inicial A/B/C agotada.
- cola de recolación directa: 22 casos = 8 A / 4 B / 10 C.
- 14/14 fórmulas `Lo miſmo` auditadas, 0 convertidas en remisión canónica.

### Interoperabilidad

La vista TEI contiene 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 targets estrictos. Conserva las formas históricas de lengua meta como `xml:lang="und"` y no infiere identidad lingüística moderna.

El CI valida el XML contra `https://lex-0.org/releases/v0.9.5/schema/lex-0.rng`, cuyo SHA-256 está fijado en `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`. El XML validado tiene SHA-256 `bad06dad39f216b8dde661b4219845c4c19db945bdfbc4478ff5e0846b72e828`.

CLDF se evaluó como alternativa/complemento. Dado que `ALC1737` está estructurado históricamente castellano → cahíta, una proyección CLDF Dictionary exige decisiones adicionales sobre unidad de entrada, variante, sentido e identidad lingüística. Estas decisiones no se fuerzan para v1.0; CLDF permanece disponible para una fase analítica posterior con trazabilidad completa a `articleId` y validación `pycldf`.

### Release candidate reproducible

`scripts/build_release_candidate.py` y `scripts/validate_release_candidate.py` construyen el paquete dos veces y exigen igualdad byte-a-byte. El manifiesto registra la decisión de interoperabilidad y exige:

- `primaryLexicalReleaseProfile="TEI Lex-0 0.9.5"`;
- `cldfRequiredForV1=false`;
- `cldfStatus="deferred_post_v1_analytic_derivative"`;
- `canonicalDataReplacedByInteroperabilityFormats=false`;
- `releaseReady=false`;
- `humanVerifiedCount=0`.

El hash del paquete cambia legítimamente cuando cambia la documentación/manifest de release y sólo se congelará en el commit candidato final.

## Cuatro gates restantes

### A — 22 recolaciones

Cada caso debe cotejarse contra imagen del mismo testimonio cuando sea posible o congelarse como incertidumbre editorial explícita. El OCR no sustituye el facsímil y la similitud diagnóstica no produce enlaces canónicos.

### B — congelamiento de contratos y metadatos

Falta declarar qué schemas/formatos son estables en v1.0, fijar sus versiones, congelar cobertura y limitaciones y sincronizar `CITATION.cff`, `codemeta.json` y changelog.

### C — tag/release final

El paquete reproducible existe, pero debe reconstruirse desde el commit definitivo, registrar su hash final y crear el tag estable sólo después de cerrar los gates científicos seleccionados.

### D — preservación

Faltan GitHub Release, depósito archivístico y DOI de versión/Concept DOI cuando corresponda.

## Qué significa terminar

Una v1.0 válida no requiere ocultar incertidumbres ni atribuir revisión humana inexistente. Requiere un alcance estable, incertidumbres explícitas, derivados interoperables, checksums, metadatos, procedimiento de reconstrucción y preservación duradera.

El siguiente orden de cierre es: **congelamiento de schemas/metadatos → política/cotejo de recolaciones → candidata final y changelog → preservación/DOI**. Si una recolación no puede resolverse con imagen verificable, puede congelarse transparentemente como incertidumbre; no debe resolverse por OCR o similitud.
