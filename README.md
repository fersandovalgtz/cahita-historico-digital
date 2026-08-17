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

A 2026-08-16:

- **2,072 candidatos lexicográficos** `hybrid_margin_mode_v0.2` están persistidos canónicamente;
- **1,045 artículos históricos estructurados** integran la capa curatorial;
- las páginas **133–144** están cerradas técnicamente en reconciliación de candidatos, censo de inicios visibles y promoción/enlace IA-asistidos;
- la página **145** tiene sus **39 candidatos canónicos reconciliados**: 33 `article`, 3 `continuation` y 3 `unresolved`; su censo visible exhaustivo y la promoción de 20 fronteras permanecen abiertos;
- la página **146** tiene sus **47 candidatos canónicos reconciliados**: 45 `article` y 2 `continuation`, sin candidatos `unresolved`; conserva 22 fronteras `pending_promotion` y un censo visible todavía no exhaustivo;
- la página **147** tiene sus **51 candidatos canónicos reconciliados**: 51 `article`, sin candidatos `unresolved`; conserva 36 fronteras `pending_promotion` y un censo visible todavía no exhaustivo;
- la página **148** tiene sus **44 candidatos canónicos reconciliados**: 44 `article`, sin candidatos `unresolved`; conserva 29 fronteras `pending_promotion`. Cinco artículos seleccionados (`ALC1737-art-000231`–`000235`) recibieron corrección documentada de metadatos espaciales de columna derecha→izquierda, sin modificar su transcripción;
- la página **149** tiene sus **61 candidatos canónicos reconciliados**: 55 `article`, 5 `continuation` y 1 `unresolved`; conserva 40 fronteras `pending_promotion`. El candidato L-019 permanece irresuelto por intercalación OCR en el bloque `Calentura`;
- la página **150** tiene sus **56 candidatos canónicos reconciliados**: 55 `article` y 1 `unresolved`; los 15 artículos seleccionados `ALC1737-art-000254`–`000268` quedaron enlazados, permanecen 40 fronteras `pending_promotion` y el censo visible todavía no es exhaustivo;
- las páginas **151–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;
- no existen objetos `human_verified` y la política vigente no contempla intervención humana independiente;
- las lecturas inciertas se conservan como tales y no se completan por inferencia silenciosa.

El detalle cuantitativo y el siguiente frente de trabajo se mantienen en [`docs/LEXICON_PROGRESS.md`](docs/LEXICON_PROGRESS.md) y [`COVERAGE.md`](COVERAGE.md).

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

El proyecto incluye validadores de JSONL, control de identificadores lexicográficos, reconstrucción del inventario canónico de candidatos y un flujo de QA en GitHub Actions. Una corrida verde verifica consistencia computacional; no certifica corrección filológica humana.

Consulte [`docs/QA_AUTOMATION.md`](docs/QA_AUTOMATION.md), [`docs/LEXICON_RECONCILIATION_PROTOCOL.md`](docs/LEXICON_RECONCILIATION_PROTOCOL.md) y [`docs/TRANSCRIPTION_CONVENTIONS.md`](docs/TRANSCRIPTION_CONVENTIONS.md).

## Incertidumbres y límites abiertos

El repositorio conserva explícitamente problemas materiales y textuales en lugar de ocultarlos. Entre ellos se encuentran la discontinuidad material registrada entre las páginas digitales 157–158, lecturas de baja confianza en tipografía pequeña y artículos transpaginales cuya microestructura no puede resolverse con seguridad a partir de la evidencia disponible. El artículo `ALC1737-art-001045` (`Atormentar`) enlaza las pp.144–145 y permanece parcialmente `unresolved` en su forma cahíta.

La ausencia de una capa humana no autoriza a fortalecer estas lecturas. Cuando la evidencia de máquina no basta, la incertidumbre permanece codificada.

## Próximo frente científico

En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; y en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`. Las páginas 145–150 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 151**, con 50 candidatos canónicos; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual.

## Cita

Autor del proyecto: **Fernando Sandoval Gutierrez**, Universidad Autónoma de Ciudad Juárez, ORCID `0000-0002-3168-6725`.

La forma canónica de citación se encuentra en [`CITATION.cff`](CITATION.cff). Mientras el proyecto permanezca en `0.2.0-dev`, se recomienda citar también el commit exacto utilizado para garantizar reproducibilidad.

## Licencia

El repositorio declara **CC BY 4.0** para el dataset y la documentación correspondiente. Consulte [`LICENSE`](LICENSE) y [`DATA_LICENSE.md`](DATA_LICENSE.md) para el alcance y las condiciones aplicables.

## Principio editorial

**Preservar primero; estructurar después; inferir sólo en capas explícitas; mantener toda incertidumbre visible y trazable.**
