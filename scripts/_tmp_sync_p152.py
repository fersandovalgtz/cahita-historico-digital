from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


# README
path = Path("README.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "- las páginas **152–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;",
    "- la página **152** tiene sus **52 candidatos canónicos reconciliados**: 52 `article`, sin continuaciones ni candidatos estructuralmente irresueltos; los 15 artículos seleccionados `ALC1737-art-000284`–`000298` quedaron enlazados, permanecen 37 fronteras `pending_promotion` y el censo visible sigue no exhaustivo;\n- las páginas **153–177** ya poseen representación lexicográfica estructurada, pero su reconciliación exhaustiva página por página sigue pendiente;",
    "README coverage",
)
text = replace_once(
    text,
    "En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; y en **p.151** quedan 34 `pending_promotion`. Las páginas 145–151 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 152**, con 52 candidatos canónicos —28 izquierda y 24 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual.",
    "En **p.145** quedan 20 fronteras `pending_promotion` y 3 candidatos `unresolved`; en **p.146** quedan 22 `pending_promotion`; en **p.147** quedan 36 `pending_promotion`; en **p.148** quedan 29 `pending_promotion`; en **p.149** quedan 40 `pending_promotion` y 1 candidato `unresolved`; en **p.150** quedan 40 `pending_promotion` y 1 candidato estructural `unresolved`; en **p.151** quedan 34 `pending_promotion`; y en **p.152** quedan 37 `pending_promotion`. Las páginas 145–152 tienen reconciliación de candidatos completa, pero sus censos visibles aún no se consideran exhaustivos. El siguiente frente geométrico es la **página 153**, con 51 candidatos canónicos —25 izquierda y 26 derecha—; se mantendrá la misma separación entre frontera estructural confirmada, promoción curatorial e incertidumbre textual.",
    "README next front",
)
path.write_text(text, encoding="utf-8")

# LEXICON_PROGRESS
path = Path("docs/LEXICON_PROGRESS.md")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "Las páginas **145–151 tienen reconciliación completa de sus candidatos canónicos**",
    "Las páginas **145–152 tienen reconciliación completa de sus candidatos canónicos**",
    "LEXICON top coverage",
)
marker = "## Próximo frente\n"
if text.count(marker) != 1:
    raise SystemExit(f"LEXICON next-front marker count={text.count(marker)}")
section = """## Página 152 — reconciliación de candidatos completada

La página digital **152** contiene **52 candidatos canónicos: 28 izquierda y 24 derecha**. La reconciliación machine-only clasifica los **52 como `article`**, sin candidatos `continuation`, `unresolved`, `paratext` o `false_positive`; las **52 fronteras** se conservan como `exact` en el plano estructural.

La capa seleccionada preexistente contiene **15 artículos `ALC1737-art-000284`–`ALC1737-art-000298`** y los quince quedaron enlazados directamente a candidatos canónicos. El OCR conserva dos incidencias sin convertirlas en hechos lexicográficos nuevos. **R-002** (`Cuyo ? Abcatea. Iotuc*`) arrastra `Iotuc`, forma que pertenece al artículo izquierdo seleccionado `Crecer el hombre`; se registra como probable contaminación OCR/layout entre columnas y no como un inicio adicional. **L-006** (`Criador Dios. Itotq tehuaca-`) termina truncado por guion, pero L-007 inicia el artículo fresco `Crucificar`; no se inventa una continuación inexistente en el inventario canónico.

Los bordes de página también quedan modelados conservadoramente. El `Coronilla...` final de p.151 puede continuar en material superior no representado antes de p.152 L-001, mientras L-001 abre de forma fresca `Crecer el hombre`. En el extremo opuesto, p.152 R-024 comienza `Cuñado de muger...`, pero p.153 L-001 abre el artículo fresco `Cuñado de hombre. Mocari.`; no se afirma una continuidad larga p.152→153.

Quedan **37 candidatos de artículo `pending_promotion`**. No hubo promociones nuevas y el corpus permanece en **1,045 artículos**. Los 52 candidatos establecen al menos 52 comienzos estructurales conocidos, pero la capa seleccionada no es exhaustiva y no permite demostrar ausencia de falsos negativos; por ello no se calculan TP/FP/FN, precisión, recall ni F1. `p152_machine_reconciliation_status.json` conserva el detalle y los límites de autoridad.

"""
text = text.replace(marker, section + marker, 1)
text = replace_once(
    text,
    "En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; y en p.151, **34 `pending_promotion`**. Las páginas 145–151 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 152**, con **52 candidatos canónicos: 28 izquierda y 24 derecha**. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.",
    "En p.145 quedan **20 `pending_promotion`** y 3 `unresolved`; en p.146, **22 `pending_promotion`**; en p.147, **36 `pending_promotion`**; en p.148, **29 `pending_promotion`**; en p.149, **40 `pending_promotion`** y 1 `unresolved`; en p.150, **40 `pending_promotion`** y 1 candidato estructural `unresolved`; en p.151, **34 `pending_promotion`**; y en p.152, **37 `pending_promotion`**. Las páginas 145–152 tienen reconciliación de candidatos completa, pero no un censo visible exhaustivo.\n\nEl siguiente frente geométrico es la **página digital 153**, con **51 candidatos canónicos: 25 izquierda y 26 derecha**. Hasta que p.145 complete censo visible y promoción, el corpus sigue publicando **1,045 artículos estructurados** y **pp.133–144** como último tramo técnicamente cerrado.",
    "LEXICON next front",
)
path.write_text(text, encoding="utf-8")

# QA
path = Path(".github/workflows/qa.yml")
text = path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "            data/lexicon/reconciliation/p151_right_reconciliation.jsonl; do",
    "            data/lexicon/reconciliation/p151_right_reconciliation.jsonl \\\n            data/lexicon/reconciliation/p152_left_reconciliation.jsonl \\\n            data/lexicon/reconciliation/p152_right_reconciliation.jsonl; do",
    "QA reconciliation list",
)
text = replace_once(
    text,
    "          python -m json.tool data/lexicon/reconciliation/p151_preflight.json >/dev/null",
    "          python -m json.tool data/lexicon/reconciliation/p151_preflight.json >/dev/null\n          python -m json.tool data/lexicon/reconciliation/p152_machine_reconciliation_status.json >/dev/null\n          python -m json.tool data/lexicon/reconciliation/p152_preflight.json >/dev/null",
    "QA JSON list",
)
path.write_text(text, encoding="utf-8")
