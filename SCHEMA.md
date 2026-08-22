# Modelo de datos y contratos

Cahíta Histórico Digital utiliza un modelo por capas. Los objetos canónicos conservan evidencia y autoridad; los productos derivados se regeneran desde esas capas y no se convierten silenciosamente en una segunda fuente de verdad.

## Principio de capas

```text
ALC1737 / metadata fuente
        ↓
OCR y transcripción IA-asistida
        ↓
candidatos y decisiones de frontera
        ↓
artículos lexicográficos / objetos gramaticales canónicos
        ↓
capas de revisión y procedencia
        ↓
derivados reproducibles: CSV · JSON · JSONL · TEI Lex-0 · concordancias · paquetes
```

Cada transición debe conservar procedencia y no elevar autoridad por el mero hecho de transformar el formato.

## Contratos v1.0.0

La release congela **26 contratos**:

- **22 JSON Schema Draft 2020-12**;
- **4 archivos de metadatos de alcance fuente** para `ALC1737`.

El inventario completo, bytes y SHA-256 de cada contrato se encuentra en [`release/v1_contract_manifest.json`](release/v1_contract_manifest.json). Cualquier cambio post-v1 a un contrato requiere un nuevo freeze explícito; CI prohíbe deriva silenciosa.

## Núcleo lexicográfico

### `schemas/vocabulary-candidate.schema.json`
Representa candidatos computacionales de comienzo de artículo. Un candidato no equivale por sí mismo a una entrada histórica.

### `schemas/lexicon-candidate-review.schema.json`
Registra decisiones de reconciliación entre candidatos, censos visibles y artículos curatoriales.

### `schemas/lexicon-missed-start.schema.json`
Modela comienzos históricos visibles no capturados por el extractor de candidatos.

### `schemas/lexical-article.schema.json`
Contrato principal para los 2,302 artículos históricos curatoriales. Entre otros campos conserva identificador, fuente, página/columna, guía española, formas cahítas en bruto, remisiones, notas, transcripción, spans físicos, estado de revisión, `humanVerified` y procedencia.

### `schemas/lexical-entry.schema.json`
Contrato de una representación lexicográfica más compacta/derivada; no sustituye al artículo histórico canónico cuando la microestructura requiere más información.

### `schemas/crossreference-source-review.schema.json`
Registra revisión de remisiones `Buſca` sin modificar el grafo estricto por inferencia.

### `schemas/lo-mismo-source-review.schema.json`
Mantiene la fórmula `Lo miſmo` como fenómeno separado mientras su función exacta no esté demostrada.

## Núcleo gramatical

Los schemas gramaticales representan categorías documentales/analíticas específicas del _Arte_, entre ellas:

- `grammatical-rule.schema.json`;
- `grammatical-paradigm.schema.json`;
- `modal-construction.schema.json`;
- `nonfinite-construction.schema.json`;
- `participle-construction.schema.json`;
- `predicative-modal-construction.schema.json`;
- `irregular-verb.schema.json`;
- `preposition-entry.schema.json`;
- `adverb-group.schema.json`;
- `conjunction-group.schema.json`;
- `numeral-system.schema.json`;
- `historical-variety-observation.schema.json`.

Estas estructuras no se presentan como una gramática descriptiva moderna definitiva; conservan las categorías y evidencias históricas antes de reinterpretaciones comparativas posteriores.

## Transcripción y layout

`page-transcription.schema.json`, `vocabulary-layout-line.schema.json` y los contratos de frontera permiten mantener separados el contenido textual, la geometría/layout y la segmentación lexicográfica. Esto evita usar la salida de OCR como si fuera directamente una entrada de diccionario.

## Identificadores

Los artículos usan IDs persistentes del tipo `ALC1737-art-000001`. Una release publicada no recicla un ID para una entidad distinta. Correcciones de lectura conservan el ID cuando la identidad del objeto permanece estable y registran la modificación mediante procedencia.

## Autoridad

Los campos de revisión describen estados editoriales; `humanVerified=true` se reserva para objetos que hayan sido revisados por una persona identificable contra evidencia admisible. En v1.0.0 el conteo es **0**.

## Canónico vs derivado

**Canónico:** metadata fuente, inventarios persistidos, decisiones de reconciliación, artículos, objetos gramaticales y capas de procedencia/revisión designadas por la documentación.

**Derivado:** exportaciones consolidadas, grafos, concordancias, diagnósticos, TEI, CSV/JSON y paquetes de release. Los derivados deben poder regenerarse determinísticamente desde entradas canónicas.

## Interoperabilidad

TEI Lex-0 0.9.5 es la proyección lexicográfica primaria de v1.0.0. La validación externa con Jing comprueba conformidad estructural con el perfil; no certifica interpretación lingüística.

CLDF no es obligatorio para v1.0.0. Su posible implementación futura será una vista analítica derivada, con IDs CHD, procedencia y política explícita de identidad lingüística, no un reemplazo de la microestructura histórica.
