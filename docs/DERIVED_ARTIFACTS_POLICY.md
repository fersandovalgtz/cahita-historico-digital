# Política de artefactos derivados y empaquetado

## Principio

Cahíta Histórico Digital distingue entre **fuentes**, **datos curatoriales versionados** y **artefactos derivados reproducibles**. No todo archivo producido durante una corrida debe almacenarse en Git para que el proyecto sea reproducible.

Git se utilizará para aquello que define o modifica el estado científico del proyecto: código, esquemas, manifiestos, decisiones editoriales, muestras de auditoría, transcripciones curatoriales y datos de producción. Los derivados voluminosos que puedan reconstruirse determinísticamente a partir de una fuente identificada por hash y de código versionado podrán conservarse fuera del historial Git, siempre que el proyecto registre cómo regenerarlos y cómo verificar sus bytes.

## Fuente `ALC1737`

Los dos archivos de trabajo iniciales se identifican mediante SHA-256 en `data/source/alc1737/ingest_manifest.json`. El repositorio no redistribuye por ahora el PDF ni la copia HTML completos.

A partir de esos archivos, `scripts/ingest_alc1737.py` genera:

- `archive_fulltext_raw.txt`;
- `ocr_raw_pages.jsonl`;
- `page_manifest_full.csv`;
- `ingest_manifest.json`.

Los hashes y tamaños de la corrida de referencia están fijados en el manifiesto. Por tanto, el OCR bruto queda **preservado como derivado reproducible y verificable**, aunque el payload completo no se incorpore al historial Git.

## Razones para no versionar todo derivado en Git

1. **Separación de autoridad:** una copia OCR producida por la cadena de digitalización no debe adquirir apariencia de dato curatorial de CHD por el solo hecho de residir en el repositorio.
2. **Trazabilidad:** un derivado regenerable desde una fuente con hash y un script versionado puede auditarse sin duplicar innecesariamente el contenido.
3. **Historia limpia:** Git debe mostrar cambios científicos y editoriales significativos, no cambios masivos provocados por regeneraciones equivalentes.
4. **Derechos y procedencia:** la redistribución de materiales procedentes de terceros se evalúa separadamente de la licencia aplicada al código y a los metadatos originales de CHD.
5. **Escalabilidad:** el mismo criterio permite incorporar futuras fuentes sin convertir el repositorio Git en almacén indiscriminado de facsímiles y salidas intermedias.

## Qué sí debe versionarse

Se versionarán directamente cuando formen parte del estado científico:

- manifiestos y checksums;
- mapeos de páginas y segmentaciones estructurales;
- esquemas JSON/TEI;
- transcripciones diplomáticas curatoriales;
- correcciones y normalizaciones aprobadas para una versión;
- entradas lexicográficas de producción;
- colas de incertidumbre y decisiones de revisión;
- muestras necesarias para auditar algoritmos;
- resultados compactos de validación y métricas;
- scripts y pruebas.

## Qué puede permanecer como artefacto reconstruible

Pueden permanecer fuera del historial Git, con hash y receta de construcción:

- OCR bruto completo regenerado desde el PDF;
- salidas completas de layout/bounding boxes;
- candidatos masivos de segmentación mientras no hayan sido promovidos a dato curatorial;
- bases SQLite, índices de búsqueda y otros artefactos de rendimiento;
- renders intermedios de páginas.

## Releases y preservación a largo plazo

Una release científica cerrada podrá empaquetar ciertos derivados reproducibles —por ejemplo OCR bruto, candidatos completos o bases de datos generadas— como **assets de release o depósitos archivísticos**, siempre separados conceptualmente de la fuente primaria y acompañados de checksums, versión del código y documentación de generación.

El hecho de que un artefacto se distribuya con una release no cambia su nivel de autoridad. `raw_ocr` seguirá siendo `raw_ocr` aunque tenga DOI.

## Criterio de integridad

Un artefacto reproducible se considera íntegro cuando:

1. la fuente de entrada coincide con el SHA-256 documentado;
2. se utiliza la versión declarada del script;
3. la corrida termina sin error;
4. el SHA-256 del artefacto resultante coincide con el manifiesto de referencia o, si cambia justificadamente, el cambio se documenta como nueva corrida/versionado.
