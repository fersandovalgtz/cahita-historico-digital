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

## Universo de comparación

La auditoría usa como universo técnico los números **1–373**, correspondiente a la secuencia numerada del Arte hasta su cierre. Para cada número se pregunta únicamente si algún objeto estructurado actual lo reclama de manera explícita mediante `ruleNumberNumeric`, `ruleNumberRaw` o el primer número/rango de `sourceRuleRange`.

Una fila `no_structured_object_claim` significa sólo:

> ningún objeto estructurado actual declara explícitamente cobertura de ese número de regla.

No significa que la regla falte en el impreso, que sea inválida, que esté perdida ni que carezca de contenido. Tampoco autoriza a reconstruirla automáticamente.

## Lectura conservadora de localizadores

El parser evita convertir números de página en números de regla. Por ejemplo, `293; continuation to p.107` sólo reclama la regla 293. Un localizador como `post-373` se conserva como localización no numerada posterior y no se convierte en cobertura de la regla 373.

Los objetos sin localizador explícito de regla se inventarían si fueran asignados por proximidad de página o contenido. Por eso la auditoría los conserva en una lista separada `objectsWithoutExplicitRuleClaim`.

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

La salida permite priorizar con precisión la siguiente expansión de `data/grammar/`: primero pueden atacarse bloques extensos sin objetos estructurados, después huecos internos entre bloques ya representados y, por separado, objetos existentes que aún necesitan un localizador de regla más preciso.

`scripts/validate_grammar_exports.py` ejecuta esta auditoría dos veces en directorios independientes, exige identidad byte-a-byte y comprueba que los conteos de cubiertas/no cubiertas sumen exactamente 373 sin reclamaciones fuera del universo.
