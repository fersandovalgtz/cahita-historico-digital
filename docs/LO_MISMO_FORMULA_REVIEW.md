# Revisión de la fórmula histórica `Lo miſmo`

Actualización: 21 de agosto de 2026.

## Resultado

El corpus canónico de `ALC1737` contiene **14 artículos** con **14 ocurrencias** de la fórmula superficial `Lo miſmo`. La detección se realiza exclusivamente sobre `transcriptionRaw` tras normalización técnica de Unicode y `ſ/s` y no resuelve por sí misma la función de la fórmula.

La revisión conjunta de las 14 ocurrencias obliga a retirar una premisa anterior: **`Lo miſmo` no debe modelarse automáticamente como una remisión anafórica al artículo precedente**. En contextos como `Bronce. Lo miſmo.`, `Lobo. Lo miſmo.`, `Mina. Lo miſmo.` o `Pulpito. Lo miſmo.`, la secuencia local no proporciona un antecedente léxico anterior defendible. Por ello, la fórmula se conserva como **instrucción metalingüística histórica de función exacta aún no inferida**.

Esta decisión es deliberadamente más conservadora que interpretar `Lo miſmo` como “misma forma”, préstamo, equivalencia semántica o remisión. Esas lecturas pueden formularse como hipótesis filológicas futuras, pero no se incorporan automáticamente a los datos canónicos.

## Corrección de `Azero`

`ALC1737-art-000174` había sido la única excepción: `Azero. Lo miſmo.` estaba codificado como `cross_reference` hacia `Azedo tener el eſtomago`. La revisión corpus-wide muestra que esa resolución no era metodológicamente sostenible como regla de estructura. Se retira, por tanto, la arista y el artículo vuelve a `unresolved`, conservando íntegramente la fórmula impresa.

La consecuencia estructural es clara: el inventario de remisiones canónicas pasa de 151 referencias mixtas a **150 remisiones `Buſca`**. Las 90 remisiones `Buſca` estrictamente `not_located`, sus 90 revisiones explícitas, las 60 aristas estrictas y las 40 aristas editoriales permanecen sin cambios.

## Capa de revisión

`data/lexicon/review/lo_mismo_source_review_2026-08-21.jsonl` contiene una revisión explícita para cada una de las 14 ocurrencias. Cada registro separa:

- confirmación de la ocurrencia histórica;
- interpretación de la función;
- posible anáfora al artículo anterior;
- alcance referencial;
- posible forma de lengua meta;
- posible préstamo;
- equivalencia semántica;
- evidencia y procedencia.

En el estado actual las 14 ocurrencias tienen `decisionStatus=source_confirms_formula_occurrence` e `interpretationStatus=function_unresolved`. Ningún registro infiere alcance, forma cahíta, préstamo o equivalencia semántica y ninguno tiene `humanVerified=true`.

## Ejemplos discriminantes

La secuencia `Bruñidor ... / Bronce. Lo miſmo. / Bronco ...` no permite resolver `Bronce` hacia `Bruñidor`. De forma semejante, `Lobanillo ... / Lobo. Lo miſmo. / Loco ...`, `Mierda ... / Mina. Lo miſmo. / Mitad ...` y `Pulga ... / Pulpito. Lo miſmo. / Punzar ...` muestran que la proximidad lineal del artículo anterior no constituye una política general de resolución.

`Noez, y nogal. Lo miſmo.` ofrece además una prueba útil de separación de mecanismos, porque el mismo vocabulario contiene de manera independiente `Noez. Buſca nogal.`. La fórmula `Lo miſmo` no debe colapsarse con `Buſca`.

## Guarda epistemológica

**Confirmar que la fórmula está impresa no equivale a saber qué relación lexicográfica codifica. `Lo miſmo` no autoriza por sí solo a copiar la guía castellana como forma cahíta, afirmar un préstamo, crear una arista de remisión ni declarar equivalencia semántica. La capa actual es AI-assisted y mantiene `humanVerified=false`.**
