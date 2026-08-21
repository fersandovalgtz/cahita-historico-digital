# Cahíta Histórico Digital — cierre de Phase II lexicográfica

**Fecha de cierre técnico:** 21 de agosto de 2026  
**Fuente primaria:** `ALC1737`  
**PDF de trabajo SHA-256:** `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`  
**Inventario canónico de candidatos:** `hybrid_margin_mode_v0.2` — 2,072 filas  
**JSONL canónico SHA-256:** `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`

## Resultado

La Phase II de promoción/enlace y censo exhaustivo del vocabulario castellano–cahíta quedó técnicamente cerrada para las páginas digitales **145–177**. El estado canónico, regenerado desde los archivos de reconciliación y la capa de artículos, registra:

- **33 / 33 páginas** con censo visible exhaustivo;
- **33 / 33 páginas** con cierre técnico;
- **0** candidatos `pending_promotion`;
- **0** candidatos estructuralmente `unresolved`;
- **0** fronteras `ambiguous`;
- **2,302 artículos históricos estructurados** en la capa curatorial total;
- **0** objetos `human_verified`.

Sumado al tramo p.133–144, previamente cerrado, el vocabulario completo p.133–177 queda con **45 / 45 páginas** técnicamente cerradas dentro del alcance IA-asistido declarado.

La fuente canónica de estas métricas es `data/lexicon/reconciliation/phase2_open_work_summary.json`, regenerable mediante `scripts/summarize_open_lexicon_work.py`. Los estados de página anteriores conservan snapshots históricos de cada pasada y no sustituyen el conteo vigente.

## Cierre de la página 177

La última página del vocabulario fue el cierre material de la fase. El cotejo facsimilar directo estableció:

- **60 inicios léxicos visibles**;
- **57 candidatos canónicos verdaderos**;
- **3 falsos negativos** del detector;
- **45 artículos nuevos**, `ALC1737-art-002258`–`ALC1737-art-002302`;
- resolución directa de las dos fronteras que anteriormente permanecían `ambiguous`;
- corrección de dos lecturas de la capa seleccionada, conservando trazabilidad;
- terminación del vocabulario antes de la sección histórica de numerales de las páginas digitales 178–180.

El cierre fue integrado en `main` mediante el commit `105bebed7ccc0561eea3fa0fc192a7057cc5dbec`. La corrida `CHD QA #563` quedó registrada como satisfactoria antes de la integración.

## Qué significa “cierre técnico”

El cierre técnico afirma que, para el alcance declarado, las fronteras candidatas, continuidades, falsos negativos visibles, promociones/enlaces y decisiones estructurales están modelados de forma reproducible y pasan los controles computacionales del repositorio.

**No significa**:

- que exista una edición diplomática humana definitiva;
- que todas las microlecturas sean filológicamente seguras;
- que una anáfora `Lo miſmo` haya sido resuelta semánticamente;
- que una remisión `Buſca` haya sido convertida automáticamente en equivalencia;
- que las formas históricas hayan sido normalizadas como lexemas modernos;
- que exista validación comunitaria o lingüística contemporánea;
- que el proyecto esté listo para una release científica estable.

Las incertidumbres internas a artículos ya estructurados permanecen visibles y no se cuentan como candidatos estructuralmente abiertos.

## Autoridad textual

`ALC1737` continúa siendo la autoridad primaria. La reimpresión `BUE1890` sólo puede utilizarse como control secundario explícito de glyphs o secuencias y nunca como sustitución silenciosa de una lectura del testimonio de 1737.

El estado editorial de los objetos sigue siendo `machine_corrected_unverified` o `unresolved` cuando corresponde. `humanVerified=false` permanece como política efectiva de la capa actual.

## Consecuencias para el trabajo siguiente

Con la fase de detección/promoción cerrada, el trabajo lexicográfico debe cambiar de naturaleza. Las prioridades post-cierre son:

1. generar exportaciones canónicas JSON/CSV a partir de los 2,302 artículos, con unicidad y hashes verificables;
2. construir y auditar el grafo de remisiones `Buſca`;
3. inventariar y mantener explícitas las anáforas `Lo miſmo` sin resolverlas por automatismo;
4. detectar y normalizar sólo como metadato las etiquetas históricas explícitas Hiaqui/Mayo/Thehueco y otras marcas de variedad;
5. auditar continuidades y `sourceSpans` de artículos transcolumna/transpágina;
6. preparar un perfil TEI y evaluar TEI Lex-0/CLDF sólo como capas derivadas interoperables;
7. sincronizar documentación, metadatos de citación, cobertura y checklist de release antes de cualquier congelamiento de versión.

## Guarda de versión

El proyecto **permanece en `0.2.0-dev`**. El cierre de Phase II es un hito científico y técnico importante, pero no autoriza por sí mismo a crear `v1.0.0`, asignar un DOI o describir el recurso como edición crítica terminada.
