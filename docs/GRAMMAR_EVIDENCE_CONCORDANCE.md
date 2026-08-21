# Concordancia reproducible de evidencia gramatical

## Alcance

Esta capa convierte los objetos estructurados de `data/grammar/` en una vista tabular y trazable de la evidencia explícita ya registrada: lemas, formas paradigmáticas, partículas, marcadores de formación, cabeceras, formas de inventarios temáticos y ejemplos.

El objetivo es facilitar la navegación **forma / ejemplo ↔ regla ↔ objeto gramatical ↔ página**, sin crear análisis lingüístico nuevo ni reescribir los objetos canónicos.

El generador es:

```bash
python scripts/export_grammar_evidence_concordance.py
```

Por omisión produce en `build/grammar-evidence-concordance/`:

- `chd_grammar_evidence_concordance.jsonl`
- `chd_grammar_evidence_concordance.csv`
- `manifest.json`

## Unidad de salida

Cada fila corresponde a una cadena explícita localizada dentro de un objeto gramatical y conserva:

- identificador del objeto canónico cuando existe;
- clave estable de procedencia cuando el objeto no tiene `id` propio;
- archivo y número de registro de origen;
- tipo de objeto;
- Parte del Arte, cuando está explícita;
- regla o rango de reglas, cuando está explícito;
- páginas digitales e impresas declaradas por el objeto;
- ruta JSON exacta de la evidencia;
- rol de evidencia;
- texto crudo;
- glosa y etiqueta histórica de variedad cuando están explícitamente asociadas en el contexto estructurado;
- estado de revisión y `humanVerified`.

Los roles incluyen, según la estructura de origen: `lemma`, `headword`, `particle`, `formation_marker`, `paradigm_form`, `form`, `item_form`, `numeral_form`, `alternative_form`, `historical_variety_example` y `example`.

## Precisión de página

La concordancia **no inventa localización token a token**. Si un objeto sólo declara un rango o una lista de páginas, cada evidencia hereda ese alcance documental. `pageLocatorKind` distingue:

- `explicit_single_page`;
- `explicit_page_list`;
- `range_endpoints`;
- `not_recorded`.

En particular, `numerals_p178_p180.json` declara un rango global 178–180; sus formas no se asignan artificialmente a una página individual.

## Guardas epistemológicas

El manifiesto declara explícitamente:

- `linguisticIdentityInferred: false`;
- `normalizedFormGenerated: false`;
- `crossObjectLinkingPerformed: false`;
- `tokenPagePrecisionInferred: false`;
- `canonicalGrammarModified: false`.

Dos cadenas iguales en objetos distintos permanecen como dos evidencias distintas. La concordancia no afirma que sean el mismo morfema, lexema o construcción.

## Reproducibilidad

El manifiesto registra archivos canónicos, número de objetos, filas de evidencia, distribución por tipo de objeto y rol, estados de revisión, formatos y hashes SHA-256.

`scripts/validate_grammar_exports.py` ejecuta el exportador dos veces en directorios temporales independientes, exige el mismo conjunto de archivos y bytes idénticos y verifica las guardas de no inferencia.

## Próximas capas

Esta concordancia establece la infraestructura mínima para análisis posteriores. Una futura capa podrá estudiar coincidencias de forma, conectar reglas relacionadas o construir índices por variedad, pero esas operaciones deberán distinguir rigurosamente coincidencia gráfica, relación declarada por la fuente e inferencia lingüística moderna.
