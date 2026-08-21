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

Después de la revisión documental de los cinco objetos que inicialmente no producían una reclamación numerada, `CHD QA` establece para el universo técnico de reglas **1–373**:

- **180 / 373 reglas** con al menos una reclamación estructurada explícita;
- **193 / 373 reglas** sin reclamación estructurada explícita;
- **9 rangos contiguos** sin reclamación: **1–45**, **61–189**, **191–197**, **199**, **201–206**, **235–236**, **285**, **292** y **294**;
- **3 objetos gramaticales** sin reclamación de regla numerada;
- **0** reclamaciones fuera del universo 1–373.

Los bloques y puntos actualmente cubiertos son: **46–60**, **190**, **198**, **200**, **207–234**, **237–284**, **286–291**, **293** y **295–373**. Esto describe la cobertura actual de los objetos, no una edición crítica de la numeración histórica.

La salida fue idéntica byte a byte en dos corridas independientes. En ese estado del repositorio:

- `chd_grammar_rule_coverage.csv`: SHA-256 `6e1ac4b2019c974ee75efd4305ace0b36409a854c00f8040e241253f586c7c3d`;
- `chd_grammar_rule_coverage.jsonl`: SHA-256 `a3e33de2b9464c153b122b33d751bf5cf03d505fc7f3f8ef57675ddda3bc4829`;
- `chd_grammar_rule_gap_ranges.json`: SHA-256 `e88ea7fc3c4857981216f3125403310ca4a4877f9e00405082ca7102956424ed`;
- `manifest.json`: SHA-256 `0f98daf8c2c294f72b2fe406ebc71a8323c0faa64892976ee15fd6799ab66a24`.

Estos hashes corresponden a ese estado concreto y deben regenerarse cuando cambien los objetos canónicos.

## Universo de comparación

La auditoría usa como universo técnico los números **1–373**, correspondiente a la secuencia numerada del Arte hasta su cierre. Para cada número se pregunta únicamente si algún objeto estructurado actual lo reclama de manera explícita mediante `sourceRuleNumbers`, `ruleNumberNumeric`, `ruleNumberRaw` o el primer número/rango de `sourceRuleRange`.

Una fila `no_structured_object_claim` significa sólo:

> ningún objeto estructurado actual declara explícitamente cobertura de ese número de regla.

No significa que la regla falte en el impreso, que sea inválida, que esté perdida ni que carezca de contenido. Tampoco autoriza a reconstruirla automáticamente.

La revisión de localizadores demostró por qué esta distinción importa. `ALC1737-par-0002` contiene evidencia explícita de la regla **190** además de celdas paradigmáticas no numeradas; `ALC1737-par-0003` contiene evidencia de las reglas **198 y 200**, pero **no** de la 199. La auditoría admite por ello `sourceRuleNumbers` como lista explícita no contigua y no convierte `[198,200]` en el rango 198–200.

## Lectura conservadora de localizadores

El parser evita convertir números de página en números de regla. Por ejemplo, `293; continuation to p.107` sólo reclama la regla 293. Un localizador como `post-373` se conserva como localización no numerada posterior y no se convierte en cobertura de la regla 373.

Los tres objetos que no producen actualmente una reclamación numerada tienen situaciones distintas:

- `ALC1737-par-0001`: paradigma impreso sin número propio; requiere revisar por separado una afirmación de su `sourceClaim` que remite al contexto de la regla 189;
- `numerals_p178_p180.json`: material posterior al vocabulario y fuera de la secuencia numerada del Arte;
- `ALC1737-conj-0006`: cierre de interjecciones explícitamente localizado como `post-373`.

Por tanto, `objectsWithoutExplicitRuleClaim` no debe traducirse automáticamente como “objetos mal localizados”: dos de los tres son legítimamente no numerados.

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

El archivo de huecos agrupa rangos contiguos sin reclamación estructurada y lista también objetos gramaticales que no producen una reclamación numerada explícita.

## Guardas epistemológicas

El manifiesto fija:

- `sourceRuleExistenceInferred: false`;
- `ruleContentInferred: false`;
- `implicitCoverageInferred: false`;
- `canonicalGrammarModified: false`.

La auditoría no asigna una regla por semejanza temática, página cercana, orden del archivo ni conocimiento lingüístico externo.

## Uso editorial

La salida permite priorizar con precisión la siguiente expansión de `data/grammar/`. El orden recomendado es:

1. mantener separado `ALC1737-par-0001` hasta resolver su mezcla de paradigma p.70 y afirmación general asociada al contexto de la regla 189;
2. estructurar de manera continua el bloque **189–206**, para el que existen transcripciones completas en pp.69–76, respetando que 190, 198 y 200 ya poseen reclamaciones adicionales desde paradigmas;
3. estructurar el bloque temprano **1–45** desde la transcripción y el facsímil;
4. abordar progresivamente **61–188**, ya sin confundir los paradigmas cotejados con huecos absolutos;
5. resolver de manera puntual los huecos internos **235–236, 285, 292 y 294** contra el testimonio;
6. regenerar la auditoría después de cada lote para medir avance sin llevar conteos manuales paralelos.

`scripts/validate_grammar_exports.py` ejecuta esta auditoría dos veces en directorios independientes, exige identidad byte-a-byte y comprueba que los conteos de cubiertas/no cubiertas sumen exactamente 373 sin reclamaciones fuera del universo.
