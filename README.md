# Cahíta Histórico Digital

**Edición histórico-digital, corpus abierto e infraestructura reproducible del _Arte de la lengua cahita_ impreso en México en 1737.**

Cahíta Histórico Digital (CHD) es una infraestructura de investigación orientada a conservar, describir, transcribir y estructurar de forma reproducible una fuente fundamental para la historia de las lenguas cahítas y de la lingüística misionera novohispana. El proyecto separa explícitamente el testimonio histórico, el OCR, la transcripción, la segmentación computacional y las decisiones curatoriales IA-asistidas.

> **Estado:** `1.0.0` — primera release científica estable del alcance técnico declarado. El vocabulario, la cobertura gramatical numerada, la interoperabilidad TEI Lex-0, los contratos, el freeze de datos y las incertidumbres de recolación están versionados y validados reproduciblemente. La preservación archivística y el DOI de versión permanecen pendientes hasta su depósito efectivo.

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

- **2,072 candidatos lexicográficos** `hybrid_margin_mode_v0.2` están persistidos canónicamente;
- **2,302 artículos históricos estructurados** integran la capa curatorial actual;
- las **45/45 páginas del Vocabulario (133–177)** tienen reconciliación candidate-level completa y cierre técnico IA-asistido dentro del alcance declarado;
- las páginas **145–177** completaron la Phase II de promoción/enlace y censo exhaustivo: **33/33 páginas** con censo visible exhaustivo y **33/33** con cierre técnico;
- en ese alcance quedan **0 candidatos `pending_promotion`**, **0 candidatos estructuralmente `unresolved`** y **0 fronteras `ambiguous`**;
- la auditoría gramatical registra **370/373 números nominales** con reclamación estructurada; los tres restantes —**127, 178 y 294**— son omisiones materiales documentadas del impreso;
- al conservar además las **dos reglas impresas como 129**, CHD representa **371/371 unidades gramaticales numeradas efectivamente impresas**;
- la concordancia gramatical derivada contiene **302 objetos** y **1,215 filas de evidencia explícita**;
- las incertidumbres semánticas, anafóricas o de microlectura que permanecen dentro de objetos ya estructurados se conservan explícitamente y no contradicen el cierre estructural;
- no existen objetos `human_verified`; la autoridad de las capas IA-asistidas permanece explícitamente separada de cualquier revisión humana independiente.

Los totales de Phase II no se mantienen manualmente como una segunda fuente de verdad. Se regeneran desde los estados de página y los `articleId` curatoriales mediante [`scripts/summarize_open_lexicon_work.py`](scripts/summarize_open_lexicon_work.py), cuyo resultado versionado es [`data/lexicon/reconciliation/phase2_open_work_summary.json`](data/lexicon/reconciliation/phase2_open_work_summary.json). Los snapshots históricos almacenados en estados de página conservan valor de procedencia, pero no sustituyen el conteo actual.

El cierre de Phase II y sus guardas epistemológicas se documentan en [`docs/PHASE2_COMPLETION_2026-08-21.md`](docs/PHASE2_COMPLETION_2026-08-21.md). El cierre técnico de la numeración gramatical se documenta en [`docs/GRAMMAR_COMPLETION_2026-08-21.md`](docs/GRAMMAR_COMPLETION_2026-08-21.md). El detalle página por página y la cobertura científica se mantienen en [`docs/LEXICON_PROGRESS.md`](docs/LEXICON_PROGRESS.md), [`COVERAGE.md`](COVERAGE.md) y [`ROADMAP.md`](ROADMAP.md).

## Modelo epistemológico

CHD no equipara OCR con transcripción ni reconciliación computacional con edición crítica. La autoridad primaria permanece en `ALC1737`. Las capas derivadas registran su método, procedencia y estado de revisión. `BUE1890`, cuando se utiliza, funciona sólo como reimpresión histórica de control; nunca sustituye silenciosamente una lectura del ejemplar de 1737.

Los estados `machine_corrected_unverified` y `unresolved` identifican explícitamente el carácter IA-asistido del trabajo. Bajo la política vigente, `humanVerified` permanece en `false`; `human_verified` se conserva únicamente como estado reservado del esquema, no como una etapa futura obligatoria.

Una página o capa puede alcanzar **cierre técnico** cuando sus fronteras, continuidades, enlaces, reclamaciones estructurales y zonas irresueltas quedan completamente modeladas dentro del alcance declarado y el QA computacional es satisfactorio. Ese cierre no debe confundirse con autoridad diplomática o filológica humana.

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

El proyecto incluye validadores de JSONL, control de identificadores lexicográficos, reconstrucción del inventario canónico de candidatos y un flujo de QA en GitHub Actions. El workflow valida además la sintaxis del resumen de Phase II, lo regenera desde las fuentes canónicas y falla si el archivo versionado queda desincronizado. Para gramática genera y comprueba en doble corrida una concordancia de evidencia y una auditoría de cobertura numerada. Una corrida verde verifica consistencia computacional; no certifica corrección filológica humana.

El cierre de p.177 y de Phase II quedó registrado el 21 de agosto de 2026; el cierre de la cobertura gramatical numerada se confirmó posteriormente ese mismo día con **370/373 números nominales**, siendo los tres huecos restantes omisiones impresas documentadas.

Consulte [`docs/QA_AUTOMATION.md`](docs/QA_AUTOMATION.md), [`docs/LEXICON_RECONCILIATION_PROTOCOL.md`](docs/LEXICON_RECONCILIATION_PROTOCOL.md), [`docs/TRANSCRIPTION_CONVENTIONS.md`](docs/TRANSCRIPTION_CONVENTIONS.md) y [`docs/GRAMMAR_COMPLETION_2026-08-21.md`](docs/GRAMMAR_COMPLETION_2026-08-21.md).

## Incertidumbres y límites abiertos

El repositorio conserva explícitamente problemas materiales y textuales en lugar de ocultarlos. Entre ellos se encuentran la discontinuidad material registrada entre las páginas digitales 157–158, lecturas de baja confianza en tipografía pequeña y artículos o reglas transpaginales cuya microestructura no puede resolverse con seguridad a partir de la evidencia disponible.

El hecho de que el vocabulario y la numeración gramatical tengan cierre técnico no convierte las lecturas IA-asistidas en una edición diplomática humana ni resuelve automáticamente todas las remisiones, anáforas o microlecturas.

## Próximo frente científico

Con v1.0.0, el frente inmediato deja de ser el cierre estructural del corpus y pasa a **preservación, revisión filológica post-release y explotación científica de los datos**. Las prioridades son:

1. depositar la release archivada y registrar DOI de versión/Concept DOI cuando sean efectivamente asignados;
2. reabrir las 22 recolaciones sólo cuando exista cotejo directo del mismo testimonio o revisión filológica humana trazable;
3. consolidar las 76 evidencias de etiquetas históricas de variedad y ampliar su relación explícita con la gramática;
4. continuar estudios lingüísticos e historiográficos derivados sin retroproyectar automáticamente categorías modernas sobre `ALC1737`;
5. evaluar CLDF como derivado analítico post-v1 únicamente cuando la segmentación y la identidad lingüística requeridas estén sustentadas.

## Cita

Autor del proyecto: **Fernando Sandoval Gutierrez**, Universidad Autónoma de Ciudad Juárez, ORCID `0000-0002-3168-6725`.

La forma canónica de citación de v1.0.0 se encuentra en [`CITATION.cff`](CITATION.cff). Para reproducibilidad se recomienda conservar el tag `v1.0.0` y, cuando sea pertinente, el commit exacto utilizado. El DOI se añadirá únicamente después de su asignación archivística efectiva.

## Licencia

El repositorio declara **CC BY 4.0** para el dataset y la documentación correspondiente. Consulte [`LICENSE`](LICENSE) y [`DATA_LICENSE.md`](DATA_LICENSE.md) para el alcance y las condiciones aplicables.

## Principio editorial

**Preservar primero; estructurar después; inferir sólo en capas explícitas; mantener toda incertidumbre visible y trazable.**
