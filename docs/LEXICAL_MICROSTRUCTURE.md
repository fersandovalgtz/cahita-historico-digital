# Microestructura del vocabulario histórico

## Por qué CHD distingue artículo y entrada léxica

El vocabulario de `ALC1737` no puede reducirse de manera fiable a una tabla simple `castellano → cahíta`. Las páginas muestran artículos con una o varias formas, expresiones castellanas complejas, explicaciones, continuaciones, remisiones internas como `Busca`, variantes y materiales cuya función sólo puede determinarse después de cotejar la página.

Por ello CHD introduce una unidad intermedia: **`historical lexical article`**. Esta unidad representa la estructura del artículo tal como aparece en la fuente antes de abstraer un lema moderno, una relación semántica o una entidad léxica normalizada.

El contrato se define en `schemas/lexical-article.schema.json`.

## Niveles

```text
candidato geométrico
  ↓ revisión de frontera
artículo histórico
  ↓ análisis de microestructura
entrada(s) lexicográfica(s) derivada(s)
  ↓ normalización / comparación / TEI Lex-0
```

La distinción evita dos errores frecuentes: contar automáticamente cada agrupación OCR como entrada y obligar a artículos complejos a encajar en una pareja bilingüe única.

## Campos del artículo histórico

### Identificación y localización

- `articleId`: identificador interno estable del artículo ya promovido;
- `sourcePageDigital` y `column`;
- continuidad desde/hacia página siguiente cuando exista;
- `derivedFromCandidates`: candidatos computacionales de los que procede.

### Tipo de artículo

`articleType` admite:

- `equivalence`: artículo que presenta una guía castellana y una o más formas cahítas;
- `cross_reference`: remisión interna, por ejemplo con marcador histórico `Busca`;
- `mixed`: combina equivalencia, explicación, remisión u otros componentes;
- `descriptive`: artículo cuyo contenido funciona principalmente como explicación o descripción;
- `unresolved`: la microestructura todavía no puede determinarse con seguridad.

El tipo describe la **forma documental del artículo**, no una clasificación lexicológica universal.

### Guía castellana

`spanishGuideRaw` conserva literalmente la frase guía histórica. No se obliga a que sea una sola palabra ni se denomina automáticamente “lema”, porque la fuente utiliza expresiones y construcciones que pueden exceder el modelo lexicográfico moderno de lema aislado.

La eventual normalización castellana pertenecerá a una capa derivada.

### Formas cahítas

`cahitaFormsRaw` es una lista, no un campo singular. Cada forma conserva:

- `formRaw`;
- un posible calificador tal como aparece en la fuente;
- `historicalVariety` sólo cuando la fuente atribuye explícitamente la forma a `Hiaqui`, `Mayo`, `Thehueco` u otra denominación histórica.

La ausencia de etiqueta se codifica como `unspecified`; no se infiere una variedad a partir de conocimiento contemporáneo.

### Remisiones

`crossReferences` conserva por separado:

- `markerRaw`: marcador histórico visible, por ejemplo `Busca`;
- `targetRaw`: destino escrito en la fuente;
- una relación estructural mínima (`see`, `same_as` u `other_unresolved`) cuando pueda determinarse sin forzar interpretación.

No se resuelve automáticamente el destino contra un identificador moderno. Esa vinculación será una capa posterior y deberá registrar si el objetivo fue encontrado, ambiguo o inexistente.

### Abreviaturas y notas

`abbreviationsRaw` preserva abreviaturas que formen parte del artículo; `notesRaw` permite conservar explicaciones o fragmentos que no sean estrictamente formas equivalentes. No se expanden silenciosamente abreviaturas dudosas.

## Relación con `lexical-entry.schema.json`

El esquema existente de `lexical-entry` se mantiene por ahora para los **12 registros piloto simples** de la página 134. No será el formato maestro del vocabulario de producción hasta demostrar que la microestructura del artículo puede proyectarse sin pérdida.

La política vigente es:

1. reconstruir y revisar el artículo histórico;
2. conservar su transcripción completa;
3. estructurar su microestructura con `lexical-article`;
4. sólo después generar una o más entradas lexicográficas derivadas cuando sea metodológicamente justificable.

Una misma unidad histórica podría producir más de una entidad derivada, o ninguna si permanece irresuelta.

## Ejemplos de fenómenos que motivan el modelo

En las páginas del vocabulario se observan repetidamente:

- artículos distribuidos en varias líneas;
- múltiples elementos separados por signos o abreviaturas;
- fórmulas `Busca ...` que remiten a otra voz;
- expresiones castellanas que funcionan como frase guía;
- continuaciones entre páginas;
- series de nombres para animales, plantas u objetos;
- formas históricas que no deben atribuirse a una variedad contemporánea sin evidencia explícita de la fuente.

Estos fenómenos justifican un modelo de artículo primero y una abstracción léxica después.

## Autoridad

Un objeto `lexical-article` puede ser `machine_corrected_unverified`, `editorial_proposal`, `human_verified` o `unresolved`. El esquema impide combinar `humanVerified: true` con otro estado.

La microestructura no transforma una lectura IA-asistida en una lectura humana: **estructurar y verificar son actividades distintas**.
