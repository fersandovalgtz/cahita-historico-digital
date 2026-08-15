# Candidatos de artículos del vocabulario — ALC1737

## Finalidad

El vocabulario castellano–cahíta de `ALC1737` está dispuesto en dos columnas y presenta artículos de longitud variable, remisiones, continuaciones de línea, abreviaturas y casos en que una misma entrada ocupa más de una línea tipográfica. Por ello, Cahíta Histórico Digital no identifica una línea OCR con una entrada lexicográfica.

La fase descrita aquí introduce una capa intermedia: **candidatos de límites de artículo**. Un candidato es una agrupación de líneas sugerida por la geometría del impreso. No afirma todavía cuál es el lema castellano, cuál es la forma cahíta ni siquiera que el agrupamiento coincida exactamente con un artículo histórico.

## Procedimiento

`scripts/extract_vocab_candidates.py` reutiliza la reconstrucción de columnas producida por `scripts/extract_vocab_layout.py` y trabaja página por página y columna por columna.

Para cada columna:

1. elimina únicamente ruido sin contenido alfabético y la zona superior usada por encabezados;
2. estima el margen de comienzo de artículo mediante el decil inferior de las coordenadas `xMin` de las líneas;
3. considera comienzo candidato una línea alfabética cuyo inicio se encuentra dentro de cinco puntos del margen estimado;
4. agrega las líneas indentadas siguientes al mismo candidato hasta detectar otro comienzo;
5. conserva el primer candidato de cada columna con una advertencia porque puede continuar un artículo procedente de la página o columna anterior;
6. no intenta dividir el texto resultante en lema, glosa, forma cahíta, variante o remisión.

Cada objeto conserva `sourcePageDigital`, columna, posición vertical inicial, líneas OCR originales, texto concatenado, método de frontera, estado `machine_candidate`, revisión `raw_ocr` y banderas de riesgo.

## Resultado de la corrida completa

La ejecución sobre las páginas digitales **133–177** produjo localmente:

- **1,680 candidatos de límites de artículo**;
- **903** candidatos en columna izquierda;
- **777** en columna derecha;
- **45 páginas** procesadas;
- entre **14 y 55 candidatos por página**;
- media de **37.33 candidatos por página**;
- SHA-256 del JSONL completo derivado: `f00318329c1116254388aac0ffe978fea330c8466f3863e318df1f01fd010b59`.

El conjunto completo fue validado localmente contra `schemas/vocabulary-candidate.schema.json`: **1,680 / 1,680 objetos estructuralmente válidos**.

Estas cifras **no son un recuento del vocabulario histórico**. El número de artículos reales sólo podrá declararse después de revisar continuaciones, falsas fronteras, remisiones y agrupamientos erróneos.

## Muestra versionada: página digital 134

Para hacer auditable el comportamiento del algoritmo sin subir todavía todos los derivados voluminosos, el repositorio incluye `data/lexicon/candidates/p134_candidates.jsonl`, con **38 candidatos** de la página digital 134.

La muestra es deliberadamente reveladora de los límites del método. Junto a agrupamientos plausibles como `Abofetear. Achonfu.` o `Aborrecer. Caería.`, aparecen falsos comienzos y OCR defectuoso. Por ejemplo, una secuencia como `Aiepji- ca*` puede recibir una frontera geométrica aunque no constituya un artículo autónomo. Precisamente por ello la capa se denomina `machine_candidate` y no `lexical_entry`.

El archivo de muestra tiene SHA-256 `8df242f1862cf5610473416907bdd3815246a7e4e4ba25b5ea5751278e185d1`.

## Relación con las entradas lexicográficas

La arquitectura queda explícitamente separada:

```text
facsímil
  ↓
OCR bruto
  ↓
líneas con layout y columnas
  ↓
candidatos de límites de artículo
  ↓
revisión/corrección de fronteras
  ↓
segmentación interna del artículo
  ↓
entrada lexicográfica estructurada
  ↓
normalización y análisis derivados
```

Un candidato sólo puede convertirse en entrada de `schemas/lexical-entry.schema.json` mediante una actividad editorial posterior. La promoción debe conservar el identificador o la relación con el candidato del que procede y registrar quién o qué realizó la transformación.

## Reproducibilidad

```bash
python scripts/extract_vocab_candidates.py \
  --pdf /ruta/Cahíta.pdf \
  --start-page 133 \
  --end-page 177 \
  --out build/alc1737/vocabulary_candidates.jsonl

python scripts/validate_jsonl.py \
  --schema schemas/vocabulary-candidate.schema.json \
  --jsonl build/alc1737/vocabulary_candidates.jsonl
```

El algoritmo se conserva deliberadamente simple y conservador. Las mejoras futuras deberán compararse contra una muestra revisada y reportar falsos positivos, falsos negativos y cambios de cobertura antes de sustituir esta versión.
