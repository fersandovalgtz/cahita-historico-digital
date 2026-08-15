# Procedencia

## Fuente inicial de trabajo

Cahíta Histórico Digital inicia con dos archivos de trabajo proporcionados para el proyecto el **15 de agosto de 2026**:

- `Cahíta.pdf`: digitalización de 182 páginas;
- `Cahíta.html`: copia guardada de la vista de texto completo de Internet Archive.

Ambos remiten al registro de Internet Archive:

- identificador: `artedelalenguaca00gonz`
- registro: https://archive.org/details/artedelalenguaca00gonz
- texto OCR: https://archive.org/stream/artedelalenguaca00gonz/artedelalenguaca00gonz_djvu.txt

El HTML conserva como enlace canónico el registro anterior.

## Ejemplar

El escaneo corresponde a un ejemplar asociado a la **John Carter Brown Library, Brown University**. En las páginas preliminares del PDF se observa el ex libris institucional. El registro de la Biblioteca Virtual de la Filología Española identifica el ejemplar con la signatura `B737 .A786d`.

## Cadena de procedencia prevista

La procedencia se modelará como:

`ejemplar físico → reproducción digital de tercero → archivo de trabajo → OCR → transcripción → corrección → normalización → estructura de datos → análisis`.

Cada capa debe registrar como mínimo:

- identificador de fuente;
- página digital;
- página/folio impreso cuando sea recuperable;
- método de obtención;
- fecha de procesamiento;
- agente o herramienta;
- estado de revisión;
- vínculo con la capa anterior.

## Redistribución del facsímil

La versión 0.1.0 **no incorpora todavía el PDF ni las imágenes del proveedor al repositorio**. Antes de redistribuir reproducciones de terceros se documentarán explícitamente las condiciones de uso del proveedor y la conveniencia técnica de conservar copias, enlaces o checksums.

## Checksums

Los checksums de los archivos de trabajo se incorporarán durante la fase de ingestión reproducible. Hasta entonces, la referencia canónica del testimonio digital es el identificador de Internet Archive y la descripción del archivo de trabajo utilizada para esta inicialización.
