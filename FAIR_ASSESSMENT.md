# Evaluación FAIR — Cahíta Histórico Digital

Este documento registra una **preauditoría interna y reproducible** de Cahíta Histórico Digital frente a los principios FAIR. **No constituye certificación FAIR** ni sustituye una evaluación externa como F-UJI. Mientras no exista una evaluación pública verificable, el proyecto no debe usar expresiones como “FAIR certified” o “FAIR compliant”.

## Objeto evaluado

- Recurso: **Cahíta Histórico Digital — _Arte de la lengua cahita_ (1737)**
- Versión estable: **1.0.0**
- Repositorio: <https://github.com/fersandovalgtz/cahita-historico-digital>
- Release: <https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0>
- Depósito archivístico: <https://zenodo.org/records/22061986>
- DOI de versión: **10.5281/zenodo.22061986**
- DOI conceptual: **10.5281/zenodo.22061985**
- Metadatos FAIR complementarios: [`metadata/fair-dataset.jsonld`](metadata/fair-dataset.jsonld)
- Estado de autoridad humana: `humanVerified=0`

## Findable — Localizable

| Criterio | Evidencia | Estado |
|---|---|---|
| Identidad estable de versión | tag inmutable `v1.0.0` y commit fijado | Fuerte |
| Metadatos descriptivos | `CITATION.cff`, `codemeta.json`, `project-metadata.json`, JSON-LD | Fuerte |
| Identificador persistente global | DOI de versión `10.5281/zenodo.22061986`; DOI conceptual `10.5281/zenodo.22061985` | Fuerte |
| Descubrimiento en repositorios académicos | GitHub Release pública; Zenodo publicado; indexación visible en OpenAIRE | Fuerte |
| Identificadores internos persistentes | `articleId`, source IDs y capas versionadas | Fuerte |

## Accessible — Accesible

| Criterio | Evidencia | Estado |
|---|---|---|
| Acceso por protocolo estándar | HTTPS/Git/GitHub Release/Zenodo | Fuerte |
| Datos descargables sin software propietario | JSON, JSONL, CSV, XML/TEI y ZIP | Fuerte |
| Condiciones de acceso documentadas | licencias por componente y procedencia | Fuerte |
| Persistencia archivística independiente | depósito publicado en Zenodo con DOI | Fuerte |

## Interoperable — Interoperable

| Criterio | Evidencia | Estado |
|---|---|---|
| Formatos abiertos | JSON, JSONL, CSV, TEI XML | Fuerte |
| Vocabulario/esquemas formales | 22 JSON Schema Draft 2020-12 | Fuerte |
| Estándar lexicográfico | TEI Lex-0 0.9.5 validado con Jing | Fuerte |
| Metadatos machine-readable | CodeMeta, CFF, JSON-LD | Fuerte |
| Código lingüístico único moderno | deliberadamente no asignado al rótulo histórico `Cahita` | No aplicable por política |
| CLDF | derivado analítico post-v1 reproducible y validado | Fuerte como capa post-v1 |

## Reusable — Reutilizable

| Criterio | Evidencia | Estado |
|---|---|---|
| Licencia explícita | MIT para código; CC BY 4.0 para datos/editorial propio; ambas declaradas también en Zenodo | Fuerte |
| Procedencia | `PROVENANCE.md`, `SOURCES.md`, source spans y manifests | Fuerte |
| Calidad y límites | `QUALITY_REPORT.md`, `DATASHEET.md`, `COVERAGE.md` | Fuerte |
| Citación | DOI, `CITATION.cff`, ORCID, versión y release | Fuerte |
| Reproducibilidad | CI, exports deterministas, freezes y atestación post-release | Fuerte |
| Autoridad/validación | estados explícitos; `humanVerified=0` | Fuerte en transparencia; validación humana pendiente |
| Preservación | GitHub Release atestada + depósito Zenodo publicado | Fuerte |

## Evidencia de integridad v1.0.0

La release publicada fue reconstruida desde el tag inmutable `v1.0.0` y comparada con sus assets públicos. La atestación durable se encuentra en [`release/github_release_attestation_v1.0.0.json`](release/github_release_attestation_v1.0.0.json). El ZIP final publicado tiene 1,076,296 bytes y SHA-256 `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`.

La misma versión fue depositada en Zenodo como registro `22061986`, con DOI de versión `10.5281/zenodo.22061986` y DOI conceptual `10.5281/zenodo.22061985`. El registro se publica como **Software** y declara **CC BY 4.0** y **MIT**. La página pública de Zenodo muestra indexación en **OpenAIRE**.

## Brechas prioritarias posteriores al DOI

1. **Ejecutar una evaluación FAIR externa** —por ejemplo F-UJI— sobre el objeto con DOI y conservar el resultado público/versionado.
2. **Verificar preservación adicional cuando corresponda**, por ejemplo Software Heritage, sin confundir ese estado con el depósito Zenodo ya completado.
3. **Mantener explícita la semántica histórica**: no obtener una aparente interoperabilidad asignando un código moderno único o equivalencias modernas que la fuente no sustenta.
4. **Ampliar revisión filológica trazable** de las 22 incertidumbres cuando exista acceso a evidencia admisible.

## Relación con CARE

FAIR no agota las obligaciones éticas asociadas con datos lingüísticos indígenas. Aunque el corpus v1.0.0 deriva de una fuente histórica, sus contenidos se relacionan con lenguas y comunidades indígenas vivas y con historias coloniales de documentación. Para reutilización contemporánea se recomienda aplicar además criterios de beneficio, autoridad, responsabilidad y ética inspirados en CARE, tal como se desarrolla en [`GOVERNANCE.md`](GOVERNANCE.md).

## Política de badges

El README puede mostrar **FAIR pre-assessment** mientras el enlace apunte a este documento y no sugiera certificación. Un porcentaje o afirmación de cumplimiento sólo debe publicarse cuando proceda de una evaluación externa identificable por herramienta, versión, fecha y objeto evaluado.
