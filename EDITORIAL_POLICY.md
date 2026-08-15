# Política editorial

## 1. Principio general

Cahíta Histórico Digital conserva la diferencia entre **evidencia documental** y **decisión editorial**. Ninguna corrección debe borrar el estado anterior de la fuente o presentarse como lectura histórica segura cuando sea una inferencia.

## 2. Capas editoriales

### 2.1 Testimonio

Imagen, facsímil o reproducción digital del ejemplar. Es la autoridad documental primaria para la lectura del impreso.

### 2.2 OCR bruto

Salida automática preservada sin correcciones silenciosas. Su función es permitir auditoría del proceso y medir errores.

### 2.3 Transcripción diplomática

Debe reproducir, hasta donde sea técnicamente viable, grafía, puntuación, capitalización, abreviaturas y distribución significativa del original. Los caracteres históricos como `ſ` pueden preservarse en esta capa. Las lecturas inciertas deben marcarse, no completarse por intuición.

### 2.4 Transcripción corregida

Corrige errores evidentes del OCR contra el facsímil, pero conserva la ortografía histórica. No moderniza automáticamente `u/v`, `i/j`, grafías antiguas, morfología o puntuación.

### 2.5 Normalización

Capa derivada destinada a búsqueda, comparación y análisis. Toda regla de normalización deberá ser documentada y reversible en la medida de lo posible. La normalización nunca sustituye a la transcripción histórica.

### 2.6 Datos estructurados

Entradas lexicográficas, ejemplos, formas, glosas, referencias de página y etiquetas analíticas derivadas de las capas anteriores. Cada registro debe conservar un vínculo explícito con la evidencia que lo sustenta.

## 3. Estados de revisión

Los registros podrán utilizar, entre otros, los siguientes estados:

- `raw_ocr`: salida automática sin cotejo;
- `machine_corrected_unverified`: corrección asistida sin revisión humana independiente;
- `editorial_proposal`: interpretación o reconstrucción propuesta;
- `human_verified`: lectura cotejada por una persona identificable contra el testimonio;
- `unresolved`: la evidencia no permite decidir con seguridad.

No se utilizará `human_verified` como etiqueta honorífica o presunta.

## 4. Autoría histórica

La portada de 1737 no proporciona un nombre personal. Por ello, el registro primario de CHD utiliza **autor anónimo en la fuente**. Las atribuciones bibliográficas posteriores se almacenan como `attributedTo` o notas de historia catalográfica, no como reemplazo silencioso del dato de portada.

## 5. Denominaciones lingüísticas

Las formas `Cahita`, `Hiaqui`, `Mayo`, `Thehueco` y otras denominaciones presentes en el impreso se conservarán como datos históricos de la fuente. Las equivalencias con denominaciones contemporáneas se incorporarán únicamente en capas analíticas, acompañadas de fuente y nivel de certeza.

## 6. Contenido histórico sensible

Los juicios religiosos, coloniales, etnográficos o valorativos presentes en el impreso pertenecen al documento histórico. CHD los atribuye a la fuente y evita convertirlos en voz editorial contemporánea.

## 7. Correcciones y erratas

La obra incluye una sección de erratas. Las correcciones históricas declaradas por el propio impreso deberán registrarse como una capa específica, distinguiendo:

- lectura impresa;
- corrección indicada en la fe de erratas;
- lectura editorial de CHD.

## 8. Interoperabilidad

Una vez estabilizada la segmentación, CHD proyectará los datos a formatos abiertos como CSV, JSON y TEI/XML. La serialización interoperable no deberá empobrecer la distinción entre fuente, corrección, normalización e inferencia.

## 9. Versiones cerradas

Una release científica debe declarar explícitamente:

- qué capas incluye;
- qué proporción fue cotejada;
- qué validación humana existe;
- qué unidades permanecen inciertas;
- qué cambios se introdujeron respecto de la versión anterior.
