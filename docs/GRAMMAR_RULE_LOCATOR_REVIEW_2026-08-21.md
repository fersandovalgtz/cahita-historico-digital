# Revisión de localizadores de reglas gramaticales — 21 de agosto de 2026

## Propósito

La auditoría inicial de cobertura detectó cinco objetos de `data/grammar/` sin reclamación de regla numerada reconocible. Esta revisión coteja esos cinco casos con las transcripciones de página y con la estructura ya conservada, sin asignar números por proximidad.

El resultado distingue entre **reglas explícitamente representadas dentro de un objeto mixto** y material que debe permanecer legítimamente no numerado o pendiente de una revisión de procedencia más fina.

## Casos revisados

### `ALC1737-par-0001` — permanece sin reclamación numerada

El objeto representa la tabla impresa `CONJUGACION DEL VERBO. MODO INDICATIVO. TIEMPO PRESENTE. Eria amar.` en p.70. La tabla aparece después de la regla 191, pero no lleva número propio.

Además, el `sourceClaim` actual menciona que el verbo no tiene números ni personas morfológicas propias, afirmación que está formulada explícitamente en la regla 189 de p.69, mientras que el objeto declara actualmente p.70 como su única página fuente. Por ello **no se asigna automáticamente 189 ni 191**. El caso requiere una revisión posterior que decida si conviene separar la afirmación general del paradigma o ampliar formalmente su procedencia.

Estado: `remain_without_numbered_rule_claim`.

### `ALC1737-par-0002` — anclado a regla 190

La regla 190 comienza en p.69 y continúa al inicio de p.70. Esa continuación contiene explícitamente la distribución de terminaciones temporales entre Tehuecos, Hiaquis y Mayos que constituye el núcleo comparativo del objeto.

El objeto también incorpora celdas de la tabla paradigmática de pp.70–71. Esas celdas no se convierten por ello en contenido exclusivo de la regla 190. El nuevo campo:

```json
"sourceRuleNumbers": [190]
```

significa únicamente que **existe evidencia explícita de la regla 190 representada dentro del objeto**.

Estado: `explicit_numbered_claim_added`.

### `ALC1737-par-0003` — anclado a reglas 198 y 200; 199 excluida

La p.73 contiene la regla 198, que distribuye `hau` y `amatuc` por denominaciones históricas. A continuación, la regla 199 describe otra formación del optativo mediante `uaua`. La p.74 contiene la regla 200, que contrasta el uso de `na` entre Tehuecos y las demás Naciones.

Las celdas del objeto identificaban ya internamente `regla 198` y `regla 200`. La revisión confirma que el objeto **no representa la regla 199**. Por eso se usa un localizador no contiguo:

```json
"sourceRuleNumbers": [198, 200]
```

y se corrige la nota editorial previa que podía sugerir un rango continuo 198–200.

Estado: `explicit_noncontiguous_numbered_claims_added`.

### `numerals_p178_p180.json` — legítimamente fuera de la secuencia numerada del Arte

El sistema numeral estructurado procede de las pp.178–180, posteriores al vocabulario y fuera de la secuencia de reglas 1–373 del Arte. No debe recibir un número de regla artificial.

Estado: `legitimately_unnumbered_post_arte_material`.

### `ALC1737-conj-0006` — legítimamente `post-373`

El objeto conserva la declaración final sobre `INTERJECCIONES` después de la regla 373 y antes de `FIN DEL ARTE`. Su `sourceRuleRange` ya dice `post-373`; esa localización es informativa precisamente porque **no equivale a la regla 373**.

Estado: `legitimately_unnumbered_post_373_material`.

## Cambio de modelo

La auditoría admite ahora el campo opcional `sourceRuleNumbers`, reservado para números de regla explícitamente demostrados que no puedan representarse honestamente mediante un único número o un rango continuo. El campo debe contener una lista no vacía de enteros sin duplicados.

Su presencia no afirma que todo el objeto pertenezca exclusivamente a esas reglas. Afirma únicamente que el objeto contiene evidencia estructurada explícita de esos números y que esa relación fue documentada.

## Resultado reproducible

Antes de esta revisión, la auditoría registraba **177/373** reglas con reclamación estructurada y **5** objetos sin reclamación numerada. Después de incorporar documentalmente 190, 198 y 200, `CHD QA` produce:

- **180/373** reglas con reclamación estructurada explícita;
- **193** reglas sin reclamación;
- **3** objetos sin reclamación numerada;
- **9** rangos contiguos de hueco;
- **0** reclamaciones fuera del universo 1–373.

La regla **199 permanece sin reclamación**, confirmando que `sourceRuleNumbers: [198, 200]` no se interpreta como rango continuo.

Hashes de la corrida reproducible:

- cobertura CSV: `6e1ac4b2019c974ee75efd4305ace0b36409a854c00f8040e241253f586c7c3d`;
- cobertura JSONL: `a3e33de2b9464c153b122b33d751bf5cf03d505fc7f3f8ef57675ddda3bc4829`;
- rangos de hueco JSON: `e88ea7fc3c4857981216f3125403310ca4a4877f9e00405082ca7102956424ed`;
- manifiesto: `0f98daf8c2c294f72b2fe406ebc71a8323c0faa64892976ee15fd6799ab66a24`.

## Autoridad

Todos los objetos conservan `humanVerified: false`. Esta revisión corrige metadatos de relación entre objetos estructurados y números impresos; no convierte las transcripciones ni los paradigmas en validación filológica humana y no completa reglas ausentes mediante inferencia.
