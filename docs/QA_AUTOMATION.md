# QA automatizado y puertas de reproducibilidad

## Propósito

Cahíta Histórico Digital ejecuta una capa de **integración continua (CI)** mediante GitHub Actions para comprobar que los contratos estructurales, identificadores y artefactos reproducibles sigan siendo válidos después de cambios en `main` y en pull requests.

El workflow vive en `.github/workflows/qa.yml` y se denomina **CHD QA**. Su función es detectar deriva computacional y documental verificable; no sustituye el cotejo filológico del testimonio.

## Qué comprueba actualmente

La ejecución automatizada:

1. prepara un entorno Python 3.13;
2. instala las dependencias declaradas en `requirements-dev.txt`;
3. reconstruye y verifica el inventario canónico de **2,072 candidatos v0.2** mediante `scripts/reconstruct_candidate_inventory.py`;
4. comprueba parseo JSONL, unicidad global de `articleId` y coherencia `humanVerified`/`reviewStatus` mediante `scripts/validate_lexicon_ids.py`;
5. valida todos los objetos de `data/lexicon/articles/*.jsonl` contra `schemas/lexical-article.schema.json`;
6. valida los lotes de reconciliación históricos y las capas izquierda/derecha de las páginas del vocabulario contra `schemas/lexicon-candidate-review.schema.json`;
7. valida las capas de inicios visibles omitidos contra `schemas/lexicon-missed-start.schema.json`;
8. comprueba sintaxis JSON de CodeMeta, manifiestos, estados de reconciliación, preflights, archivos de procedencia y controles seleccionados;
9. valida la sintaxis de `data/lexicon/reconciliation/phase2_open_work_summary.json`;
10. regenera el resumen de trabajo abierto de fase II mediante `scripts/summarize_open_lexicon_work.py` y exige coincidencia exacta con el archivo versionado.

El paso 10 constituye una **puerta de frescura**: si cambian artículos curatoriales o estados de página y el resumen de fase II no se regenera, CI falla. Así se impide que `pending_promotion`, el conteo curatorial y los indicadores de cierre queden silenciosamente desfasados respecto de sus fuentes computables.

## Primera ejecución verde y evolución del QA

La primera ejecución completamente satisfactoria fue **CHD QA run #3**, disparada por el commit `26be9763b8001ff082524368000ab7fccfa6778c` el 16 de agosto de 2026.

Durante la puesta en marcha, el CI detectó dos problemas reales de infraestructura:

- el caché de `setup-python` no conocía `requirements-dev.txt`; se corrigió declarando `cache-dependency-path`;
- una condición JSON Schema sobre `articleLinkStatus = linked` se activaba también cuando la propiedad estaba ausente, debido a la semántica de `if/properties` de JSON Schema. Se corrigió exigiendo explícitamente la presencia de `articleLinkStatus` antes de aplicar la condición.

Aquella primera corrida verde confirmó el estado histórico de **734 objetos lexicográficos**. Esa cifra debe leerse únicamente como un hito de evolución del corpus, no como el tamaño actual.

Al **17 de agosto de 2026**, el estado computacional vigente es:

- **2,072 candidatos canónicos** en el inventario v0.2;
- **1,049 `articleId` curatoriales únicos** en `data/lexicon/articles/*.jsonl`;
- reconciliación candidate-level completa en las **45/45 páginas del Vocabulario (133–177)**;
- fase II p.145–177 con **1,047 candidatos `pending_promotion`**, **1 candidato estructuralmente `unresolved`** y **9 fronteras `ambiguous`**;
- **0/33 páginas** de ese alcance con censo visible exhaustivo y **0/33** con cierre técnico;
- `humanVerified=false` preservado como política vigente.

La fuente reproducible de estos indicadores es `data/lexicon/reconciliation/phase2_open_work_summary.json`, generado desde los estados de página y el conteo independiente de `articleId` únicos. Las cifras históricas presentes en commits o estados de pasada permanecen como evidencia de procedencia y no deben confundirse con el conteo actual.

## Qué NO comprueba

Una ejecución verde **no significa** que:

- la transcripción histórica sea filológicamente correcta;
- una forma cahíta haya sido leída correctamente del facsímil;
- una frontera editorial haya sido validada por una persona;
- el corpus sea exhaustivo;
- las categorías históricas hayan sido interpretadas correctamente desde una teoría lingüística moderna;
- las lagunas del testimonio estén resueltas;
- exista revisión `human_verified`.

El CI comprueba principalmente **integridad computacional, contratos estructurales y reproducibilidad de artefactos seleccionados**. La autoridad primaria permanece en `ALC1737`; cuando la evidencia disponible no basta, la incertidumbre debe permanecer codificada en lugar de resolverse para satisfacer una prueba automática.

## Política de fallos

Un fallo de CI debe tratarse como una señal de inconsistencia que requiere diagnóstico, no como una invitación a debilitar el schema hasta que los datos pasen. Si el fallo revela una incompatibilidad entre el modelo y datos legítimos, el cambio del schema debe documentarse y conservar la intención científica original.

La puerta de frescura de fase II sigue el mismo principio: ante una discrepancia, debe determinarse si cambió legítimamente el corpus, si un estado de página quedó obsoleto o si falta regenerar el resumen. No se debe editar manualmente el resultado sólo para igualar una cifra esperada.

## Próximas ampliaciones

La siguiente generación de QA debería incorporar progresivamente:

- consistencia de `data/transcription/status.csv` frente a los JSON de página y lotes;
- referencias cruzadas a `articleId` existentes más allá de las capas actualmente validadas;
- conteos canónicos de reconciliación por página con invariantes explícitos;
- validación de las capas gramaticales contra sus respectivos schemas;
- comprobación de exportaciones derivadas reproducibles;
- validación de `CITATION.cff` y metadatos de release;
- detección de enlaces internos rotos;
- comprobaciones derivadas para evitar que README, COVERAGE, ROADMAP y documentación de progreso contradigan las fuentes computables, procurando no convertir esos documentos en fuentes manuales duplicadas de métricas.

## Autoridad

El resultado de GitHub Actions debe citarse como **QA computacional automatizado**, nunca como revisión filológica humana.
