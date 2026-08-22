# Datasheet del corpus — Cahíta Histórico Digital v1.0.0

## 1. Identidad

**Nombre:** Cahíta Histórico Digital (CHD)  
**Versión estable:** `1.0.0`  
**Tag:** `v1.0.0`  
**Fuente principal:** `ALC1737`  
**Objeto:** _Arte de la lengua cahita conforme à las reglas de muchos peritos en ella_ (México, 1737)  
**Responsable:** Fernando Sandoval Gutierrez — Universidad Autónoma de Ciudad Juárez — ORCID `0000-0002-3168-6725`  
**Estado:** release científica técnica estable publicada y atestada; DOI/preservación externa pendientes  
**Repositorio:** <https://github.com/fersandovalgtz/cahita-historico-digital>  
**Release:** <https://github.com/fersandovalgtz/cahita-historico-digital/releases/tag/v1.0.0>

## 2. Propósito

CHD produce una edición histórico-digital y un corpus reproducible a partir de fuentes cahítas históricas. No reemplaza la fuente, no moderniza silenciosamente sus formas y no convierte resultados computacionales en autoridad filológica. Separa evidencia documental, OCR, transcripción, segmentación, objetos curatoriales, revisión, procedencia y derivados analíticos.

El recurso está diseñado para investigación en lexicografía histórica, gramática, lingüística misionera, variación histórica, humanidades digitales, historia de la descripción lingüística y estudios comparativos posteriores con capas explícitas.

## 3. Fuente principal

El testimonio de trabajo es una digitalización de **182 páginas** asociada con John Carter Brown Library / Internet Archive, identificador `artedelalenguaca00gonz`.

La portada impresa fecha la obra en 1737, la sitúa en México y atribuye la composición a un padre de la Compañía de Jesús con más de treinta años de experiencia misionera en la provincia de Sinaloa, sin declarar nombre personal. CHD conserva esa evidencia de portada y registra por separado atribuciones nominales posteriores.

El PDF local de trabajo utilizado durante la ingestión quedó fijado por SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`.

## 4. Alcance histórico y lingüístico

La fuente contiene preliminares, cuatro partes gramaticales materialmente presentes, ejemplos, vocabulario castellano–cahíta y numerales. Nombra históricamente variedades o grupos con etiquetas como `Hiaqui`, `Mayo` y `Thehueco`.

CHD **no asigna un único código ISO 639-3 al rótulo histórico `Cahita`** y no deriva automáticamente una correspondencia uno-a-uno con identidades lingüísticas contemporáneas. Los mapeos modernos, cuando se estudien, deben existir como capas analíticas separadas.

## 5. Estado cuantitativo v1.0.0

### Fuente y transcripción

- páginas digitales inventariadas: **182/182**;
- páginas impresas numeradas del cuerpo gramatical mapeadas: **118/118**;
- OCR paginado reproducible: **182/182**;
- páginas `full_page`: **128**;
- Partes I–IV: representadas de forma continua en capa IA-asistida;
- objetos/páginas con validación humana independiente general declarada: **0**.

### Lexicografía

- candidatos canónicos `hybrid_margin_mode_v0.2`: **2,072/2,072** reconstruibles;
- artículos históricos estructurados: **2,302**;
- archivos JSONL canónicos de artículos: **211**;
- vocabulario p.133–177: **45/45 páginas** con cierre técnico candidate-level;
- Phase II p.145–177: **33/33 páginas** técnicamente cerradas;
- `pendingPromotionTotal=0`;
- `unresolvedCandidateTotal=0` para fronteras estructurales;
- `ambiguousBoundaryTotal=0`.

### Remisiones y anáforas

- remisiones canónicas `Buſca`: **150**;
- `exact_unique` estrictas: **60**;
- `not_located` estrictas: **90**;
- `not_located` con revisión explícita: **90/90**;
- destinos editoriales sustentados en la vista revisada: **40**;
- casos de recolación abiertos: **22 = 8 A / 4 B / 10 C**;
- candidatos rechazados: **5**;
- destinos no localizados tras revisión: **23**;
- ocurrencias `Lo miſmo` auditadas fuera del grafo `Buſca`: **14/14**.

### Gramática

- secuencia nominal histórica: 1–373;
- números con reclamación estructurada: **370/373**;
- omisiones materiales documentadas: **127, 178, 294**;
- el número **129** aparece dos veces y ambas unidades se conservan;
- unidades numeradas efectivamente impresas representadas: **371/371**;
- objetos gramaticales: **302** en **24 archivos**;
- filas de evidencia: **1,215**.

## 6. Unidad de análisis

Según la capa, CHD distingue:

- testimonio/fuente;
- página digital e impresa;
- zona/columna y span físico;
- transcripción o fragmento textual;
- línea OCR/layout;
- candidato de frontera;
- decisión de reconciliación;
- artículo histórico;
- forma cahíta y guía castellana;
- remisión/anaphora;
- regla, paradigma o construcción gramatical;
- observación histórica de variedad;
- nota editorial, incertidumbre y estado de autoridad;
- producto derivado reproducible.

Un candidato computacional no equivale automáticamente a un artículo histórico y una salida interoperable no sustituye a la capa curatorial canónica.

## 7. Capas de datos

`source` → metadatos, alcance, paginación y procedencia.  
`ocr_raw` → OCR preservado sin corrección destructiva.  
`transcription` → representación textual IA-asistida y estados.  
`layout/candidate` → geometría y propuestas computacionales de frontera.  
`reconciliation` → decisiones editoriales sobre candidatos e inicios visibles.  
`structured` → artículos, reglas, paradigmas y construcciones canónicas.  
`review/provenance` → correcciones, remisiones, recolaciones y autoridad.  
`derived` → CSV/JSON/JSONL consolidados, TEI, grafos, concordancias y paquetes.

## 8. Calidad y autoridad

Los estados de autoridad distinguen OCR, corrección IA-asistida, propuesta editorial, incertidumbre y verificación humana. `humanVerified=true` sólo corresponde a revisión humana identificable contra evidencia admisible.

**Estado v1.0.0: `humanVerified=0`.**

Las 22 recolaciones se publican como `frozen_open_uncertainty`: la release conserva el problema, no selecciona destinos por similitud y no modifica el grafo canónico para aparentar cierre filológico.

El diagnóstico OCR y las métricas del extractor de fronteras se conservan como indicadores de ingeniería editorial; no constituyen estimaciones de exactitud filológica poblacional.

## 9. Contratos e interoperabilidad

La v1.0.0 congela **22 JSON Schema Draft 2020-12 + 4 metadatos de alcance = 26 contratos**. El manifiesto está en `release/v1_contract_manifest.json`, SHA-256 `c0b897b9dbad2107b40db6169d4207bca752c2b84161e0c9c980409d94b86e56`.

La proyección lexicográfica primaria es **TEI Lex-0 0.9.5**, validada externamente con Jing. Contiene 2,302 entradas, 2,221 citas de traducción, 150 remisiones y 60 `@target` estrictos.

CLDF fue evaluado y diferido como derivado analítico post-v1; no se fuerza como representación primaria del diccionario histórico.

## 10. Reproducibilidad

Además del freeze contractual, la release congela byte a byte **267 archivos científicos / 2,698,997 bytes**. El manifiesto científico tiene SHA-256 `8bb2274e13a82d3425a1ee985ce3077789d07c0d0479b63de7dda2767c6a495b`.

CHD QA valida inventarios, IDs, schemas, reconciliación, documentación, derivados, remisiones, recolaciones, `Lo miſmo`, TEI/Lex-0, gramática, freezes y empaquetado reproducible.

El tag `v1.0.0` apunta a `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`. La Release publicada fue reconstruida posteriormente desde ese tag y comparada byte a byte con los assets públicos.

ZIP final publicado:

- bytes: **1,076,296**;
- SHA-256: **`583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158`**.

La atestación durable está en `release/github_release_attestation_v1.0.0.json`.

## 11. Riesgos y limitaciones

- tipografía histórica y calidad desigual de digitalización/OCR;
- autoría nominal histórica discutida;
- variación ortográfica del siglo XVIII;
- errores de composición e impresión;
- microlecturas no resueltas dentro de objetos estructuralmente cerrados;
- discontinuidad material registrada entre p.157–158 del testimonio de trabajo;
- anomalía `Lucer-` entre p.161–162;
- 22 recolaciones aún abiertas;
- dependencia principal de un testimonio digital de trabajo para muchas decisiones;
- **ausencia de validación filológica humana general**;
- riesgo de retroproyectar categorías, ortografías o identidades contemporáneas sobre evidencia histórica.

## 12. Uso responsable y gobernanza

CHD es un recurso histórico. No habla en nombre de comunidades yaquis, mayos ni de otros pueblos contemporáneos. Las comparaciones modernas deben distinguir evidencia histórica, hipótesis filológica y análisis lingüístico contemporáneo.

Las reglas de reutilización, contribución y atribución están en `GOVERNANCE.md`, `EDITORIAL_POLICY.md`, `CONTRIBUTING.md` y `CONTRIBUTORS.md`.

## 13. Licencias

- software original: **MIT**;
- datos estructurados, metadatos y capas editoriales originales: **CC BY 4.0**;
- facsímiles/digitalizaciones/materiales de terceros: no relicenciados por CHD.

## 14. Metadatos y FAIR

- `CITATION.cff` — citación;
- `codemeta.json` — metadata de software;
- `project-metadata.json` — perfil integral de proyecto/release;
- `metadata/fair-dataset.jsonld` — JSON-LD complementario;
- `FAIR_ASSESSMENT.md` — preauditoría FAIR, **no certificación**;
- `QUALITY_REPORT.md` — calidad demostrable y límites;
- `SCHEMA.md` — modelo y contratos.

## 15. Preservación

La GitHub Release v1.0.0 está publicada y atestada. El depósito archivístico externo y el DOI real permanecen pendientes y se siguen en issue #169.

Hasta asignación efectiva:

- `versionDoi=null`;
- `conceptDoi=null`;
- no se infiere ni inventa DOI.

Una vez depositada la versión, los identificadores persistentes se sincronizarán mediante cambios post-release sin mover ni reescribir el tag `v1.0.0`.
