# Cahíta Histórico Digital — Release Candidate Manifest v1.0.0

## Objetivo

Este documento define los criterios de preparación de una primera versión científica estable del repositorio.

## Artefactos esperados

- Datos derivados canónicos.
- Documentación metodológica.
- Información de procedencia.
- Esquemas de datos.
- Reportes de QA.
- Exportaciones reproducibles.

## Exclusiones

No forman parte de una release estable:

- archivos OCR intermedios sin procesamiento;
- candidatos lexicográficos no reconciliados;
- pruebas experimentales;
- salidas temporales de desarrollo.

## Requisitos antes de v1.0.0

- Consistencia entre README, CITATION.cff y CHANGELOG.
- Versionado único.
- Paquete reproducible.
- Metadatos de preservación completos.
- Registro de commit asociado.

## Flujo de liberación

Fuente histórica → procesamiento reproducible → datos derivados → documentación → release archivada.
