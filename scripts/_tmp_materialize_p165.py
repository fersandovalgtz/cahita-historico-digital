import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')
links = {
    'L-001':['ALC1737-art-000479'],
    'L-002':['ALC1737-art-000480'],
    'L-007':['ALC1737-art-000481'],
    'L-008':['ALC1737-art-000482'],
    'L-009':['ALC1737-art-000483'],
    'L-010':['ALC1737-art-000484'],
    'L-012':['ALC1737-art-000485'],
    'L-013':['ALC1737-art-000486'],
    'L-016':['ALC1737-art-000487','ALC1737-art-000488'],
    'L-017':['ALC1737-art-000489'],
    'R-007':['ALC1737-art-000490'],
    'R-011':['ALC1737-art-000491'],
    'R-012':['ALC1737-art-000492'],
    'R-014':['ALC1737-art-000493'],
}
continuations = {'L-004','L-015','R-003','R-008'}
continuation_links = {'R-008':['ALC1737-art-000490']}
over = {'L-003','L-014','R-002','R-007'}
merged = {'L-016'}
under = {'R-014'}
ambiguous = {'R-016'}
prov = {
    'derivedFrom':'canonical-v0.2 candidate inventory; p165 selected article layer; p164 reconciliation edge context; p166 canonical candidates and selected opening',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}
notes = {
    'L-001':'Fresh selected 000479 (`Obra aſſi, hechura. Chupari.`) after p164 `Obr...` edge/catchword-like material; no long p164→p165 lexical continuation is asserted.',
    'L-002':'Aligned to selected 000480 (`Oveja. Sopoc.`).',
    'L-003':'Distinct `Ocaſion dar à otro`-like article start split from form-only continuation L-004.',
    'L-004':'Form-only continuation of the article begun in L-003; not a fresh lexical start.',
    'L-007':'Aligned to selected 000481 (`Odio tener. Aomta.`).',
    'L-008':'Aligned to selected cross-reference 000482 (`Ofender. Buſca pecar.`).',
    'L-009':'Aligned to selected cross-reference 000483 (`Ofenſa. Buſca pecado.`).',
    'L-010':'Aligned to selected cross-reference 000484 (`Ofenſor. Buſca pecador.`).',
    'L-012':'Aligned to selected 000485 (`Oficio propio del hombre. Atequia.`). The OCR group also carries displaced tail material `...de tiempo, ientapo` from a neighboring selected entry; no second start is inferred here.',
    'L-013':'Aligned to selected 000486 (`Oy, adv. de tiempo. ientapo.`).',
    'L-014':'Distinct additional `Oy`-like article start split from continuation/form material L-015. No selected anchor is used to strengthen its transcription.',
    'L-015':'Continuation/form material of the `Oy`-like article begun in L-014; not a fresh lexical start.',
    'L-016':'Merged selected starts 000487 (`Oydor el que oye. Hicahame.`) and 000488 (`Oyr. Hicaha.`). The second selected start is recorded separately as a known internal miss.',
    'L-017':'Aligned to selected 000489 (`Ojo. Puſi.`). Additional damaged OCR words are retained as reading-order leakage without inventing another selected start.',
    'R-002':'Distinct `Orador tal` article start whose form continues into R-003.',
    'R-003':'Form-only continuation of the `Orador tal` article begun in R-002.',
    'R-007':'Aligned to selected cross-reference 000490 (`Orejear. Buſca menear las orejas.`) and split from its final continuation R-008.',
    'R-008':'Continuation `...jas` of selected 000490; not a fresh lexical start.',
    'R-011':'Aligned to selected cross-reference 000491 (`Orina. Buſca meados.`).',
    'R-012':'Aligned to selected cross-reference 000492 (`Orinar. Buſca mear.`).',
    'R-014':'Aligned to selected cross-reference 000493 (`Oſado ſer. Buſca atrevido.`) but the same OCR group carries additional damaged adjacent material; retained `undersegmented` without promotion of the extra material.',
    'R-016':'Canonical geometry supports a distinct article start, but OCR does not preserve a responsibly recoverable Spanish guide. Retained as article/pending with `ambiguous` assessment rather than assigning an invented lemma.',
    'R-026':'Distinct `Padre` article start with a damaged/incomplete cross-reference-like tail `Buſca apre-`; p165 R-027 opens fresh `Padrino`, so no continuation is asserted.',
    'R-027':'Fresh `Padrino` article start; p166 opens separately with selected `Paga tal. Bebeti.`.',
}

def note_for(key, linked):
    if key in notes:
        return notes[key]
    if linked:
        return 'Aligned to selected direct-collation article anchor.'
    return 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'

def row(side,n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p165-{key}'
    col='left' if side=='L' else 'right'
    if key in continuations:
        linked=continuation_links.get(key,[])
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':165,'column':col,
            'classification':'continuation','boundaryAssessment':'not_applicable','linkedArticleIds':linked,
            'articleLinkStatus':'not_applicable','continuationType':'from_previous_line',
            'editorialNote':note_for(key,linked),'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
        }
    linked=links.get(key,[])
    if key in over: assessment='oversegmented'
    elif key in merged: assessment='merged_articles'
    elif key in under: assessment='undersegmented'
    elif key in ambiguous: assessment='ambiguous'
    else: assessment='exact'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':165,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note_for(key,linked),
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
    }

for side,count,name in [('L',29,'p165_left_reconciliation.jsonl'),('R',27,'p165_right_reconciliation.jsonl')]:
    rows=[row(side,i) for i in range(1,count+1)]
    (OUT/name).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

miss={
    'missedStartId':'ALC1737-miss-p165-L-001','sourceId':'ALC1737','sourcePageDigital':165,'column':'left',
    'visibleStartRaw':'Oyr. Hicaha.','missType':'inside_candidate_group',
    'containingCandidateId':'ALC1737-vcand-p165-L-016','linkedArticleIds':['ALC1737-art-000488'],
    'editorialNote':'Selected 000488 is a distinct historical start absorbed inside canonical L-016 after selected 000487 (`Oydor el que oye`). Recorded as a known internal false negative without claiming exhaustive visible-start coverage.',
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
    'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p165 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None},
}
(OUT/'p165_missed_visible_starts.jsonl').write_text(json.dumps(miss,ensure_ascii=False)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':165,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':56,'left':29,'right':27,
        'classification':{'article':52,'continuation':4,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':45,'oversegmented':4,'undersegmented':1,'merged_articles':1,'ambiguous':1,'not_applicable':4},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000479','ALC1737-art-000493'],
        'articleCandidateRecordsLinked':14,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':1,
        'selectedStartsInsideMergedCandidate':1,'selectedStartsOutsideCandidateInventory':0,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleIds':['ALC1737-art-000488'],
    },
    'promotion':{'articleCandidatesPendingPromotion':38,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':53,'knownMissedStartRecords':1,'unresolvedCandidateRecords':0,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 52 article candidates plus selected internal miss 000488 establish at least 53 starts, but the selected layer is non-exhaustive and damaged/undersegmented groups may contain additional unanchored starts.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p164-R-022','to':'ALC1737-vcand-p165-L-001','type':'fresh_page_transition_after_edge_fragment','note':'p164 `Obr...` is treated as edge/catchword-like material; p165 opens fresh selected 000479.'},
        {'from':'ALC1737-vcand-p165-L-003','to':'ALC1737-vcand-p165-L-004','type':'article_continuation','note':'The L-003 article continues in form-only L-004.'},
        {'from':'ALC1737-vcand-p165-L-014','to':'ALC1737-vcand-p165-L-015','type':'article_continuation','note':'The additional `Oy`-like article in L-014 continues into L-015.'},
        {'from':'ALC1737-vcand-p165-R-002','to':'ALC1737-vcand-p165-R-003','type':'article_continuation','note':'`Orador tal` continues into form-only R-003.'},
        {'from':'ALC1737-vcand-p165-R-007','to':'ALC1737-vcand-p165-R-008','type':'article_continuation','note':'Selected 000490 `Orejear. Buſca menear las orejas.` continues into R-008.'},
        {'from':'ALC1737-vcand-p165-R-027','to':'ALC1737-vcand-p166-L-001','type':'fresh_page_transition','note':'p166 opens fresh selected 000494 `Paga tal. Bebeti.`.'},
    ],
    'structuralNotes':[
        'L-016 is a merged region containing selected 000487 (`Oydor`) and 000488 (`Oyr`); 000488 is recorded as a known internal miss.',
        'R-014 is undersegmented because selected 000493 begins there and the OCR group also carries damaged adjacent material without an independent anchor.',
        'R-016 remains an article boundary with ambiguous assessment because geometry supports a start but the Spanish guide is not responsibly recoverable from OCR.',
        'Four canonical rows are continuations rather than fresh starts: L-004, L-015, R-003 and R-008.'
    ],
    'nextPage':{'sourcePageDigital':166,'candidateInventoryTotal':50,'left':28,'right':22,'firstCandidate':'ALC1737-vcand-p166-L-001','firstSelectedArticle':'ALC1737-art-000494','opening':'Paga tal. Bebeti.'},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP165LayerUsedAsAnchor':True,'p164ReconciliationUsedForOpeningEdge':True,'p166CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and the known internal miss. OCR-only ambiguous/adjacent material is preserved without invented lexical transcription or promotion; metrics remain withheld without an exhaustive visible-start census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p165_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
