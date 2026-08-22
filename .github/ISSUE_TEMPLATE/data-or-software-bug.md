---
name: Error de datos, software o reproducibilidad
about: Reportar fallos de schema, scripts, exportaciones, CI, manifests o integridad
labels: bug
---

## Componente

- [ ] Datos canónicos
- [ ] Schema
- [ ] Script/exportador
- [ ] CI/QA
- [ ] Release/manifiesto/checksum
- [ ] Documentación machine-readable

## Comportamiento observado

Describa el fallo y el archivo/comando afectado.

## Comportamiento esperado

Indique la invariante que debería cumplirse.

## Reproducción

```text
comando, ruta o pasos mínimos
```

## Versión

- tag/commit:
- sistema/Python si aplica:

## Integridad científica

¿El problema puede modificar IDs, autoridad, procedencia, `humanVerified`, contratos congelados o la identidad de una release? Explíquelo.

No proponga regenerar datos canónicos únicamente para hacer que coincidan con un derivado: identifique primero cuál capa tiene autoridad.
