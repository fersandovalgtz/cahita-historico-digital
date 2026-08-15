# Extractor de fronteras lexicográficas v0.2

## Motivo de la revisión

La primera versión `indentation_margin_v0.1` fue deliberadamente conservadora. En la muestra diagnóstica de páginas 133, 134, 150 y 177 alcanzó una precisión de **95.32%**, pero un recall menor, **86.70%**. La inspección visual mostró que muchas omisiones no procedían de una falta de señal tipográfica, sino de una mala estimación del margen de inicio en páginas donde las líneas indentadas eran numerosas.

La versión **`hybrid_margin_mode_v0.2`** cambia únicamente la detección geométrica del comienzo candidato. Mantiene intacta la regla científica central: un candidato no es una entrada lexicográfica.

## Algoritmo v0.2

Para páginas ordinarias del vocabulario (digitales 134–177), el extractor:

1. reconstruye las dos columnas mediante `extract_vocab_layout.py`;
2. elimina encabezados reconocibles y material por encima de `y = 50`;
3. agrupa las coordenadas `xMin` de comienzos de línea en bins de 3 puntos;
4. identifica el grupo modal de comienzos y utiliza la mediana de su vecindad como margen estimado de inicio;
5. considera inicio candidato una línea alfabética situada a ±6 puntos de ese margen;
6. agrega las líneas siguientes hasta el próximo comienzo candidato.

La página digital **133** recibe una regla especial. Al ser la primera página del vocabulario contiene material de transición y encabezado que vuelve inestable el estimador modal; por ello v0.2 conserva allí el criterio más conservador de v0.1.

Cada candidato v0.2 registra ahora `pageRule` y `estimatedStartMarginX`, además de `boundaryMethod = hybrid_margin_mode_v0.2`.

## Reejecución completa

La corrida reproducible sobre páginas digitales 133–177 produjo:

- **2,072 candidatos**;
- **1,055** en columna izquierda;
- **1,017** en columna derecha;
- **45** páginas procesadas;
- mínimo de **24** y máximo de **61** candidatos por página;
- media de **46.04** candidatos por página;
- tamaño del JSONL derivado: **997,356 bytes**;
- SHA-256: `f2a5b0e0319e57cc8d13c4a0eed79505d69941bf48ee993559f97b64bec8e6b3`;
- validación: **2,072 / 2,072** objetos válidos contra `schemas/vocabulary-candidate.schema.json`.

La cifra de 2,072 sigue siendo una **cantidad de candidatos computacionales**, no un recuento del vocabulario histórico.

## Comparación sobre la misma muestra

| Método | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| `indentation_margin_v0.1` | 163 | 8 | 25 | 95.32% | 86.70% | 90.81% |
| `hybrid_margin_mode_v0.2` | 169 | 5 | 19 | **97.13%** | **89.89%** | **93.37%** |

La comparación utiliza exactamente las mismas páginas —133, 134, 150 y 177— y las mismas fronteras visibles de referencia. v0.2 mejora simultáneamente precisión, recall y F1 en la muestra.

Por página, v0.2 produjo:

| Página | TP | FP | FN |
|---:|---:|---:|---:|
| 133 | 20 | 4 | 9 |
| 134 | 37 | 0 | 6 |
| 150 | 55 | 1 | 1 |
| 177 | 57 | 0 | 3 |

La página 133 permanece como el estrato más problemático y conserva por diseño el comportamiento de v0.1. En las otras tres páginas el estimador modal recupera comienzos adicionales con muy pocos falsos positivos.

## Inspección adicional de páginas con grandes cambios

La reejecución completa aumenta el número de candidatos en varias páginas respecto de v0.1. Antes de adoptar v0.2 se inspeccionaron adicionalmente páginas con incrementos fuertes, entre ellas las digitales **149** y **165**. Ambas contienen densas secuencias de artículos independientes; la inspección confirmó que el bajo conteo de v0.1 estaba asociado a omisiones sistemáticas y que el mayor número de candidatos de v0.2 es plausible como capa de triage.

Esta comprobación no convierte los candidatos en artículos validados. Sólo reduce el riesgo de interpretar el aumento global de 1,680 a 2,072 como una explosión espuria producida por el nuevo margen.

## Decisión

CHD adopta **`hybrid_margin_mode_v0.2` como método vigente de generación de candidatos**. La versión v0.1 permanece recuperable en el historial Git, sus hashes y su documentación de evaluación. No se sobrescriben retrospectivamente los datos del piloto v0.1.

La próxima fase ya no debe concentrarse principalmente en aumentar la cantidad de candidatos. La prioridad es revisar fronteras y microestructura por lotes, empezando por páginas de alto rendimiento y conservando explícitamente los casos de continuación y ambigüedad.

## Limitación

La muestra de comparación es deliberada y no probabilística, y sus referencias son producto de cotejo visual IA-asistido sin revisión humana independiente. Por ello las cifras son **métricas de ingeniería editorial**, no estimaciones filológicas poblacionales.

Los datos de comparación se conservan en `data/lexicon/review/boundary_algorithm_comparison.json`.
