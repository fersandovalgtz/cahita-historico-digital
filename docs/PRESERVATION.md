# Preservación, DOI e identidad persistente

## Estado archivístico — cerrado

Cahíta Histórico Digital `v1.0.0` cuenta con una GitHub Release estable, reconstruible y atestada, y con un depósito archivístico público en Zenodo.

- GitHub Release: <https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0>
- Zenodo: <https://zenodo.org/records/22061986>
- DOI de versión: **10.5281/zenodo.22061986**
- DOI conceptual: **10.5281/zenodo.22061985**
- proveedor: **Zenodo**
- fecha de depósito/publicación: **2026-08-22**
- tipo de recurso en Zenodo: **Software**
- licencias visibles en Zenodo: **Creative Commons Attribution 4.0 International** y **MIT License**
- indexación visible al cierre: **OpenAIRE**

El DOI de versión identifica específicamente la versión `1.0.0`. El DOI conceptual identifica la serie completa de versiones y está diseñado para resolver a la versión más reciente disponible en Zenodo.

## Identidad que no cambia

La preservación externa refiere exactamente a esta publicación:

- versión: `1.0.0`;
- tag: `v1.0.0`;
- commit del tag: `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`;
- GitHub Release: `https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0`;
- asset: `cahita-historico-digital-v1.0.0.zip`;
- SHA-256 del ZIP: `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`.

Zenodo muestra para el ZIP archivado el MD5 `9f61305189221c6f8dcb7f790c74e092` y un tamaño aproximado de 1.1 MB.

La asignación de DOI es metadato post-release. No autoriza mover el tag, reconstruir la Release con contenido distinto, reescribir el corpus congelado ni convertir revisión técnica en validación filológica humana.

## Atestaciones

La identidad binaria de la GitHub Release se conserva en:

- [`release/github_release_attestation_v1.0.0.json`](../release/github_release_attestation_v1.0.0.json)

La identidad archivística y los DOI asignados externamente se conservan en:

- [`release/archival_deposit_v1.0.0.json`](../release/archival_deposit_v1.0.0.json)

La atestación archivística fija proveedor, URL del registro, DOI de versión, DOI conceptual, fecha del depósito y la identidad inmutable del tag/ZIP.

## Sincronización reproducible

Los identificadores reales se incorporan mediante `scripts/sync_persistent_identifiers.py`. El sincronizador actualiza de forma coordinada:

- `project-metadata.json`;
- `CITATION.cff`;
- `codemeta.json`;
- `metadata/fair-dataset.jsonld`;
- `release/archival_deposit_v1.0.0.json`.

El estado archivístico resultante es `archived with DOI`. `scripts/validate_persistent_identifiers.py` exige que el DOI de versión sea consistente en todas las superficies, que el DOI conceptual y el registro Zenodo sean trazables, y que `doiInferred=false` y `tagModified=false` permanezcan invariables.

## Citación

Para citar específicamente la versión científica congelada `1.0.0`, use:

> Sandoval Gutiérrez, F. (2026). *Cahíta Histórico Digital* (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.22061986

Para referirse al proyecto como serie de versiones puede usarse el DOI conceptual:

**10.5281/zenodo.22061985**

## Licenciamiento por componentes

El registro Zenodo declara las dos licencias principales, pero el alcance jurídico del proyecto sigue documentado por componentes:

- código original: **MIT**;
- datos, metadatos y capas editoriales originales: **CC BY 4.0**;
- fuentes históricas, facsímiles, digitalizaciones y materiales de terceros: no son relicenciados por CHD.

Véanse [`LICENSING.md`](../LICENSING.md), [`LICENSE`](../LICENSE) y [`DATA_LICENSE.md`](../DATA_LICENSE.md).

## Preservación adicional

El depósito Zenodo está confirmado. Cualquier preservación adicional —por ejemplo Software Heritage— debe registrarse sólo cuando exista evidencia pública verificable; no se infiere automáticamente a partir del depósito Zenodo.

## Cierre del gate de preservación

El gate externo de preservación de `v1.0.0` puede cerrarse cuando estos identificadores estén fusionados en `main`, la documentación pública exponga el DOI sin ambigüedad y CI confirme que la identidad de la release inmutable permanece intacta.
