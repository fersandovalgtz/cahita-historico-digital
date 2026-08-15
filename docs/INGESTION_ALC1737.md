# Ingestión reproducible de ALC1737

Este documento fija la primera ingestión técnica reproducible de la fuente `ALC1737`.

## Archivos de trabajo

La sesión de trabajo del 15 de agosto de 2026 utilizó:

| Archivo | Tamaño | SHA-256 |
|---|---:|---|
| `Cahíta.pdf` | 23,955,938 bytes | `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37` |
| `Cahíta.html` | 497,979 bytes | `e03f3b34730f737c64cd551a5c14a5095ce243e61c19ccff5358b5c79a45de62` |

El PDF contiene 182 páginas digitales de 309 × 433 puntos, no está cifrado y declara en sus metadatos que fue digitalizado por Internet Archive. El HTML es una copia guardada de la vista de texto completo del mismo registro.

Estos hashes identifican **los archivos concretos procesados**. No son hashes universales de la obra ni de todas las descargas posibles de Internet Archive.

## Artefactos derivados durante la ingestión

La ejecución local produjo:

| Derivado | Registros / tamaño | SHA-256 |
|---|---:|---|
| `archive_fulltext_raw.txt` | 346,869 bytes | `22e344ab8e26d3d161118ba54a718c7bcdbafc1bdb99de07a9d64abf2e93105c` |
| `ocr_raw_pages.jsonl` | 182 registros / 541,208 bytes | `7dfcf45f6b4b5f9e6a626105bfa6d83acf3acabc1d154be072a38b580c319912` |
| `page_manifest_full.csv` | 182 registros / 26,735 bytes | `4cdf47db732b8cdd93a8c61336035eef6f67be822b9e0420a1e961bada1b782a` |

`archive_fulltext_raw.txt` procede del bloque `<pre>` del HTML. `ocr_raw_pages.jsonl` procede de la capa textual del PDF mediante `pdftotext -layout`, una extracción independiente y paginada. La existencia de dos representaciones OCR es útil para comparación, pero **ninguna se considera lectura crítica**.

El repositorio conserva de inmediato un `page_manifest.csv` estructural (182 filas) y el manifiesto de ingestión; los hashes OCR por página pertenecen al derivado local `page_manifest_full.csv`; el empaquetado del payload OCR completo se mantiene como decisión separada para no confundir fuente, derivado y distribución.

## Paginación impresa

El facsímil permite establecer una relación estable para el cuerpo numerado del *Arte*:

- digital 15 = impresa 1;
- digital 51 = impresa 37;
- digital 69 = impresa 55;
- digital 105 = impresa 91;
- digital 132 = impresa 118.

Por tanto, entre las páginas digitales 15 y 132:

```text
printed_page = digital_page - 14
```

Este mapeo cubre exactamente las 118 páginas impresas numeradas del cuerpo gramatical. Los preliminares, el vocabulario y los numerales se conservan como secuencias no paginadas.

## Auditoría visual de fronteras

Se renderizaron y cotejaron visualmente las páginas 3, 11, 13, 15, 51, 69, 105, 132, 133, 178 y 180. Además se inspeccionaron 14, 181 y 182 para aclarar páginas con OCR nulo o residual.

La observación confirma:

- p. digital 3: portada;
- p. 11: `AL LECTOR`;
- p. 13: `ERRATA SIC CORRIGE` y nota de abreviaturas del vocabulario;
- p. 14: verso sin texto impreso propio, con transparencia del recto;
- p. 15: `PROHEMIO`, primera página impresa numerada (`Pag. 1`);
- p. 51: `PARTE II`, impresa 37;
- p. 69: `PARTE III`, impresa 55;
- p. 105: `IV. ULT. PARTE`, impresa 91;
- p. 132: `FIN DEL ARTE`, impresa 118;
- p. 133: comienzo del vocabulario;
- p. 178: final alfabético y comienzo de `NOMBRES NUMERALES`;
- p. 180: `FIN` del volumen;
- p. 181: interior de la cubierta posterior con marcas materiales/manuscritas;
- p. 182: cubierta posterior exterior.

## Reproducibilidad

Ejecute:

```bash
python scripts/ingest_alc1737.py \
  --pdf /ruta/Cahíta.pdf \
  --html /ruta/Cahíta.html \
  --out build/alc1737
```

Requisitos:

- Python 3.10 o superior;
- Poppler `pdftotext` disponible en `PATH`;
- ninguna conexión de red durante la ingestión.

La comparación de hashes permite detectar cualquier cambio en archivos fuente o derivados.
