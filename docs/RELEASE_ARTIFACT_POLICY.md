# Política de artefactos para release científica

## Objetivo

Definir qué productos pueden formar parte de una futura versión estable de Cahíta Histórico Digital y cuáles deben permanecer como materiales internos o de desarrollo.

## Artefactos candidatos para release

- datos canónicos derivados de las fuentes existentes en el repositorio;
- esquemas JSON utilizados para validación;
- documentación metodológica;
- manifiestos de procedencia;
- reportes reproducibles de QA;
- exportaciones generadas directamente desde las capas canónicas.

## Artefactos de desarrollo

Los siguientes elementos no deben presentarse como corpus final sin documentación adicional:

- OCR bruto;
- candidatos lexicográficos sin reconciliación;
- salidas intermedias de algoritmos;
- archivos generados durante pruebas;
- métricas diagnósticas sin contexto metodológico.

## Principio de trazabilidad

Toda liberación debe permitir reconstruir:

fuente histórica → proceso computacional → datos derivados → versión publicada.

## Criterio de versión estable

Una versión científica estable requiere coherencia entre:

- README;
- CITATION.cff;
- CHANGELOG;
- documentación de cobertura;
- datos publicados;
- validaciones automáticas.
