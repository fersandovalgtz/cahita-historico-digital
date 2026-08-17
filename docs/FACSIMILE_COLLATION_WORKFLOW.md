# Colación facsimilar reproducible

## Propósito

La fase II del Vocabulario separa la **detección estructural** de la **promoción curatorial**. Un candidato `pending_promotion` sólo debe convertirse en artículo cuando el testigo primario `ALC1737` ofrece evidencia suficiente para sostener la guía y, cuando corresponde, la forma cahíta. El OCR es una herramienta de lectura asistida, no autoridad diplomática.

`scripts/prepare_facsimile_collation.py` normaliza la preparación técnica de esa evidencia. Recupera un derivado PDF de Internet Archive, extrae una sola página, calcula su SHA-256, la renderiza, separa las dos columnas y ejecuta tres lecturas OCR independientes por columna. La salida se destina a un directorio temporal ignorado por Git.

## Dependencias

Se requieren `pdfseparate` y `pdftoppm` de Poppler, Tesseract con el paquete de idioma correspondiente y Pillow para Python. En Ubuntu, una instalación de referencia es:

```bash
sudo apt-get install poppler-utils tesseract-ocr tesseract-ocr-spa
python -m pip install Pillow
```

## Ejecución

```bash
python scripts/prepare_facsimile_collation.py \
  --ia-id artedelalenguaca00gonz \
  --pdf-page 177 \
  --out-dir .tmp_facsimile/p177 \
  --language spa
```

El directorio generado contiene `source-page.pdf`, seis lecturas OCR (`left/right × gray_psm4, gray_psm6, bin_psm4`) y `manifest.json`. El manifiesto registra el identificador de Internet Archive, el derivado elegido, URL, número de página, SHA-256 del PDF de una sola página, resolución, dimensiones, parámetros de preprocesamiento, versión de Tesseract y hashes de cada lectura.

## Regla de autoridad

La herramienta **no modifica** candidatos, artículos, estados de página ni datos canónicos. Tampoco decide qué lectura es correcta. Sus salidas son evidencia de máquina derivada del testigo primario y permanecen fuera de Git mediante `.tmp_facsimile/`.

Una promoción exige revisión a nivel de candidato y procedencia explícita. El criterio piloto adoptado en p.145 fue conservador: frontera limpia y convergencia fuerte de guía española y forma cahíta entre lecturas independientes del mismo facsímil. Cuando las lecturas divergen materialmente, el candidato permanece `pending_promotion`.

`BUE1890` puede emplearse como control histórico secundario de orden, identidad de guía o segmentación, pero nunca para completar silenciosamente una forma ausente o insegura de `ALC1737`.

## Reproducibilidad y limpieza

El SHA-256 de `source-page.pdf` debe copiarse al registro de evidencia permanente de cualquier lote de promoción. Las imágenes y OCR auxiliares no se incorporan a `main`; sólo se conservan los artículos promovidos, enlaces de candidatos, estado actualizado y el registro JSON de evidencia necesario para reconstruir la decisión.

El directorio `.tmp_facsimile/` está excluido en `.gitignore` para reducir el riesgo de publicar accidentalmente auxiliares voluminosos o transitorios.
