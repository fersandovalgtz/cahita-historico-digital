# CLDF Dictionary post-v1

Cahíta Histórico Digital dispone de una proyección reproducible al módulo **CLDF Dictionary**. Esta capa es un producto derivado posterior a `v1.0.0`: no forma parte del corpus científico congelado ni modifica la Release publicada. La autoridad continúa residiendo en `data/lexicon/articles/*.jsonl` y en las capas de procedencia y revisión del repositorio.

## Norma y herramienta

La proyección sigue el módulo `Dictionary` de Cross-Linguistic Data Formats (CLDF), cuyo mínimo normativo se organiza alrededor de `EntryTable` y `SenseTable`. Para construcción y validación se fija `pycldf==2.1.1` en `requirements-cldf.txt`.

El uso de una versión fija del validador no altera la versión del estándar declarada en los URI de la ontología CLDF (`http://cldf.clld.org/v1.0/terms.rdf#...`), que es la forma normativa utilizada por la especificación.

## Principio lingüístico y documental

El exportador no identifica automáticamente el rótulo histórico **Cahita** ni las etiquetas históricas **Hiaqui**, **Mayo** y **Thehueco** con lenguas, variedades o identificadores contemporáneos. La fuente canónica del proyecto establece expresamente que esas denominaciones deben conservarse como datos históricos y no equipararse de manera automática con identidades lingüísticas modernas.

Por esa razón:

- todas las entradas usan el `Language_ID` documental `cahita-historical-source`;
- `languages.csv` no asigna `Glottocode` ni `ISO639P3code`;
- `historicalVariety` se conserva como `Historical_Variety_Label` en `EntryTable`;
- una futura vinculación con catálogos lingüísticos deberá ser una capa explícita, argumentada y separada, nunca una inferencia del exportador.

## Mapeo conservador

Cada objeto de `cahitaFormsRaw` genera una fila de `EntryTable`. `Headword` reproduce literalmente `formRaw`; no se normaliza ortografía, segmentación, mayúsculas, diacríticos ni grafías históricas. El identificador de la entrada se deriva del `articleId` y del orden de la forma dentro del artículo, por ejemplo `ALC1737-art-000690-f01`.

Cada entrada recibe una fila correspondiente de `SenseTable`. `Description` conserva `spanishGuideRaw`; únicamente cuando ese campo no existe se utiliza `transcriptionRaw` como respaldo descriptivo. Este mecanismo no pretende producir análisis semántico moderno ni desambiguación lexicográfica.

La proyección conserva además el identificador del artículo, índice de forma, etiqueta histórica de variedad, calificador de fuente, página digital, columna, tipo de artículo, estado de revisión, indicador de verificación humana, transcripción fuente y referencia bibliográfica a `ALC1737`.

Los artículos históricos que no contienen `cahitaFormsRaw` —por ejemplo ciertos artículos de referencia cruzada o estructuras no equivalenciales— **no son forzados artificialmente a convertirse en entradas de diccionario**. Permanecen íntegros en el corpus canónico y el manifiesto generado contabiliza explícitamente cuántos artículos quedan fuera de `EntryTable` por esta razón.

## Verificación humana

CLDF no eleva autoridad editorial. `Human_Verified` reproduce exactamente el estado canónico de cada artículo. El exportador no convierte revisión automática, colación asistida por IA ni corrección editorial en validación lingüística humana.

## Construcción local

Instalación de la dependencia:

```bash
python -m pip install -r requirements-cldf.txt
```

Generación:

```bash
python scripts/generate_cldf_dictionary.py --output build/cldf --force
```

Validación estándar y validación CHD:

```bash
cldf validate build/cldf/Dictionary-metadata.json
python scripts/validate_cldf_dictionary.py --cldf-dir build/cldf
```

También pueden usarse:

```bash
make cldf
make cldf-qa
```

## Salida generada

La carpeta generada contiene como mínimo:

- `Dictionary-metadata.json`: metadatos CSVW/CLDF del módulo;
- `entries.csv`: `EntryTable` con las formas cahíta históricas;
- `senses.csv`: `SenseTable` con las guías españolas;
- `languages.csv`: fila documental del rótulo histórico Cahita, sin identificadores modernos inferidos;
- `sources.bib`: referencia a la fuente de 1737;
- `projection-manifest.json`: conteos, versión de la proyección, ancla a `v1.0.0` y políticas de mapeo.

`build/` es espacio regenerable y no se incorpora al freeze. La reproducibilidad se prueba reconstruyendo la proyección desde el corpus canónico en CI, ejecutando el validador oficial de `pycldf` y comparando después cada entrada y cada sentido contra los JSONL de origen.

## Ancla a v1.0.0

El manifiesto derivado registra como origen científico:

- versión canónica: `1.0.0`;
- tag: `v1.0.0`;
- commit del tag: `dbcdecf0003ac5a10ae963caf6babdcf5c22128d`.

Esta referencia de procedencia no modifica el tag ni la Release. El CLDF es una vista interoperable reproducible sobre datos congelados, no una reescritura de la publicación v1.
