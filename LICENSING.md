# Licenciamiento por componentes

Cahíta Histórico Digital combina software, datos/editorial propio y materiales de procedencia externa. Una sola licencia no describe correctamente todos esos componentes.

| Componente | Licencia / condición | Archivo de referencia |
|---|---|---|
| Código y software original | MIT | [`LICENSE`](LICENSE) |
| Datos estructurados originales | CC BY 4.0 | [`DATA_LICENSE.md`](DATA_LICENSE.md) |
| Metadatos y capas editoriales originales | CC BY 4.0 | [`DATA_LICENSE.md`](DATA_LICENSE.md) |
| Transcripciones originales del proyecto | CC BY 4.0, salvo indicación expresa | [`DATA_LICENSE.md`](DATA_LICENSE.md) |
| JSON Schema y documentación editorial original | CC BY 4.0 salvo que el archivo indique otra cosa | [`DATA_LICENSE.md`](DATA_LICENSE.md) |
| Facsímiles, scans y reproducciones de terceros | **No relicenciados por CHD** | [`SOURCES.md`](SOURCES.md), [`PROVENANCE.md`](PROVENANCE.md) |
| Ediciones o recursos externos enlazados | Condiciones del proveedor/titular correspondiente | procedencia del recurso |

## Por qué `LICENSE` contiene sólo MIT

El archivo raíz `LICENSE` utiliza el texto MIT estándar para que gestores de paquetes, GitHub y herramientas automatizadas identifiquen correctamente la licencia del **software original**. Esto no convierte los datos ni materiales de terceros en software MIT.

La licencia aplicable al dataset y a las capas editoriales originales se declara separadamente en `DATA_LICENSE.md` con SPDX `CC-BY-4.0`.

## Fuente histórica y dominio público

El estatus histórico de una obra y las condiciones de una reproducción digital son cuestiones distintas. CHD no presupone que el derecho a reutilizar el texto histórico implique automáticamente derechos sobre imágenes, scans o reproducciones producidas por terceros. Por ello la release científica prioriza datos estructurados, transcripciones y metadatos propios y conserva enlaces/procedencia de los custodios digitales.

## Atribución

Al reutilizar datos CHD, cite al menos:

1. la versión concreta del dataset/release;
2. a Fernando Sandoval Gutierrez como responsable del proyecto según `CITATION.cff`;
3. la fuente histórica `ALC1737` cuando el dato derive del impreso;
4. página, `articleId` u otro identificador cuando sea pertinente para reproducibilidad.

## DOI

El DOI está pendiente del depósito archivístico. No sustituya temporalmente ese identificador con un DOI inferido o perteneciente a otro recurso.
