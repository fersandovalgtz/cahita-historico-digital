# Revisión de remisiones históricas `Buſca`: cierre de revisión inicial

Actualización: 21 de agosto de 2026.

## Alcance

Este documento registra el cierre de la revisión post-cierre de las remisiones históricas `Buſca` del vocabulario `ALC1737`. El **grafo canónico estricto**, la **capa diagnóstica** y la **capa de revisión editorial de fuente** permanecen separados. Cerrar la revisión inicial significa que cada remisión estrictamente `not_located` recibió una decisión explícita; no significa que todas tengan destino resuelto ni que exista validación filológica humana.

La fórmula histórica `Lo miſmo` se administra ahora en una capa independiente. La única ocurrencia que había sido codificada excepcionalmente como remisión (`Azero. Lo miſmo.`) fue retirada del grafo porque la revisión corpus-wide no sustenta tratar la fórmula como una remisión anafórica automática. Esta corrección no modifica ninguna de las 150 remisiones `Buſca` ni sus 90 revisiones editoriales.

## Estado canónico estricto

El inventario contiene **150 remisiones históricas `Buſca`**. El grafo estricto conserva **60 aristas `exact_unique`**, **90 remisiones `not_located`** y 4 ciclos exactos. Ninguna decisión editorial de los lotes de revisión altera esos conteos.

## Diagnóstico reproducible

Las 90 remisiones estrictamente no localizadas conservan su clasificación diagnóstica original: **44 `A_unique_strong`**, **16 `B_multiple_strong`** y **30 `C_no_strong`**. La clasificación expresa prioridad computacional de revisión y no autoridad de resolución.

## Revisión explícita acumulada: 90/90

Se han registrado **90 revisiones explícitas**: 44 Tier A, 16 Tier B y 30 Tier C. Todas mantienen `humanVerified=false`.

- **40** tienen `decisionStatus=source_supports_unique_target` y un destino editorial explícito;
- 22 tienen `decisionStatus=source_or_destination_requires_recollation`;
- 5 tienen `decisionStatus=candidate_rejected`;
- 23 tienen `decisionStatus=target_not_located`.

La aritmética es 40 + 22 + 5 + 23 = 90. Las 40 propuestas editoriales no se promueven al grafo canónico estricto y ninguna equivale a validación humana.

## Cierre por niveles

`A_unique_strong` quedó cerrado **44/44**: 29 propuestas editoriales, 8 recolaciones, 5 candidatos rechazados y 2 destinos no localizados.

`B_multiple_strong` quedó cerrado **16/16**: 8 propuestas editoriales, 4 recolaciones y 4 destinos no localizados.

`C_no_strong` queda cerrado **30/30**: 3 propuestas editoriales, 10 recolaciones y 17 destinos no localizados. Las tres recuperaciones positivas Tier C son `Baſta, coſa ſin pulir → Aſpera coſa`, `Cueva → Caberna, ò cueva` y `Montear → Cazar ſalir a caza`. Todas se sustentan en evidencia explícita del mismo testimonio y estructura canónica; ninguna procede de elevar automáticamente un candidato débil.

## Lote 12: seis casos finales

| Fuente histórica | Resultado editorial |
| --- | --- |
| `Podre` — `Buſca materia` | `target_not_located`; el OCR conserva `materia`, pero no existe una guía independiente `Materia`. |
| `Ponerſe el capote` — `Buſca taparſe` | `target_not_located`; existe `Tapar`, pero no se colapsa el target reflexivo `taparſe` con la guía no reflexiva. |
| `Rebolver una coſa con otra` — `Buſca mezclar` | `source_or_destination_requires_recollation`; el OCR del entorno está fuertemente entremezclado y no permite confirmar de forma independiente el target estructurado `mezclar`; tampoco existe guía `Mezclar/Mesclar`. |
| `Retar, ò deſafiar` — `Buſca pelear` | `target_not_located`; el OCR conserva `pelear`, pero la única guía próxima es `Pelearſe`, que no se colapsa con el target no reflexivo. |
| `Ser` — `Buſca al ſin` | `source_or_destination_requires_recollation`; el OCR muestra una fórmula semejante a `Buſca ai fin`, mientras el target estructurado es `al ſin`. La discrepancia de glifos requiere cotejo directo de imagen. |
| `Sonarſe las narizes` — `Buſca limpiarſe los mocos` | `target_not_located`; la remisión se conserva en OCR, pero las guías próximas `Limpiar`, `Limpiar las narizes` y `Moco de narizes` no reproducen la frase reflexiva remitida. |

El lote 12 no crea nuevas aristas: aporta 2 recolaciones y 4 destinos no localizados.

## Vista revisada derivada

Tras el cierre 90/90, la vista revisada debe contener:

- 150 remisiones `Buſca` representadas;
- 60 aristas estrictas con `edgeAuthority=strict_exact_normalized_equality`;
- 40 aristas editoriales con `edgeAuthority=editorial_source_review`;
- **100 aristas efectivas**;
- **22 casos `editorial_requires_recollation`**;
- 5 casos `editorial_candidate_rejected`;
- 23 casos `editorial_target_not_located`;
- **0 casos `strict_not_located_unreviewed`**;
- 0 aristas editoriales `humanVerified=true`.

Los exportadores JSONL, CSV y grafo JSON se validan mediante doble ejecución determinista byte a byte. La vista revisada es una derivación editorial explícita y nunca sustituye el grafo canónico estricto.

## Cola reproducible de trabajo

La cola permanente resta las **90 revisiones explícitas** al universo de 90 remisiones estrictamente `not_located`. Su estado final esperado es **0 casos pendientes**: 0 `A_unique_strong`, 0 `B_multiple_strong` y 0 `C_no_strong`.

La cola de revisión inicial queda, por tanto, agotada. El trabajo filológico pendiente se concentra ahora en los **22 casos de recolación directa**, además de cualquier validación humana posterior que se decida realizar. Los 23 `target_not_located` permanecen documentados como ausencia de destino localizado bajo la evidencia disponible, no como errores ni como resoluciones aproximadas.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica no es una resolución. Un candidato rechazado no desaparece de la historia de revisión. Un destino no localizado no debe sustituirse por una coincidencia aproximada. Una recolación pendiente no es una resolución. `Lo miſmo` no se convierte automáticamente en una remisión ni en una forma cahíta. Cerrar la revisión inicial significa que los 90 casos `Buſca` no localizados recibieron una decisión explícita; no significa que los 90 hayan sido resueltos positivamente ni que exista validación filológica humana. Una corrida verde de QA no es validación filológica humana.**
