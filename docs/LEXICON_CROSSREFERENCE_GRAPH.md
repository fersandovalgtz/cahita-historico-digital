# Grafo conservador de remisiones históricas

## Propósito

Esta capa continúa el inventario reproducible de `crossReferences` sin modificar los artículos canónicos. Su objetivo es determinar qué destinos `Buſca` pueden enlazarse por una regla estrictamente mecánica y cuáles deben permanecer abiertos para revisión editorial.

El generador es:

```bash
python scripts/export_lexicon_crossreference_graph.py
```

Por omisión escribe en `build/lexicon-crossreference-graph/`:

- `chd_lexicon_crossreference_resolution.jsonl`
- `chd_lexicon_crossreference_resolution.csv`
- `chd_lexicon_crossreference_graph.json`
- `manifest.json`

## Regla de resolución

Un destino sólo se enlaza automáticamente cuando `targetRaw`, después de una normalización técnica mínima, coincide con **una y sólo una** `spanishGuideRaw` canónica.

La clave técnica aplica:

1. `ſ → s`;
2. `casefold`;
3. descomposición Unicode NFKD y retirada de diacríticos combinantes;
4. puntuación convertida en espacio;
5. colapso de espacios.

Después de esa transformación se exige igualdad exacta. No se usan distancia de edición, similitud fonética, lematización, stemming, embeddings, modelos lingüísticos ni equivalencia semántica.

## Estados

Cada remisión recibe uno de estos estados derivados:

- `exact_unique`: existe una sola guía canónica con la misma clave normalizada; se crea una arista del grafo derivado;
- `exact_multiple`: la clave coincide con más de un artículo y no se elige entre homógrafos;
- `not_located`: no existe coincidencia exacta normalizada;
- `non_normalizable`: el destino no produce una clave técnica utilizable;
- `not_busca`: el marcador histórico no pertenece a la clase técnica `Buſca`; no se intenta resolver.

`matchedArticleIds` conserva todas las coincidencias exactas cuando hay más de una. Sólo `exact_unique` produce `exactUniqueTargetArticleId`.

## Resultado reproducible vigente

Sobre los 2,302 artículos canónicos, la corrida integrada a `CHD QA` del 21 de agosto de 2026 procesa **151 remisiones** y obtiene:

- **60** `exact_unique` — aristas que pueden enlazarse por la regla estricta;
- **90** `not_located` — destinos que requieren una capa posterior de revisión;
- **1** `not_busca` — remisión excluida de la resolución `Buſca`;
- **0** `exact_multiple`;
- **0** `non_normalizable`;
- **4** ciclos exactos en el subgrafo de 60 aristas.

Estos conteos son resultados derivados, no datos curatoriales incorporados a los artículos. Si cambia la capa canónica, deben regenerarse.

## Ciclos

El grafo se construye exclusivamente con aristas `exact_unique`. Sobre ese subgrafo se calculan componentes fuertemente conexos mediante un algoritmo determinista. Se distinguen:

- `self_loop`: una remisión exacta vuelve al mismo artículo;
- `cycle_member`: dos o más artículos forman un ciclo dirigido;
- `none`: la arista no pertenece a un ciclo exacto.

La existencia de un ciclo describe la estructura de las remisiones históricas; no autoriza a resolver su contenido por equivalencia.

## Autoridad editorial

Este derivado resuelve **identidad de destino dentro del dataset**, no identidad de lexema ni equivalencia lingüística. El manifiesto declara expresamente:

- `fuzzyMatchingUsed: false`;
- `linguisticSimilarityUsed: false`;
- `semanticEquivalenceInferred: false`;
- `probableResolutionInferred: false`;
- `canonicalArticlesModified: false`.

Las remisiones `exact_multiple` y `not_located` forman una cola explícita para una futura revisión filológica. Las propuestas probables, si se incorporan, deberán vivir en una capa curatorial separada con evidencia y estado de autoridad propios.

## Reproducibilidad

El manifiesto registra conteos por estado, número de aristas exactas, ciclos, archivos canónicos utilizados y SHA-256/tamaño de cada salida. `CHD QA` ejecuta el exportador dos veces en directorios independientes y exige salidas byte-a-byte idénticas. También verifica que el número de remisiones coincida con el inventario canónico derivado de `crossReferences`.
