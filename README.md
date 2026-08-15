<p align="center">
  <strong>Cahíta Histórico Digital</strong><br>
  <em>Arte de la lengua cahita (México, 1737) · edición histórico-digital · corpus abierto · infraestructura reproducible</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/estado-0.1.4--dev-6b7280?style=flat-square" alt="Estado 0.1.4-dev">
  <img src="https://img.shields.io/badge/fuente-1737-7a263a?style=flat-square" alt="Fuente 1737">
  <img src="https://img.shields.io/badge/páginas-182%2F182-2d6a4f?style=flat-square" alt="182 de 182 páginas inventariadas">
  <img src="https://img.shields.io/badge/OCR%20micro--CER-25.66%25-b7791f?style=flat-square" alt="Micro CER OCR 25.66%">
  <img src="https://img.shields.io/badge/candidatos-1%2C680-455B55?style=flat-square" alt="1680 candidatos de límites de artículo">
  <a href="DATA_LICENSE.md"><img src="https://img.shields.io/badge/datos-CC%20BY%204.0-9a6b1f?style=flat-square" alt="Datos CC BY 4.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/código-MIT-172033?style=flat-square" alt="Código MIT"></a>
  <a href="https://orcid.org/0000-0002-3168-6725"><img src="https://img.shields.io/badge/ORCID-0000--0002--3168--6725-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"></a>
</p>

<p align="center">
  <a href="docs/SOURCE_ALC1737.md"><strong>Fuente histórica</strong></a> ·
  <a href="COVERAGE.md"><strong>Cobertura</strong></a> ·
  <a href="docs/OCR_QUALITY.md"><strong>Calidad OCR</strong></a> ·
  <a href="docs/VOCAB_CANDIDATES.md"><strong>Vocabulario</strong></a> ·
  <a href="EDITORIAL_POLICY.md"><strong>Política editorial</strong></a> ·
  <a href="PROVENANCE.md"><strong>Procedencia</strong></a> ·
  <a href="ROADMAP.md"><strong>Hoja de ruta</strong></a> ·
  <a href="docs/ECOSYSTEM.md"><strong>Ecosistema</strong></a>
</p>

---

## Qué es Cahíta Histórico Digital

**Cahíta Histórico Digital (CHD)** es una infraestructura de investigación destinada a transformar testimonios históricos sobre la lengua cahíta y las variedades documentadas por sus fuentes en objetos digitales **trazables, versionados, citables, interoperables y reproducibles**. El proyecto mantiene separadas la reproducción histórica, el OCR, la reconstrucción de layout, la segmentación, la transcripción, la normalización, los datos estructurados y las inferencias analíticas.

La fuente inicial es el *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella*, impreso en México en 1737 por Francisco Xavier Sánchez. La portada no declara un autor personal: atribuye la obra a “vn Padre de la Compañía de JESUS, Missionero de mas de treinta años en la Provincia de Cynaloa”. Por ello, CHD conserva la **anonimia de la fuente primaria** y registra por separado la historia de atribuciones posteriores, sin convertir una atribución discutida en autoría resuelta.

El testimonio inicial se identifica internamente como **`ALC1737`**. La arquitectura permite incorporar futuras fuentes cahítas sin mezclar obras, ediciones, ejemplares, capas editoriales ni estados de autoridad.

## Fuente ALC1737

**Referencia primaria de trabajo:**

> *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella. Compuesto por vn Padre de la Compañía de JESUS, Missionero de mas de treinta años en la Provincia de Cynaloa.* México: Imprenta de D. Francisco Xavier Sánchez, 1737.

El ejemplar digital de trabajo procede del registro de Internet Archive [`artedelalenguaca00gonz`](https://archive.org/details/artedelalenguaca00gonz), asociado a la John Carter Brown Library, Brown University.

La obra contiene una gramática extensa y un vocabulario castellano–cahíta. `AL LECTOR` menciona expresamente **Hiaquis, Mayes y Thehuecos**, con observaciones sobre similitudes léxicas y diferencias de uso. CHD conserva esas denominaciones como categorías históricas de la fuente y no las proyecta automáticamente sobre identidades lingüísticas contemporáneas.

Un problema filológico de interés aparece en la organización declarada del impreso: `AL LECTOR` denomina la obra “tripartita”, mientras el `PROHEMIO` anuncia **cuatro partes** y el ejemplar desarrolla `PARTE I`–`PARTE IV`. La inconsistencia se documenta, no se corrige silenciosamente.

→ [Fuente e historia material](docs/SOURCE_ALC1737.md) · [Autoría y atribuciones](docs/AUTHORSHIP.md) · [Fuentes](SOURCES.md)

## Estado científico actual

CHD se encuentra en desarrollo **`0.1.4-dev`**. La ingestión y el modelado inicial ya permiten auditar el proceso, pero el repositorio **no declara todavía una edición filológica cerrada**.

| Dimensión | Estado |
|---|---:|
| Páginas digitales inventariadas | **182 / 182** |
| Páginas impresas numeradas mapeadas | **118 / 118** |
| Segmentación macro | **182 / 182** |
| Checksums de archivos fuente de trabajo | **2 / 2** |
| Extracción OCR reproducible | **182 / 182** |
| Muestra de calidad OCR | **6 estratos** |
| Micro-CER OCR normalizado | **25.66%** |
| Micro-WER OCR normalizado | **51.96%** |
| Líneas OCR/layout del vocabulario extraídas localmente | **3,899** |
| Candidatos de límites de artículo | **1,680** |
| Candidatos versionados como muestra | **38** |
| Entradas lexicográficas piloto | **12** |
| Entradas de producción | **0** |
| Revisión humana independiente | **0** |

Las cifras `3,899` y `1,680` describen **capas computacionales**, no el número de entradas del vocabulario histórico. Los 12 registros piloto están marcados `machine_corrected_unverified`; ninguno es `human_verified`.

→ [Cobertura y significado de las métricas](COVERAGE.md)

## Arquitectura de evidencia

CHD adopta una cadena no destructiva:

**testimonio → OCR bruto → líneas/layout → candidatos de límites de artículo → revisión de fronteras → transcripción diplomática → transcripción corregida → estructuración lexicográfica → normalización → análisis derivado → revisión humana independiente cuando exista**.

Cinco reglas gobiernan el proyecto:

1. **La fuente no se sobrescribe.** Correcciones, expansiones y modernizaciones viven en capas separadas.
2. **La procedencia acompaña al dato.** Cada unidad debe poder remontarse a una fuente, página y actividad de procesamiento.
3. **La incertidumbre se conserva.** Una lectura dudosa o una frontera incierta son resultados documentales legítimos.
4. **La autoridad está tipada.** OCR, candidato computacional, corrección IA-asistida, propuesta editorial y revisión humana no son estados intercambiables.
5. **La comparación diacrónica es una inferencia.** Ninguna forma histórica se declara automáticamente equivalente a una forma contemporánea.

Documentos normativos: [EDITORIAL_POLICY.md](EDITORIAL_POLICY.md) · [PROVENANCE.md](PROVENANCE.md) · [DATASHEET.md](DATASHEET.md) · [docs/TRANSCRIPTION_CONVENTIONS.md](docs/TRANSCRIPTION_CONVENTIONS.md).

## Paginación y estructura del volumen

El PDF de trabajo contiene **182 páginas digitales**. El cuerpo gramatical numerado ocupa las páginas digitales 15–132 y corresponde exactamente a las páginas impresas 1–118:

```text
printed_page = digital_page - 14
```

| Sección | Digital | Impresa |
|---|---:|---:|
| Preliminares | 1–14 | no paginadas |
| Parte I | 15–50 | 1–36 |
| Parte II | 51–68 | 37–54 |
| Parte III | 69–104 | 55–90 |
| Parte IV | 105–132 | 91–118 |
| Vocabulario | 133–177 | no paginado |
| Numerales | 178–180 | no paginados |
| Finales materiales | 181–182 | no paginados |

El inventario máquina-legible se conserva en [`data/source/alc1737/page_manifest.csv`](data/source/alc1737/page_manifest.csv) y [`data/source/alc1737/sections.json`](data/source/alc1737/sections.json).

## OCR: por qué no se usa como transcripción

Una evaluación estratificada en seis zonas del volumen produjo un **micro-CER de 25.66%** y un **micro-WER de 51.96%** después de neutralizar `ſ/s`, diacríticos, mayúsculas y puntuación. El resultado confirma que el OCR bruto es útil como capa de recuperación y alineación, pero no puede promoverse directamente a texto científico.

En el vocabulario, la reconstrucción previa de las dos columnas mejora sustancialmente el fragmento probado, lo que indica que la geometría de la página es parte importante del problema. Esta observación guía el pipeline, pero no se extrapola como tasa global.

→ [Diagnóstico, muestra y método reproducible](docs/OCR_QUALITY.md)

## Vocabulario: de la página al artículo

El vocabulario utiliza dos columnas y admite artículos multilínea. `scripts/extract_vocab_layout.py` conserva líneas OCR, coordenadas y columna; `scripts/extract_vocab_candidates.py` genera después agrupaciones **conservadoras** basadas en indentación.

La corrida completa de páginas 133–177 produjo **1,680 candidatos de límites de artículo**, todos validados estructuralmente contra un esquema específico. Esta capa no separa todavía lema castellano y forma cahíta y no se presenta como censo lexicográfico.

Una muestra de 38 candidatos de la página 134 está versionada para mostrar tanto aciertos como falsas fronteras. La existencia visible de errores es deliberada: permite evaluar el algoritmo antes de escalar una corrección.

→ [Candidatos y limitaciones](docs/VOCAB_CANDIDATES.md) · [Piloto de 12 entradas](docs/PILOT_LEXICON_P134.md)

## Reproducibilidad

La ingestión puede reconstruirse localmente a partir de los dos archivos de trabajo identificados por SHA-256. El repositorio incluye scripts para:

- calcular hashes e inventariar las 182 páginas;
- extraer OCR por página;
- reconstruir columnas mediante `pdftotext -bbox-layout`;
- generar candidatos de límites de artículo;
- validar JSONL contra JSON Schema;
- medir CER/WER sobre una muestra versionada.

→ [Ingestión reproducible](docs/INGESTION_ALC1737.md) · [`scripts/`](scripts/) · [`schemas/`](schemas/)

## Estructura principal

```text
cahita-historico-digital/
├── README.md
├── CITATION.cff
├── codemeta.json
├── DATASHEET.md
├── EDITORIAL_POLICY.md
├── PROVENANCE.md
├── COVERAGE.md
├── SOURCES.md
├── ROADMAP.md
├── CHANGELOG.md
├── docs/
│   ├── SOURCE_ALC1737.md
│   ├── AUTHORSHIP.md
│   ├── INGESTION_ALC1737.md
│   ├── TRANSCRIPTION_CONVENTIONS.md
│   ├── OCR_QUALITY.md
│   ├── VOCAB_CANDIDATES.md
│   ├── PILOT_LEXICON_P134.md
│   └── ECOSYSTEM.md
├── data/
│   ├── source/alc1737/
│   ├── diplomatic/pilot/
│   ├── lexicon/pilot/
│   ├── lexicon/candidates/
│   └── validation/
├── schemas/
└── scripts/
```

## Citación

GitHub puede generar una cita desde [`CITATION.cff`](CITATION.cff). Mientras no exista una release archivada en Zenodo, cite el proyecto como versión de desarrollo:

> Sandoval Gutierrez, Fernando. 2026. *Cahíta Histórico Digital — Arte de la lengua cahita (1737)*. Versión de desarrollo. GitHub. https://github.com/fersandovalgtz/cahita-historico-digital

Cuando una afirmación dependa de una lectura histórica concreta, cite además el impreso de 1737 y la página correspondiente. Un futuro DOI del proyecto no sustituirá la referencia a la fuente primaria.

## Licencias y derechos

- **Software y código original:** [MIT](LICENSE).
- **Datos, metadatos, anotaciones y capas editoriales originales de CHD:** [CC BY 4.0](DATA_LICENSE.md).
- **Fuente histórica y digitalizaciones de terceros:** conservan su propio estatus jurídico y condiciones de procedencia; CHD no las relicencia.

## Ecosistema científico

CHD forma parte del ecosistema de humanidades digitales y ciencia abierta mantenido por Fernando Sandoval Gutierrez. Comparte principios metodológicos con [Rarámuri Histórico Digital](https://github.com/fersandovalgtz/raramuri-historico), pero mantiene corpus, vocabularios, decisiones editoriales e inferencias separados. También se vincula con [Rarámuri Digital](https://github.com/fersandovalgtz/raramuri-digital) y [Libro de Texto Mexicano Digital](https://github.com/fersandovalgtz/libro-texto-mexicano-digital).

→ [Mapa del ecosistema](docs/ECOSYSTEM.md)

## Autor y contacto académico

**Dr. Fernando Sandoval Gutierrez**  
ORCID: [0000-0002-3168-6725](https://orcid.org/0000-0002-3168-6725)  
Universidad Autónoma de Ciudad Juárez  
GitHub: [@fersandovalgtz](https://github.com/fersandovalgtz)

---

**Estado:** desarrollo científico activo. No existe todavía una release cerrada ni un DOI de Cahíta Histórico Digital.
