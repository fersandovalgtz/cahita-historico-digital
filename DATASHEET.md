# Datasheet del corpus

## 1. Identidad

**Nombre:** Cahíta Histórico Digital (CHD)  
**Fuente inicial:** `ALC1737`  
**Objeto:** *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella* (México, 1737)  
**Responsable del proyecto:** Fernando Sandoval Gutierrez  
**Estado:** desarrollo activo `0.2.0-dev`; sin release científica estable ni DOI

## 2. Propósito

CHD busca producir una edición histórico-digital y un corpus de investigación reproducible a partir de fuentes cahítas históricas. El objetivo no es reemplazar la fuente ni modernizarla silenciosamente, sino ofrecer capas documentales y analíticas separadas que permitan estudiar gramática, léxico, variación, historia de la descripción lingüística y transmisión textual.

## 3. Fuente inicial

El testimonio de trabajo es una digitalización de **182 páginas** disponible mediante Internet Archive bajo el identificador `artedelalenguaca00gonz`, asociada a la John Carter Brown Library, Brown University.

La portada impresa fecha la obra en 1737, la sitúa en México y atribuye la composición a un padre de la Compañía de Jesús con más de treinta años de experiencia misionera en la provincia de Cynaloa, sin declarar nombre personal. CHD conserva la anonimia de la portada y registra separadamente las atribuciones catalográficas e historiográficas divergentes.

El PDF de trabajo está fijado por SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`.

## 4. Contenido observado

La fuente contiene:

- materiales preliminares;
- prólogo `AL LECTOR`;
- cuatro partes gramaticales materialmente presentes;
- ejemplos en cahíta;
- observaciones históricas que nombran Hiaquis, Mayes, Thehuecos y otras denominaciones de la fuente;
- vocabulario castellano–cahíta;
- sección final de numerales;
- finales materiales no textuales.

Existe una discrepancia interna entre la caracterización de la obra como “tripartita” en `AL LECTOR` y la división anunciada/materializada en cuatro partes. CHD conserva esa inconsistencia como problema filológico.

## 5. Estado cuantitativo actual

### Fuente y transcripción

- páginas digitales inventariadas: **182 / 182**;
- páginas impresas numeradas mapeadas: **118 / 118**;
- OCR paginado reproducible: **182 / 182**;
- páginas `full_page`: **128**;
- Partes I–IV del Arte: representadas de forma continua en capa IA-asistida;
- revisión humana independiente: **0**.

### Lexicografía

- líneas OCR/layout documentadas en el vocabulario: **3,899**;
- candidatos vigentes `hybrid_margin_mode_v0.2`: **2,072**;
- candidatos v0.2 persistidos canónicamente: **2,072 / 2,072**;
- artículos históricos estructurados: **734**;
- páginas del vocabulario con representación curatorial: **45 / 45**;
- reconciliación pp.133–134: **61 / 61 candidatos**;
- inicios visibles omitidos observados en pp.133–134: **14**;
- candidatos `article` pendientes de promoción en pp.133–134: **36**.

### Gramática y variación

La capa derivada incluye, entre otros objetos, 3 paradigmas, 9 construcciones modales, 5 no finitas, 3 participiales, 6 predicativas/modales, 6 grupos de verbos irregulares, 43 preposiciones/grupos, 11 grupos de adverbios, 6 grupos de conjunciones/metacategorías, un bloque numeral estructurado y 17+ observaciones de variación histórica identificadas.

## 6. Unidad de análisis

CHD distingue, según la capa:

- testimonio/fuente;
- página digital;
- página impresa cuando existe;
- segmento intra-página;
- bloque o párrafo;
- regla gramatical;
- paradigma/construcción;
- ejemplo lingüístico;
- línea OCR/layout;
- candidato de frontera lexicográfica;
- reconciliación de candidato;
- inicio visible omitido/falso negativo;
- artículo histórico;
- forma cahíta;
- glosa/guía castellana;
- remisión y anáfora;
- atribución histórica de variedad cuando la fuente la explicita;
- nota editorial, incertidumbre y estado de autoridad.

Un candidato computacional no se identifica automáticamente con un artículo histórico.

## 7. Capas de datos

`source` → metadatos, manifestaciones y procedencia del testimonio.  
`ocr_raw` → OCR sin corrección destructiva.  
`layout` → líneas y geometría.  
`candidate` → propuestas computacionales de frontera.  
`reconciliation` → clasificación editorial de candidatos y calidad de frontera.  
`diplomatic` → transcripción diplomática IA-asistida o revisada.  
`structured` → artículos lexicográficos, reglas, paradigmas y construcciones históricas.  
`normalized` → futura capa para búsqueda y análisis con reglas explícitas.  
`research` → concordancias, comparaciones y relaciones hipotéticas.

## 8. Calidad y autoridad

Los estados de autoridad incluyen:

- `raw_ocr`;
- `machine_corrected_unverified`;
- `editorial_proposal`;
- `human_verified`;
- `unresolved`.

Ningún registro se presenta como validado por una persona sin evidencia explícita de revisión humana independiente.

El diagnóstico OCR reporta micro-CER 25.66% y micro-WER 51.96% bajo su protocolo de normalización. El extractor v0.2, sobre una muestra intencional de pp.133, 134, 150 y 177, reporta precisión 97.13%, recall 89.89% y F1 93.37%. Esas cifras son métricas diagnósticas de ingeniería editorial, no estimaciones filológicas poblacionales.

## 9. Reproducibilidad

El inventario canónico de 2,072 candidatos queda fijado por:

- método `hybrid_margin_mode_v0.2`;
- revisión generadora `f175b4bc455ff40a066d092a94e0a89a0ca2ae10`;
- PDF SHA-256 `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37`;
- JSONL SHA-256 `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`;
- manifiesto de partes y script de reconstrucción/verificación.

Todavía falta implantar CI que ejecute automáticamente validadores, reconstrucciones, hashes y pruebas de referencias en cada cambio relevante.

## 10. Riesgos y limitaciones

- OCR degradado por tipografía histórica, manchas, encuadernación y grafías antiguas;
- ambigüedad en la autoría histórica;
- variación ortográfica significativa;
- errores de composición e impresión del siglo XVIII;
- candidatos geométricos que fusionan o fragmentan artículos;
- falsos negativos del extractor;
- discontinuidad F→H entre pp.157–158 del testimonio de trabajo;
- anomalía `Lucer-` entre pp.161–162;
- riesgo de proyectar categorías contemporáneas sobre denominaciones históricas;
- riesgo de confundir la lengua descrita por el impreso con variedades modernas sin evidencia comparativa suficiente;
- ausencia actual de revisión humana independiente;
- dependencia principal de un único testimonio digital de trabajo mientras no se incorpore un control textual independiente.

## 11. Uso responsable

CHD es un proyecto documental e histórico. No pretende hablar en nombre de comunidades yaquis, mayos ni de otros pueblos contemporáneos. Las comparaciones modernas deberán distinguir claramente entre evidencia histórica, inferencia filológica y análisis lingüístico actual.

## 12. Versionado y criterios de publicación

Las versiones públicas cerradas deberán conservar:

- fecha y número de versión;
- identificador de commit;
- métricas de cobertura;
- cambios editoriales;
- esquemas vigentes;
- checksums de fuentes y derivados canónicos;
- estado de revisión humana;
- limitaciones conocidas;
- DOI específico de versión cuando se archive en Zenodo.

`0.2.0-dev` es una **instantánea de desarrollo**, no una release científica estable. Antes de `v1.0.0` deberán cerrarse el alcance lexicográfico declarado, QA, interoperabilidad, preservación y documentación de autoridad.
