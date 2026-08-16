# Testimonios y ediciones de control

## Propósito

Cahíta Histórico Digital distingue estrictamente entre el **testimonio primario de trabajo**, ejemplares independientes de la misma edición y materiales posteriores utilizados para control textual, historia de transmisión o comparación editorial.

`ALC1737` continúa siendo la autoridad para la transcripción del ejemplar de trabajo. Ningún testimonio o reimpresión se utiliza para sobrescribir silenciosamente una lectura: las coincidencias y divergencias deben vivir como colación explícita.

## BNF1737-REPORTED — ejemplar independiente de la edición de 1737

La bibliografía especializada aporta una pista especialmente importante para el control textual. Rosío Molina Landeros declara que el ejemplar de la edición de **1737** utilizado para su estudio del vocabulario cahíta pertenece a la **Réserve des Livres rares de la Bibliothèque nationale de France**. También distingue expresamente esa edición de la reimpresión posterior de Buelna.

CHD registra esta noticia como `BNF1737-REPORTED` en `data/source/control/bnf1737_reported_witness.json`.

### Estado de autoridad

Este registro significa que existe **evidencia académica publicada de un ejemplar independiente de la misma edición de 1737**. Todavía no significa que CHD haya:

- verificado directamente su ficha catalográfica específica;
- localizado un facsímil digital abierto del ejemplar;
- descargado o ingerido imágenes/PDF;
- establecido su signatura definitiva;
- realizado colación página por página.

Por ello su estado es `reported_witness_requires_direct_verification`.

### Valor científico potencial

Si se obtiene acceso directo, este ejemplar será prioritario para:

- comprobar la discontinuidad F→H entre digitales 157–158 de `ALC1737`;
- comprobar la anomalía `Lucer-` entre digitales 161–162;
- cotejar lecturas `[ileg.]` y pasajes dañados;
- distinguir posibles defectos del ejemplar de trabajo frente a características de la edición;
- estudiar variantes de estado de impresión o diferencias de ejemplar.

Un ejemplar independiente de 1737 tendrá mayor peso para control textual que una reimpresión del siglo XIX, aunque `ALC1737` seguirá conservándose como testimonio autónomo y no será reescrito retrospectivamente.

## BUE1890 — reimpresión de Eustaquio Buelna

Se registra `BUE1890` como una **edición histórica de control**, no como segundo ejemplar de la edición de 1737.

Datos bibliográficos básicos:

- título: *Arte de la lengua cahita*;
- editor: Eustaquio Buelna;
- México: Imprenta del Gobierno Federal;
- año: 1890;
- extensión catalográfica: 264 páginas en diversos registros digitalizados;
- existen varios ejemplares digitalizados independientes en Google Books y un registro asociado a Internet Archive/Open Library.

La reimpresión incorpora intervención editorial, notas y materiales adicionales. Por tanto, sus lecturas deben tratarse como evidencia de **transmisión editorial posterior**, no como reproducción neutral del testimonio `ALC1737`.

## Primer uso de control: apertura del vocabulario

El comienzo del vocabulario de `ALC1737` muestra visualmente, bajo el encabezado alfabético `A.`:

`A. denotando la persona que padece.`

seguido por:

`A. Aa.`

La geometría del OCR v0.2 produjo dos candidatos internos problemáticos (`p133-L-001` y `p133-L-002`) en lugar de detectar el comienzo de esa unidad.

La reimpresión de 1890 conserva la misma microestructura como una sola entrada: `A, denotando la persona que padece. A, Aa.`. Esta coincidencia se utiliza únicamente como **corroboración secundaria** de una lectura que ya es visible en el facsímil de 1737.

La decisión editorial resultante mantiene ambos niveles de evidencia separados:

1. autoridad primaria: imagen/facsímil de `ALC1737`;
2. control posterior: `BUE1890` como reimpresión concordante.

## Política de colación

Toda comparación futura entre `ALC1737` y una edición/testimonio de control deberá registrar al menos:

- unidad y página en `ALC1737`;
- fuente de control e identificador;
- lectura en cada fuente;
- tipo de relación (`agreement`, `orthographic_variant`, `editorial_normalization`, `substantive_variant`, `omission`, `addition`, `uncertain`);
- decisión editorial;
- estado de autoridad;
- si existe o no revisión humana.

## Próximo frente de control textual

1. identificar directamente en BnF la signatura/ficha del ejemplar 1737 referido por Molina Landeros;
2. determinar si existe reproducción digital accesible o posibilidad de solicitar imágenes;
3. si se obtiene, ingerirlo bajo un nuevo identificador de testimonio con manifiesto y hashes propios;
4. realizar primero una colación dirigida de p157→158, p161→162 y lecturas `[ileg.]`;
5. conservar `BUE1890` para historia de transmisión y corroboración secundaria.
