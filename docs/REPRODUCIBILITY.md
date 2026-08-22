# Guía de reproducibilidad

Esta guía describe cómo inspeccionar y reconstruir productos de Cahíta Histórico Digital (CHD) sin depender del entorno de desarrollo original. La meta es distinguir una reproducción exitosa de una mera coincidencia visual y, después de una release, distinguir `main` de los bytes históricos del tag publicado.

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

Para inspeccionar exactamente la release científica estable:

```bash
git clone https://github.com/fersandovalgtz/cahita-historico-digital.git
cd cahita-historico-digital
git checkout v1.0.0
```

El tag `v1.0.0` debe resolver a:

```text
dbcdecf0003ac5a10ae963caf6babdcf5c22128d
```

No use `main` como sustituto del tag cuando el objetivo sean los bytes históricos de v1.0.0: `main` contiene mantenimiento post-release, documentación mejorada y futuros desarrollos.

## 2. Inspeccionar el corpus

En `main`, la herramienta de consulta ofrece una entrada conservadora:

```bash
python scripts/query_lexicon.py --stats
python scripts/query_lexicon.py "Danzar" --field spanish --limit 5
```

La búsqueda usa substring Unicode sin modernización ortográfica, sustitución de `ſ` ni inferencia lingüística.

## 3. Validación local rápida de `main`

```bash
make qa-surface
make qa
```

`qa-surface` verifica que README, datasheet, calidad, FAIR, metadata JSON/JSON-LD, release, licencias, enlaces y métricas públicas permanezcan sincronizados con los hechos canónicos.

`make qa` ejecuta los validadores locales principales de inventario, IDs, documentación, derivados, remisiones, recolaciones, `Lo miſmo`, TEI interno, gramática y freezes.

## 4. Validación completa post-release

Con `jing` instalado:

```bash
make qa-full
```

Además de la QA local, este objetivo:

1. valida TEI contra el Relax NG archivado de Lex-0 0.9.5;
2. resuelve el tag inmutable `v1.0.0`;
3. crea un worktree temporal en ese tag;
4. reconstruye el paquete usando el código almacenado dentro de la propia release;
5. compara ZIP y `RELEASE_MANIFEST.json` contra la atestación pública final.

GitHub Actions constituye la referencia de entorno limpio para esta batería.

> **Importante:** el antiguo `scientific_release_candidate` fue un artefacto de preparación pre-v1. Después de publicada la release ya no forma parte del gate normal de `main`; su historial se conserva, pero la QA actual valida la identidad publicada real.

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

## 9. Validar la release publicada desde `main`

Use:

```bash
python scripts/validate_published_v1.py
# o
make release-check
```

Este validador **no reconstruye v1.0.0 desde el HEAD actual**. Primero exige que el tag siga apuntando al commit publicado y después reconstruye desde un worktree temporal en `v1.0.0`.

Comprueba exactamente:

```text
v1.0.0 -> dbcdecf0003ac5a10ae963caf6babdcf5c22128d

cahita-historico-digital-v1.0.0.zip
bytes: 1076296
sha256: 583183eabb90080dccd1ea63a069e248b28cd3ce41e99ba754ac71ce26586158

RELEASE_MANIFEST.json
bytes: 67757
sha256: 05970080840ed0cde9c4ca67b40432b492ba2f0afadade5efe2b9d0f60b8cb79
```

La evidencia post-publicación está en `release/github_release_attestation_v1.0.0.json`.

## 10. Reconstruir manualmente dentro del tag

Si ya hizo `git checkout v1.0.0`, puede utilizar las herramientas históricas incluidas en ese tag:

```bash
python scripts/validate_v1_release.py
```

Ese comando es válido **dentro de la checkout de v1.0.0**, porque allí `HEAD` coincide con el commit publicado. En `main`, `build_v1_release.py` está deliberadamente protegido y se niega a generar otro paquete con la misma etiqueta de versión desde un commit posterior.

La protección impide que una mejora de README, licencias o metadatos post-release produzca silenciosamente un ZIP diferente llamado todavía “v1.0.0”.

## 11. Qué significa reproducir

Una reproducción exitosa puede demostrar:

- que los datos satisfacen contratos estructurales;
- que los IDs y estados son consistentes;
- que un derivado puede regenerarse;
- que los hashes coinciden;
- que TEI satisface el perfil estructural Lex-0;
- que la release publicada se reconstruye determinísticamente desde su tag.

No demuestra por sí sola que una lectura histórica sea filológicamente correcta. En v1.0.0 `humanVerified=0`, y las 22 recolaciones permanecen abiertas.

## 12. Reportar diferencias

Si un comando produce resultados distintos:

1. registre commit/tag exacto;
2. registre versión de Python y dependencias;
3. conserve el comando y salida mínima;
4. distinga datos canónicos de derivados;
5. abra un issue con la plantilla de error de datos/software.

No edite manualmente el resultado para hacerlo coincidir con el esperado: la discrepancia es evidencia útil.
