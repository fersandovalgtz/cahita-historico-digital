# Piloto lexicográfico ALC1737 — página digital 134

## Propósito

Este piloto comprueba el flujo mínimo de Cahíta Histórico Digital desde el facsímil hasta registros estructurados validables. **No constituye todavía una edición filológica cerrada ni una muestra de validación humana independiente.**

La página digital 134 pertenece al inicio del vocabulario castellano–cahíta. Se seleccionaron doce entradas cuya lectura resulta suficientemente clara en el facsímil para ensayar el modelo de datos sin forzar las lecturas más dudosas.

## Cadena de evidencia

El piloto conserva tres niveles distintos:

1. la imagen del testimonio, autoridad documental;
2. un extracto diplomático IA-asistido en `data/diplomatic/pilot/ALC1737_p134_excerpt.txt`;
3. doce registros estructurados en `data/lexicon/pilot/ALC1737_p134_entries.jsonl`.

Los doce registros están marcados `machine_corrected_unverified`. Ninguno usa `human_verified`.

## Entradas del piloto

| ID | Entrada castellana histórica | Forma cahíta histórica |
|---|---|---|
| `ALC1737-lex-000001` | Abofetear | Achonſu |
| `ALC1737-lex-000002` | Abofeteador | Iorechoname |
| `ALC1737-lex-000003` | Abogacia | Nocria |
| `ALC1737-lex-000004` | Abollar | Hepeſte |
| `ALC1737-lex-000005` | Aborrecer | Caeria |
| `ALC1737-lex-000006` | Aborrecimiento | Caeriari |
| `ALC1737-lex-000007` | Abortadura tal | Tomaherete |
| `ALC1737-lex-000008` | Abraſarſe de calor interior | Tatare |
| `ALC1737-lex-000009` | Abrigado lugar | Cabecapo |
| `ALC1737-lex-000010` | Abrigar à otro con ropa | Senu bintua |
| `ALC1737-lex-000011` | Abrojo | Huichacame |
| `ALC1737-lex-000012` | Abſtenerſe | Abiore |

Las formas de esta tabla se registran como lectura histórica del piloto, no como equivalentes modernos de yaqui, mayo u otra variedad contemporánea.

## Validación estructural

Los doce objetos fueron validados localmente, uno por uno, contra `schemas/lexical-entry.schema.json` mediante `scripts/validate_jsonl.py`:

```text
VALID: 12 record(s)
```

La validación JSON Schema verifica estructura y tipos de datos; **no verifica que una lectura sea filológicamente correcta**.

## Extracción de disposición a dos columnas

El vocabulario impreso utiliza dos columnas y el facsímil alterna la posición horizontal de páginas recto/verso. Por ello se añadió `scripts/extract_vocab_layout.py`, que utiliza `pdftotext -bbox-layout`, infiere por página dos grupos de comienzos de línea y conserva las líneas que parecen fusionar ambas columnas como `other`.

Una ejecución sobre las páginas digitales 133–177 produjo localmente:

- **3,899** líneas OCR con coordenadas;
- 1,731 clasificadas en columna izquierda;
- 2,107 en columna derecha;
- 61 líneas `other`, principalmente fusiones OCR entre columnas;
- SHA-256 del JSONL derivado completo: `9b5eb47fc7d93a63e8345a33da844863d8228fe7149a303ee35a1c2c00cb1871`.

Este resultado es una **capa de evidencia OCR/layout**, no un recuento de entradas del vocabulario. La segmentación de artículos deberá ser una actividad posterior y conservar estos límites brutos para auditoría.

## Siguiente umbral científico

Antes de promover cientos o miles de registros, CHD debe medir el error del OCR en una muestra estratificada, estabilizar reglas de segmentación de artículos, tratar remisiones (`Busca`), abreviaturas y múltiples equivalentes, y someter al menos una muestra a revisión humana independiente.
