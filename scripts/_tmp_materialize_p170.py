import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')
links = {
    'L-001':['ALC1737-art-000555'],
    'L-002':['ALC1737-art-000556'],
    'L-003':['ALC1737-art-000557'],
    'L-004':['ALC1737-art-000558'],
    'L-005':['ALC1737-art-000559'],
    'L-006':['ALC1737-art-000560'],
    'L-007':['ALC1737-art-000561'],
    'L-008':['ALC1737-art-000562','ALC1737-art-000563'],
    'L-010':['ALC1737-art-000564'],
    'L-012':['ALC1737-art-000565'],
    'L-013':['ALC1737-art-000566'],
    'L-014':['ALC1737-art-000567'],
}
merged={'L-008','L-024'}
under={'L-004','R-022'}
prov={
    'derivedFrom':'canonical-v0.2 candidate inventory; p170 selected article layer; p169 reconciliation edge context; p171 canonical candidates and selected layer',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}
notes={
    'L-001':'Aligned to selected 000555 (`Porqué? Hita bechibuo?`). Selected 000554 (`Por donde? Hacumbichaca?`) is a fresh page-top start before L-001 and is recorded separately as a missed start.',
    'L-002':'Aligned to selected 000556 (`Poſſeer. Ahipure.`).',
    'L-003':'Aligned to selected 000557 (`Pozo. Batequi.`).',
    'L-004':'Aligned to selected 000558 (`Predicar hazer ſermon. Hinabaca.`). The OCR group also carries `Hinababacame`-like material from selected 000559, whose guide boundary remains independently represented at L-005; retained `undersegmented` as reading-order leakage.',
    'L-005':'Aligned to selected 000559 (`Predicador. Hinababacame.`).',
    'L-006':'Aligned to selected 000560 (`Predicacion. Hinabacame.`).',
    'L-007':'Aligned to selected 000561 (`Preguntar. Natema.`).',
    'L-008':'Merged selected starts 000562 (`Pregunta. Atema.`) and 000563 (`Premiar. Buſca pagar.`); 000563 lacks an independent canonical boundary and is recorded separately as a known internal miss.',
    'L-010':'Aligned to selected 000564 (`Preñada eſtar. Tomaca.`).',
    'L-012':'Aligned to selected 000565 (`Preſto, adv. Banſe.`).',
    'L-013':'Aligned to selected cross-reference 000566 (`Prieto. Buſca negro.`).',
    'L-014':'Aligned to selected 000567 (`Primero. Nepacki.`).',
    'L-024':'Canonical group begins a `Proximo`-like article and visibly contains a second `Publico ſer`-like guide unit. Retained `merged_articles`; the unselected internal start is not promoted or counted as a missed start without independent direct-collation support.',
    'R-001':'Distinct `Pulga. Teput.` article start. Selected 000568 (`Puerco, ò puerca. Cobuu.`) occurs above/before R-001 at the right-column top and is recorded separately as a page/column-edge missed start.',
    'R-022':'Distinct Querellarse-like lexical start plus trailing `Que-` edge/catchword material. P171 L-001 opens fresh selected 000569 (`Querella. Natebo.`), so no p170→p171 lexical continuation is asserted.',
}

def row(side,n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p170-{key}'
    col='left' if side=='L' else 'right'
    linked=links.get(key,[])
    if key in merged: assessment='merged_articles'
    elif key in under: assessment='undersegmented'
    else: assessment='exact'
    note=notes.get(key)
    if note is None:
        note='Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':170,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
    }

for side,count,name in [('L',26,'p170_left_reconciliation.jsonl'),('R',22,'p170_right_reconciliation.jsonl')]:
    rows=[row(side,i) for i in range(1,count+1)]
    (OUT/name).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

misses=[
    {
        'missedStartId':'ALC1737-miss-p170-L-001','sourceId':'ALC1737','sourcePageDigital':170,'column':'left',
        'visibleStartRaw':'Por donde? Hacumbichaca?','missType':'page_or_column_edge','containingCandidateId':None,
        'linkedArticleIds':['ALC1737-art-000554'],
        'editorialNote':'Selected 000554 is a fresh page-top article before canonical L-001 (`Porqué?`). P169 R-016 contains earlier `Por...` entries but no long lexical continuation is asserted.',
    },
    {
        'missedStartId':'ALC1737-miss-p170-L-002','sourceId':'ALC1737','sourcePageDigital':170,'column':'left',
        'visibleStartRaw':'Premiar. Buſca pagar.','missType':'inside_candidate_group','containingCandidateId':'ALC1737-vcand-p170-L-008',
        'linkedArticleIds':['ALC1737-art-000563'],
        'editorialNote':'Selected 000563 is a distinct cross-reference start absorbed inside canonical L-008 after selected 000562 (`Pregunta`).',
    },
    {
        'missedStartId':'ALC1737-miss-p170-R-001','sourceId':'ALC1737','sourcePageDigital':170,'column':'right',
        'visibleStartRaw':'Puerco, ò puerca. Cobuu.','missType':'page_or_column_edge','containingCandidateId':None,
        'linkedArticleIds':['ALC1737-art-000568'],
        'editorialNote':'Selected 000568 belongs to the right column and precedes canonical R-001 (`Pulga. Teput.`), but no independent canonical boundary represents its guide start.',
    },
]
for m in misses:
    m.update({
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,
        'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p170 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None},
    })
(OUT/'p170_missed_visible_starts.jsonl').write_text('\n'.join(json.dumps(m,ensure_ascii=False) for m in misses)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':170,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':48,'left':26,'right':22,
        'classification':{'article':48,'continuation':0,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':44,'oversegmented':0,'undersegmented':2,'merged_articles':2,'ambiguous':0,'not_applicable':0},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000554','ALC1737-art-000568'],
        'articleCandidateRecordsLinked':12,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsInsideMergedCandidate':1,'selectedStartsOutsideCandidateInventory':2,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleIds':['ALC1737-art-000554','ALC1737-art-000563','ALC1737-art-000568'],
    },
    'promotion':{'articleCandidatesPendingPromotion':36,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':51,'knownMissedStartRecords':3,'unresolvedCandidateRecords':0,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 48 article candidates plus three selected missed starts establish at least 51 starts, but the selected layer is non-exhaustive and merged/undersegmented OCR groups may contain additional unanchored starts.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p169-R-016','to':'ALC1737-vcand-p170-L-001','type':'fresh_page_transition_with_top_selected_miss','note':'p170 selected 000554 (`Por donde?`) is a fresh top-of-page start without its own candidate; L-001 begins selected 000555 (`Porqué?`).'},
        {'from':'ALC1737-vcand-p170-R-022','to':'ALC1737-vcand-p171-L-001','type':'catchword_or_edge_fragment_to_fresh_next_page_article','note':'R-022 ends with `Que-` edge/catchword material; p171 L-001 opens fresh selected 000569 (`Querella. Natebo.`).'}
    ],
    'structuralNotes':[
        'All 48 canonical p170 rows are retained as article boundaries; no canonical continuation or structurally unresolved row is asserted.',
        'Selected 000554 and 000568 are page/column-edge starts outside the canonical inventory; selected 000563 is an internal start absorbed in L-008.',
        'L-008 and L-024 are `merged_articles`; only the selected internal start 000563 is added to the missed-start census.',
        'L-004 and R-022 are `undersegmented` because of reading-order leakage and page-edge/catchword material, respectively.',
        'No OCR-only internal unit is promoted or counted as a false negative without selected/direct-collation support.'
    ],
    'nextPage':{'sourcePageDigital':171,'candidateInventoryTotal':24,'left':7,'right':17,'firstCandidate':'ALC1737-vcand-p171-L-001','firstSelectedArticle':'ALC1737-art-000569','opening':'Querella. Natebo.'},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP170LayerUsedAsAnchor':True,'p169ReconciliationUsedForOpeningEdge':True,'p171CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and known misses. OCR-only internal/adjacent units are preserved structurally without invented lexical transcription or promotion; metrics remain withheld without an exhaustive visible-start census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p170_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
