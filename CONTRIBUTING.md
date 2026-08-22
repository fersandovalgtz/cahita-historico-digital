# Contribuir a Cahíta Histórico Digital

Cahíta Histórico Digital (CHD) acepta contribuciones orientadas a mejorar trazabilidad, lectura, estructuración, interoperabilidad, software y documentación. La prioridad no es maximizar el número de cambios, sino conservar **evidencia, autoridad, procedencia e incertidumbre**.

Lea también [`GOVERNANCE.md`](GOVERNANCE.md), [`EDITORIAL_POLICY.md`](EDITORIAL_POLICY.md), [`SCHEMA.md`](SCHEMA.md) y [`SCIENTIFIC_REPOSITORY_STANDARD.md`](SCIENTIFIC_REPOSITORY_STANDARD.md).

## Formas de contribuir

Son especialmente útiles:

- correcciones de lectura contra el mismo testimonio `ALC1737`;
- errores de OCR o transcripción;
- paginación, columnas, spans o continuidades trans-página;
- erratas históricas y bibliografía sobre autoría/transmisión;
- revisión de artículos lexicográficos o reglas gramaticales;
- mejoras de JSON Schema, validadores y QA;
- exportadores o herramientas reproducibles;
- TEI/TEI Lex-0 e interoperabilidad sustentada;
- metadatos FAIR/preservación;
- análisis históricos o diacrónicos en capas separadas.

Use las plantillas de `.github/ISSUE_TEMPLATE/` para reportes nuevos y la plantilla de pull request para cambios de código/datos.

## Regla de autoridad

Una contribución debe identificar qué capa modifica:

1. fuente/metadata;
2. OCR;
3. transcripción;
4. candidato o reconciliación;
5. objeto canónico lexicográfico/gramatical;
6. revisión/procedencia;
7. derivado reproducible;
8. documentación o metadata pública.

No cambie una capa de menor autoridad sólo para hacerla coincidir con una derivada. Si existe una discrepancia, determine primero cuál objeto tiene autoridad según la documentación.

## Correcciones textuales

Toda propuesta debería indicar, cuando sea posible:

- `sourceId` (`ALC1737` u otro testimonio futuro);
- `articleId`, regla u objeto afectado;
- página digital e impresa;
- columna/zona;
- lectura actual;
- lectura propuesta;
- evidencia o justificación;
- persona revisora y alcance, cuando se reclame verificación humana.

Una reimpresión u OCR de control puede apoyar el diagnóstico, pero no sustituye silenciosamente al testimonio primario.

## `humanVerified`

`humanVerified=true` significa revisión humana identificable contra evidencia admisible. **No** significa:

- “pasó CI”;
- “lo revisó una IA”;
- “parece correcto”;
- “coincide con otra edición”;
- “el algoritmo tiene alta confianza”.

En v1.0.0 el conteo permanece en **0**.

## Identidad lingüística y comparaciones modernas

No introduzca equivalencias modernas de yaqui, mayo u otras lenguas como si fueran lecturas de 1737. El rótulo histórico `Cahita` no tiene asignado por CHD un código ISO 639-3 único.

Una propuesta comparativa puede ser valiosa si se modela como capa separada y distingue, por ejemplo:

- semejanza gráfica;
- traducción propuesta;
- posible cognación;
- préstamo;
- continuidad histórica;
- identidad de variedad.

Ninguna de estas relaciones debe promoverse automáticamente a hecho canónico.

## IDs y compatibilidad

Los IDs publicados son contratos de investigación. Si una corrección conserva la identidad del objeto, conserve también el ID y registre procedencia. No recicle un `articleId` para una entidad distinta.

Los cambios incompatibles a schemas o contratos congelados requieren un nuevo freeze/versionado explícito; CI debe impedir deriva silenciosa.

## Derivados

CSV, JSON consolidado, grafos, diagnósticos, concordancias y TEI son productos derivados. Cuando sea posible deben generarse mediante scripts deterministas. No edite manualmente un derivado para ocultar una discrepancia con su fuente canónica.

## Flujo de pull request

1. cree una rama pequeña y temática;
2. documente evidencia y alcance;
3. ejecute validadores locales pertinentes;
4. use `make qa-surface` para cambios de documentación/metadatos;
5. deje que **CHD QA** ejecute la batería completa;
6. no fusione si el head definitivo no está verde;
7. use squash merge para mantener un historial de cambio científico legible cuando corresponda.

Comandos útiles:

```bash
make stats
make qa-surface
make qa
python scripts/validate_v1_release.py
```

## Releases publicadas

El tag `v1.0.0` es inmutable. Los cambios post-release se realizan en `main` y en versiones futuras; no se reescribe retrospectivamente la identidad científica de v1.0.0.

Los DOI se incorporarán sólo cuando un repositorio archivístico los asigne realmente.

## Autoría y crédito

Los roles se registran mediante CRediT en [`CONTRIBUTORS.md`](CONTRIBUTORS.md). Una contribución sustancial debe recibir atribución proporcional y específica. La participación de hablantes o especialistas contemporáneos debe reconocer explícitamente su función y autoridad sin convertir una revisión individual en supuesto consenso comunitario.

## Conducta científica

Las discusiones deben centrarse en evidencia, método y reproducibilidad. Las denominaciones históricas potencialmente problemáticas se describen como lenguaje de la fuente cuando corresponda, no como formulaciones normativas contemporáneas.
