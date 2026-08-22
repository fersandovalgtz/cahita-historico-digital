# Ecosistema de investigación

Cahíta Histórico Digital (CHD) forma parte de una línea de trabajo sobre infraestructuras reproducibles para documentación lingüística, patrimonio documental y humanidades digitales. Su arquitectura comparte principios con otros proyectos, pero su objeto histórico exige reglas propias de autoridad y de identidad lingüística.

## CHD y Rarámuri Digital

[Rarámuri Digital](https://github.com/fersandovalgtz/raramuri-digital) es el referente metodológico más cercano en la cartera del proyecto. Ambos repositorios comparten:

- IDs y procedencia explícita;
- exports reproducibles;
- contratos de datos y QA automatizado;
- CFF/CodeMeta y documentación científica;
- interoperabilidad lexicográfica;
- separación entre disponibilidad técnica y validación lingüística;
- preocupación por FAIR, preservación y reutilización responsable.

La diferencia central es epistemológica. Rarámuri Digital trabaja como infraestructura lexicográfica orientada a una lengua indígena contemporánea y a reutilización educativa/aplicada. CHD trabaja sobre un **testimonio histórico de 1737**. Por ello, CHD prioriza microestructura histórica, fidelidad documental, capas de incertidumbre, autoría/transmisión y no mapeo automático a identidades lingüísticas modernas.

## Otros proyectos relacionados

### Rarámuri Histórico Digital

<https://github.com/fersandovalgtz/raramuri-historico>

Proyecto hermano de edición histórico-digital. CHD comparte separación de capas, procedencia e incertidumbre tipada sin mezclar corpus ni asumir equivalencias lingüísticas.

### Libro de Texto Mexicano Digital

<https://github.com/fersandovalgtz/libro-texto-mexicano-digital>

Proyecto hermano de patrimonio documental, datos abiertos e investigación histórica. Comparte la lógica de convertir fuentes digitalizadas en corpus investigables y productos reproducibles.

## Complementariedad, no fusión

CHD no es una “versión antigua” de Rarámuri Digital. Los proyectos pueden compartir herramientas y estándares, pero no comparten automáticamente:

- código ISO de lengua;
- ortografía;
- categorías gramaticales;
- autoridad lingüística;
- políticas de validación comunitaria;
- semántica de entrada lexicográfica.

La interoperabilidad debe ocurrir en la capa técnica, no mediante homogeneización de la evidencia.

## Interoperabilidad externa

### TEI Lex-0

Es el perfil lexical primario de CHD v1.0.0 porque permite representar una estructura de diccionario histórico con mayor fidelidad que una tabla analítica plana. La salida se valida contra Lex-0 0.9.5.

### CLDF

Se mantiene como opción post-v1 para una vista analítica derivada. Cualquier adapter futuro deberá conservar IDs CHD, procedencia, fuente y estados de autoridad, y declarar explícitamente cómo trata formas históricas, variedades y sentidos.

### Preservación

Zenodo u otro repositorio archivístico constituye el siguiente paso para DOI y persistencia independiente de GitHub. La release v1.0.0 ya está congelada, publicada y atestada; el depósito debe preservar esa identidad, no crear una variante silenciosa.

## Productos académicos derivados

CHD puede sustentar:

- artículos de datos y metodología;
- estudios de lexicografía histórica;
- historia de la lingüística misionera;
- análisis de variación histórica;
- concordancias gramaticales;
- estudios comparativos diacrónicos con capas modernas separadas;
- herramientas de consulta y docencia sobre patrimonio documental.

## Principio para expansión futura

La infraestructura puede reutilizarse para otras fuentes cahítas o de lenguas indígenas históricas sólo después de modelar su fuente y autoridad por separado. Compartir software no significa homogenizar corpus. Cada nuevo testimonio debe tener identificador, procedencia, contratos y política de relación lingüística propios.
