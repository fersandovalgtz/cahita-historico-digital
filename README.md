<p align="center">
  <strong>Cahíta Histórico Digital</strong><br>
  <em>Arte de la lengua cahita (México, 1737) · edición histórico-digital · corpus abierto · infraestructura reproducible</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/estado-pre--release%200.1.0-6b7280?style=flat-square" alt="Estado pre-release 0.1.0">
  <img src="https://img.shields.io/badge/fuente-1737-7a263a?style=flat-square" alt="Fuente 1737">
  <a href="DATA_LICENSE.md"><img src="https://img.shields.io/badge/datos-CC%20BY%204.0-9a6b1f?style=flat-square" alt="Datos CC BY 4.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/código-MIT-172033?style=flat-square" alt="Código MIT"></a>
  <a href="https://orcid.org/0000-0002-3168-6725"><img src="https://img.shields.io/badge/ORCID-0000--0002--3168--6725-A6CE39?style=flat-square&logo=orcid&logoColor=white" alt="ORCID"></a>
</p>

<p align="center">
  <a href="docs/SOURCE_ALC1737.md"><strong>Fuente histórica</strong></a> ·
  <a href="EDITORIAL_POLICY.md"><strong>Política editorial</strong></a> ·
  <a href="PROVENANCE.md"><strong>Procedencia</strong></a> ·
  <a href="DATASHEET.md"><strong>Datasheet</strong></a> ·
  <a href="ROADMAP.md"><strong>Hoja de ruta</strong></a> ·
  <a href="docs/ECOSYSTEM.md"><strong>Ecosistema</strong></a>
</p>

---

## Qué es Cahíta Histórico Digital

**Cahíta Histórico Digital (CHD)** es una infraestructura de investigación destinada a transformar testimonios históricos sobre la lengua cahíta y sus variedades documentadas en objetos digitales trazables, versionados, citables, interoperables y reproducibles. El proyecto distingue de manera estricta entre el testimonio histórico, el OCR, la transcripción, la normalización, la estructuración de datos y las inferencias analíticas.

La fuente inicial es el **Arte de la lengua cahita conforme à las reglas de muchos peritos en ella**, impreso en México en 1737 por Francisco Xavier Sánchez. La portada no declara un autor personal: atribuye la obra a “vn Padre de la Compañía de JESUS, Missionero de mas de treinta años en la Provincia de Cynaloa”. Por ello, CHD conserva la **anonimia editorial de la fuente primaria** y documenta por separado las atribuciones posteriores a Tomás Basilio, Diego Pablo González y Juan Bautista de Velasco, sin convertir ninguna de ellas en autoría resuelta.

El proyecto comienza con un único testimonio digital identificado internamente como **`ALC1737`**. La arquitectura, sin embargo, está diseñada para incorporar futuras fuentes cahítas y para mantener separadas las distintas obras, ediciones, ejemplares, transcripciones y capas derivadas.

## La fuente ALC1737

**Referencia primaria de trabajo:**

> *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella. Compuesto por vn Padre de la Compañía de JESUS, Missionero de mas de treinta años en la Provincia de Cynaloa.* México: Imprenta de D. Francisco Xavier Sánchez, 1737.

El ejemplar digital utilizado procede del registro de Internet Archive [`artedelalenguaca00gonz`](https://archive.org/details/artedelalenguaca00gonz), asociado al ejemplar de la John Carter Brown Library, Brown University.

La obra contiene descripción gramatical extensa, abundantes ejemplos cahítas y un vocabulario castellano–cahíta. En el prólogo “Al lector” se mencionan expresamente **Hiaquis, Mayes y Thehuecos**, con observaciones sobre uniformidad léxica y diferencias de uso. El volumen concluye con materiales de vocabulario y numerales.

Un aspecto que CHD conservará como problema filológico es la propia arquitectura declarada del impreso: “Al lector” llama a la obra **tripartita**, mientras que en el desarrollo se anuncia una división en **cuatro partes** y el ejemplar contiene una `PARTE IV`. Esta tensión no se corrige silenciosamente: se documentará como rasgo de la historia textual y editorial del testimonio.

→ Véanse [docs/SOURCE_ALC1737.md](docs/SOURCE_ALC1737.md), [docs/AUTHORSHIP.md](docs/AUTHORSHIP.md) y [SOURCES.md](SOURCES.md).

## Principios científicos

CHD adopta una cadena editorial no destructiva:

**testimonio → OCR bruto → segmentación → transcripción diplomática → transcripción corregida → normalización explícita → estructuración → análisis derivado → revisión humana independiente cuando exista**.

Las reglas básicas son:

1. **La fuente no se sobrescribe.** Toda corrección o modernización vive en una capa separada.
2. **La procedencia acompaña al dato.** Cada unidad debe poder remontarse a fuente, página y actividad de procesamiento.
3. **La incertidumbre se conserva.** Una lectura dudosa es un estado documental legítimo, no un hueco que deba rellenarse.
4. **La autoridad está tipada.** OCR, corrección asistida, propuesta editorial y validación humana no son equivalentes.
5. **Las variedades históricas no se proyectan automáticamente sobre identidades lingüísticas contemporáneas.** Las comparaciones con yaqui, mayo u otras variedades modernas deberán registrarse como relaciones analíticas explícitas y revisables.

## Arquitectura inicial

```text
cahita-historico-digital/
├── README.md
├── CITATION.cff
├── codemeta.json
├── DATASHEET.md
├── EDITORIAL_POLICY.md
├── PROVENANCE.md
├── SOURCES.md
├── ROADMAP.md
├── DATA_LICENSE.md
├── LICENSE
├── docs/
│   ├── SOURCE_ALC1737.md
│   ├── AUTHORSHIP.md
│   └── ECOSYSTEM.md
├── data/
│   ├── README.md
│   └── source/alc1737/metadata.json
└── schemas/
    └── lexical-entry.schema.json
```

El repositorio todavía **no declara un corpus crítico terminado**. La versión 0.1.0 establece la infraestructura documental y los contratos de datos necesarios para comenzar el procesamiento reproducible del testimonio.

## Identificador de la fuente

| Campo | Valor |
|---|---|
| Identificador interno | `ALC1737` |
| Título abreviado | *Arte de la lengua cahita* |
| Año | 1737 |
| Lugar | México |
| Impresor | Francisco Xavier Sánchez |
| Autoría en portada | Anónima / “vn Padre de la Compañía de JESUS” |
| Testimonio digital inicial | Internet Archive `artedelalenguaca00gonz` |
| Extensión del PDF de trabajo | 182 páginas digitales |
| Estado CHD | fuente registrada; ingestión filológica pendiente |

## Datos previstos

La primera fase producirá, sin mezclar niveles de autoridad:

- manifiesto de páginas y procedencia;
- OCR bruto preservado;
- transcripción diplomática por página;
- transcripción corregida con estados de revisión;
- versión normalizada para búsqueda;
- extracción estructurada del vocabulario;
- registros de variantes históricas explícitamente atribuidas por la fuente;
- serializaciones CSV, JSON y, cuando la estructura esté estabilizada, TEI/XML;
- métricas de cobertura, incertidumbre y revisión;
- scripts reproducibles de transformación y validación.

## Citación

GitHub puede generar una cita desde [`CITATION.cff`](CITATION.cff). Mientras no exista una release archivada en Zenodo, la forma recomendada es:

> Sandoval Gutierrez, Fernando. 2026. *Cahíta Histórico Digital — Arte de la lengua cahita (1737)*. Versión de desarrollo 0.1.0. GitHub. https://github.com/fersandovalgtz/cahita-historico-digital

Cuando una afirmación dependa de una lectura histórica concreta deberá citarse además el impreso de 1737 y la página correspondiente. El futuro DOI del repositorio no sustituirá la referencia a la fuente primaria.

## Licencias y derechos

- **Software y código original:** [MIT](LICENSE).
- **Datos, metadatos, anotaciones y capas editoriales originales de CHD:** [CC BY 4.0](DATA_LICENSE.md).
- **Fuente histórica y digitalizaciones de terceros:** conservan su propio estatus jurídico y sus condiciones de procedencia; CHD no las relicencia.

## Ecosistema científico

CHD forma parte del ecosistema de humanidades digitales y ciencia abierta mantenido por Fernando Sandoval Gutierrez. Comparte principios metodológicos con [Rarámuri Histórico Digital](https://github.com/fersandovalgtz/raramuri-historico), pero mantiene corpus, vocabularios, decisiones editoriales e inferencias completamente separados. También se vincula con [Rarámuri Digital](https://github.com/fersandovalgtz/raramuri-digital) y [Libro de Texto Mexicano Digital](https://github.com/fersandovalgtz/libro-texto-mexicano-digital).

→ [Mapa del ecosistema](docs/ECOSYSTEM.md)

## Autor y contacto académico

**Dr. Fernando Sandoval Gutierrez**  
ORCID: [0000-0002-3168-6725](https://orcid.org/0000-0002-3168-6725)  
Universidad Autónoma de Ciudad Juárez  
GitHub: [@fersandovalgtz](https://github.com/fersandovalgtz)

---

**Estado:** infraestructura inicial en desarrollo. No existe todavía una release científica cerrada ni un DOI de CHD.