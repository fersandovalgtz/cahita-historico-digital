import json
from pathlib import Path

ARTICLE_IDS = {
    'ALC1737-art-000398': 'ALC1737-vcand-p159-L-017',
    'ALC1737-art-000399': 'ALC1737-vcand-p159-L-023',
    'ALC1737-art-000400': 'ALC1737-vcand-p159-L-024',
}

articles_path = Path('data/lexicon/articles/p159_selected_articles.jsonl')
rows = [json.loads(line) for line in articles_path.read_text(encoding='utf-8').splitlines() if line.strip()]
seen = set()
for row in rows:
    aid = row['articleId']
    if aid not in ARTICLE_IDS:
        continue
    if row['column'] != 'right':
        raise SystemExit(f'{aid}: expected old column right, found {row["column"]}')
    old_derived = row['provenance']['derivedFrom']
    if old_derived != 'ALC1737:digital-page-159:right':
        raise SystemExit(f'{aid}: unexpected old derivedFrom {old_derived}')
    row['column'] = 'left'
    row['provenance']['derivedFrom'] = 'ALC1737:digital-page-159:left'
    seen.add(aid)
if seen != set(ARTICLE_IDS):
    raise SystemExit(f'missing target articles: {set(ARTICLE_IDS) - seen}')
articles_path.write_text('\n'.join(json.dumps(r, ensure_ascii=False, separators=(',', ':')) for r in rows) + '\n', encoding='utf-8')

prov_path = Path('data/lexicon/provenance/p159_column_metadata_corrections.jsonl')
prov_rows = []
for aid, cid in ARTICLE_IDS.items():
    prov_rows.append({
        'articleId': aid,
        'sourcePageDigital': 159,
        'field': 'column',
        'oldValue': 'right',
        'newValue': 'left',
        'oldDerivedFrom': 'ALC1737:digital-page-159:right',
        'newDerivedFrom': 'ALC1737:digital-page-159:left',
        'candidateId': cid,
        'reason': 'Canonical-v0.2 candidate geometry and the matching selected guide place this article in the p159 left column; no lexical transcription, article type, or historical form is changed.',
        'reviewStatus': 'machine_corrected_unverified',
        'humanVerified': False,
    })
prov_path.write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in prov_rows) + '\n', encoding='utf-8')

left_path = Path('data/lexicon/reconciliation/p159_left_reconciliation.jsonl')
left_rows = [json.loads(line) for line in left_path.read_text(encoding='utf-8').splitlines() if line.strip()]
for row in left_rows:
    aid_list = row.get('linkedArticleIds', [])
    target = next((aid for aid in aid_list if aid in ARTICLE_IDS), None)
    if not target:
        continue
    stale = ' Selected metadata says right column while canonical geometry places this text in left; mismatch is documented without silent correction.'
    stale2 = ' Selected metadata says right column while canonical geometry places the matching text in left; mismatch is documented without silent correction.'
    note = row.get('editorialNote', '')
    note = note.replace(stale, '').replace(stale2, '')
    note += ' Selected column metadata was corrected right→left in `p159_column_metadata_corrections.jsonl`; lexical transcription is unchanged.'
    row['editorialNote'] = note
left_path.write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in left_rows) + '\n', encoding='utf-8')

status_path = Path('data/lexicon/reconciliation/p159_machine_reconciliation_status.json')
status = json.loads(status_path.read_text(encoding='utf-8'))
selected = status['selectedLayer']
selected['selectedColumnMetadataMismatches'] = []
selected['columnMetadataCorrectionAppliedThisPass'] = True
selected['columnMetadataCorrections'] = [
    {'articleId': aid, 'oldColumn': 'right', 'newColumn': 'left', 'candidateId': cid}
    for aid, cid in ARTICLE_IDS.items()
]
status['structuralNotes'] = [
    note for note in status['structuralNotes']
    if not note.startswith('Selected article column metadata for 000398–000400')
]
status['structuralNotes'].append('Selected article column metadata for 000398–000400 was corrected right→left with a dedicated provenance layer; lexical transcription was not changed.')
status['evidence']['policy'] = 'Candidate geometry and selected direct collations are used only to support demonstrated starts and continuations. The demonstrated 000398–000400 column drift is corrected with explicit provenance; unanchored internal guide-like material remains unpromoted.'
status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

preflight_path = Path('data/lexicon/reconciliation/p159_preflight.json')
preflight = json.loads(preflight_path.read_text(encoding='utf-8'))
preflight['selectedLayer']['columnMetadataCorrection'] = {
    'applied': True,
    'articleIds': list(ARTICLE_IDS),
    'oldColumn': 'right',
    'newColumn': 'left',
    'provenancePath': 'data/lexicon/provenance/p159_column_metadata_corrections.jsonl',
    'lexicalTranscriptionChanged': False,
}
preflight['nextAction'] = 'Validate the full p159 package, synchronize documentation with the applied column-metadata correction, restore permanent QA through p159, remove temporary scripts/workflows, and integrate only after green PR and post-merge runs.'
preflight_path.write_text(json.dumps(preflight, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

readme = Path('README.md')
text = readme.read_text(encoding='utf-8')
text = text.replace(
    'las discrepancias de columna de `000398`–`000400` quedan documentadas sin corrección silenciosa;',
    'la columna de `000398`–`000400` se corrigió de forma trazable de derecha a izquierda, con procedencia dedicada y sin cambiar la transcripción;'
)
readme.write_text(text, encoding='utf-8')

progress = Path('docs/LEXICON_PROGRESS.md')
text = progress.read_text(encoding='utf-8')
text = text.replace(
    'La alineación detecta además una discrepancia de metadatos que se preserva para auditoría: `ALC1737-art-000398`, `000399` y `000400` están marcados como columna derecha en la capa seleccionada, mientras los textos coinciden con los candidatos geométricos izquierdos L-017, L-023 y L-024. **No se aplicó corrección silenciosa de columna en esta pasada estructural.**',
    'La alineación detectó además una discrepancia de metadatos: `ALC1737-art-000398`, `000399` y `000400` estaban marcados como columna derecha, mientras sus textos coinciden con los candidatos geométricos izquierdos L-017, L-023 y L-024. Se corrigió **right→left** de forma auditada en `data/lexicon/provenance/p159_column_metadata_corrections.jsonl`; la transcripción, el tipo de artículo y las formas históricas no cambiaron.'
)
progress.write_text(text, encoding='utf-8')
