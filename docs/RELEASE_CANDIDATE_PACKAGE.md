# Cahíta Histórico Digital — paquete científico reproducible de release candidate

Fecha de corte: 21 de agosto de 2026.

## Propósito

`scripts/build_release_candidate.py` construye un artefacto único, auditable y reproducible desde los datos y exportadores versionados de CHD sin declarar prematuramente `v1.0.0`.

El resultado es `cahita-historico-digital-release-candidate.zip`, acompañado durante la construcción por un directorio expandido y `RELEASE_CANDIDATE_MANIFEST.json`.

## Contenido

El paquete reúne corpus lexicográfico JSONL/JSON/CSV; inventario y grafo de remisiones; diagnósticos y vista editorial revisada; cola inicial agotada y cola explícita de 22 recolaciones; inventario `Lo miſmo`; evidencia histórica de variedad; auditoría de spans físicos; concordancia y cobertura gramatical; vista TEI Lex-0 0.9.5; documentación, licencias, citación y metadatos de fuente.

El facsímil histórico no se incluye y las reproducciones de terceros no se relicencian.

## Estado científico fijado

La corrida vigente exige:

- 2,302 artículos lexicográficos;
- 150 remisiones canónicas `Buſca`;
- 60 aristas estrictas y 4 ciclos;
- 90 revisiones editoriales de `not_located`;
- 100 aristas en la vista revisada;
- 22 casos en cola de recolación directa;
- 302 objetos gramaticales y 1,215 filas de evidencia;
- 370/373 números nominales con reclamación estructurada;
- 2,302 entradas TEI;
- conformidad TEI Lex-0 0.9.5 respaldada por CI contra el schema archivado SHA-256 `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`;
- `humanVerifiedCount=0`;
- `releaseReady=false`.

La última batería verde de esta rama produjo un ZIP de **600,630 bytes**, SHA-256 `0ee719535b2014f88e05c12cce620192ce15173fc21c1d364b643901c65a9217`, con **60 archivos** y **9,173,536 bytes** de artefactos inventariados antes de compresión.

## Gates abiertos para v1.0.0

Tras cerrar la validación TEI Lex-0, quedan cinco gates explícitos:

1. decidir y documentar el tratamiento final de las 22 recolaciones directas contra facsímil;
2. cerrar la decisión de alcance CLDF frente a la vista TEI Lex-0 ya validada;
3. congelar esquemas y metadatos de producción;
4. preparar tag y changelog final de release;
5. realizar depósito archivístico y registrar DOI de versión/Concept DOI cuando corresponda.

## Determinismo

El ZIP usa orden fijo de miembros, timestamps normalizados a `1980-01-01T00:00:00`, permisos normalizados y manifiesto con tamaño/SHA-256 de cada artefacto y commit Git de origen. `scripts/validate_release_candidate.py` construye el paquete dos veces de manera independiente y exige igualdad byte-a-byte.

El paquete demuestra que el gate de infraestructura de empaquetado está técnicamente resuelto; sigue siendo una **release candidate**, no una release estable, mientras los cinco gates anteriores permanezcan abiertos.
