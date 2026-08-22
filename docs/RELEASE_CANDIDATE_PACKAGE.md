# Cahíta Histórico Digital — paquete científico reproducible de release candidate

Fecha de corte: 21 de agosto de 2026.

## Propósito

`scripts/build_release_candidate.py` construye un artefacto único, auditable y reproducible sin declarar prematuramente `v1.0.0`.

## Estado científico fijado

El paquete conserva 2,302 artículos lexicográficos, 150 remisiones `Buſca`, 60 aristas estrictas, 90 revisiones editoriales, 100 aristas en la vista revisada, 22 casos de recolación, 302 objetos gramaticales, 1,215 filas de evidencia y 2,302 entradas TEI.

La vista TEI se valida en CI contra TEI Lex-0 0.9.5, usando el schema archivado con SHA-256 `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`.

La decisión de interoperabilidad para v1.0 queda fijada así:

- TEI Lex-0 0.9.5 es el perfil lexicográfico interoperable primario;
- `cldfRequiredForV1=false`;
- CLDF se difiere como derivado analítico posterior a v1.0;
- la decisión completa está en `docs/CLDF_SCOPE_DECISION_V1_0.md`;
- ningún formato interoperable sustituye la representación canónica curatorial.

El facsímil histórico no se incluye, no se relicencian reproducciones de terceros y `humanVerifiedCount=0` se mantiene donde corresponde.

## Gates abiertos para v1.0.0

Tras cerrar TEI Lex-0 y el alcance CLDF quedan cuatro gates:

1. tratamiento final de las 22 recolaciones directas contra facsímil;
2. congelamiento de esquemas, contratos de datos y metadatos;
3. tag y changelog final;
4. depósito archivístico y DOI de versión/Concept DOI cuando corresponda.

## Determinismo

El ZIP usa orden fijo de miembros, timestamps normalizados, permisos normalizados y manifiesto con tamaño/SHA-256 de cada artefacto y commit de origen. `scripts/validate_release_candidate.py` lo construye dos veces y exige igualdad byte-a-byte. También exige que la decisión CLDF permanezca explícita y no vuelva a aparecer como gate de v1.0.

El paquete sigue siendo una **release candidate**, no una release estable, mientras estos cuatro gates permanezcan abiertos.
