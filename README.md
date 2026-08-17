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
- la página **151** tiene sus **50 candidatos canónicos reconciliados**: 47 `article` y 3 `continuation`; los 15 artículos seleccionados `ALC1737-art-000269`–`000283` quedaron enlazados mediante 13 candidatos, con L-002 modelado como `merged_articles`; permanecen 34 fronteras `pending_promotion` y el censo visible sigue no exhaustivo;
- la página **152** tiene sus **52 candidatos canónicos reconciliados**: 52 `article`, sin continuaciones ni candidatos estructuralmente irresueltos; los 15 artículos seleccionados `ALC1737-art-000284`–`000298` quedaron enlazados, permanecen 37 fronteras `pending_promotion` y el censo visible sigue no exhaustivo;
- la página **153** tiene sus **51 candidatos canónicos reconciliados**: 46 `article`, 1 `continuation` y 4 `unresolved`; se documentan además 2 falsos negativos conocidos en el borde superior derecho, 34 fronteras `pending_promotion` y un censo visible no exhaustivo;
- la página **154** tiene sus **56 candidatos canónicos reconciliados**: 56 `article`, con 54 fronteras `exact`, 1 `undersegmented` y 1 `oversegmented`; los 15 artículos seleccionados `ALC1737-art-000314`–`000328` quedaron enlazados, permanecen 41 fronteras `pending_promotion` y el censo visible sigue no exhaustivo;
- la página **155** tiene sus **49 candidatos canónicos reconciliados**: 45 `article` y 4 `continuation`; se documentan 2 falsos negativos conocidos, los 15 artículos seleccionados `ALC1737-art-000329`–`000343` quedaron enlazados, permanecen 32 fronteras `pending_promotion` y el censo visible sigue no exhaustivo;
- la página **156** tiene sus **52 candidatos canónicos reconciliados**: 52 `article`, sin continuaciones ni candidatos estructuralmente irresueltos; L-001 queda `merged_articles` con `Enſeñar` + `Enſeñanza`, se documenta 1 falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000344`–`000358` quedaron enlazados, permanecen 38 fronteras `pending_promotion` y el censo visible sigue no exhaustivo;
- la página **157** tiene sus **42 candidatos canónicos reconciliados**: 38 `article`, 2 `continuation` y 2 `unresolved`; se documentan 4 falsos negativos internos dentro de regiones `merged_articles`, los 15 artículos seleccionados `ALC1737-art-000359`–`000373` quedaron enlazados, permanecen 27 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; el salto p.157→158 se conserva como `ALC1737-gap-0001`, sin reconstruir el material F/G ausente;
- la página **158** tiene sus **53 candidatos canónicos reconciliados**: 50 `article` y 3 `continuation`, sin candidatos estructuralmente `unresolved`; L-014 queda `merged_articles` con `Henchir` + `Henchimiento`, se documenta 1 falso negativo interno seleccionado, los 15 artículos `ALC1737-art-000374`–`000388` quedaron enlazados, permanecen 36 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; la página inicia una secuencia H fresca después de `ALC1737-gap-0001`;
- la página **159** tiene sus **52 candidatos canónicos reconciliados**: 49 `article` y 3 `continuation`, sin candidatos estructuralmente `unresolved`; los 15 artículos seleccionados `ALC1737-art-000389`–`000403` quedaron enlazados, permanecen 34 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; la columna de `000398`–`000400` se corrigió de forma trazable de derecha a izquierda, con procedencia dedicada y sin cambiar la transcripción;
- la página **160** tiene sus **45 candidatos canónicos reconciliados**: 44 `article` y 1 `continuation`, sin candidatos estructuralmente `unresolved`; se documenta 1 falso negativo seleccionado (`Ladrona. Eet buame.`), los 15 artículos `ALC1737-art-000404`–`000418` quedaron enlazados a evidencia estructural, permanecen 30 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-026 (`Latir la vena, ò el corazón`) continúa físicamente en p.161 L-001;
- la página **161** tiene sus **33 candidatos canónicos reconciliados**: 31 `article`, 1 `continuation` y 1 `unresolved`; se documentan 3 falsos negativos seleccionados (`Lengua de buey`, `Libro`, `Limon`), los 15 artículos `ALC1737-art-000419`–`000433` quedaron enlazados a evidencia estructural, permanecen 19 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; L-001 continúa `Latir la vena, ò el corazón` desde p.160 y p.162 abre fresco en `Media coſa la mitad`;
- la página **162** tiene sus **39 candidatos canónicos reconciliados**: 39 `article`, sin candidatos estructuralmente `unresolved`; L-006 queda `merged_articles` con `Melon` + `Memoria`, se documenta `Memoria. Aubuate.` como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000434`–`000448` quedaron enlazados, permanecen 25 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-006 y R-019 quedan `undersegmented`, `Mirar` (000448) se alinea a R-016 y el `Mozo` final funciona como reclamo hacia una voz fresca de p.163;
- la página **163** tiene sus **49 candidatos canónicos reconciliados**: 42 `article` y 7 `continuation`, sin candidatos estructuralmente `unresolved`; se documenta `Mozo de edad. Buſca mancebo.` (000449) como falso negativo de borde superior, los 15 artículos seleccionados `ALC1737-art-000449`–`000463` quedaron enlazados a evidencia estructural, permanecen 28 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; L-026→R-001 cruza columnas y p.164 abre fresco con `Nacimiento. Ioleria.`;
- la página **164** tiene sus **51 candidatos canónicos reconciliados**: 51 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; R-018, R-020 y R-022 quedan `merged_articles`, los 15 artículos seleccionados `ALC1737-art-000464`–`000478` quedaron enlazados, permanecen 36 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; `000477` (`Noez, y nogal. Lo miſmo.`) conserva su anáfora semántica `unresolved` sin volver irresuelta su frontera física; p.165 abre fresco con `Obra aſſi, hechura. Chupari.`;
- la página **165** tiene sus **56 candidatos canónicos reconciliados**: 52 `article` y 4 `continuation`, sin candidatos estructuralmente `unresolved`; L-016 queda `merged_articles` con `Oydor` + `Oyr`, se documenta `Oyr. Hicaha.` (000488) como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000479`–`000493` quedaron enlazados a evidencia estructural, permanecen 38 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-014 queda `undersegmented`, R-016 conserva frontera `ambiguous` sin lema inventado y p.166 abre fresco con `Paga tal. Bebeti.`;
- la página **166** tiene sus **50 candidatos canónicos reconciliados**: 50 `article`, sin continuaciones ni candidatos estructuralmente `unresolved`; L-003 queda `merged_articles` con `Palabra` + `Palma arbol conocido`, se documenta `Palma arbol conocido. Taco.` (000497) como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000494`–`000508` quedaron enlazados a evidencia estructural, permanecen 36 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; L-007, R-008 y R-022 quedan `undersegmented` por mezcla/fuga de orden OCR o material de borde, y p.167 abre fresco con `Paſſo de las beſtias. Arabuerama.`;
- la página **167** tiene sus **55 candidatos canónicos reconciliados**: 54 `article` y 1 `continuation`, sin candidatos estructuralmente `unresolved`; L-010 queda `merged_articles` con `Pato. Tepciabiri.` + `Paxaro generalmente. Moel.`, se documenta `Paxaro generalmente. Moel.` (000519) como falso negativo interno, los 15 artículos seleccionados `ALC1737-art-000509`–`000523` quedaron enlazados a evidencia estructural, permanecen 40 fronteras `pending_promotion` y el censo visible sigue no exhaustivo; R-002→R-003 modela la única continuidad, L-030 conserva frontera `ambiguous`, R-011/R-013/R-025 quedan `undersegmented`, R-020 queda `merged_articles` sin inflar el censo y p.168 abre fresco con `Penacho`;
- las páginas **168–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;
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

En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; en **p.152** quedan 37 `pending_promotion`; en **p.153** quedan 34 `pending_promotion` y 4 candidatos estructurales `unresolved`; en **p.154** quedan 41 `pending_promotion`; en **p.155** quedan 32 `pending_promotion`; en **p.156** quedan 38 `pending_promotion`; en **p.157** quedan 27 `pending_promotion` y 2 candidatos `unresolved`; en **p.158** quedan 36 `pending_promotion`; en **p.159** quedan 34 `pending_promotion`; en **p.160** quedan 30 `pending_promotion`; en **p.161** quedan 19 `pending_promotion` y 1 candidato `unresolved`; y en **p.162** quedan 25 `pending_promotion`; en **p.163** quedan 28 `pending_promotion`; en **p.164** quedan 36 `pending_promotion`; en **p.165** quedan 38 `pending_promotion`; en **p.166** quedan 36 `pending_promotion`; y en **p.167** quedan 40 `pending_promotion`. Las páginas 145–167 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 168**, con 32 candidatos canónicos —14 izquierda y 18 derecha—; el primer candidato conserva `Penacho`, mientras la capa seleccionada `ALC1737-art-000524`–`000538` comienza con `Penca de miſcal. Cuumaicoa.`.

## Cita

Autor del proyecto: **Fernando Sandoval Gutierrez**, Universidad Autónoma de Ciudad Juárez, ORCID `0000-0002-3168-6725`.

La forma canónica de citación se encuentra en [`CITATION.cff`](CITATION.cff). Mientras el proyecto permanezca en `0.2.0-dev`, se recomienda citar también el commit exacto utilizado para garantizar reproducibilidad.

## Licencia

El repositorio declara **CC BY 4.0** para el dataset y la documentación correspondiente. Consulte [`LICENSE`](LICENSE) y [`DATA_LICENSE.md`](DATA_LICENSE.md) para el alcance y las condiciones aplicables.

## Principio editorial

**Preservar primero; estructurar después; inferir sólo en capas explícitas; mantener toda incertidumbre visible y trazable.**
