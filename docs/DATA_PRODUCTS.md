# Productos de datos y vías de reutilización

Cahíta Histórico Digital publica una representación canónica de investigación y múltiples productos derivados. La fuente de verdad no es el formato más cómodo para cada tarea, sino las capas canónicas identificadas por la documentación y los manifests.

## Release estable

**v1.0.0:** <https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0>

Assets externos comprobados:

| Asset | Función | Integridad |
|---|---|---|
| `cahita-historico-digital-v1.0.0.zip` | paquete autocontenido de la release | 1,076,296 bytes · SHA-256 `583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158` |
| `RELEASE_MANIFEST.json` | inventario e identidad del payload | 67,757 bytes · SHA-256 `05970080840ed0cde9c4ca67b40432b492ba2f0afadade5efe2b9d0f60b8cb79` |
| `SHA256SUMS.txt` | checksums publicados | verificado por atestación post-release |

La atestación reproducible está versionada en `release/github_release_attestation_v1.0.0.json`.

## Léxico canónico

`data/lexicon/articles/*.jsonl` contiene los **2,302 artículos históricos** en **211 archivos JSONL**. Es la capa curatorial principal para trabajo detallado sobre microestructura, spans, revisión y procedencia.

Use esta capa cuando necesite:

- preservar todos los campos curatoriales;
- rastrear páginas y columnas;
- estudiar remisiones y agrupaciones;
- auditar `reviewStatus`, `humanVerified` y procedencia;
- proponer correcciones con IDs estables.

## Exportaciones consolidadas

`scripts/export_lexicon_corpus.py` genera determinísticamente:

- `chd_lexicon_articles.jsonl`;
- `chd_lexicon_articles.json`;
- `chd_lexicon_articles.csv`;
- `manifest.json` con conteos, tamaños y SHA-256.

Estas vistas son apropiadas para análisis tabular, notebooks, R/Python y procesamiento en lote. Son derivados reproducibles: no deben editarse como fuente canónica.

## TEI Lex-0

La proyección TEI está diseñada para intercambio lexicográfico. v1.0.0 valida externamente contra **TEI Lex-0 0.9.5** mediante Jing y conserva 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 `@target` estrictos.

Es el formato preferido cuando el objetivo es interoperabilidad lexicográfica preservando mejor la naturaleza de diccionario histórico.

## Gramática

`data/grammar/` contiene objetos estructurados del _Arte_. Los exportadores producen concordancias y auditorías de cobertura sin reemplazar los objetos fuente.

Estado v1.0.0:

- 302 objetos gramaticales;
- 1,215 filas de evidencia;
- 371/371 unidades numeradas efectivamente impresas representadas.

## Remisiones y revisión

Las capas de `Buſca`, `Lo miſmo` y recolación permiten trabajar con relaciones sin confundir grafos estrictos y decisiones editoriales.

- 150 `Buſca` canónicos;
- 60 enlaces estrictos `exact_unique`;
- 90 `not_located` revisados explícitamente;
- 22 casos conservados como incertidumbres abiertas en v1.0.0.

## Metadatos y citación

- `CITATION.cff` — citación humana/machine-readable;
- `codemeta.json` — metadata de software;
- `project-metadata.json` — perfil integrado de proyecto, release y métricas;
- `metadata/fair-dataset.jsonld` — metadata FAIR/Schema.org complementaria;
- `SOURCES.md` y `PROVENANCE.md` — fuente y trazabilidad.

## Consulta rápida local

```bash
python scripts/query_lexicon.py --stats
python scripts/query_lexicon.py "Danzar" --field spanish --limit 5
python scripts/query_lexicon.py "Danzar" --field all --json
```

La herramienta consulta las capas canónicas y no normaliza automáticamente `ſ`, ortografía histórica ni identidades modernas.

## Descarga con GitHub CLI

```bash
gh release download v1.0.0 \
  -R fersandovalgtz/cahita-historico-digital \
  -p 'cahita-historico-digital-v1.0.0.zip'
```

## Qué producto elegir

| Necesidad | Producto recomendado |
|---|---|
| Auditoría filológica/editorial | JSONL canónico por artículo |
| Análisis estadístico/tabular | CSV consolidado |
| Procesamiento programático completo | JSON/JSONL consolidado |
| Intercambio lexicográfico | TEI Lex-0 |
| Investigación gramatical | `data/grammar/` + concordancia |
| Citar/reproducir una versión | GitHub Release + tag + manifest/checksums |
| Verificar límites y autoridad | `QUALITY_REPORT.md`, `DATASHEET.md`, `GOVERNANCE.md` |

## CLDF

CLDF no se incluye como requisito v1.0.0. La decisión está documentada: puede ser útil como derivado analítico futuro, pero no debe forzarse si ello aplana la microestructura histórica o introduce un mapeo lingüístico moderno no demostrado.
