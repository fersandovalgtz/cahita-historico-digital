# Guía de reproducibilidad

Esta guía describe cómo inspeccionar y reconstruir productos de Cahíta Histórico Digital (CHD) sin depender del entorno de desarrollo original. La meta es poder distinguir una reproducción exitosa de una mera coincidencia visual.

## Requisitos

- Git;
- Python 3.11 o posterior recomendado;
- `pip`;
- GNU Make opcional, para atajos;
- **Jing** únicamente para reproducir la validación externa TEI Lex-0.

Instale las dependencias Python:

```bash
python -m pip install -r requirements-dev.txt
```

## 1. Fijar la versión

Para reproducir exactamente la release científica estable:

```bash
git clone https://github.com/fersandovalgtz/cahita-historico-digital.git
cd cahita-historico-digital
git checkout v1.0.0
```

El tag `v1.0.0` debe resolver a:

```text
dbcdecf0003ac5a10ae963caf6babdcf5c22128d
```

No use `main` cuando el objetivo sea reconstruir los bytes históricos de v1.0.0: `main` contiene mantenimiento post-release.

## 2. Inspeccionar el corpus

En `main`, la herramienta de consulta ofrece una entrada conservadora:

```bash
python scripts/query_lexicon.py --stats
python scripts/query_lexicon.py "Danzar" --field spanish --limit 5
```

La búsqueda usa substring Unicode sin modernización ortográfica, sustitución de `ſ` ni inferencia lingüística.

## 3. Validación local rápida

En una checkout actual de `main`:

```bash
make qa-surface
make qa
```

`qa-surface` verifica que README, datasheet, calidad, FAIR, metadata JSON/JSON-LD, release y métricas públicas permanezcan sincronizados con el corpus.

`make qa` ejecuta los validadores locales principales de inventario, IDs, documentación, derivados, remisiones, recolaciones, `Lo miſmo`, TEI interno, gramática y freezes.

## 4. Validación completa

Con `jing` instalado:

```bash
make qa-full
```

Además de la QA local, este objetivo:

1. valida TEI contra el Relax NG archivado de Lex-0 0.9.5;
2. valida el release candidate científico;
3. reconstruye y comprueba el paquete estable v1.0.0.

GitHub Actions constituye la referencia de entorno limpio para esta batería.

## 5. Exportaciones léxicas

```bash
python scripts/export_lexicon_corpus.py --out-dir build/lexicon-exports
```

Se generan:

- `chd_lexicon_articles.jsonl`;
- `chd_lexicon_articles.json`;
- `chd_lexicon_articles.csv`;
- `manifest.json` con bytes y SHA-256.

El exportador lee `data/lexicon/articles/*.jsonl` y no reescribe las fuentes canónicas.

## 6. TEI Lex-0

Validación interna:

```bash
python scripts/validate_tei_export.py
```

Validación externa, si `jing` está disponible:

```bash
bash scripts/validate_tei_lex0_external.sh
```

El gate externo descarga el schema archivado de Lex-0 0.9.5 y comprueba su SHA-256 fijado antes de validar el XML.

## 7. Freeze de contratos

```bash
python scripts/validate_v1_contract_freeze.py
```

La v1.0.0 fija 26 contratos: 22 JSON Schema y cuatro metadatos de alcance de `ALC1737`. Un cambio posterior a esos bytes no puede presentarse como idéntico al contrato v1.

## 8. Freeze científico

```bash
python scripts/validate_v1_data_freeze.py
```

La v1.0.0 fija 267 archivos científicos. El freeze es una identidad de versión, no una prohibición de investigación futura: las mejoras post-v1 deben producir nuevas capas/versiones en lugar de reescribir la release histórica.

## 9. Paquete estable

```bash
python scripts/validate_v1_release.py
```

La validación construye el paquete dos veces y exige identidad determinística. Para la publicación real, el workflow post-merge volvió a construir desde el commit definitivo y creó la GitHub Release.

La identidad binaria pública definitiva —atestada posteriormente mediante reconstrucción desde el tag— es:

```text
cahita-historico-digital-v1.0.0.zip
bytes: 1076296
sha256: 583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158
```

Véase `release/github_release_attestation_v1.0.0.json`.

## 10. Qué significa reproducir

Una reproducción exitosa puede demostrar:

- que los datos satisfacen contratos estructurales;
- que los IDs y estados son consistentes;
- que un derivado puede regenerarse;
- que los hashes coinciden;
- que TEI satisface el perfil estructural Lex-0;
- que la release se reconstruye determinísticamente.

No demuestra por sí sola que una lectura histórica sea filológicamente correcta. En v1.0.0 `humanVerified=0`, y las 22 recolaciones permanecen abiertas.

## 11. Reportar diferencias

Si un comando produce resultados distintos:

1. registre commit/tag exacto;
2. registre versión de Python y dependencias;
3. conserve el comando y salida mínima;
4. distinga datos canónicos de derivados;
5. abra un issue con la plantilla de error de datos/software.

No edite manualmente el resultado para hacerlo coincidir con el esperado: la discrepancia es evidencia útil.
