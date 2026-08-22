# Revisión de remisiones históricas `Buſca`: estado de avance

Actualización: 21 de agosto de 2026.

## Alcance

Este documento registra la revisión post-cierre de las remisiones históricas del vocabulario `ALC1737`. El grafo canónico estricto, la capa diagnóstica y la capa de revisión editorial permanecen separados.

## Estado canónico estricto

El inventario contiene **151 remisiones históricas**. El grafo estricto conserva **60 aristas `exact_unique`**, **90 remisiones `not_located`**, 1 remisión `not_busca` y 4 ciclos exactos. La revisión editorial no modifica estos conteos.

## Diagnóstico reproducible

Las 90 remisiones estrictamente no localizadas conservan su clasificación diagnóstica original: **44 `A_unique_strong`**, **16 `B_multiple_strong`** y **30 `C_no_strong`**. La clase expresa prioridad, no resolución.

## Revisión explícita acumulada

Se han registrado **84 revisiones explícitas**: 44 Tier A, 16 Tier B y 24 Tier C. Todas mantienen `humanVerified=false`.

- **40** tienen `decisionStatus=source_supports_unique_target`;
- 20 tienen `decisionStatus=source_or_destination_requires_recollation`;
- 5 tienen `decisionStatus=candidate_rejected`;
- 19 tienen `decisionStatus=target_not_located`.

La aritmética es 40 + 20 + 5 + 19 = 84. Ninguna propuesta editorial se convierte retroactivamente en coincidencia estricta.

## Tier A y Tier B

`A_unique_strong` está cerrado **44/44**: 29 propuestas, 8 recolaciones, 5 rechazos y 2 destinos no localizados. `B_multiple_strong` está cerrado **16/16**: 8 propuestas, 4 recolaciones y 4 destinos no localizados.

## Tier C: 24/30

Tier C sólo admite recuperaciones fuera del shortlist cuando existe evidencia positiva del mismo testimonio y evidencia de estructura canónica. Las similitudes débiles no son autoridad de enlace.

### Lote 09

Aportó 2 propuestas editoriales, 3 recolaciones y 3 destinos no localizados. Las dos recuperaciones positivas fueron `Baſta, coſa ſin pulir → Aſpera coſa` y `Cueva → Caberna, ò cueva`.

### Lote 10

Aportó 1 propuesta editorial (`Montear → Cazar ſalir a caza`), 1 recolación (`Orejear`) y 6 destinos no localizados (`mancebo`, `meados`, `mear`, `atrevido`, `gozo`, `pelear`).

### Lote 11

| Fuente histórica | Resultado editorial |
| --- | --- |
| `Anguſtia` — `Buſca afliccion` | `target_not_located`; la remisión es legible, pero no existe una guía independiente `Afliccion`. |
| `Eſtender, ò tender` — `Buſca deſenvolver` | `source_or_destination_requires_recollation`; el OCR del target parece acercarse a `Deſembolver`, por lo que puede existir una discrepancia de lectura del propio `targetRaw`. |
| `Levantarſe amotinarſe` — `Buſca alzarſe` | `source_or_destination_requires_recollation`; el OCR mezcla columnas y no conserva la remisión con precisión suficiente. |
| `Luchar` — `Buſca forcejar` | `source_or_destination_requires_recollation`; el target aparece degradado y no existe guía independiente `Forcejar`. |
| `Morirſe de frío` — `Buſca frío tener` | `source_or_destination_requires_recollation`; el OCR conserva sólo parcialmente la frase remitida. |
| `Nuevamente` — `Buſca otra vez` | `target_not_located`; `Otras vezes` no se colapsa automáticamente con `otra vez`. |
| `Permitir algo` — `Buſca conſentir` | `target_not_located`; la remisión se corrobora localmente, pero no se localiza guía independiente `Conſentir`. |
| `Permiſſion` — `Buſca conſentimiento` | `target_not_located`; no se localiza guía independiente `Conſentimiento`. |

El lote 11 no crea nuevas aristas: aporta 4 recolaciones y 4 destinos no localizados. Esto es deliberado; una posible corrección de lectura de fuente no se convierte en resolución editorial sin cotejo suficiente.

## Vista revisada derivada

Tras el lote 11, la vista revisada debe contener:

- 151 remisiones representadas;
- 60 aristas estrictas;
- 40 aristas editoriales;
- **100 aristas efectivas**;
- **20 casos `editorial_requires_recollation`**;
- 5 casos `editorial_candidate_rejected`;
- 19 casos `editorial_target_not_located`;
- **6 casos `strict_not_located_unreviewed`**;
- 0 aristas editoriales `humanVerified=true`.

## Cola reproducible de trabajo

La cola resta las **84 revisiones explícitas** al universo de 90 remisiones estrictamente `not_located`. Debe producir **6 pendientes**: 0 A, 0 B y 6 C. Tier C queda en **24/30**; el siguiente lote es el cierre de los seis casos finales.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica no es una resolución. Un destino no localizado no debe sustituirse por una coincidencia aproximada. Cerrar un nivel significa revisar todos sus casos, no producir una resolución positiva para todos. Una corrida verde de QA no es validación filológica humana.**
