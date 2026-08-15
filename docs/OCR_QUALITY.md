# Diagnóstico inicial de calidad OCR — ALC1737

## Objetivo

Este diagnóstico estima la calidad de la capa OCR utilizada como entrada de Cahíta Histórico Digital. Su propósito es decidir cuánto trabajo editorial y de segmentación será necesario; **no mide la calidad filológica de CHD ni sustituye una revisión humana**.

## Muestra estratificada

Se seleccionaron seis zonas que representan arquitecturas textuales distintas del volumen:

| Estrato | Página digital | Contenido |
|---|---:|---|
| Parte I | 15 | proemio y comienzo del cuerpo gramatical |
| Parte II | 51 | comienzo de la sección del nombre |
| Parte III | 69 | comienzo de la sección del verbo |
| Parte IV | 105 | encabezado de preposiciones/adverbios |
| Vocabulario | 134 | artículos lexicográficos en dos columnas |
| Numerales | 178 | inicio de nombres numerales |

Las referencias fueron cotejadas visualmente de manera IA-asistida contra el facsímil y **no cuentan con validación humana independiente**. Por ello los resultados deben interpretarse como diagnóstico de ingeniería editorial.

## Normalización para la métrica

Antes de comparar referencia y OCR se aplica:

- Unicode NFKD;
- `ſ → s`;
- eliminación de marcas diacríticas combinantes;
- minúsculas;
- puntuación convertida a espacios;
- colapso de espacios.

Esta transformación evita que la métrica quede dominada por puntuación o diacríticos, pero conserva errores de reconocimiento de letras, segmentación de palabras y omisiones.

El vocabulario requiere una excepción metodológica: `pdftotext -layout` mezcla con frecuencia las dos columnas. Para la página 134 se utilizó la salida `-bbox-layout` reorganizada por columna mediante `scripts/extract_vocab_layout.py`. Así se evalúa reconocimiento textual después de restaurar un orden de lectura razonable, y no solamente el fallo de geometría de columnas.

## Resultados

| Estrato | CER | WER |
|---|---:|---:|
| Parte I, p. 15 | 27.95% | 50.00% |
| Parte II, p. 51 | 28.62% | 61.90% |
| Parte III, p. 69 | 36.02% | 53.85% |
| Parte IV, p. 105 | 13.51% | 50.00% |
| Vocabulario, p. 134 | **9.68%** | 51.72% |
| Numerales, p. 178 | 30.43% | 36.36% |

**Micro-CER:** **25.66%**  
**Macro-CER:** **24.37%**  
**Micro-WER:** **51.96%**  
**Macro-WER:** **50.64%**

Los valores exactos y las ventanas OCR comparadas se conservan en `data/validation/ocr_sample_results.json`.

## Interpretación

El resultado principal es que **el OCR bruto no es suficientemente fiable para convertirse directamente en corpus científico**. Un micro-CER de aproximadamente una cuarta parte de los caracteres de la muestra hace indispensable conservar el OCR como evidencia, cotejarlo contra el facsímil y separar corrección, transcripción y normalización.

La WER es especialmente alta porque la tipografía histórica y la maquetación generan separaciones y fusiones de tokens (`cor menzarfe`, `aboga cia`, etc.). En consecuencia, la WER no debe utilizarse sola para juzgar recuperación léxica.

El comportamiento del vocabulario es revelador: una vez restaurado el orden de la columna, el fragmento seleccionado alcanza un CER bastante menor que varias secciones gramaticales. Esto sugiere que **una parte importante del problema del vocabulario es geométrica/estructural y no sólo reconocimiento de caracteres**. Es una hipótesis operativa del pipeline, no una estimación de todo el vocabulario.

## Reproducibilidad

```bash
python scripts/evaluate_ocr_sample.py \
  --pdf /ruta/Cahíta.pdf \
  --references data/validation/ocr_sample_references.json \
  --out data/validation/ocr_sample_results.json
```

La evaluación usa únicamente Python estándar, Poppler y el extractor de layout incluido en el repositorio. Las referencias y resultados están versionados para que cualquier modificación futura de la muestra o del método produzca un diff auditable.
