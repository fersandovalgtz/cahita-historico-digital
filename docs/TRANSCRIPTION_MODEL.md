# Modelo de transcripción por página

## Unidad maestra

La unidad básica de la Fase 2 de Cahíta Histórico Digital es la **página digital del testimonio `ALC1737`**. La página digital funciona como ancla técnica estable; cuando existe paginación impresa se añade `sourcePagePrinted` sin sustituir el identificador digital.

La representación maestra de una transcripción es un objeto JSON validable contra `schemas/page-transcription.schema.json`.

Ruta prevista:

```text
data/transcription/pages/ALC1737_pNNN.json
```

La elección de JSON para la capa maestra de trabajo permite conservar texto, cobertura, estado de revisión, incertidumbres y procedencia sin convertir todavía decisiones provisionales en una codificación TEI definitiva.

## Campos esenciales

Cada objeto debe registrar:

- `sourceId`: siempre `ALC1737`;
- `sourcePageDigital`: página 1–182;
- `sourcePagePrinted`: 1–118 cuando corresponda, o `null`;
- `section`: segmento macro del volumen;
- `transcriptionType`: `diplomatic`;
- `coverage`: `full_page` o `excerpt`;
- `text`: transcripción;
- `lineBreakPolicy`: convención utilizada para saltos;
- `reviewStatus`: autoridad editorial actual;
- `humanVerified`: bandera estricta, coherente con `reviewStatus`;
- `uncertainties`: lecturas marcadas para revisión;
- `provenance`: fuente inmediata, agente, método y fecha cuando esté disponible.

## Estados y autoridad

El esquema admite:

- `machine_corrected_unverified`: cotejo o corrección asistida sin revisión humana independiente;
- `editorial_proposal`: reconstrucción o decisión interpretativa propuesta;
- `human_verified`: cotejo humano identificable contra el facsímil;
- `unresolved`: la lectura permanece abierta.

Una restricción del esquema exige que `humanVerified: true` sólo pueda coexistir con `reviewStatus: human_verified`, y viceversa. Así se impide que una etiqueta de revisión humana aparezca por accidente en datos producidos por automatización.

## Cobertura de página

`full_page` significa que la transcripción pretende cubrir todo el texto impreso relevante de la página. No implica que todas las lecturas estén resueltas ni que exista validación humana.

`excerpt` significa que sólo una región o selección de la página ha sido transcrita. Los pilotos deben permanecer como `excerpt` hasta completar la página.

Las cubiertas, hojas materialmente significativas sin texto impreso propio y otros elementos no transcribibles se registran en `data/transcription/status.csv` como `not_applicable_material`, no mediante objetos de transcripción vacíos.

## TXT y otras proyecciones

Los archivos TXT pueden generarse como proyecciones de lectura o utilizarse para pilotos, pero la Fase 2 considera al JSON la representación maestra porque el texto plano no puede expresar por sí solo estado, incertidumbre y procedencia.

Cuando el modelo se estabilice, una fase posterior definirá una proyección TEI/XML. La TEI no se utilizará prematuramente para ocultar incertidumbres del modelo de datos: primero debe demostrarse que las unidades y estados de CHD pueden reconstruirse sin pérdida.

## Manifiesto de estado

`data/transcription/status.csv` contiene una fila por cada una de las 182 páginas digitales y permite calcular cobertura sin recorrer todos los objetos JSON.

Estados iniciales relevantes:

- `pending / unreviewed`: página textual todavía sin transcripción maestra;
- `excerpt / machine_corrected_unverified`: existe sólo un fragmento piloto;
- `not_applicable_material / material_identified`: página material identificada pero sin texto impreso que deba transcribirse.

El manifiesto deberá actualizarse en el mismo commit que incorpore o cambie una transcripción de página.

## Relación con el vocabulario

Los objetos `page-transcription` no sustituyen a las entradas lexicográficas. Una página del vocabulario puede tener transcripción diplomática completa mientras sus artículos permanecen en estado de candidatos o revisión. La cadena de derivación debe conservarse:

```text
página transcrita → límites de artículo revisados → artículo histórico → entrada estructurada
```

Esto impide que la estructura lexicográfica fuerce retrospectivamente la lectura diplomática del impreso.
