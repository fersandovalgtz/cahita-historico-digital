# Cahíta Histórico Digital

**Edición histórico-digital, corpus abierto e infraestructura reproducible del _Arte de la lengua cahita_ impreso en México en 1737.**

Cahíta Histórico Digital (CHD) es una infraestructura de investigación orientada a conservar, describir, transcribir y estructurar de forma reproducible una fuente fundamental para la historia de las lenguas cahítas y de la lingüística misionera novohispana. El proyecto separa explícitamente el testimonio histórico, el OCR, la transcripción, la segmentación computacional y las decisiones curatoriales IA-asistidas.

> **Estado:** `0.2.0-dev` — desarrollo activo. No existe todavía una release científica estable ni un DOI del proyecto.

## Fuente histórica principal

- **ID:** `ALC1737`
- **Título:** _Arte de la lengua cahita conforme à las reglas de muchos peritos en ella_
- **Impresión:** México, 1737, D. Francisco Xavier Sánchez
- **Autoría de portada:** un padre de la Compañía de Jesús, misionero de más de treinta años en la provincia de Sinaloa; las atribuciones nominales posteriores se tratan como historia catalográfica, no como sustitución de la evidencia de portada.
- **Ejemplar digital de trabajo:** John Carter Brown Library / Internet Archive, identificador `artedelalenguaca00gonz`
- **Extensión procesada:** 182 páginas digitales; 118 páginas impresas numeradas en el cuerpo gramatical.

Véanse [`docs/SOURCE_ALC1737.md`](docs/SOURCE_ALC1737.md), [`docs/AUTHORSHIP.md`](docs/AUTHORSHIP.md) y [`PROVENANCE.md`](PROVENANCE.md).

## Estado del corpus

La fuente está representada de forma continua desde los preliminares y el cuerpo gramatical hasta el vocabulario y el sistema numeral. El vocabulario castellano–cahíta ocupa las páginas digitales **133–177** y el sistema numeral las páginas **178–180**.

Estado computacional vigente al **21 de agosto de 2026**:

- **2,072 candidatos lexicográficos** `hybrid_margin_mode_v0.2` están persistidos canónicamente y son reconstruibles;
- **2,302 artículos históricos estructurados** integran la capa curatorial actual;
- las **45/45 páginas del Vocabulario (133–177)** tienen reconciliación candidate-level completa;
- las **45/45 páginas** tienen censo exhaustivo de inicios visibles, promoción/enlace cerrado y cierre técnico IA-asistido dentro del alcance declarado;
- la subfase de cierre de **p.145–177** terminó con **33/33 páginas** técnicamente cerradas;
- quedan **0 candidatos `pending_promotion`**, **0 candidatos estructuralmente `unresolved`** y **0 fronteras `ambiguous`** en el resumen canónico de esa subfase;
- el cierre de p.177 fija el final del Vocabulario; las digitales **178–180** pertenecen al sistema numeral histórico;
- no existen objetos `human_verified`; la autoridad de las capas IA-asistidas permanece explícitamente separada de cualquier revisión humana independiente.

Estos totales no se mantienen manualmente como una segunda fuente de verdad. Se regeneran desde los estados de página y los `articleId` curatoriales mediante [`scripts/summarize_open_lexicon_work.py`](scripts/summarize_open_lexicon_work.py), cuyo resultado versionado es [`data/lexicon/reconciliation/phase2_open_work_summary.json`](data/lexicon/reconciliation/phase2_open_work_summary.json). Los snapshots históricos almacenados en estados de página conservan valor de procedencia, pero no sustituyen el conteo actual.

El detalle de cobertura se mantiene en [`docs/LEXICON_PROGRESS.md`](docs/LEXICON_PROGRESS.md), [`COVERAGE.md`](COVERAGE.md) y [`ROADMAP.md`](ROADMAP.md).

## Modelo epistemológico

CHD no equipara OCR con transcripción ni reconciliación computacional con edición crítica. La autoridad primaria permanece en `ALC1737`. Las capas derivadas registran su método, procedencia y estado de revisión. `BUE1890`, cuando se utiliza, funciona sólo como reimpresión histórica de control; nunca sustituye silenciosamente una lectura del ejemplar de 1737.

Los estados `machine_corrected_unverified` y `unresolved` identifican explícitamente el carácter IA-asistido del trabajo. Bajo la política vigente, `humanVerified` permanece en `false`; `human_verified` se conserva únicamente como estado reservado del esquema.

Una página alcanza **cierre técnico** cuando sus fronteras, continuidades, inicios visibles, falsos negativos, enlaces/promociones y zonas de incertidumbre quedan explícitamente modelados y el QA computacional es satisfactorio. Ese cierre no equivale a autoridad diplomática o filológica humana.

## Arquitectura del repositorio

- `data/source/` — metadatos, manifiestos, paginación y discontinuidades del testimonio;
- `data/transcription/` — capa de transcripción y control de avance;
- `data/grammar/` — reglas, paradigmas y construcciones gramaticales estructuradas;
- `data/lexicon/candidates/` — inventario canónico de fronteras candidatas;
- `data/lexicon/reconciliation/` — decisiones de frontera, censos visibles y estados de cierre;
- `data/lexicon/articles/` — artículos históricos estructurados y promociones;
- `data/lexicon/provenance/` — correcciones versionadas y evidencia de procedencia;
- `schemas/` — esquemas JSON para validación;
- `scripts/` — ingestión, extracción, reconstrucción y validación reproducibles;
- `docs/` — metodología, protocolos, cobertura, decisiones editoriales y documentación científica.

## Reproducibilidad y QA

El proyecto incluye validadores de JSONL, control de identificadores lexicográficos, reconstrucción del inventario canónico de candidatos y un flujo de QA en GitHub Actions. El workflow regenera además el resumen de trabajo lexicográfico y falla si el archivo versionado queda desincronizado de sus fuentes canónicas. Una corrida verde verifica consistencia computacional; no certifica corrección filológica humana.

Consulte [`docs/QA_AUTOMATION.md`](docs/QA_AUTOMATION.md), [`docs/LEXICON_RECONCILIATION_PROTOCOL.md`](docs/LEXICON_RECONCILIATION_PROTOCOL.md) y [`docs/TRANSCRIPTION_CONVENTIONS.md`](docs/TRANSCRIPTION_CONVENTIONS.md).

## Incertidumbres y límites abiertos

El cierre estructural del vocabulario no elimina incertidumbres de microestructura o lectura material que ya están codificadas dentro de artículos concretos. El repositorio conserva, entre otros problemas, la discontinuidad material `ALC1737-gap-0001` entre digitales 157–158, lecturas de baja confianza en tipografía pequeña, anáforas históricas como `Lo miſmo`, remisiones `Buſca` todavía no cerradas como grafo y artículos transpaginales cuya microestructura permanece parcialmente incierta. `ALC1737-art-001045` (`Atormentar`) continúa siendo un ejemplo explícito de incertidumbre localizada.

La ausencia de una capa humana no autoriza a fortalecer esas lecturas. Cierre estructural, incertidumbre textual y autoridad editorial son dimensiones distintas.

## Próximo frente científico

Con la reconciliación, el censo visible y la promoción/enlace cerrados para **pp.133–177**, el siguiente frente de la **Fase 3 — Corpus lexicográfico** es de consolidación e interoperabilidad, no de nuevas promociones masivas. Las prioridades inmediatas son:

1. construir un inventario maestro final de artículos históricos, separado del inventario de candidatos;
2. cerrar de forma explícita el grafo de remisiones `Buſca`;
3. modelar las anáforas `Lo miſmo` sin resolverlas automáticamente cuando la evidencia no baste;
4. detectar y estructurar atribuciones históricas explícitas `Hiaqui`, `Mayo` y `Thehueco` dentro del vocabulario;
5. generar exportaciones canónicas JSONL/JSON/CSV sin duplicados y con procedencia preservada;
6. preparar, sólo sobre una microestructura estabilizada, proyecciones TEI Lex-0 y otros derivados interoperables.

En paralelo permanecen abiertos los frentes de transcripción diplomática integral, gramática/variación histórica y reproducibilidad avanzada definidos en [`ROADMAP.md`](ROADMAP.md).

## Cita

Autor del proyecto: **Fernando Sandoval Gutierrez**, Universidad Autónoma de Ciudad Juárez, ORCID `0000-0002-3168-6725`.

La forma canónica de citación se encuentra en [`CITATION.cff`](CITATION.cff). Mientras el proyecto permanezca en `0.2.0-dev`, se recomienda citar también el commit exacto utilizado para garantizar reproducibilidad.

## Licencia

El repositorio declara **CC BY 4.0** para el dataset y la documentación correspondiente. Consulte [`LICENSE`](LICENSE) y [`DATA_LICENSE.md`](DATA_LICENSE.md) para el alcance y las condiciones aplicables.

## Principio editorial

**Preservar primero; estructurar después; inferir sólo en capas explícitas; mantener toda incertidumbre visible y trazable.**
