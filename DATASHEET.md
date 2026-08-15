# Datasheet del corpus

## 1. Identidad

**Nombre:** Cahíta Histórico Digital (CHD)  
**Fuente inicial:** `ALC1737`  
**Objeto:** *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella* (México, 1737)  
**Responsable del proyecto:** Fernando Sandoval Gutierrez  
**Estado:** pre-release 0.1.0

## 2. Propósito

CHD busca producir una edición histórico-digital y un corpus de investigación reproducible a partir de fuentes cahítas históricas. El objetivo no es reemplazar la fuente ni modernizarla silenciosamente, sino ofrecer capas documentales y analíticas separadas que permitan estudiar gramática, léxico, variación, historia de la descripción lingüística y procesos de transmisión textual.

## 3. Fuente inicial

El testimonio de trabajo es una digitalización de 182 páginas disponible mediante Internet Archive bajo el identificador `artedelalenguaca00gonz`. La portada impresa fecha la obra en 1737, la sitúa en México y atribuye la composición a un padre de la Compañía de Jesús con más de treinta años de experiencia misionera en la provincia de Sinaloa/Cynaloa, sin declarar nombre personal.

## 4. Contenido observado

La fuente contiene:

- materiales preliminares y dedicatoria;
- prólogo “Al lector”;
- descripción gramatical extensa;
- ejemplos en cahíta;
- observaciones comparativas que nombran Hiaquis, Mayes y Thehuecos;
- vocabulario castellano–cahíta;
- sección final de numerales.

El proyecto documentará además la discrepancia interna entre la caracterización de la obra como “tripartita” en el prólogo y la posterior división anunciada y materializada en cuatro partes.

## 5. Unidad de análisis prevista

CHD distinguirá al menos:

- página digital;
- página/folio impreso cuando pueda determinarse;
- bloque textual;
- párrafo o sección gramatical;
- ejemplo lingüístico;
- entrada lexicográfica;
- forma cahíta;
- glosa castellana;
- atribución histórica de variedad, cuando la fuente la explicite;
- nota editorial o estado de incertidumbre.

## 6. Capas de datos

`source` → metadatos y procedencia del testimonio.  
`ocr_raw` → OCR sin corrección destructiva.  
`diplomatic` → transcripción diplomática.  
`corrected` → transcripción corregida conservando ortografía histórica.  
`normalized` → capa para búsqueda y análisis, con reglas explícitas.  
`structured` → datos lexicográficos y gramaticales derivados.  
`research` → análisis computacionales, concordancias y relaciones hipotéticas.

## 7. Calidad y autoridad

Ningún registro deberá presentarse como validado por una persona si no existe evidencia explícita de revisión humana independiente. Los estados recomendados incluyen:

- `raw_ocr`
- `machine_corrected_unverified`
- `editorial_proposal`
- `human_verified`
- `unresolved`

La procedencia de cada transformación debe conservarse.

## 8. Riesgos y limitaciones

- OCR degradado por tipografía histórica, manchas, encuadernación y grafías antiguas.
- Ambigüedad en la autoría histórica.
- Variación ortográfica significativa.
- Posibles errores de composición e impresión del siglo XVIII.
- Riesgo de proyectar categorías contemporáneas sobre denominaciones históricas.
- Riesgo de confundir la lengua descrita por el impreso con variedades modernas sin evidencia comparativa suficiente.

## 9. Uso responsable

CHD es un proyecto documental e histórico. No pretende hablar en nombre de comunidades yaquis, mayos ni de otros pueblos contemporáneos. Las comparaciones modernas deberán distinguir claramente entre evidencia histórica, inferencia filológica y análisis lingüístico actual.

## 10. Versionado

Las versiones públicas cerradas deberán conservar:

- fecha;
- identificador de commit;
- métricas de cobertura;
- cambios editoriales;
- esquemas vigentes;
- checksums de fuentes que puedan redistribuirse o, cuando no sea posible, de los archivos de trabajo locales;
- DOI específico de versión cuando se archive en Zenodo.
