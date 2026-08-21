# Auditoría reproducible de cobertura de reglas gramaticales

## Propósito

Esta capa mide qué números de regla del *Arte* están explícitamente representados por los objetos actuales de `data/grammar/`. Su función es orientar la expansión de la estructuración gramatical y hacer visibles los huecos del **dataset**, no diagnosticar ausencias del testimonio histórico.

El generador es:

```bash
python scripts/export_grammar_rule_coverage.py
```

Por omisión produce en `build/grammar-rule-coverage/`:

- `chd_grammar_rule_coverage.jsonl`;
- `chd_grammar_rule_coverage.csv`;
- `chd_grammar_rule_gap_ranges.json`;
- `manifest.json`.

## Estado reproducible al 21 de agosto de 2026

La primera ejecución integrada en `CHD QA` establece, para el universo técnico de reglas **1–373**:

- **177 / 373 reglas** con al menos una reclamación estructurada explícita;
- **196 / 373 reglas** sin reclamación estructurada explícita;
- **6 rangos contiguos** sin reclamación: **1–45**, **61–206**, **235–236**, **285**, **292** y **294**;
- **5 objetos gramaticales** existentes sin localizador de regla numerada explícito;
- **0** reclamaciones fuera del universo 1–373.

Los bloques con reclamación explícita son: **46–60**, **207–234**, **237–284**, **286–291**, **293**, **295–373**. Esto describe la cobertura actual de los objetos, no una edición crítica de la numeración histórica.

La salida fue idéntica byte a byte en dos corridas independientes. En ese estado del repositorio:

- `chd_grammar_rule_coverage.csv`: SHA-256 `cb53019d316c91dec220d2a2230f48d02297ec341f7a70ceb2074324a10ef887`;
- `chd_grammar_rule_coverage.jsonl`: SHA-256 `f77acccd78e75f46fdc054cb13ea7d46db3939f76a820249933b78cbc47b31d7`;
- `chd_grammar_rule_gap_ranges.json`: SHA-256 `1cb499d51ebfe379aa417ea88381181aefbfca65a5a613f2d61a9ea2abec4455`;
- `manifest.json`: SHA-256 `1ba78cc12307a879da09187bdc608170be5fd03741847d358d56691d05bea4b6`.

Estos hashes corresponden a ese estado concreto y deben regenerarse cuando cambien los objetos canónicos.

## Universo de comparación

La auditoría usa como universo técnico los números **1–373**, correspondiente a la secuencia numerada del Arte hasta su cierre. Para cada número se pregunta únicamente si algún objeto estructurado actual lo reclama de manera explícita mediante `ruleNumberNumeric`, `ruleNumberRaw` o el primer número/rango de `sourceRuleRange`.

Una fila `no_structured_object_claim` significa sólo:

> ningún objeto estructurado actual declara explícitamente cobertura de ese número de regla.

No significa que la regla falte en el impreso, que sea inválida, que esté perdida ni que carezca de contenido. Tampoco autoriza a reconstruirla automáticamente.

El rango **61–206** requiere especial cautela: no debe interpretarse como vacío absoluto de trabajo gramatical. El repositorio ya contiene, por ejemplo, paradigmas estructurados en páginas posteriores a la regla 60 que todavía no llevan un anclaje explícito a número de regla. Esos objetos forman parte de los cinco registros separados como `objectsWithoutExplicitRuleClaim` y deben cotejarse antes de cualquier asignación numérica.

## Lectura conservadora de localizadores

El parser evita convertir números de página en números de regla. Por ejemplo, `293; continuation to p.107` sólo reclama la regla 293. Un localizador como `post-373` se conserva como localización no numerada posterior y no se convierte en cobertura de la regla 373.

Los objetos sin localizador explícito de regla se inventarían si fueran asignados por proximidad de página o contenido. Por eso la auditoría los conserva en una lista separada `objectsWithoutExplicitRuleClaim`.

El caso **294** también se conserva como hueco técnico: la estructuración actual registra la regla 293 y después 295, pero esta auditoría no decide si 294 fue omitida tipográficamente, absorbida por otra unidad o simplemente no estructurada. Esa cuestión requiere volver al testimonio.

## Unidad de salida

Cada una de las 373 filas conserva:

- número de regla;
- estado `structured_claim` o `no_structured_object_claim`;
- número de objetos que la reclaman;
- identificadores y tipos de esos objetos;
- archivos canónicos de procedencia;
- páginas digitales e impresas declaradas por los objetos;
- estados de revisión;
- detalle de cada reclamación y su localizador bruto.

El archivo de huecos agrupa rangos contiguos sin reclamación estructurada y lista también objetos gramaticales que carecen de localizador de regla explícito.

## Guardas epistemológicas

El manifiesto fija:

- `sourceRuleExistenceInferred: false`;
- `ruleContentInferred: false`;
- `implicitCoverageInferred: false`;
- `canonicalGrammarModified: false`.

La auditoría no asigna una regla por semejanza temática, página cercana, orden del archivo ni conocimiento lingüístico externo.

## Uso editorial

La salida permite priorizar con precisión la siguiente expansión de `data/grammar/`. El orden recomendado es:

1. cotejar los **5 objetos ya existentes sin localizador explícito**, para separar los que puedan anclarse directamente de los que son legítimamente no numerados;
2. estructurar el bloque temprano **1–45** desde la transcripción y el facsímil;
3. abordar progresivamente **61–206**, descontando sólo aquello que pueda vincularse documentalmente a objetos ya existentes;
4. resolver de manera puntual los huecos internos **235–236, 285, 292 y 294** contra el testimonio;
5. regenerar la auditoría después de cada lote para medir avance sin llevar conteos manuales paralelos.

`scripts/validate_grammar_exports.py` ejecuta esta auditoría dos veces en directorios independientes, exige identidad byte-a-byte y comprueba que los conteos de cubiertas/no cubiertas sumen exactamente 373 sin reclamaciones fuera del universo.
