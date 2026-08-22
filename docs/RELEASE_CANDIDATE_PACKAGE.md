# Cahíta Histórico Digital — paquete científico reproducible de release candidate

Fecha de referencia: 21 de agosto de 2026.

## Propósito

CHD dispone ya de múltiples exportadores deterministas, pero una release científica necesita además un artefacto de distribución único, auditable y reconstruible desde un checkout limpio. `scripts/build_release_candidate.py` crea ese artefacto sin declarar prematuramente `v1.0.0`.

El resultado es `cahita-historico-digital-release-candidate.zip`, acompañado durante la construcción por un directorio expandido y `RELEASE_CANDIDATE_MANIFEST.json`.

## Contenido

El paquete reúne, en subdirectorios separados, las vistas reproducibles que actualmente pasan QA:

- corpus lexicográfico histórico JSONL/JSON/CSV;
- inventario de remisiones `Buſca`;
- grafo estricto de remisiones;
- diagnósticos de candidatos;
- vista editorial revisada de remisiones;
- cola de revisión inicial, actualmente agotada;
- cola explícita de 22 recolaciones facsimilares;
- inventario `Lo miſmo`;
- evidencia histórica de variedad;
- auditoría de spans físicos;
- concordancia gramatical y cobertura numerada;
- proyección TEI lexicográfica experimental;
- documentación, licencias, citación, metadatos de fuente y estado de release.

El facsímil histórico no se incluye. La licencia del repositorio no se usa para relicenciar reproducciones de terceros.

## Estado científico que debe conservar el manifiesto

El paquete debe declarar, como mínimo:

- 2,302 artículos lexicográficos;
- 150 remisiones canónicas `Buſca`;
- 60 aristas estrictas y 4 ciclos;
- 90 revisiones editoriales de `not_located`;
- 100 aristas en la vista revisada;
- 22 casos todavía en cola de recolación directa;
- 302 objetos gramaticales y 1,215 filas de evidencia;
- 370/373 números nominales con reclamación estructurada, con las tres omisiones materiales documentadas;
- 2,302 entradas en la vista TEI;
- `humanVerifiedCount=0`;
- `teiLex0ConformanceClaimed=false`;
- `externalLex0SchemaValidationPerformed=false`;
- `releaseReady=false`.

## Gates que impiden llamar al paquete v1.0.0

El manifiesto mantiene explícitos seis gates abiertos:

1. recolación directa contra facsímil de los 22 casos pendientes;
2. validación externa contra un perfil/schema TEI Lex-0 versionado;
3. decisión final sobre alcance CLDF/Lex-0;
4. congelamiento final de esquemas y metadatos;
5. tag/changelog final de release;
6. depósito archivístico y DOI específico de versión.

## Determinismo

El ZIP se construye con:

- orden léxico fijo de miembros;
- timestamps ZIP fijados en `1980-01-01T00:00:00`;
- permisos normalizados;
- compresión determinista dentro del mismo entorno;
- manifiesto con tamaño y SHA-256 de cada artefacto;
- commit Git de origen registrado.

`scripts/validate_release_candidate.py` construye el paquete dos veces en directorios independientes y exige igualdad byte-a-byte del ZIP, del manifiesto y de todos los invariantes científicos centrales.

Este paquete reduce el gate de “pipeline/paquete reproducible de release” a una infraestructura comprobable, pero no constituye por sí solo una release estable.