# Preservación, DOI e identidad persistente

## Estado

Cahíta Histórico Digital v1.0.0 cuenta con una GitHub Release estable, reconstruible y atestada. La preservación archivística externa y los DOI permanecen pendientes hasta que un repositorio de preservación publique efectivamente el registro y asigne identificadores reales.

No se reserva, deduce, fabrica ni anticipa ningún DOI dentro del repositorio. Mientras el depósito no exista, `project-metadata.json` conserva `doi: null`, `concept_doi: null` y `status: "pending archival deposit"`.

## Identidad que no debe cambiar

La preservación externa debe referirse exactamente a esta publicación:

- versión: `1.0.0`;
- tag: `v1.0.0`;
- commit del tag: `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`;
- GitHub Release: `https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0`;
- asset: `cahita-historico-digital-v1.0.0.zip`;
- SHA-256 del ZIP: `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`.

La asignación de DOI es metadato post-release. No autoriza mover el tag, reconstruir la Release con contenido distinto, reescribir el corpus congelado ni convertir revisión técnica en validación filológica humana.

## Flujo de depósito

El depósito archivístico se realiza fuera de GitHub, preferentemente mediante una integración que archive la Release estable. Antes de publicar el registro se debe comprobar que la versión sea `1.0.0`, que la autoría y afiliación sean correctas, que el objeto depositado corresponda a la Release atestada y que la descripción preserve la matriz de licenciamiento del proyecto: código original bajo MIT; datos, metadatos y capas editoriales originales bajo CC BY 4.0; materiales históricos o reproducciones de terceros sin relicenciamiento por CHD.

Cuando el repositorio archivístico publique el registro, se deben conservar como evidencia:

- DOI de versión;
- DOI conceptual, si el proveedor lo asigna;
- URL HTTPS del registro publicado;
- proveedor de preservación;
- fecha efectiva de publicación o depósito.

## Sincronización reproducible

Los identificadores reales se incorporan mediante `scripts/sync_persistent_identifiers.py`. El comando primero puede ejecutarse sin `--apply`; ese modo valida sintaxis y muestra la identidad que sería registrada sin modificar archivos.

Ejemplo con valores ficticios deliberadamente no utilizables como registro real:

```bash
python scripts/sync_persistent_identifiers.py \
  --version-doi '10.0000/REEMPLAZAR-CON-DOI-REAL' \
  --concept-doi '10.0000/REEMPLAZAR-CON-CONCEPT-DOI-REAL' \
  --record-url 'https://example.invalid/registro-real' \
  --deposited-at 'YYYY-MM-DD' \
  --provider 'Zenodo'
```

Solo después de verificar visualmente el registro archivístico se repite con `--apply`. Si no existe DOI conceptual, se omite `--concept-doi`.

El sincronizador actualiza de forma coordinada:

- `project-metadata.json` como estado operativo canónico;
- `CITATION.cff` con el DOI de la versión;
- `codemeta.json` con el identificador persistente;
- `metadata/fair-dataset.jsonld` con la identidad DOI y su estado;
- `release/archival_deposit_v1.0.0.json` como atestación post-release del depósito.

Después ejecuta `scripts/validate_persistent_identifiers.py`. El validador también forma parte de CI y admite únicamente dos estados coherentes: depósito pendiente sin DOI, o depósito archivado con DOI real sincronizado en todas las superficies.

## Propiedades de seguridad

El mecanismo aplica las siguientes restricciones:

1. un DOI no puede aparecer parcialmente en unas superficies y faltar en otras;
2. el estado pendiente no puede contener URL, proveedor o fecha que aparenten un depósito inexistente;
3. una vez registrado un DOI archivístico, el sincronizador se niega a sustituirlo automáticamente por otro diferente;
4. la atestación archivística debe conservar tag, commit, URL de Release, nombre del ZIP y SHA-256 de la publicación ya fijada;
5. `doiInferred` y `tagModified` deben permanecer en `false`;
6. la capa de preservación está fuera del freeze de datos científicos y no modifica los 267 archivos de v1.0.0.

## Cierre del gate de preservación

El issue `#169` solo puede cerrarse cuando exista un registro archivístico público y comprobable, el DOI de versión esté resuelto por el proveedor, los identificadores hayan sido sincronizados y validados en `main`, y la documentación pública de citación haya sido revisada para exponer el DOI sin ambigüedad.

La existencia de este mecanismo no cierra por sí misma el gate: prepara el repositorio para cerrarlo de forma controlada cuando la evidencia externa exista.
