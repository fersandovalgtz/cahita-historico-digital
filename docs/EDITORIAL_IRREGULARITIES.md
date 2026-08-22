# Derivado de irregularidades editoriales y materiales

## Propósito

Esta capa post-v1 formaliza como inventario reproducible las irregularidades editoriales, de numeración, estructura material y discrepancias OCR/facsímil ya documentadas en las capas canónicas de Cahíta Histórico Digital. No corrige retrospectivamente el impreso de 1737, no renumera reglas y no altera la release inmutable `v1.0.0`.

El objetivo es que anomalías hasta ahora dispersas entre transcripciones, metadatos gramaticales y notas de secciones tengan identificadores estables, procedencia explícita y una exportación determinista apta para cita, auditoría y análisis posterior.

## Alcance actual

El derivado contiene **9 irregularidades documentadas** en cinco clases:

- `structural_self_description_conflict`: 1 caso, la autodescripción `obra tripartita` frente a la declaración de `quatro partes`;
- `printed_number_omission`: 3 casos, reglas 127, 178 y 294;
- `printed_number_repetition`: 1 caso, duplicación material de 129;
- `intra_page_section_boundary`: 2 casos, fronteras II→III en la página digital 69 y III→IV en la 105;
- `ocr_facsimile_disagreement`: 2 casos, OCR 241 frente a lectura visual 242 en p.89 y repetición OCR 281 frente a lectura visual 282 en p.102.

Estas nueve unidades son un inventario de irregularidades **ya comprobadas en las capas canónicas actuales**. No se presenta como censo universal de todos los rasgos tipográficos posibles del impreso.

## Fuentes canónicas

El generador `scripts/export_editorial_irregularities.py` exige y recorre las siguientes evidencias:

- `data/grammar/metadata/rule_numbering_closure.json`;
- `data/grammar/metadata/rule_numbering_anomalies_p052.json`;
- `data/grammar/metadata/rule_numbering_anomalies_p066.json`;
- `data/grammar/metadata/rule_numbering_anomalies_p107.json`;
- `data/source/alc1737/sections.json`;
- transcripciones canónicas de las páginas digitales 11, 15, 89 y 102.

El exportador falla si desaparece o cambia de forma incompatible cualquiera de las evidencias esperadas. Esto evita que el derivado continúe produciendo una apariencia de estabilidad después de una modificación sustantiva de las capas fuente.

## Productos

```bash
python scripts/export_editorial_irregularities.py \
  --out-dir build/editorial-irregularities
```

produce:

- `chd_editorial_irregularities.jsonl`: inventario machine-readable completo;
- `chd_editorial_irregularities.csv`: vista tabular para revisión y análisis;
- `manifest.json`: versión, ancla de procedencia, conteos, páginas implicadas, inputs canónicos y checksums SHA-256.

Cada registro posee un ID estable `ALC1737-irreg-*`, páginas digitales/impresas, archivos de evidencia, fragmentos fuente breves, explicación de la anomalía, tratamiento editorial explícito y estado de autoridad.

## Política editorial y de autoridad

El derivado mantiene de forma obligatoria:

- `sourceDescriptionPreserved: true`;
- `silentNormalizationPerformed: false`;
- `silentRenumberingPerformed: false`;
- `modernLinguisticInferencePerformed: false`;
- `humanVerified: false` para todos los registros mientras no exista cotejo humano identificable.

Una omisión numérica del impreso no autoriza a crear una regla inexistente. Una duplicación no autoriza a renumerar unidades vecinas. Una discrepancia OCR/facsímil conserva el OCR como procedencia de una capa secundaria y la lectura visual como la lectura editorialmente observada, sin borrar el desacuerdo.

## Casos estructurales

La obra se autodescribe en los preliminares como `obra tripartita`, pero el PROHEMIO declara `las quatro partes, en que se ha de dividir esta obra`. El derivado conserva ambas afirmaciones como un conflicto de autodescripción histórica, sin decidir que una deba sobrescribir a la otra.

Las páginas digitales 69 y 105 contienen fronteras internas de parte. Por ello, el inventario documenta que una misma página física/digital puede pertenecer materialmente a dos secciones consecutivas; este hecho no debe simplificarse asignando toda la página a una sola parte.

## Numeración de reglas

La secuencia nominal 1–373 presenta tres números omitidos materialmente —127, 178 y 294— y una duplicación material de 129. CHD mantiene el hueco documental y las dos unidades 129 como entidades separadas. El derivado registra este hecho, pero no crea reglas ficticias ni cambia la numeración histórica.

## Discrepancias OCR/facsímil

Dos desacuerdos de numeración ya identificados se incorporan como irregularidades de capa:

- en la página digital 89, el OCR repite 241, mientras el cotejo visual sustenta 242 bajo `SEGUNDO MODO DE INFINITIVO`;
- en la página digital 102, el OCR repite 281, mientras el cotejo visual sustenta 282.

Estas unidades son especialmente útiles para demostrar que el OCR se utiliza como ayuda de navegación y comparación, no como autoridad textual.

## QA y determinismo

```bash
make irregularities-qa
```

realiza dos construcciones independientes y exige igualdad byte a byte de JSONL, CSV y manifiesto. Además:

- valida cada registro contra `schemas/editorial-irregularity.schema.json`;
- exige exactamente las nueve irregularidades actualmente documentadas;
- comprueba las omisiones 127/178/294 y la repetición 129;
- comprueba las fronteras 69/105;
- comprueba los pares OCR/facsímil 241→242 y 281→282;
- impide normalización o renumeración silenciosa;
- impide elevar `humanVerified`.

El workflow `CHD Editorial Irregularities` ejecuta la misma validación en GitHub Actions y publica el derivado validado como artifact temporal.

## Relación con Fase 4

Este producto cierra el pendiente de Fase 4 relativo a **formalizar irregularidades editoriales, duplicaciones, omisiones, contradicciones estructurales y fronteras materiales como derivado reproducible propio**.

Después de esta capa, Fase 4 queda concentrada en un trabajo distinto: establecer enlaces explícitos entre reglas/paradigmas y observaciones históricas de variedad únicamente cuando la fuente lo sustente, además de colaciones filológicas puntuales que puedan mejorar lecturas inciertas sin cambiar el estado `humanVerified=0`.
