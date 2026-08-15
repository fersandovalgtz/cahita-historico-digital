# Procedencia

## Fuente inicial de trabajo

Cahíta Histórico Digital inicia con dos archivos de trabajo proporcionados para el proyecto el **15 de agosto de 2026**:

| Archivo | Tamaño | SHA-256 |
|---|---:|---|
| `Cahíta.pdf` | 23,955,938 bytes | `69ccbe5da1d0834d78ea3957dcc79e64bd4fe165a1a7133ae408e5a656160e37` |
| `Cahíta.html` | 497,979 bytes | `e03f3b34730f737c64cd551a5c14a5095ce243e61c19ccff5358b5c79a45de62` |

Ambos remiten al registro de Internet Archive `artedelalenguaca00gonz`.

Los hashes identifican la copia concreta empleada para esta fase. Cualquier ingestión posterior debe recalcularlos antes de reutilizar resultados derivados.

## Registro y ejemplar

El registro de Internet Archive identifica:

- título: *Arte de la lengua cahita conforme à las reglas de muchos peritos en ella*;
- publicación: México, Imprenta de D. Francisco Xavier Sánchez, 1737;
- autor catalogado: `unknown`;
- contribuyente: John Carter Brown Library;
- signatura JCB indicada: `B737 .A786d`;
- identificador: `artedelalenguaca00gonz`;
- ARK: `ark:/13960/t1kh1mc46`.

El propio registro señala atribuciones bibliográficas divergentes a Diego Pablo González y Tomás Basilio. Esas atribuciones se conservan como metadatos secundarios.

## Nota sobre extensión

El PDF de trabajo contiene **182 páginas digitales**. La descripción física del registro (`[12], 118, [52] p.`) también suma 182, aunque el campo técnico `Pages` de Internet Archive muestra 184. CHD registra la discrepancia y utiliza el PDF efectivamente procesado como autoridad técnica para la numeración digital.

## Cadena de procedencia

La procedencia se modela como:

`ejemplar físico → reproducción digital de tercero → archivo de trabajo → OCR/text layer → extracción paginada → transcripción → corrección → normalización → estructura de datos → análisis`.

Cada capa debe registrar como mínimo:

- identificador de fuente;
- página digital;
- página/folio impreso cuando sea recuperable;
- método de obtención;
- fecha de procesamiento;
- agente o herramienta;
- estado de revisión;
- vínculo con la capa anterior.

## Ingestión 2026-08-15

La primera ingestión técnica produjo:

- `page_manifest.csv`: 182 filas de inventario estructural versionado;
- `page_manifest_full.csv`: 182 registros locales con longitud y hash de OCR por página;
- `ocr_raw_pages.jsonl`: 182 registros derivados localmente mediante `pdftotext -layout`;
- `archive_fulltext_raw.txt`: texto contenido en `<pre>` de la copia HTML;
- `ingest_manifest.json`: checksums y metadatos de la corrida.

Los hashes de todos estos derivados se conservan en [`data/source/alc1737/ingest_manifest.json`](data/source/alc1737/ingest_manifest.json). El proceso se reproduce con [`scripts/ingest_alc1737.py`](scripts/ingest_alc1737.py).

## Redistribución

La fase actual no incorpora al repositorio el PDF ni las imágenes facsimilares originales del proveedor. Esta separación evita atribuir a las licencias de CHD derechos sobre reproducciones de terceros. El texto histórico de 1737 y los metadatos originales de CHD deben distinguirse de la reproducción digital suministrada por una institución externa.
