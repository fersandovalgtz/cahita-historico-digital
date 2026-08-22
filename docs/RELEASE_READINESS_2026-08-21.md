# Cahíta Histórico Digital — estado de preparación para v1.0

Fecha de corte: **21 de agosto de 2026**.

## Resumen ejecutivo

Cahíta Histórico Digital está en fase de cierre de release, no de construcción gruesa del corpus. El vocabulario y la gramática numerada tienen cierre técnico; las 90 remisiones `Buſca` inicialmente no localizadas tienen revisión editorial explícita; `Lo miſmo` está separado del grafo; los principales derivados son deterministas; existe un paquete científico reproducible; y la vista TEI pasa el schema oficial archivado de **TEI Lex-0 0.9.5** mediante Jing dentro del CI.

Para una **v1.0 técnica, reproducible y científicamente publicable dentro del alcance declarado**, la preparación se estima ahora en **91–93 %**. El intervalo refleja que los gates restantes tienen costes desiguales y algunos dependen del acceso al testimonio o de infraestructura externa de preservación.

Esta estimación no mide validación filológica humana. Los estados `humanVerified=false` se conservan y una edición revisada por especialistas sigue siendo una meta distinta.

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
- cola de recolación directa: 22 casos = 8 A / 4 B / 10 C, determinista y auditable.
- 14/14 fórmulas `Lo miſmo` auditadas, 0 convertidas en remisión canónica.

### Interoperabilidad TEI

La vista vigente contiene 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 targets estrictos. Conserva las formas históricas de lengua meta como `xml:lang="und"` y no infiere identidad lingüística moderna.

El CI valida el XML contra `https://lex-0.org/releases/v0.9.5/schema/lex-0.rng`, cuyo SHA-256 está fijado en `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`. La corrida verde produjo XML de 1,391,422 bytes, SHA-256 `bad06dad39f216b8dde661b4219845c4c19db945bdfbc4478ff5e0846b72e828`.

### Release candidate reproducible

`scripts/build_release_candidate.py` y `scripts/validate_release_candidate.py` construyen el paquete dos veces y exigen igualdad byte-a-byte. Tras cerrar el gate Lex-0, la corrida vigente produjo:

- 60 archivos en el paquete;
- 9,173,536 bytes de artefactos inventariados;
- ZIP de 600,630 bytes;
- SHA-256 `0ee719535b2014f88e05c12cce620192ce15173fc21c1d364b643901c65a9217`;
- `openGates=5`;
- `releaseReady=false`;
- `humanVerified=0`.

## Cinco gates restantes

### A — 22 recolaciones

Cada caso debe cotejarse contra imagen del mismo testimonio cuando sea posible o congelarse como incertidumbre editorial explícita. El OCR no sustituye el facsímil y la similitud diagnóstica no produce enlaces canónicos.

### B — decisión CLDF

Debe decidirse si una vista CLDF aporta suficiente valor como producto v1.0 o si, por la naturaleza histórico-diccionarística de CHD, TEI Lex-0 constituye el formato interoperable principal y CLDF queda para una futura proyección analítica normalizada.

### C — congelamiento de contratos y metadatos

Falta declarar qué schemas/formatos son estables en v1.0, fijar sus versiones, congelar cobertura y limitaciones, y sincronizar `CITATION.cff`, `codemeta.json` y changelog.

### D — tag/release final

El paquete reproducible existe, pero falta construirlo desde el commit definitivo, registrar el hash final y crear el tag estable sólo después de cerrar los gates científicos seleccionados.

### E — preservación

Faltan GitHub Release, depósito archivístico y DOI de versión/Concept DOI cuando corresponda.

## Qué significa terminar

Una v1.0 válida no requiere ocultar incertidumbres ni atribuir revisión humana inexistente. Requiere un alcance estable, incertidumbres explícitas, derivados interoperables, checksums, metadatos, un procedimiento de reconstrucción y preservación duradera.

El siguiente orden de cierre es: **decisión CLDF → congelamiento de schemas/metadatos → política/cotejo de recolaciones → candidata final y changelog → preservación/DOI**, manteniendo las recolaciones abiertas cuando no exista acceso verificable a imagen y sin convertir OCR en evidencia facsimilar.
