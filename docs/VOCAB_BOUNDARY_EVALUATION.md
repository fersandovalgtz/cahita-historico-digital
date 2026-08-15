# Evaluación diagnóstica del extractor de fronteras lexicográficas

## Pregunta

¿Hasta qué punto los candidatos generados por `scripts/extract_vocab_candidates.py` recuperan los comienzos visibles de artículos del vocabulario de `ALC1737`?

La evaluación mide únicamente **fronteras iniciales de artículo**. No mide exactitud del OCR, corrección de la forma cahíta, segmentación interna ni equivalencia semántica.

## Diseño de la muestra

Se realizó un muestreo diagnóstico deliberadamente estratificado por posición y dificultad:

| Página | Estrato | Motivo |
|---:|---|---|
| 133 | inicio del vocabulario | encabezado, arrastre desde texto previo, cruces de columna |
| 134 | vocabulario temprano | artículos multilínea y continuación hacia p. 135 |
| 150 | zona media | página densa de la letra C |
| 177 | zona final | letra V, cerca del cierre del vocabulario alfabético |

La muestra es **intencional, no probabilística**. Sirve para detectar fortalezas y fallos del algoritmo; no proporciona intervalos de confianza para las 45 páginas.

El cotejo fue visual e IA-asistido contra renders del facsímil. No existe todavía revisión humana independiente, por lo que el estado de la evaluación es `machine_corrected_unverified`.

## Criterio

- TP: candidato cuyo inicio coincide con un comienzo visible de artículo;
- FP: candidato cuyo inicio es continuación, ruido o falsa frontera;
- FN: comienzo visible de artículo que no recibió candidato.

La comparación se hace sobre **inicios**, incluso si el candidato después agrupa mal las líneas. Un candidato puede, por tanto, contar como TP de inicio y necesitar `split_group`, `trim_group` o `reconstruct_group` en la revisión de agrupación.

## Resultados

| Página | Candidatos | Comienzos visibles | TP | FP | FN |
|---:|---:|---:|---:|---:|---:|
| 133 | 24 | 29 | 20 | 4 | 9 |
| 134 | 38 | 43 | 37 | 1 | 6 |
| 150 | 55 | 56 | 52 | 3 | 4 |
| 177 | 54 | 60 | 54 | 0 | 6 |
| **Total** | **171** | **188** | **163** | **8** | **25** |

Sobre el conjunto agregado:

- **precisión: 95.32%**;
- **recall: 86.70%**;
- **F1: 90.81%**.

Los datos máquina-legibles se conservan en `data/lexicon/review/stratified_boundary_evaluation.json`.

## Lectura metodológica

La precisión alta indica que, en esta muestra, la mayoría de las fronteras propuestas son útiles para revisión. Esto permite usar el algoritmo como **acelerador de triage**: un investigador parte de una lista que contiene relativamente pocos falsos comienzos.

El recall es menor. El algoritmo deja artículos sin candidato cuando:

- una línea queda demasiado cerca del encabezado o pie y es excluida por el filtro geométrico;
- el OCR une dos o más artículos en un mismo bloque;
- una continuación de columna altera el margen estimado;
- el comienzo aparece al final de página y continúa en la siguiente;
- el layout OCR mezcla fragmentos de columnas.

La página 133 es el estrato más débil del piloto. Sus 20 TP, 4 FP y 9 FN muestran que la primera página del vocabulario exige reglas especiales para encabezados, arrastres y transiciones. En cambio, la página 177 no produjo falsos positivos en los 54 candidatos, aunque omitió seis inicios.

## Consecuencia de diseño

El extractor actual **no debe sustituirse todavía por un modelo más agresivo**. Su precisión elevada es valiosa. La mejora prioritaria debe aumentar recall sin destruir esa precisión, mediante reglas específicas para:

1. primeras líneas bajo encabezados;
2. comienzos al pie de página;
3. múltiples artículos absorbidos por un candidato;
4. detección explícita de tipografía de inicio de artículo;
5. continuidad página→página y columna→columna.

Cualquier nueva versión del algoritmo debe ejecutarse sobre esta misma muestra y reportar cambios en TP/FP/FN antes de reemplazar `indentation_margin_v0.1`.

## Limitación esencial

Estas métricas son de **ingeniería editorial**, no de calidad lingüística o filológica. Un candidato puede tener una frontera correcta y un OCR muy deficiente. De igual manera, una frontera correctamente recuperada no autoriza a publicar la forma histórica sin cotejo textual posterior.
