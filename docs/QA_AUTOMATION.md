# QA automatizado y puertas de reproducibilidad

## Propósito

Cahíta Histórico Digital ejecuta una capa de **integración continua (CI)** mediante GitHub Actions para comprobar que ciertos contratos estructurales y artefactos reproducibles siguen siendo válidos después de cambios en `main` y en pull requests.

El workflow vive en `.github/workflows/qa.yml` y se denomina **CHD QA**.

## Qué comprueba actualmente

La ejecución automatizada:

1. prepara un entorno Python 3.13;
2. instala las dependencias declaradas en `requirements-dev.txt`;
3. reconstruye y verifica el inventario canónico de **2,072 candidatos v0.2** con `scripts/reconstruct_candidate_inventory.py`;
4. comprueba parseo JSONL, unicidad global de `articleId` y coherencia `humanVerified`/`reviewStatus` mediante `scripts/validate_lexicon_ids.py`;
5. valida todos los objetos de `data/lexicon/articles/*.jsonl` contra `schemas/lexical-article.schema.json`;
6. valida los lotes de reconciliación pp.133–134 contra `schemas/lexicon-candidate-review.schema.json`;
7. valida la capa de inicios visibles omitidos contra `schemas/lexicon-missed-start.schema.json`;
8. comprueba sintaxis JSON de metadatos y estados canónicos seleccionados.

## Primera ejecución verde

La primera ejecución completamente satisfactoria fue **CHD QA run #3**, disparada por el commit `26be9763b8001ff082524368000ab7fccfa6778c` el 16 de agosto de 2026.

Durante la puesta en marcha, el CI detectó dos problemas reales de infraestructura:

- el caché de `setup-python` no conocía `requirements-dev.txt`; se corrigió declarando `cache-dependency-path`;
- una condición JSON Schema sobre `articleLinkStatus = linked` se activaba también cuando la propiedad estaba ausente, debido a la semántica de `if/properties` de JSON Schema. Se corrigió exigiendo explícitamente la presencia de `articleLinkStatus` antes de aplicar la condición.

La ejecución verde confirmó además:

- reconstrucción íntegra de las **2,072 filas** del inventario candidato con SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`;
- **734 objetos lexicográficos**, **734 `articleId` únicos**;
- validación de todos los JSONL de artículos contra su schema;
- validación de los lotes de reconciliación y de la capa de falsos negativos;
- sintaxis válida de los JSON de control incluidos en el workflow.

## Qué NO comprueba

Una ejecución verde **no significa** que:

- la transcripción histórica sea filológicamente correcta;
- una forma cahíta haya sido leída correctamente del facsímil;
- una frontera editorial haya sido validada por una persona;
- el corpus sea exhaustivo;
- las categorías históricas hayan sido interpretadas correctamente desde una teoría lingüística moderna;
- las lagunas del testimonio estén resueltas;
- exista revisión `human_verified`.

El CI comprueba principalmente **integridad computacional, contratos estructurales y reproducibilidad de artefactos seleccionados**. La autoridad filológica sigue dependiendo de la procedencia, el cotejo contra la fuente y la revisión humana explícita cuando exista.

## Política de fallos

Un fallo de CI debe tratarse como una señal de inconsistencia que requiere diagnóstico, no como una invitación a debilitar el schema hasta que los datos pasen. Si el fallo revela una incompatibilidad entre el modelo y datos legítimos, el cambio del schema debe documentarse y conservar la intención científica original.

## Próximas ampliaciones

La siguiente generación de QA debería incorporar progresivamente:

- consistencia de `data/transcription/status.csv` frente a los JSON de página y lotes;
- referencias cruzadas a `articleId` existentes;
- conteos canónicos de reconciliación por página;
- validación de las capas gramaticales contra sus respectivos schemas;
- comprobación de exportaciones derivadas reproducibles;
- validación de `CITATION.cff` y metadatos de release;
- detección de enlaces internos rotos;
- prueba de sincronización de métricas canónicas entre README, COVERAGE y archivos de estado.

## Autoridad

El resultado de GitHub Actions debe citarse como **QA computacional automatizado**, nunca como revisión filológica humana.
