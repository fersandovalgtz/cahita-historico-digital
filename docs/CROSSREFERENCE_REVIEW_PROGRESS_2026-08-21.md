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

Se han registrado **28 revisiones explícitas**, todas sobre casos `A_unique_strong` y todas con `humanVerified=false`.

De esas 28 revisiones:

- **21** tienen `decisionStatus=source_supports_unique_target` y un `selectedTargetArticleId` explícito;
- **5** tienen `decisionStatus=source_or_destination_requires_recollation` y no reciben destino efectivo;
- **2** tienen `decisionStatus=candidate_rejected`: el candidato diagnóstico mostrado fue inspeccionado y descartado como destino lexicográfico.

Las 21 propuestas positivas actualmente registradas son:

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
| `Embolver` — `Buſca doblar` | `Doblar algo` |
| `Eſperar` — `Buſca confiar` | `Confiar en alguno` |
| `Juntar lo que eſtá eſparcido` — `Buſca recoger` | `Recoger lo eſparcido` |
| `Moſtrar con el dedo` — `Buſca apuntar` | `Apuntar con el dedo à alguna parte` |
| `Mudar poniendo vna coſa en lugar de otra` — `Buſca feriar` | `Feriar vna coſa por otra` |
| `Ninguna coſa` — `Buſca nada` | `Nada ninguna coſa` |
| `Premiar` — `Buſca pagar` | `Pagar deuda` |
| `Sepultar` — `Buſca enterrar` | `Enterrar muerto` |
| `Sobrar` — `Buſca quedar` | `Quedar ſobrar` |
| `Tentar con las manos` — `Buſca palpar` | `Palpar con las manos` |

Los **5 casos `editorial_requires_recollation`** son:

- `Danzar` — `Buſca bailar`: el candidato `Bailar algún ſon` sigue siendo diagnóstico, pero no se recuperó con suficiente limpieza el contexto fuente;
- `Apercibirſe para hazer algo` — `Buſca aparejarſe`: se localizó un OCR ruidoso del destino `Aparejarſe para hazer algo`, pero no una remisión fuente suficientemente limpia;
- `Yr delante` — `Buſca guiar`: la fórmula fuente es visible, pero el token de destino aparece gravemente corrompido en OCR;
- `Loco bolverſe` — `Buſca enloquecer`: el destino `Enloquecer, ò perder el juizio` es localizable, pero la remisión fuente está demasiado dañada en OCR para promoverla editorialmente sin cotejo de imagen;
- `Reglar con regla` — `Buſca rayar`: el OCR localiza la guía fuente como `Reglar con regla` pero no conserva una remisión `Buſca rayar` inequívoca; el contexto incluso puede reflejar una forma léxica adyacente, por lo que debe cotejarse directamente el facsímil y el límite de columna.

Los **2 candidatos rechazados** son:

- `Nombrar, poner nombre` — `Buſca llamar`: el diagnóstico propuso `O, adv. para llamar`, pero `llamar` aparece dentro de una descripción de uso y no constituye la guía de esa entrada; el candidato se rechaza y el destino histórico permanece pendiente de localización;
- `Rueda` — `Buſca redonda coſa`: el diagnóstico propuso la entrada genérica `Coſa`, que sólo reproduce el token no discriminante `coſa` y omite `redonda`; no es suficiente para sostener identidad de destino.

Los casos en recolación deben volver al facsímil. Los candidatos rechazados permanecen documentados como resultados negativos, no como resoluciones. Una puntuación diagnóstica fuerte no sustituye evidencia lexicográfica suficiente.

## Vista revisada derivada

`scripts/export_lexicon_crossreference_reviewed_view.py` genera una vista independiente que incorpora las decisiones editoriales sin alterar el grafo estricto.

El estado reproducible de esa vista es:

- **151 remisiones** representadas;
- **60 aristas estrictas** con `edgeAuthority=strict_exact_normalized_equality`;
- **21 aristas editoriales** con `edgeAuthority=editorial_source_review`;
- **81 aristas efectivas** en la vista revisada;
- **5 casos `editorial_requires_recollation`**;
- **2 casos `editorial_candidate_rejected`**;
- **62 casos `strict_not_located_unreviewed`**;
- **0 aristas editoriales `humanVerified=true`**.

La vista se exporta en JSONL, CSV y grafo JSON, y se valida mediante doble ejecución determinista byte-a-byte. Los hashes exactos de cada estado se conservan en el manifiesto generado por el exportador; no se fijan aquí porque cambian legítimamente cada vez que se incorpora un nuevo lote de revisión.

## Cola reproducible de trabajo

La cola permanente `scripts/export_crossreference_review_queue.py` resta las 28 revisiones explícitas al universo de 90 remisiones estrictamente `not_located`. El corte actual debe producir **62 casos pendientes**, distribuidos como **16 A**, **16 B** y **30 C**. La cola es estado de trabajo reproducible: no crea destinos ni modifica la autoridad de las remisiones.

## Siguiente frente

Quedan **16 casos `A_unique_strong` todavía sin revisión explícita**. La prioridad sigue siendo agotar este nivel antes de pasar a los 16 casos `B_multiple_strong`.

El procedimiento se mantiene conservador: localizar la fórmula histórica y el destino candidato en el mismo testimonio, registrar la propuesta en la capa editorial sólo cuando el soporte textual sea suficiente, rechazar candidatos que coincidan únicamente por material genérico y enviar a recolación cualquier caso en que el OCR no permita sostener la decisión. Los 30 casos `C_no_strong` constituirán el frente posterior de mayor dificultad textual.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica fuerte no es una resolución. Un candidato rechazado no desaparece de la historia de revisión. Una corrida verde de QA no es validación filológica humana.**
