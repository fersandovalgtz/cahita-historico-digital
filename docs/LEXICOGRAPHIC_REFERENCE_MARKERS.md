# Marcadores de remisión, anáfora e instrucción editorial

## Propósito

El vocabulario y sus preliminares no pueden modelarse correctamente como una serie uniforme de pares castellano–cahíta. La fuente emplea marcadores que remiten a otros artículos, reutilizan una equivalencia previa o instruyen al lector sobre una corrección. CHD conserva esos marcadores como **datos históricos explícitos** y evita expandirlos silenciosamente.

Este catálogo distingue cuatro funciones que no deben confundirse: remisión lexicográfica, anáfora de equivalencia, anáfora de localización e instrucción de errata.

## `Buſca`

**Función CHD:** remisión lexicográfica explícita.  
**Relación mínima:** `see`.  
**Regla:** conservar literalmente `markerRaw` y `targetRaw`; no sustituir el artículo por el contenido del destino.

El piloto visual de la página digital 165 ya estructura cuatro casos:

- `Orejear. Buſca menear las orejas.`
- `Orina. Buſca meados.`
- `Orinar. Buſca mear.`
- `Oſado ſer. Buſca atrevido.`

La búsqueda sobre el OCR del vocabulario detecta además ocurrencias en distintas zonas alfabéticas —por ejemplo alrededor de *Angustiarse*, *Cueva*, *Culpar*, *Diablo*, *Dilatar*, *Embolver*, *Nuevamente* y *Viento*—, pero esos resultados no se promueven a artículos estructurados hasta cotejar cada página contra el facsímil.

### Modelo

```json
{
  "articleType": "cross_reference",
  "crossReferences": [
    {
      "markerRaw": "Buſca",
      "targetRaw": "meados",
      "relation": "see"
    }
  ]
}
```

## `Lo miſmo`

**Función CHD:** anáfora de equivalencia o reutilización de la respuesta inmediatamente pertinente en el contexto impreso.  
**Relación provisional:** `same_as_previous_equivalent`.  
**Regla:** no copiar automáticamente una forma cahíta al artículo actual. Primero debe determinarse visualmente cuál es el antecedente tipográfico y semántico.

El OCR detecta este patrón en al menos tres zonas del vocabulario, asociado a artículos como *Cobre metal*, *Mina* y *Púlpito*. Estas detecciones son **candidatos de anáfora**, no relaciones editoriales cerradas.

Para producción, el artículo deberá conservar:

```json
{
  "articleType": "anaphoric_reference",
  "transcriptionRaw": "Cobre metal. Lo miſmo.",
  "crossReferences": [
    {
      "markerRaw": "Lo miſmo",
      "targetRaw": null,
      "relation": "same_as_previous_equivalent"
    }
  ]
}
```

El campo `targetRaw` permanecerá nulo hasta que el antecedente haya sido cotejado. Una futura relación estructurada podrá apuntar a un `articleId`, pero esa relación será una decisión editorial derivada y versionada.

## `Ibid.`

**Función CHD:** anáfora de localización dentro de una secuencia de correcciones.  
**Relación:** `same_locator_as_previous`.

La hoja histórica de erratas de la página digital 13 contiene, dentro del bloque `VOCABULARIO`, una secuencia visible:

- `L. P. V. pecado: ...`
- `Ibid. pecador: ...`
- `Ibid. pecar: ...`

Aquí `Ibid.` no se interpreta como equivalente léxico. Reutiliza la localización de la corrección precedente. CHD debe mantener separado este uso de las remisiones `Buſca` y de la anáfora `Lo miſmo`.

## `lee`

**Función CHD:** instrucción histórica de corrección, equivalente a “léase”.  
**Relación:** `read_as` dentro de la capa de erratas, no del artículo lexicográfico ordinario.

La página 13 define y utiliza una lista de correcciones del vocabulario con construcciones del tipo `V. amar: lee, eria`. En CHD se representa mediante `instructionRaw: "lee"`, `erratumRaw`/`guideRaw` y `correctionRaw`; la corrección no sobrescribe el testimonio original.

## `L.` y `V.` en la hoja de erratas

La propia fuente declara:

- `L. littera`
- `V. verbo`

Estas abreviaturas pertenecen a la gramática interna de la fe de erratas. No deben expandirse retrospectivamente en la transcripción diplomática. La expansión declarada por el impreso puede almacenarse como metadato estructurado.

## `vel`

`vel` es un conector latino de alternativa y aparece en distintos contextos del volumen. **No se modela por defecto como remisión lexicográfica.** Cuando aparezca dentro de un artículo del vocabulario deberá cotejarse si coordina formas alternativas, variantes, expresiones o alguna otra estructura. Sólo después se decidirá una relación específica.

## Taxonomía mínima

| Marcador | Clase | Relación CHD | ¿Se expande automáticamente? |
|---|---|---|---|
| `Buſca` | remisión | `see` | no |
| `Lo miſmo` | anáfora de equivalencia | `same_as_previous_equivalent` | no |
| `Ibid.` | anáfora de localización | `same_locator_as_previous` | no |
| `lee` | instrucción de errata | `read_as` | no |
| `L.` / `V.` | abreviaturas declaradas | metadato de errata | no |
| `vel` | conector de alternativa | por determinar según contexto | no |

## Política de autoridad

La presencia de un marcador puede detectarse automáticamente, pero su **alcance** y su **antecedente** son problemas de estructura documental. Un detector de texto puede localizar `Buſca` o `Lo miſmo`; no puede, por ese hecho, establecer de manera segura a qué artículo apunta una remisión o qué forma debe heredarse. Las relaciones de destino se publicarán solamente cuando puedan remontarse a evidencia de página y a una decisión de revisión explícita.

## Estado

Catálogo inicial `machine_corrected_unverified`. Los cuatro casos `Buſca` de p. 165 y los usos `Ibid.` de p. 13 han sido cotejados visualmente de manera IA-asistida. Las detecciones `Lo miſmo` proceden por ahora del OCR y requieren cotejo visual individual antes de promoverse a relaciones entre artículos.
