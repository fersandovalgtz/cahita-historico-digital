# Exportaciones reproducibles del corpus lexicográfico

## Principio

Los objetos canónicos de la capa curatorial permanecen en `data/lexicon/articles/*.jsonl`. Las exportaciones consolidadas son **derivados reproducibles** y no una segunda fuente editorial de verdad.

El generador es:

```bash
python scripts/export_lexicon_corpus.py
```

Por omisión escribe en `build/lexicon-exports/`:

- `chd_lexicon_articles.jsonl`
- `chd_lexicon_articles.json`
- `chd_lexicon_articles.csv`
- `manifest.json`

Puede elegirse otro destino con `--out-dir`.

## Invariantes

El exportador:

1. lee todos los JSONL de `data/lexicon/articles/`;
2. rechaza `articleId` duplicados;
3. ordena de forma determinista por el componente numérico de `articleId`;
4. compara el recuento contra `currentCuratorialArticleCount` de `phase2_open_work_summary.json`;
5. genera JSONL, JSON y CSV sin alterar los objetos fuente;
6. calcula SHA-256 y tamaño en bytes de cada salida;
7. registra esos valores en un manifiesto sin timestamp para preservar determinismo;
8. vuelve a leer los archivos escritos y verifica que sus hashes coincidan con el manifiesto.

En el estado de cierre de Phase II, el recuento esperado es **2,302 artículos**.

## Semántica del CSV

El CSV es una vista tabular conservadora. Los campos anidados —formas cahítas, remisiones, notas, `sourceSpans`, procedencia y listas de candidatos— se serializan como JSON compacto dentro de sus celdas. No se normalizan ni se resuelven automáticamente.

Por tanto, una remisión `Buſca`, una anáfora `Lo miſmo`, una forma `unresolved` o un separador histórico conservan su semántica editorial original.

## Orden

El orden de exportación es **`articleId` numérico ascendente**. Este orden garantiza reproducibilidad de bytes y no pretende reconstruir por sí solo el orden tipográfico fino dentro de una página. La estructura física se conserva mediante `sourcePageDigital`, `column`, `sourceSpans` y demás campos de cada objeto.

## Manifiesto

`manifest.json` registra:

- recuento total de artículos;
- recuento de archivos JSONL canónicos de entrada;
- recuentos por `reviewStatus`;
- número de objetos `humanVerified`;
- lista explícita de archivos canónicos usados;
- tamaño y SHA-256 de JSONL, JSON y CSV.

No contiene fecha de generación porque una marca temporal rompería la identidad byte-a-byte entre dos ejecuciones sobre el mismo checkout.

## QA

El workflow `CHD QA` ejecuta el exportador hacia un directorio temporal y falla si:

- el número de artículos no coincide con la fuente canónica de estado;
- existen IDs duplicados;
- el generador no puede producir alguno de los formatos;
- el manifiesto no es JSON válido;
- falla la verificación post-escritura de hashes.

Una ejecución satisfactoria demuestra reproducibilidad computacional de los derivados; no convierte la capa en `human_verified` ni constituye una release científica estable.
