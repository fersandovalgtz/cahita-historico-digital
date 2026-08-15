# ALC1737 — fuente de trabajo

`ALC1737` es el identificador interno de Cahíta Histórico Digital para el ejemplar digital de *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella* (México, 1737) utilizado como fuente inicial del proyecto.

## Qué contiene este directorio

- `ingest_manifest.json`: identidad técnica de los archivos de trabajo, tamaños, SHA-256, metadatos básicos del PDF y artefactos derivados durante la ingestión.
- `page_manifest.csv`: inventario estructural de las 182 páginas digitales con sección, paginación impresa cuando existe y etiquetas de frontera/materialidad.
- `sections.json`: segmentación macro del volumen y evidencia de los límites de sección.

Los archivos fuente `Cahíta.pdf` y `Cahíta.html` **no se redistribuyen aquí**. El manifiesto permite verificar que un procesamiento futuro utiliza exactamente los mismos bytes que esta fase de trabajo.

## Paginación

El cuerpo numerado del *Arte* ocupa las páginas digitales 15–132 del PDF y corresponde a las páginas impresas 1–118. En esta zona se utiliza la transformación:

```text
printed_page = digital_page - 14
```

La correspondencia fue comprobada visualmente en páginas de frontera y muestreo: digital 15 = impresa 1; 51 = 37; 69 = 55; 105 = 91; 132 = 118. Las secciones posteriores —vocabulario y numerales— son no paginadas en el impreso.

## OCR

El PDF contiene una capa textual heredada del proceso de digitalización. La ingestión local genera además `page_manifest_full.csv`, que registra longitud y SHA-256 de la extracción `pdftotext -layout` de cada página. Esa capa es **OCR bruto**, no transcripción diplomática ni lectura filológicamente validada.

La ingestión local produjo además un JSONL de 182 registros, uno por página, y una extracción del texto completo contenido en el elemento `<pre>` del HTML guardado de Internet Archive. Sus hashes constan en `ingest_manifest.json`. El payload completo se incorporará al repositorio cuando quede fijada la política de empaquetado de OCR derivado.

## Páginas sin OCR textual significativo

La extracción automática no devuelve texto sustantivo en:

- página digital 4: verso de portada con dibujo manuscrito;
- página digital 14: verso de la hoja de erratas, visualmente sin texto impreso propio y con transparencia del recto.

Las páginas 181 y 182 corresponden respectivamente al interior de la cubierta posterior y a la cubierta exterior; pueden contener marcas materiales o números manuscritos, pero no forman parte del texto impreso de la obra.
