# Protocolo de revisión de candidatos lexicográficos

## Objeto de revisión

La unidad revisada en esta fase es un objeto `vocabulary-candidate`, es decir, una agrupación geométrica producida por `scripts/extract_vocab_candidates.py`. El revisor no debe asumir que el candidato coincide con un artículo histórico: debe decidir tanto si su **inicio** corresponde a una frontera real como si las líneas agrupadas pertenecen a una sola entrada.

## Decisiones permitidas

Cada candidato recibe una decisión de frontera y una decisión de agrupación.

### Frontera inicial

- `valid_start`: el comienzo del candidato coincide con el inicio visible de un artículo histórico;
- `false_start`: el algoritmo creó una frontera dentro de una continuación, ruido o material de otra columna;
- `uncertain_start`: la imagen no permite decidir con seguridad.

### Agrupación interna

- `accept_group`: las líneas del candidato forman un solo artículo, aunque el OCR contenga errores;
- `split_group`: el candidato contiene dos o más artículos y debe dividirse;
- `trim_group`: el comienzo es válido, pero el candidato absorbió líneas pertenecientes al artículo siguiente u otro material;
- `extend_group`: el comienzo es válido, pero faltan líneas que pertenecen al mismo artículo;
- `reconstruct_group`: la agrupación mezcla omisiones y contaminaciones que requieren reconstrucción manual;
- `unresolved_group`: no existe evidencia suficiente para decidir.

Estas decisiones describen **fronteras**, no corrigen todavía la lectura de los caracteres.

## Fronteras omitidas

La revisión de una página debe registrar también artículos visibles cuyo comienzo no haya producido candidato. Se conservan como `missed_start` con página, columna, posición aproximada y un fragmento de identificación.

Este registro es indispensable para medir recall. Revisar sólo los candidatos existentes permitiría medir falsos positivos, pero ocultaría los artículos omitidos por el algoritmo.

## Métricas

Sobre una página o muestra revisada:

- **TP**: candidato cuyo comienzo es `valid_start`;
- **FP**: candidato cuyo comienzo es `false_start`;
- **FN**: `missed_start` visible sin candidato equivalente;
- `precision = TP / (TP + FP)`;
- `recall = TP / (TP + FN)`;
- `F1 = 2PR / (P + R)`.

Las métricas de frontera no evalúan la exactitud del OCR ni la corrección de la microestructura interna del artículo.

## Autoridad de la revisión

Una decisión realizada mediante cotejo visual IA-asistido se marca `machine_corrected_unverified`. Sólo una revisión humana identificable contra el facsímil puede usar `human_verified`.

Las decisiones deben conservar:

- candidato original;
- página y columna;
- decisión de inicio;
- decisión de agrupación;
- nota de evidencia;
- agente y método;
- estado de revisión.

## Promoción

Un candidato no puede promoverse directamente a `lexical-entry` por el mero hecho de tener `valid_start`. Primero debe resolverse la agrupación y, después, segmentarse la microestructura interna del artículo.

La cadena de autoridad es:

```text
candidate
  ↓ revisión de frontera
boundary_decision
  ↓ corrección de agrupación
article_span
  ↓ transcripción/microestructura
lexical_entry
```

## Piloto de la página 134

La página digital 134 se utiliza como primera prueba visual porque contiene dos columnas densas, artículos multilínea, continuaciones y un artículo que comienza al pie y continúa en la página siguiente. La evaluación IA-asistida identificó **43 comienzos históricos visibles**, frente a **38 candidatos automáticos**.

De los 38 candidatos, **37 comienzan en una frontera real** y uno (`Aiepji- ca*`) es un falso comienzo producido por mezcla geométrica/OCR. Se identificaron **seis fronteras omitidas**: `Aborrecedor`, `Abotonarſe la flor`, `Abrigarſe para defenderſe`, `Abuela paterna`, `Abuela tercera` y el artículo que comienza `Abuba-` al pie y continúa en la página 135.

Para esta página, la evaluación de **inicios de artículo** produce:

- TP = 37;
- FP = 1;
- FN = 6;
- precisión = **97.37%**;
- recall = **86.05%**;
- F1 = **91.36%**.

Estas cifras son un **piloto IA-asistido sin revisión humana independiente**. No deben extrapolarse al vocabulario completo hasta repetir el procedimiento en una muestra estratificada de páginas.
