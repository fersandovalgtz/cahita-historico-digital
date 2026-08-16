<p align="center">
  <strong>Cahíta Histórico Digital</strong><br>
  <em>Arte de la lengua cahita (México, 1737) · edición histórico-digital · corpus abierto · infraestructura reproducible</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/estado-0.2.0--dev-6b7280?style=flat-square" alt="Estado 0.2.0-dev">
  <img src="https://img.shields.io/badge/fuente-1737-7a263a?style=flat-square" alt="Fuente 1737">
  <img src="https://img.shields.io/badge/páginas-182%2F182-2d6a4f?style=flat-square" alt="182 de 182 páginas inventariadas">
  <img src="https://img.shields.io/badge/full__page-128-2d6a4f?style=flat-square" alt="128 páginas full_page">
  <img src="https://img.shields.io/badge/candidatos%20v0.2-2%2C072-455B55?style=flat-square" alt="2072 candidatos v0.2">
  <img src="https://img.shields.io/badge/artículos%20estructurados-734-455B55?style=flat-square" alt="734 artículos históricos estructurados">
  <a href="https://github.com/fersandovalgtz/cahita-historico-digital/actions/workflows/qa.yml"><img src="https://github.com/fersandovalgtz/cahita-historico-digital/actions/workflows/qa.yml/badge.svg" alt="CHD QA"></a>
  <img src="https://img.shields.io/badge/revisión%20humana-0-b7791f?style=flat-square" alt="0 unidades human_verified">
  <a href="DATA_LICENSE.md"><img src="https://img.shields.io/badge/datos-CC%20BY%204.0-9a6b1f?style=flat-square" alt="Datos CC BY 4.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/código-MIT-172033?style=flat-square" alt="Código MIT"></a>
  <a href="https://orcid.org/0000-0002-3168-6725"><img src="https://img.shields.io/badge/ORCID-0000--0002--3168--6725-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"></a>
</p>

<p align="center">
  <a href="docs/SOURCE_ALC1737.md"><strong>Fuente histórica</strong></a> ·
  <a href="COVERAGE.md"><strong>Cobertura</strong></a> ·
  <a href="docs/LEXICON_PROGRESS.md"><strong>Lexicografía</strong></a> ·
  <a href="docs/LEXICON_RECONCILIATION_PROTOCOL.md"><strong>Reconciliación</strong></a> ·
  <a href="docs/TRANSCRIPTION_MODEL.md"><strong>Transcripción</strong></a> ·
  <a href="docs/QA_AUTOMATION.md"><strong>QA automatizado</strong></a> ·
  <a href="EDITORIAL_POLICY.md"><strong>Política editorial</strong></a> ·
  <a href="PROVENANCE.md"><strong>Procedencia</strong></a> ·
  <a href="ROADMAP.md"><strong>Hoja de ruta</strong></a> ·
  <a href="docs/REPOSITORY_CONSISTENCY_AUDIT_2026-08-16.md"><strong>Auditoría</strong></a> ·
  <a href="docs/ECOSYSTEM.md"><strong>Ecosistema</strong></a>
</p>

---

## Qué es Cahíta Histórico Digital

**Cahíta Histórico Digital (CHD)** es una infraestructura de investigación destinada a transformar testimonios históricos sobre la lengua cahíta y las variedades documentadas por sus fuentes en objetos digitales **trazables, versionados, citables, interoperables y reproducibles**.

El proyecto separa deliberadamente testimonio, OCR, reconstrucción de layout, candidatos computacionales, transcripción diplomática, estructuración lexicográfica y gramatical, normalización, inferencias analíticas y eventual revisión humana independiente. Ninguna de esas capas se trata como equivalente a otra.

La fuente inicial es el *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella*, impreso en México en 1737 por Francisco Xavier Sánchez. La portada no declara un autor personal: atribuye la obra a “vn Padre de la Compañía de JESUS, Missionero de mas de treinta años en la Provincia de Cynaloa”. CHD conserva esa **anonimia de la fuente primaria** y registra por separado las atribuciones posteriores divergentes.

El testimonio inicial se identifica internamente como **`ALC1737`**. La arquitectura permite incorporar testimonios y fuentes futuras sin mezclar ejemplares, ediciones, decisiones editoriales ni estados de autoridad.

## Fuente ALC1737

> *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella. Compuesto por vn Padre de la Compañía de JESUS, Missionero de mas de treinta años en la Provincia de Cynaloa.* México: Imprenta de D. Francisco Xavier Sánchez, 1737.

El ejemplar digital de trabajo procede del registro de Internet Archive [`artedelalenguaca00gonz`](https://archive.org/details/artedelalenguaca00gonz), asociado a la John Carter Brown Library, Brown University.

La obra contiene una gramática extensa, ejemplos en cahíta, un vocabulario castellano–cahíta y una sección final de numerales. `AL LECTOR` menciona expresamente **Hiaquis, Mayes y Thehuecos**. CHD conserva esas denominaciones como categorías históricas de la fuente y no las proyecta automáticamente sobre identidades lingüísticas contemporáneas.

Un problema filológico de interés aparece en la propia organización declarada: `AL LECTOR` denomina la obra “tripartita”, mientras el `PROHEMIO` anuncia **cuatro partes** y el ejemplar desarrolla `PARTE I`–`PARTE IV`. La inconsistencia se documenta; no se corrige silenciosamente.

→ [Fuente e historia material](docs/SOURCE_ALC1737.md) · [Autoría y atribuciones](docs/AUTHORSHIP.md) · [Fuentes](SOURCES.md)

## Estado científico actual

CHD se encuentra en desarrollo **`0.2.0-dev`**. No existe todavía una edición filológica cerrada, una release científica estable ni un DOI del proyecto.

| Dimensión | Estado actual |
|---|---:|
| Páginas digitales inventariadas | **182 / 182** |
| Páginas impresas numeradas mapeadas | **118 / 118** |
| OCR paginado reproducible | **182 / 182** |
| Transcripciones diplomáticas `full_page` | **128** |
| Partes I–IV del Arte | **completas en capa IA-asistida** |
| Candidatos lexicográficos v0.2 | **2,072 / 2,072 persistidos canónicamente** |
| Páginas del vocabulario con representación estructurada | **45 / 45** |
| Artículos históricos estructurados | **734** |
| Candidatos reconciliados en pp. 133–134 | **61 / 61** |
| Inicios visibles omitidos observados en pp. 133–134 | **14** |
| Paradigmas históricos | **3** |
| Construcciones modales | **9** |
| Construcciones no finitas | **5** |
| Construcciones participiales | **3** |
| Construcciones predicativas/modales | **6** |
| Grupos de verbos irregulares | **6** |
| Preposiciones/grupos | **43** |
| Grupos de adverbios | **11** |
| Conjunciones/metacategorías | **6** |
| Sistema numeral histórico | **1 bloque estructurado** |
| Observaciones de variación histórica identificadas | **17+** |
| QA automatizado | **activo; primera ejecución verde #3** |
| Revisión humana independiente | **0** |

La cifra **2,072** describe candidatos computacionales, no entradas del vocabulario. Los **734 artículos** representan la capa curatorial actualmente estructurada y tampoco constituyen todavía el recuento final del vocabulario histórico.

En las páginas 133–134 ya se completó la reconciliación candidato por candidato: 57 candidatos fueron clasificados como `article`, 3 como `continuation` y 1 permanece `unresolved`. Esta revisión mostró además 14 inicios visibles omitidos por el extractor. Por ello CHD mantiene separadas la cobertura de candidatos y la cobertura real de comienzos de artículo.

→ [Cobertura y significado de las métricas](COVERAGE.md) · [Progreso lexicográfico](docs/LEXICON_PROGRESS.md)

## Calidad OCR y fronteras lexicográficas

El diagnóstico OCR estratificado produjo **micro-CER 25.66%** y **micro-WER 51.96%** después de una normalización que neutraliza `ſ/s`, diacríticos, mayúsculas y puntuación. El OCR bruto sirve como capa de recuperación, alineación y triage, pero no se promueve directamente a texto científico.

El extractor vigente de fronteras, `hybrid_margin_mode_v0.2`, produjo **2,072 candidatos** sobre las 45 páginas del vocabulario. En la comparación diagnóstica intencional de pp. 133, 134, 150 y 177, v0.2 registró **97.13% de precisión, 89.89% de recall y 93.37% de F1**. Esta muestra es deliberada, no probabilística, y su referencia visual es IA-asistida; las métricas son de ingeniería editorial, no estimadores filológicos poblacionales.

El inventario v0.2 completo está persistido de forma lossless y reconstruible, con revisión generadora, hashes, manifiesto y script de verificación.

→ [Calidad OCR](docs/OCR_QUALITY.md) · [Extractor v0.2](docs/VOCAB_BOUNDARY_V02.md) · [Reconciliación](docs/LEXICON_RECONCILIATION_PROTOCOL.md)

## Arquitectura de evidencia

CHD adopta una cadena no destructiva:

**testimonio → OCR bruto → líneas/layout → candidatos de frontera → reconciliación material → transcripción diplomática → estructuración histórica → normalización → análisis derivado → revisión humana independiente cuando exista**.

Reglas centrales:

1. **La fuente no se sobrescribe.** Correcciones, expansiones y modernizaciones viven en capas separadas.
2. **La procedencia acompaña al dato.** Cada unidad debe remontarse a una fuente, página y actividad de procesamiento.
3. **La incertidumbre se conserva.** Una lectura dudosa o frontera incierta es un resultado documental legítimo.
4. **La autoridad está tipada.** `raw_ocr`, `machine_corrected_unverified`, `editorial_proposal`, `human_verified` y `unresolved` no son estados intercambiables.
5. **Un candidato no es un artículo.** Una frontera material confirmada tampoco implica que la lectura curatorial esté completa.
6. **La comparación diacrónica es una inferencia.** Ninguna forma histórica se declara automáticamente equivalente a una forma contemporánea.

Documentos normativos: [EDITORIAL_POLICY.md](EDITORIAL_POLICY.md) · [PROVENANCE.md](PROVENANCE.md) · [DATASHEET.md](DATASHEET.md) · [docs/TRANSCRIPTION_CONVENTIONS.md](docs/TRANSCRIPTION_CONVENTIONS.md) · [docs/DERIVED_ARTIFACTS_POLICY.md](docs/DERIVED_ARTIFACTS_POLICY.md).

## Paginación y estructura del volumen

El PDF de trabajo contiene **182 páginas digitales**. El cuerpo gramatical numerado ocupa las digitales 15–132 y corresponde a las impresas 1–118.

| Sección | Digital | Impresa |
|---|---:|---:|
| Preliminares | 1–14 | no paginadas |
| Parte I | 15–50 | 1–36 |
| Parte II | 51–69 parcial | 37–55 parcial |
| Parte III | 69 parcial–105 parcial | 55 parcial–91 parcial |
| Parte IV | 105 parcial–132 | 91 parcial–118 |
| Vocabulario | 133–177 | no paginado |
| Numerales | 178–180 | no paginados |
| Finales materiales | 181–182 | no paginados |

Las digitales **69** y **105** contienen fronteras intra-página entre partes y se modelan explícitamente como páginas mixtas. El inventario máquina-legible se conserva en [`data/source/alc1737/page_manifest.csv`](data/source/alc1737/page_manifest.csv) y [`data/source/alc1737/sections.json`](data/source/alc1737/sections.json).

## Corpus gramatical histórico

La capa de superficie del Arte está representada continuamente hasta `FIN DEL ARTE`. Sobre ella se han estructurado, entre otros objetos:

- 3 paradigmas históricos;
- 9 construcciones modales, reglas 207–234;
- 5 construcciones no finitas, reglas 237–256;
- 3 construcciones participiales, reglas 257–265;
- 6 construcciones predicativas/modales, reglas 266–284;
- 6 grupos de verbos irregulares, reglas 286–291;
- 43 preposiciones/grupos, reglas 293–340;
- 11 grupos de adverbios, reglas 341–359;
- 6 grupos de conjunciones/metacategorías, reglas 360–373 e interjecciones;
- sistema numeral histórico de digitales 178–180;
- 17+ observaciones de variación histórica identificadas.

Estas categorías se conservan primero en los términos del gramático de 1737. Las reinterpretaciones lingüísticas modernas deberán vivir en una capa analítica separada.

→ [Issue de gramática y variación](https://github.com/fersandovalgtz/cahita-historico-digital/issues/4)

## Corpus lexicográfico

El vocabulario ocupa digitales 133–177 y utiliza dos columnas con artículos multilínea. CHD ya dispone de:

- reconstrucción de layout;
- inventario canónico de 2,072 candidatos v0.2;
- 734 artículos históricos estructurados;
- representación curatorial en 45/45 páginas;
- modelado de remisiones `Buſca`, anáforas `Lo miſmo`, agrupaciones históricas y continuidades entre columnas/páginas;
- registro de catchwords como paratexto;
- reconciliación 61/61 de candidatos en pp. 133–134;
- capa específica para falsos negativos/inicios visibles omitidos.

Persisten una discontinuidad material F→H entre digitales 157–158 (`ALC1737-gap-0001`) y una anomalía `Lucer-` entre 161–162. Ninguna se rellena desde conocimiento externo.

→ [Progreso lexicográfico](docs/LEXICON_PROGRESS.md) · [Issue de corpus lexicográfico](https://github.com/fersandovalgtz/cahita-historico-digital/issues/3)

## Reproducibilidad y QA automatizado

El repositorio incluye scripts versionados para ingestión, hashes, OCR, layout, generación de candidatos, validación JSONL/JSON Schema, evaluación de OCR, validación de identificadores y reconstrucción del inventario canónico de candidatos.

La reproducción del inventario v0.2 queda fijada al PDF de trabajo con SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37` y al JSONL canónico con SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`.

El workflow `.github/workflows/qa.yml` ejecuta automáticamente puertas de integridad sobre `main` y pull requests. La primera ejecución completamente verde fue **CHD QA #3**, en el commit `26be9763b8001ff082524368000ab7fccfa6778c`. Esa corrida reconstruyó las 2,072 filas canónicas, verificó **734 `articleId` únicos**, validó todos los artículos históricos contra su JSON Schema y validó las capas de reconciliación y falsos negativos. Esto es **QA computacional**, no revisión filológica humana.

→ [Alcance y límites del QA automatizado](docs/QA_AUTOMATION.md)

## Estado de autoridad y validación humana

**Ningún objeto del repositorio está declarado actualmente `human_verified`.** Las transcripciones y decisiones curatoriales existentes son IA-asistidas y conservan su estado correspondiente. Esta limitación es explícita y forma parte del diseño científico del proyecto.

Antes de una edición filológica cerrada deberán ampliarse el cotejo humano, la revisión de anomalías y el QA estratificado.

## Citación

GitHub puede generar una cita desde [`CITATION.cff`](CITATION.cff). Mientras no exista una release archivada en Zenodo, cite el proyecto como versión de desarrollo y, cuando una afirmación dependa de una lectura histórica concreta, cite además el impreso de 1737 y la página correspondiente.

> Sandoval Gutierrez, Fernando. 2026. *Cahíta Histórico Digital — Arte de la lengua cahita (1737)*. Versión de desarrollo. GitHub.

Un futuro DOI del proyecto no sustituirá la referencia a la fuente primaria.

## Licencias y derechos

- **Software y código original:** [MIT](LICENSE).
- **Datos, metadatos, anotaciones y capas editoriales originales de CHD:** [CC BY 4.0](DATA_LICENSE.md).
- **Fuente histórica y digitalizaciones de terceros:** conservan su propio estatus jurídico y condiciones de procedencia; CHD no las relicencia.

## Próximas prioridades antes de productos científicos finales

1. sincronizar y auditar continuamente documentación, métricas e Issues;
2. completar la reconciliación lexicográfica y promover las unidades históricas pendientes;
3. cerrar la capa de falsos negativos e inventario real de inicios visibles;
4. ampliar la estructuración gramatical exhaustiva de Partes I–II y construir concordancias forma↔regla↔ejemplo↔página;
5. consolidar la exportación de variación histórica;
6. buscar e incorporar, con procedencia separada, testimonios independientes útiles para control textual;
7. ampliar las puertas CI/QA a transcripción, capas gramaticales, enlaces y consistencia de métricas;
8. estabilizar exportaciones JSON/CSV y preparar interoperabilidad TEI/TEI Lex-0/IIIF cuando corresponda;
9. ampliar revisión humana independiente;
10. sólo después congelar una release científica estable y archivarla en Zenodo.

## Ecosistema científico

CHD forma parte del ecosistema de humanidades digitales y ciencia abierta mantenido por Fernando Sandoval Gutierrez. Comparte principios metodológicos con [Rarámuri Histórico Digital](https://github.com/fersandovalgtz/raramuri-historico), pero mantiene corpus, decisiones editoriales e inferencias separados. También se vincula con [Rarámuri Digital](https://github.com/fersandovalgtz/raramuri-digital) y [Libro de Texto Mexicano Digital](https://github.com/fersandovalgtz/libro-texto-mexicano-digital).

→ [Mapa del ecosistema](docs/ECOSYSTEM.md)

## Autor y contacto académico

**Dr. Fernando Sandoval Gutierrez**  
ORCID: [0000-0002-3168-6725](https://orcid.org/0000-0002-3168-6725)  
Universidad Autónoma de Ciudad Juárez  
GitHub: [@fersandovalgtz](https://github.com/fersandovalgtz)

---

**Estado:** desarrollo científico activo `0.2.0-dev`. No existe todavía una release científica cerrada ni un DOI de Cahíta Histórico Digital.
