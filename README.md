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

Estado computacional vigente al **17 de agosto de 2026**:

- **2,072 candidatos lexicográficos** `hybrid_margin_mode_v0.2` están persistidos canónicamente;
- **1,049 artículos históricos estructurados** integran la capa curatorial actual;
- las **45/45 páginas del Vocabulario (133–177)** tienen reconciliación candidate-level completa;
- las páginas **133–144** constituyen el tramo técnicamente cerrado en reconciliación, censo visible y promoción/enlace IA-asistidos dentro del alcance declarado;
- las páginas **145–177** forman la fase II de promoción/enlace y censo exhaustivo de inicios visibles;
- en ese alcance permanecen **1,047 candidatos `pending_promotion`**, **1 candidato estructuralmente `unresolved`** y **9 fronteras `ambiguous`**;
- **0/33 páginas** de p.145–177 tienen todavía censo visible exhaustivo y **0/33** cierre técnico;
- el primer lote conservador de fase II en p.145 promovió **4 artículos**, reduciendo los pendientes de esa página a **17**;
- no existen objetos `human_verified`; la autoridad de las capas IA-asistidas permanece explícitamente separada de cualquier revisión humana.

Los totales de fase II no se mantienen manualmente como una segunda fuente de verdad. Se regeneran desde los estados de página y los `articleId` curatoriales mediante [`scripts/summarize_open_lexicon_work.py`](scripts/summarize_open_lexicon_work.py), cuyo resultado versionado es [`data/lexicon/reconciliation/phase2_open_work_summary.json`](data/lexicon/reconciliation/phase2_open_work_summary.json). Los snapshots históricos almacenados en estados de página conservan valor de procedencia, pero no sustituyen el conteo actual.

El detalle página por página y la cobertura científica se mantienen en [`docs/LEXICON_PROGRESS.md`](docs/LEXICON_PROGRESS.md), [`COVERAGE.md`](COVERAGE.md) y [`ROADMAP.md`](ROADMAP.md).

## Modelo epistemológico

CHD no equipara OCR con transcripción ni reconciliación computacional con edición crítica. La autoridad primaria permanece en `ALC1737`. Las capas derivadas registran su método, procedencia y estado de revisión. `BUE1890`, cuando se utiliza, funciona sólo como reimpresión histórica de control; nunca sustituye silenciosamente una lectura del ejemplar de 1737.

Los estados `machine_corrected_unverified` y `unresolved` identifican explícitamente el carácter IA-asistido del trabajo. Bajo la política vigente, `humanVerified` permanece en `false`; `human_verified` se conserva únicamente como estado reservado del esquema, no como una etapa futura obligatoria.

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

La ausencia de una capa humana no autoriza a fortalecer estas lecturas. Cuando la evidencia de máquina no basta, la incertidumbre permanece codificada.

## Próximo frente científico

La reconciliación geométrica de candidatos del Vocabulario está completa en **pp.133–177 (45/45 páginas)**. El frente activo es la **fase II de p.145–177**: completar, página por página, el **censo exhaustivo de inicios visibles** y la **promoción/enlace** de fronteras todavía sustentadas sólo por geometría/OCR. El primer lote de p.145 demostró el criterio operativo: promover sólo cuando el propio testimonio `ALC1737` ofrece evidencia suficientemente convergente y mantener pendientes las lecturas materialmente divergentes.

El corpus curatorial actual contiene **1,049 artículos estructurados** y quedan **1,047 candidatos `pending_promotion`** en el alcance p.145–177. Ese conteo debe leerse como trabajo estructural abierto, no como una equivalencia automática con “artículos faltantes”. No se calculan métricas de precisión/recall/F1 para páginas cuyo denominador visible siga sin ser exhaustivo.

## Cita

Autor del proyecto: **Fernando Sandoval Gutierrez**, Universidad Autónoma de Ciudad Juárez, ORCID `0000-0002-3168-6725`.

La forma canónica de citación se encuentra en [`CITATION.cff`](CITATION.cff). Mientras el proyecto permanezca en `0.2.0-dev`, se recomienda citar también el commit exacto utilizado para garantizar reproducibilidad.

## Licencia

El repositorio declara **CC BY 4.0** para el dataset y la documentación correspondiente. Consulte [`LICENSE`](LICENSE) y [`DATA_LICENSE.md`](DATA_LICENSE.md) para el alcance y las condiciones aplicables.

## Principio editorial

**Preservar primero; estructurar después; inferir sólo en capas explícitas; mantener toda incertidumbre visible y trazable.**
