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

## Cierre de la revisión inicial Tier A

Se han registrado **44 revisiones explícitas**, correspondientes a la totalidad de los **44 casos `A_unique_strong`**. Todas mantienen `humanVerified=false`.

De esas 44 revisiones:

- **29** tienen `decisionStatus=source_supports_unique_target` y un `selectedTargetArticleId` explícito;
- **8** tienen `decisionStatus=source_or_destination_requires_recollation` y no reciben destino efectivo;
- **5** tienen `decisionStatus=candidate_rejected`: el candidato diagnóstico mostrado fue inspeccionado y descartado como destino lexicográfico;
- **2** tienen `decisionStatus=target_not_located`: la remisión histórica es legible, pero no se localizó una entrada destino independiente.

Las 29 propuestas positivas actualmente registradas son:

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
| `Tocar` — `Buſca palpar` | `Palpar con las manos` |
| `Traſponer plantas` — `Buſca plantar` | `Plantar arboles` |
| `Ninguno` — `Buſca nadie` | `Nadie por ninguno` |
| `Obligar` — `Buſca pagar` | `Pagar deuda` |
| `Peine` — `Buſca eſcobeta` | `Eſcobeta para peinarſe` |
| `Peſadumbre aſſi` — `Buſca pena` | `Pena generalmente` |
| `Remudar` — `Buſca feriar` | `Feriar vna coſa por otra` |
| `Tizné` — `Buſca tinta` | `Tinta para eſcrebir` |

Los **8 casos `editorial_requires_recollation`** son:

- `Danzar` — `Buſca bailar`: el candidato `Bailar algún ſon` sigue siendo diagnóstico, pero no se recuperó con suficiente limpieza el contexto fuente;
- `Apercibirſe para hazer algo` — `Buſca aparejarſe`: se localizó un OCR ruidoso del destino `Aparejarſe para hazer algo`, pero no una remisión fuente suficientemente limpia;
- `Yr delante` — `Buſca guiar`: la fórmula fuente es visible, pero el token de destino aparece gravemente corrompido en OCR;
- `Loco bolverſe` — `Buſca enloquecer`: el destino `Enloquecer, ò perder el juizio` es localizable, pero la remisión fuente está demasiado dañada en OCR para promoverla editorialmente sin cotejo de imagen;
- `Reglar con regla` — `Buſca rayar`: el OCR localiza la guía fuente como `Reglar con regla` pero no conserva una remisión `Buſca rayar` inequívoca; debe cotejarse directamente el facsímil y el límite de columna;
- `Obligacion` — `Buſca paga`: el OCR conserva sólo `pag**`, insuficiente para distinguir con seguridad `paga` de `pagar`, y la entrada candidata `Paga tal` no fue recuperada limpiamente en OCR;
- `Poco antes`: la capa estructurada conserva `targetRaw=mo hia mucho`, mientras el OCR del testimonio muestra `Buſca no ha mucho`; la discrepancia debe resolverse mediante cotejo directo del facsímil antes de corregir procedencia o proponer destino;
- `Topo animal` — `Buſca eſcarabajo`: el candidato `Eſcaravajo` presenta una diferencia `b/v` que puede ser histórica o producto del OCR; no se normaliza ni se enlaza sin cotejo de imagen.

Los **5 candidatos rechazados** son:

- `Nombrar, poner nombre` — `Buſca llamar`: el diagnóstico propuso `O, adv. para llamar`, pero `llamar` aparece dentro de una descripción de uso y no constituye la guía de esa entrada;
- `Rueda` — `Buſca redonda coſa`: el diagnóstico propuso la entrada genérica `Coſa`, que omite el modificador discriminante `redonda`;
- `Oprimido eſtar` — `Buſca apretado`: el candidato `Aflojar lo que eſtá apretado` contiene `apretado` sólo dentro del objeto de una entrada encabezada por `Aflojar`;
- `Palillo oloroſo` — `Buſca olor`: el candidato `Oler, echar de ſi olor` es una entrada verbal y `olor` aparece únicamente dentro de su explicación;
- `Sazonarſe la fruta` — `Buſca madura eſtar`: el candidato `Eſtar` reproduce sólo el componente verbal genérico y no la frase remitida completa.

Los **2 casos `editorial_target_not_located`** son:

- `Vadear el Rio` — `Buſca paſſar el Rio por vado`: la remisión completa es legible, pero no se localizó una entrada independiente con esa guía; el candidato automático `Rio` reproduce sólo un token genérico interno;
- `Vihuela, ó guitarra` — `Buſca guitarra`: la remisión es visible, pero el diagnóstico devuelve la propia entrada fuente porque `guitarra` aparece dentro de su guía; no se localizó una entrada independiente `Guitarra` en esta revisión.

Los casos en recolación deben volver al facsímil. Los candidatos rechazados y los destinos no localizados permanecen documentados como resultados negativos, no como resoluciones. Una puntuación diagnóstica fuerte no sustituye evidencia lexicográfica suficiente.

## Vista revisada derivada

`scripts/export_lexicon_crossreference_reviewed_view.py` genera una vista independiente que incorpora las decisiones editoriales sin alterar el grafo estricto.

El estado reproducible esperado de esa vista es:

- **151 remisiones** representadas;
- **60 aristas estrictas** con `edgeAuthority=strict_exact_normalized_equality`;
- **29 aristas editoriales** con `edgeAuthority=editorial_source_review`;
- **89 aristas efectivas** en la vista revisada;
- **8 casos `editorial_requires_recollation`**;
- **5 casos `editorial_candidate_rejected`**;
- **2 casos `editorial_target_not_located`**;
- **46 casos `strict_not_located_unreviewed`**;
- **0 aristas editoriales `humanVerified=true`**.

La vista se exporta en JSONL, CSV y grafo JSON, y se valida mediante doble ejecución determinista byte-a-byte. Los hashes exactos de cada estado se conservan en el manifiesto generado por el exportador.

## Cola reproducible de trabajo

La cola permanente `scripts/export_crossreference_review_queue.py` resta las 44 revisiones explícitas al universo de 90 remisiones estrictamente `not_located`. El corte esperado debe producir **46 casos pendientes**, distribuidos como **0 A**, **16 B** y **30 C**. La cola es estado de trabajo reproducible: no crea destinos ni modifica la autoridad de las remisiones.

## Siguiente frente

La **revisión inicial Tier A queda cerrada 44/44**. El siguiente nivel de trabajo es `B_multiple_strong`, con **16 casos** en los que el diagnóstico presenta más de un candidato fuerte. Esos casos requieren comparación explícita entre alternativas y, cuando el OCR no permita discriminar, cotejo directo del facsímil.

Después de B quedarán los **30 casos `C_no_strong`**, que constituyen el frente de mayor dificultad textual porque el diagnóstico no ofrece candidato fuerte alguno.

El procedimiento se mantiene conservador: localizar la fórmula histórica y cada destino candidato en el mismo testimonio, registrar una propuesta sólo cuando la evidencia permita discriminar, documentar candidatos rechazados, usar `target_not_located` cuando la remisión sea clara pero no aparezca destino independiente, y enviar a recolación cualquier caso en que el OCR no permita sostener la decisión.

## Guarda epistemológica

**Una arista editorial sustentada no es una arista canónica estricta. Una coincidencia diagnóstica fuerte no es una resolución. Un candidato rechazado no desaparece de la historia de revisión. Un destino no localizado no debe sustituirse por una coincidencia aproximada. Cerrar Tier A significa revisar explícitamente sus 44 casos; no significa que los 44 hayan producido resoluciones positivas ni que exista validación filológica humana. Una corrida verde de QA no es validación filológica humana.**
