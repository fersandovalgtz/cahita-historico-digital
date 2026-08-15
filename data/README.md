# Datos

Este directorio contendrá las capas de datos derivadas de las fuentes de Cahíta Histórico Digital.

## Convención general

Cada fuente tendrá un identificador estable. La primera es `ALC1737`.

La organización prevista es:

```text
data/
├── source/
│   └── alc1737/
│       └── metadata.json
├── ocr_raw/
├── diplomatic/
├── corrected/
├── normalized/
├── structured/
│   ├── lexicon/
│   └── grammar/
├── review/
└── research/
```

Git solo mostrará los directorios cuando contengan archivos versionados.

## Reglas

1. `ocr_raw` no se corrige in situ.
2. `diplomatic` conserva la forma documental del testimonio.
3. `corrected` corrige errores de lectura sin modernizar ortografía histórica.
4. `normalized` es una capa derivada y debe declarar sus reglas.
5. `structured` debe enlazar cada registro con la página y la capa de origen.
6. `research` contiene resultados analíticos y nunca debe confundirse con evidencia primaria.
7. Toda unidad debe incluir un estado de revisión explícito.

## Identificadores

Se propone la convención:

- fuente: `ALC1737`;
- página digital: `ALC1737-p0001`;
- entrada lexicográfica: `ALC1737-lex-000001`;
- ejemplo lingüístico: `ALC1737-ex-000001`.

Los identificadores no deben reciclarse después de una release pública.

## Formatos

La capa maestra deberá poder exportarse al menos a:

- CSV para análisis tabular;
- JSON/JSONL para procesamiento;
- TEI/XML para interoperabilidad editorial y lexicográfica cuando el modelo esté estabilizado.

## Estado actual

La versión 0.1.0 contiene solo metadatos de la fuente y contratos iniciales. No debe interpretarse como corpus transcrito completo.
