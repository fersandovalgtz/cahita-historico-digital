# Cahíta Histórico Digital

**Edición histórico-digital, corpus abierto e infraestructura reproducible del _Arte de la lengua cahita_ impreso en México en 1737.**

Cahíta Histórico Digital (CHD) es una infraestructura de investigación orientada a conservar, describir, transcribir y estructurar de forma reproducible una fuente fundamental para la historia de las lenguas cahítas y de la lingüística misionera novohispana. El proyecto separa explícitamente el testimonio histórico, el OCR, la transcripción, la segmentación computacional y las decisiones curatoriales IA-asistidas.

> **Estado:** `0.2.0-dev` — desarrollo activo. La fase II lexicográfica está técnicamente cerrada; todavía no existe una release científica estable ni un DOI del proyecto.

## Fuente histórica principal

- **ID:** `ALC1737`
- **Título:** _Arte de la lengua cahita conforme à las reglas de muchos peritos en ella_
- **Impresión:** México, 1737, D. Francisco Xavier Sánchez
- **Autoría de portada:** un padre de la Compañía de Jesús, misionero de más de treinta años en la provincia de Sinaloa; las atribuciones nominales posteriores se tratan como historia catalográfica, no como sustitución de la evidencia de portada.
- **Ejemplar digital de trabajo:** John Carter Brown Library / Internet Archive, identificador `artedelalenguaca00gonz`
- **Extensión procesada:** 182 páginas digitales; 118 páginas impresas numeradas en el cuerpo gramatical.

Véanse [`docs/SOURCE_ALC1737.md`](docs/SOURCE_ALC1737.md), [`docs/AUTHORSHIP.md`](docs/AUTHORSHIP.md) y [`PROVENANCE.md`](PROVENANCE.md).

## Estado del corpus

La fuente está representada de forma continua desde los preliminares y el cuerpo gramatical hasta el vocabulario y el sistema numeral. La colación directa del testimonio corrige el límite previamente documentado: el vocabulario castellano–cahíta ocupa las páginas digitales **133–178**, pero la p.178 es una **página mixta**. Su parte superior contiene los últimos 18 artículos bajo X–Z y, después de una regla ornamental, comienza **`NOMBRES NUMERALES`**. El sistema numeral continúa en pp.178–180.

Estado computacional vigente al **20 de agosto de 2026**:

- **2,072 candidatos lexicográficos** `hybrid_margin_mode_v0.2` permanecen persistidos canónicamente para el alcance original **pp.133–177**;
- **2,320 artículos históricos estructurados** integran la capa curatorial después de incorporar la cola terminal X–Z de p.178;
- las **45 páginas del alcance canónico de candidatos (133–177)** tienen reconciliación candidate-level completa;
- las **33/33 páginas de fase II (145–177)** tienen censo visible exhaustivo, promoción/enlace completa y cierre técnico;
- en p.145–177 quedan **0 candidatos `pending_promotion`**, **0 candidatos estructuralmente `unresolved`** y **0 fronteras `ambiguous`**;
- p.178 aporta **18 artículos terminales adicionales** (`ALC1737-art-002303`–`ALC1737-art-002320`) mediante colación facsimilar directa; no se puntúan como falsos negativos porque p.178 quedó fuera del alcance de generación del detector v0.2;
- no existen objetos `human_verified`; la autoridad de las capas IA-asistidas permanece explícitamente separada de cualquier revisión humana.

El cierre técnico agregado se registra en [`data/lexicon/reconciliation/phase2_closure_summary_2026-08-20.json`](data/lexicon/reconciliation/phase2_closure_summary_2026-08-20.json). El resumen histórico [`data/lexicon/reconciliation/phase2_open_work_summary.json`](data/lexicon/reconciliation/phase2_open_work_summary.json) se regenera desde los estados de página y los `articleId` curatoriales mediante [`scripts/summarize_open_lexicon_work.py`](scripts/summarize_open_lexicon_work.py); durante la rama de consolidación debe tratarse como artefacto derivado pendiente de regeneración final, no como segunda fuente de verdad.

El detalle página por página y la cobertura científica se mantienen en [`docs/LEXICON_PROGRESS.md`](docs/LEXICON_PROGRESS.md), [`COVERAGE.md`](COVERAGE.md) y [`ROADMAP.md`](ROADMAP.md).

## Modelo epistemológico

CHD no equipara OCR con transcripción ni reconciliación computacional con edición crítica. La autoridad primaria permanece en `ALC1737`. Las capas derivadas registran su método, procedencia y estado de revisión. `BUE1890`, cuando se utiliza, funciona sólo como reimpresión histórica de control; nunca sustituye silenciosamente una lectura del ejemplar de 1737.

Los estados `machine_corrected_unverified` y `unresolved` identifican explícitamente el carácter IA-asistido del trabajo. Bajo la política vigente, `humanVerified` permanece en `false`; `human_verified` se conserva únicamente como estado reservado del esquema.

Una página puede alcanzar **cierre técnico** cuando sus fronteras, continuidades, enlaces/promociones y zonas irresueltas quedan completamente modeladas y el QA computacional es satisfactorio. Ese cierre no debe confundirse con autoridad diplomática o filológica humana.

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

El proyecto incluye validadores de JSONL, control de identificadores lexicográficos, reconstrucción del inventario canónico de candidatos y un flujo de QA en GitHub Actions. El workflow valida además la sintaxis del resumen de fase II, lo regenera desde las fuentes canónicas y falla si el archivo versionado queda desincronizado. Una corrida verde verifica consistencia computacional; no certifica corrección filológica humana.

Consulte [`docs/QA_AUTOMATION.md`](docs/QA_AUTOMATION.md), [`docs/LEXICON_RECONCILIATION_PROTOCOL.md`](docs/LEXICON_RECONCILIATION_PROTOCOL.md) y [`docs/TRANSCRIPTION_CONVENTIONS.md`](docs/TRANSCRIPTION_CONVENTIONS.md).

## Incertidumbres y límites abiertos

El repositorio conserva explícitamente problemas materiales y textuales en lugar de ocultarlos. Entre ellos se encuentran la discontinuidad material registrada entre las páginas digitales 157–158, lecturas de baja confianza en tipografía pequeña y artículos transpaginales cuya microestructura no puede resolverse con seguridad a partir de la evidencia disponible. El artículo `ALC1737-art-001045` (`Atormentar`) enlaza las pp.144–145 y permanece parcialmente `unresolved` en su forma cahíta.

La ausencia de una capa humana no autoriza a fortalecer estas lecturas. Cuando la evidencia disponible no basta, la incertidumbre permanece codificada.

## Próximo frente científico

El frente inmediato ya no es la promoción ordinaria de candidatos. Corresponde **cerrar la rama de consolidación y preparar el release candidate**: regenerar `phase2_open_work_summary.json` desde las fuentes canónicas, ejecutar QA de IDs/esquemas, regenerar exportaciones derivadas, actualizar `COVERAGE.md`, `ROADMAP.md` y `docs/LEXICON_PROGRESS.md`, comprobar el pipeline completo y revisar GitHub Actions antes de abrir el PR de consolidación.

La cola terminal de p.178 se mantiene como una extensión explícita de colación directa: preserva el inventario v0.2 p.133–177 como artefacto histórico reproducible y evita reescribir retrospectivamente sus métricas.

## Cita

Autor del proyecto: **Fernando Sandoval Gutierrez**, Universidad Autónoma de Ciudad Juárez, ORCID `0000-0002-3168-6725`.

La forma canónica de citación se encuentra en [`CITATION.cff`](CITATION.cff). Mientras el proyecto permanezca en `0.2.0-dev`, se recomienda citar también el commit exacto utilizado para garantizar reproducibilidad.

## Licencia

El repositorio declara **CC BY 4.0** para el dataset y la documentación correspondiente. Consulte [`LICENSE`](LICENSE) y [`DATA_LICENSE.md`](DATA_LICENSE.md) para el alcance y las condiciones aplicables.

## Principio editorial

**Preservar primero; estructurar después; inferir sólo en capas explícitas; mantener toda incertidumbre visible y trazable.**
