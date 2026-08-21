# Revisión de remisiones históricas `Buſca`: estado de avance

Actualización: 21 de agosto de 2026.

## Alcance

Este documento registra el avance de la revisión post-cierre de las remisiones históricas del vocabulario de `ALC1737`. Debe leerse junto con `docs/CROSSREFERENCE_SOURCE_REVIEW_PROTOCOL.md` y no sustituye el grafo canónico estricto.

La arquitectura vigente conserva tres niveles separados:

1. el **grafo canónico estricto**, que resuelve destinos únicamente por igualdad normalizada exacta;
2. la **capa diagnóstica**, que prioriza los casos estrictamente no localizados mediante señales computacionales no vinculantes;
3. la **capa de revisión de fuente**, que registra decisiones editoriales explícitas con evidencia y autoridad declaradas.

## Estado canónico estricto

El inventario contiene **151 remisiones históricas**. El grafo estricto conserva:

- **60 aristas `exact_unique`**;
- **90 remisiones `not_located`**;
- **1 remisión `not_busca`**;
- **4 ciclos exactos**.

Estos conteos no se alteran por la revisión editorial posterior. Una propuesta de destino sustentada por fuente no se convierte retroactivamente en coincidencia estricta.

## Diagnóstico de las 90 remisiones `not_located`

La auditoría reproducible clasifica los 90 casos en:

- **44 `A_unique_strong`**;
- **16 `B_multiple_strong`**;
- **30 `C_no_strong`**.

El nivel A significa que se muestra un solo candidato por encima del umbral diagnóstico fuerte. No significa que el destino esté resuelto filológicamente.

## Revisión de fuente completada hasta este corte

Se han registrado **12 revisiones explícitas**, todas sobre casos `A_unique_strong` y todas con `humanVerified=false`.

De esas 12 revisiones:

- **11** tienen `decisionStatus=source_supports_unique_target` y un `selectedTargetArticleId` explícito;
- **1** tiene `decisionStatus=source_or_destination_requires_recollation` y no recibe destino efectivo.

Las 11 propuestas positivas actualmente registradas son:

| Fuente histórica | Destino editorialmente sustentado |
| --- | --- |
| `Barrenar` — `Buſca agurear con barrena` | `Agujerear con barrena` |
| `Comulgar` — `Buſca comunion` | `Comunion Miſſa Santiſſimo Sacram.` |
| `Dilatar` — `Buſca diferir` | `Diferir, ò dilatar` |
| `Saliva` — `Buſca eſcupitina` | `Eſcupitina ſaliva` |
| `Noez` — `Buſca nogal` | `Noez, y nogal` |
| `Sarna` — `Buſca roña` | `Roña, ò ſarna` |
| `Anguſtiarſe` — `Buſca afligirſe` | `Afligirſe, ò apurarſe` |
| `Anguſtiar á otro` — `Buſca afligir` | `Afligir à otro` |
| `Boſadura tal` — `Buſca bomitar` | `Boſſar, ò bomitar` |
| `Braza` — `Buſca aſqua` | `Aſqua, ò braſa` |
| `Eſpeluzarſe` — `Buſca erizarſe` | `Erizarſe los pelos` |

El caso `Danzar` — `Buſca bailar` conserva como candidato diagnóstico `Bailar algún ſon`, pero se mantiene en **recolación necesaria** porque el control OCR del mismo testimonio no permitió recuperar el contexto fuente con limpieza suficiente para convertir la señal diagnóstica en propuesta positiva.

## Vista revisada derivada

`scripts/export_lexicon_crossreference_reviewed_view.py` genera una vista independiente que incorpora las decisiones editoriales sin alterar el grafo estricto.

El estado reproducible de esa vista es:

- **151 remisiones** representadas;
- **60 aristas estrictas** con `edgeAuthority=strict_exact_normalized_equality`;
- **11 aristas editoriales** con `edgeAuthority=editorial_source_review`;
- **71 aristas efectivas** en la vista revisada;
- **1 caso `editorial_requires_recollation`**;
- **78 casos `strict_not_located_unreviewed`**;
- **0 aristas editoriales `humanVerified=true`**.

La vista se exporta en JSONL, CSV y grafo JSON, y se valida mediante doble ejecución determinista byte-a-byte. En el corte actual, los hashes de las tres salidas son:

- `chd_lexicon_crossreference_reviewed_graph.json`: `697d395aad8c7ce3c5b931709382a784622818315a6c757bce7a59883d108f3a`;
- `chd_lexicon_crossreference_reviewed_view.csv`: `f66ef1f12edead8736b0f2a349e94c434fc41dedb039ffcf6319e7e792368e7f`;
- `chd_lexicon_crossreference_reviewed_view.jsonl`: `e2923c53327b0c1f43f96ddd08366d8241053f573b6706d7061b622474314b27`.

Los hashes son verificadores del estado actual de los datos, no identificadores permanentes: cambiarán legítimamente cuando se incorporen nuevas revisiones explícitas.

## Siguiente frente

El siguiente bloque debe continuar con los **32 casos restantes de `A_unique_strong`** que aún no tienen revisión explícita. La prioridad es cotejar primero los casos donde la fórmula `Buſca` y el destino candidato puedan localizarse con suficiente claridad en el mismo testimonio. Los casos con OCR deficiente deben conservarse como pendientes de facsímil o recolación, no resolverse por fuerza de la puntuación diagnóstica.

Una vez agotado el nivel A, la revisión debe pasar a los 16 casos `B_multiple_strong`, donde la tarea principal será discriminar ambigüedades reales. Los 30 casos `C_no_strong` constituirán el frente final y probablemente exigirán mayor control textual, variantes gráficas históricas o consulta de testimonios de apoyo.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica fuerte no es una resolución. Una corrida verde de QA no es validación filológica humana.**
