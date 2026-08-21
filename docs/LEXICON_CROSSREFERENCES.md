# Inventario reproducible de remisiones históricas

## Alcance

Los artículos de `data/lexicon/articles/*.jsonl` pueden conservar remisiones explícitas mediante el campo `crossReferences`. Esta capa deriva un inventario consolidado de esas remisiones sin intentar resolver automáticamente su destino.

El generador es:

```bash
python scripts/export_lexicon_crossreferences.py
```

Por omisión escribe en `build/lexicon-crossreferences/`:

- `chd_lexicon_crossreferences.jsonl`
- `chd_lexicon_crossreferences.csv`
- `manifest.json`

## Principio editorial

`markerRaw` y `targetRaw` se preservan exactamente como aparecen en los objetos históricos estructurados. El derivado no convierte una remisión `Buſca` en equivalencia cahíta, no normaliza el destino a un lema moderno y no crea enlaces por semejanza gráfica.

El único metadato añadido es `markerClass`, con dos valores:

- `busca`: el marcador histórico, después de una normalización técnica mínima `ſ → s`, mayúsculas/minúsculas y espacios, equivale a `busca`;
- `other`: cualquier otro marcador explícito.

Esta clasificación sirve para conteo y filtrado, no altera `markerRaw`.

## Campos

Cada fila conserva:

- `sourceArticleId`;
- página digital y columna del artículo fuente;
- guía castellana fuente;
- tipo de artículo fuente;
- índice de la remisión dentro del artículo;
- `markerRaw`;
- `markerClass`;
- `targetRaw`;
- `relation`.

El orden es determinista: `sourceArticleId` numérico ascendente y, dentro de cada artículo, el índice original de la remisión.

## Manifiesto

`manifest.json` registra el número de artículos canónicos examinados, el total de remisiones, el número de artículos que contienen remisiones, conteos por clase de marcador y relación, los archivos canónicos usados y SHA-256/tamaño de cada exportación.

El manifiesto declara explícitamente `destinationResolutionPerformed: false`.

## Próxima capa

Una resolución futura de destinos debe producirse como artefacto **separado** y trazable. Deberá distinguir al menos entre destino exacto demostrado, destino probable, referencia circular, destino no localizado y formulación no normalizada. Ninguna de esas decisiones debe reescribir silenciosamente el artículo histórico.

## QA

`CHD QA` genera este inventario en un directorio temporal y comprueba que sea no vacío, que el manifiesto sea JSON válido y que los archivos derivados existan. Una corrida verde garantiza consistencia computacional del inventario, no resolución semántica de las remisiones.
