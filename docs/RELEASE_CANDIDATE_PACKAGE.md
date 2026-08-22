# Cahíta Histórico Digital — paquete científico reproducible de release candidate

Fecha de corte: 21 de agosto de 2026.

## Propósito

`scripts/build_release_candidate.py` construye un artefacto único, auditable y reproducible sin declarar prematuramente `v1.0.0`.

## Estado científico fijado

El paquete conserva 2,302 artículos lexicográficos, 150 remisiones `Buſca`, 60 aristas estrictas, 90 revisiones editoriales, 100 aristas en la vista revisada, 22 casos de recolación, 302 objetos gramaticales, 1,215 filas de evidencia y 2,302 entradas TEI.

La vista TEI se valida en CI contra TEI Lex-0 0.9.5, usando el schema archivado SHA-256 `35e73fef48526634714bdf3d16b924f958fca078a903d0bdc2dd4d7d116d1aaa`. TEI Lex-0 es el perfil interoperable primario de v1.0 y CLDF queda diferido como derivado analítico posterior.

## Freeze de contratos v1.0

El paquete incorpora `release/v1_contract_manifest.json`, que congela por bytes exactos:

- 22 JSON Schema de producción;
- 4 archivos de metadatos fuente que fijan el alcance de `ALC1737`;
- 26 contratos en total.

SHA-256 del manifiesto: `c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56`.

`scripts/validate_v1_contract_freeze.py` regenera el inventario y falla ante cualquier contrato añadido, eliminado o alterado. Todos los schemas congelados declaran JSON Schema Draft 2020-12 y mantienen `$id` únicos.

Los metadatos de identidad de release (`CITATION.cff`, `codemeta.json`, versión/tag y DOI) quedan deliberadamente fuera de este freeze: se finalizan en el gate de tag/release y no se consideran una excepción al contrato.

## Disposición de las 22 recolaciones

El paquete incorpora `docs/V1_RECOLLATION_DISPOSITION.md` y un derivado reproducible generado por `scripts/export_v1_recollation_disposition.py`.

Los 22 casos se publican en v1.0 como `frozen_open_uncertainty`, con identidad 22/22 respecto de la cola canónica, distribución 8 A / 4 B / 10 C, `canonicalAction=none`, cero destinos seleccionados, cero cambios canónicos y `humanVerified=false`.

Esta capa **cierra el gate de release** asociado al tratamiento de las recolaciones, pero conserva `philologicalResolutionStatus=open`, `facsimileResolutionClaimed=false` y `ocrAcceptedAsFacsimileSubstitute=false`. El cotejo filológico continúa post-v1 cuando exista evidencia admisible.

El facsímil histórico no se incluye, no se relicencian reproducciones de terceros y `humanVerifiedCount=0` se mantiene donde corresponde.

## Gates abiertos para v1.0.0

Quedan **dos** gates:

1. tag, changelog, congelamiento de bytes finales y metadatos de identidad de release;
2. GitHub Release, depósito archivístico y DOI de versión/Concept DOI cuando corresponda.

## Determinismo

El ZIP usa orden fijo de miembros, timestamps normalizados, permisos normalizados y manifiesto con tamaño/SHA-256 de cada artefacto y commit de origen. `scripts/validate_release_candidate.py` lo construye dos veces y exige igualdad byte-a-byte; también exige la presencia y hash del freeze de contratos y la disposición 22/22 de recolaciones.

El paquete sigue siendo una **release candidate**, no una release estable, mientras estos dos gates permanezcan abiertos.
