<p align="center">
  <strong>Cahíta Histórico Digital</strong><br>
  <em>Arte de la lengua cahita (México, 1737) · edición histórico-digital · corpus abierto · infraestructura reproducible</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/estado-0.1.5--dev-6b7280?style=flat-square" alt="Estado 0.1.5-dev">
  <img src="https://img.shields.io/badge/fuente-1737-7a263a?style=flat-square" alt="Fuente 1737">
  <img src="https://img.shields.io/badge/páginas-182%2F182-2d6a4f?style=flat-square" alt="182 de 182 páginas inventariadas">
  <img src="https://img.shields.io/badge/OCR%20micro--CER-25.66%25-b7791f?style=flat-square" alt="Micro CER OCR 25.66%">
  <img src="https://img.shields.io/badge/candidatos%20v0.2-2%2C072-455B55?style=flat-square" alt="2072 candidatos de límites de artículo v0.2">
  <img src="https://img.shields.io/badge/F1%20fronteras-93.37%25-455B55?style=flat-square" alt="F1 diagnóstico de fronteras 93.37%">
  <a href="DATA_LICENSE.md"><img src="https://img.shields.io/badge/datos-CC%20BY%204.0-9a6b1f?style=flat-square" alt="Datos CC BY 4.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/código-MIT-172033?style=flat-square" alt="Código MIT"></a>
  <a href="https://orcid.org/0000-0002-3168-6725"><img src="https://img.shields.io/badge/ORCID-0000--0002--3168--6725-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"></a>
</p>

<p align="center">
  <a href="docs/SOURCE_ALC1737.md"><strong>Fuente histórica</strong></a> ·
  <a href="COVERAGE.md"><strong>Cobertura</strong></a> ·
  <a href="docs/OCR_QUALITY.md"><strong>Calidad OCR</strong></a> ·
  <a href="docs/VOCAB_BOUNDARY_V02.md"><strong>Fronteras v0.2</strong></a> ·
  <a href="docs/TRANSCRIPTION_MODEL.md"><strong>Transcripción</strong></a> ·
  <a href="EDITORIAL_POLICY.md"><strong>Política editorial</strong></a> ·
  <a href="PROVENANCE.md"><strong>Procedencia</strong></a> ·
  <a href="ROADMAP.md"><strong>Hoja de ruta</strong></a> ·
  <a href="docs/ECOSYSTEM.md"><strong>Ecosistema</strong></a>
</p>

---

## Qué es Cahíta Histórico Digital

**Cahíta Histórico Digital (CHD)** es una infraestructura de investigación destinada a transformar testimonios históricos sobre la lengua cahíta y las variedades documentadas por sus fuentes en objetos digitales **trazables, versionados, citables, interoperables y reproducibles**. El proyecto mantiene separadas la reproducción histórica, el OCR, la reconstrucción de layout, la segmentación, la transcripción, la normalización, los datos estructurados y las inferencias analíticas.

La fuente inicial es el *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella*, impreso en México en 1737 por Francisco Xavier Sánchez. La portada no declara un autor personal: atribuye la obra a “vn Padre de la Compañía de JESUS, Missionero de mas de treinta años en la Provincia de Cynaloa”. CHD conserva esa **anonimia de la fuente primaria** y registra por separado la historia de atribuciones posteriores, sin convertir una atribución discutida en autoría resuelta.

El testimonio inicial se identifica internamente como **`ALC1737`**. La arquitectura permite incorporar futuras fuentes cahítas sin mezclar obras, ediciones, ejemplares, capas editoriales ni estados de autoridad.

## Fuente ALC1737

> *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella. Compuesto por vn Padre de la Compañía de JESUS, Missionero de mas de treinta años en la Provincia de Cynaloa.* México: Imprenta de D. Francisco Xavier Sánchez, 1737.

El ejemplar digital de trabajo procede del registro de Internet Archive [`artedelalenguaca00gonz`](https://archive.org/details/artedelalenguaca00gonz), asociado a la John Carter Brown Library, Brown University.

La obra contiene una gramática extensa y un vocabulario castellano–cahíta. `AL LECTOR` menciona expresamente **Hiaquis, Mayes y Thehuecos**, con observaciones sobre similitudes léxicas y diferencias de uso. CHD conserva esas denominaciones como categorías históricas de la fuente y no las proyecta automáticamente sobre identidades lingüísticas contemporáneas.

Un problema filológico de interés aparece en la organización declarada del impreso: `AL LECTOR` denomina la obra “tripartita”, mientras el `PROHEMIO` anuncia **cuatro partes** y el ejemplar desarrolla `PARTE I`–`PARTE IV`. La inconsistencia se documenta, no se corrige silenciosamente.

→ [Fuente e historia material](docs/SOURCE_ALC1737.md) · [Autoría y atribuciones](docs/AUTHORSHIP.md) · [Fuentes](SOURCES.md)

## Estado científico actual

CHD se encuentra en desarrollo **`0.1.5-dev`**. La Fase 1 de ingestión quedó cerrada y están activas la transcripción histórico-digital y el modelado lexicográfico. El repositorio **no declara todavía una edición filológica cerrada**.

| Dimensión | Estado |
|---|---:|
| Páginas digitales inventariadas | **182 / 182** |
| Páginas impresas numeradas mapeadas | **118 / 118** |
| Segmentación macro | **182 / 182** |
| Extracción OCR reproducible | **182 / 182** |
| Micro-CER OCR normalizado | **25.66%** |
| Micro-WER OCR normalizado | **51.96%** |
| Líneas OCR/layout del vocabulario | **3,899** |
| Candidatos de frontera v0.2 | **2,072** |
| Validación estructural de candidatos v0.2 | **2,072 / 2,072** |
| F1 diagnóstico de fronteras v0.2 | **93.37%** |
| Páginas con transcripción diplomática completa | **1** |
| Páginas con extracto diplomático piloto | **1** |
| Entradas lexicográficas piloto | **12** |
| Entradas lexicográficas de producción | **0** |
| Revisión humana independiente | **0** |

Las cifras `3,899` y `2,072` describen **capas computacionales**, no el número de entradas del vocabulario histórico. Las métricas de fronteras proceden de una muestra diagnóstica intencional y de cotejo visual IA-asistido; no son una estimación probabilística de todo el volumen. Los 12 registros lexicográficos piloto siguen marcados `machine_corrected_unverified`.

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

Documentos normativos: [EDITORIAL_POLICY.md](EDITORIAL_POLICY.md) · [PROVENANCE.md](PROVENANCE.md) · [DATASHEET.md](DATASHEET.md) · [docs/TRANSCRIPTION_CONVENTIONS.md](docs/TRANSCRIPTION_CONVENTIONS.md) · [docs/DERIVED_ARTIFACTS_POLICY.md](docs/DERIVED_ARTIFACTS_POLICY.md).

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

Una evaluación estratificada en seis zonas del volumen produjo un **micro-CER de 25.66%** y un **micro-WER de 51.96%** después de neutralizar `ſ/s`, diacríticos, mayúsculas y puntuación. El OCR bruto es útil como capa de recuperación y alineación, pero no puede promoverse directamente a texto científico.

→ [Diagnóstico, muestra y método reproducible](docs/OCR_QUALITY.md)

## Vocabulario: del layout al artículo

El vocabulario utiliza dos columnas y admite artículos multilínea. `scripts/extract_vocab_layout.py` conserva líneas OCR, coordenadas y columna. `scripts/extract_vocab_candidates.py`, actualmente en **`hybrid_margin_mode_v0.2`**, propone después fronteras conservadoras de artículo.

La versión v0.2 produjo **2,072 candidatos** en las páginas 133–177. Sobre la misma muestra diagnóstica usada para v0.1, mejoró de **95.32% / 86.70% / 90.81%** a **97.13% / 89.89% / 93.37%** en precisión / recall / F1 de inicios de artículo. La mejora no autoriza a interpretar los 2,072 candidatos como entradas: la siguiente capa sigue siendo la **revisión de fronteras y agrupación interna**.

→ [Extractor v0.2 y comparación](docs/VOCAB_BOUNDARY_V02.md) · [Protocolo de revisión](docs/VOCAB_REVIEW_PROTOCOL.md) · [Evaluación v0.1](docs/VOCAB_BOUNDARY_EVALUATION.md)

## Transcripción por página

La unidad maestra de la Fase 2 es la página digital. `schemas/page-transcription.schema.json` tipa cobertura, alcance, texto diplomático, incertidumbres, notas materiales, procedencia y estado de revisión. `data/transcription/status.csv` mantiene una fila por cada una de las 182 páginas.

La portada (página digital 3) dispone ya de una transcripción diplomática completa del texto impreso; la página 134 conserva un extracto piloto. Ambas son IA-asistidas y **no** se presentan como `human_verified`.

→ [Modelo de transcripción](docs/TRANSCRIPTION_MODEL.md)

## Reproducibilidad

El repositorio incluye scripts versionados para:

- calcular hashes e inventariar las 182 páginas;
- extraer OCR por página;
- reconstruir columnas mediante `pdftotext -bbox-layout`;
- generar candidatos de límites de artículo;
- validar JSONL contra JSON Schema;
- medir CER/WER sobre una muestra versionada.

Los artefactos masivos regenerables pueden conservarse fuera de Git cuando sus fuentes, receta y SHA-256 están fijados. Esta política evita confundir datos curatoriales con salidas intermedias sin perder reproducibilidad.

→ [Ingestión reproducible](docs/INGESTION_ALC1737.md) · [Política de derivados](docs/DERIVED_ARTIFACTS_POLICY.md) · [`scripts/`](scripts/) · [`schemas/`](schemas/)

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
