import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')

links = {
    'L-001':['ALC1737-art-000450'],
    'L-005':['ALC1737-art-000451'],
    'L-007':['ALC1737-art-000452'],
    'L-008':['ALC1737-art-000453'],
    'L-009':['ALC1737-art-000454'],
    'L-010':['ALC1737-art-000455'],
    'L-014':['ALC1737-art-000456'],
    'L-015':['ALC1737-art-000457'],
    'L-016':['ALC1737-art-000458'],
    'L-017':['ALC1737-art-000459'],
    'L-019':['ALC1737-art-000460'],
    'L-020':['ALC1737-art-000461'],
    'R-020':['ALC1737-art-000462'],
    'R-021':['ALC1737-art-000463'],
}
continuations = {'L-004','L-011','L-013','L-023','R-001','R-005','R-007'}
continuation_links = {'L-011':['ALC1737-art-000455']}
under = {'L-001','L-002','L-003','L-007','R-023'}
over = {'L-010','L-012','L-022','L-026','R-004','R-006'}

provenance = {
    'derivedFrom':'canonical-v0.2 candidate inventory; p163 selected article layer; p162 reconciliation edge context; p164 canonical candidate and selected opening',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}

notes = {
    'L-001':'Canonical page opening begins in the tail `...cebo.` of missed selected 000449 (`Mozo de edad. Buſca mancebo.`) and then opens selected 000450 (`Mofar, eſcarnecer`). Classified as article with undersegmented boundary; 000449 is represented in the missed-start layer.',
    'L-002':'Begins with continuation/cross-reference target material from selected 000450 (`menoſpreciar`) and then opens a fresh unselected `Moho como de pan` article. Retained undersegmented without reconstructing the local micro-order.',
    'L-003':'Begins with the tail of the preceding `Moho como de pan` article and then opens fresh `Moho como de hierro`; the latter continues physically into L-004.',
    'L-004':'Continuation of the `Moho como de hierro` article begun inside L-003; not a fresh lexical start.',
    'L-005':'Aligned to selected 000451 (`Mojarſe. Comonac.`).',
    'L-006':'Distinct `Mojarſe cayendo en el agua`-like article start; its form leaks into the following OCR group but no selected anchor supports additional splitting.',
    'L-007':'Begins with continuation/form material from L-006 and then opens selected 000452 (`Moler. Tuſe.`); retained undersegmented.',
    'L-008':'Aligned to selected 000453 (`Moledor de maíz. Mata.`).',
    'L-009':'Aligned to selected 000454 (`Mano ſuya. Tutua.`).',
    'L-010':'Aligned to selected 000455 (`Molendero el que muele. Tuſeme.`) and split from its form continuation L-011.',
    'L-011':'Form-only continuation `Tuſeme.` of selected 000455; not a fresh lexical start.',
    'L-012':'Distinct `Mondar algo, como habas, papas, &c.` article start split from its continuation L-013.',
    'L-013':'Continuation of the `Mondar algo...` article begun in L-012.',
    'L-014':'Aligned to selected 000456 (`Monte. Pochoi.`).',
    'L-015':'Aligned to selected 000457 (`Montear. Buſca caçar.`).',
    'L-016':'Aligned to selected 000458 (`Morar. Home.`).',
    'L-017':'Aligned to selected 000459 (`Morcielago Ave nocturna. Sochic.`).',
    'L-019':'Aligned to selected 000460 (`Morder. Queque.`).',
    'L-020':'Aligned to selected 000461 (`Mordedura. Quiri.`).',
    'L-022':'Distinct `Morirſe de frío`-like article start split from form continuation L-023.',
    'L-023':'Form-only continuation of the `Morirſe de frío`-like article begun in L-022.',
    'L-026':'Distinct `Mosquito, que llaman gegen` article start continuing across the column boundary into R-001.',
    'R-001':'Continuation from p163 L-026 across the column boundary; not a fresh lexical start.',
    'R-004':'Distinct `Mostrar con el dedo. Buſca apuntar` article start split from continuation R-005.',
    'R-005':'Continuation/cross-reference target `apuntar` of the article begun in R-004.',
    'R-006':'Distinct `Moverſe, menearſe` article start split from form continuation R-007.',
    'R-007':'Continuation `huante` of the article begun in R-006.',
    'R-020':'Aligned to selected 000462 (`Muger. Hamut.`).',
    'R-021':'Aligned to selected 000463 (`Mundo. Ania.`); trailing OCR leakage is not promoted as another start.',
    'R-023':'Distinct `Murmuyo`-like article start whose OCR group absorbs damaged page-bottom/catchword-like material. p164 opens fresh selected 000464 `Nacimiento. Ioleria.`, so no transpage continuation is asserted.',
}

def note_for(key, linked):
    if key in notes:
        return notes[key]
    if linked:
        return 'Aligned to selected direct-collation article anchor.'
    return 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'

def row(side, n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p163-{key}'
    col='left' if side=='L' else 'right'
    if key in continuations:
        linked=continuation_links.get(key,[])
        ctype='from_previous_column' if key=='R-001' else 'from_previous_line'
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':163,'column':col,
            'classification':'continuation','boundaryAssessment':'not_applicable','linkedArticleIds':linked,
            'articleLinkStatus':'not_applicable','continuationType':ctype,'editorialNote':note_for(key,linked),
            'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
        }
    linked=links.get(key,[])
    assessment='undersegmented' if key in under else ('oversegmented' if key in over else 'exact')
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':163,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note_for(key,linked),
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
    }

for side,count,filename in [('L',26,'p163_left_reconciliation.jsonl'),('R',23,'p163_right_reconciliation.jsonl')]:
    rows=[row(side,i) for i in range(1,count+1)]
    (OUT/filename).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

miss={
    'missedStartId':'ALC1737-miss-p163-L-001','sourceId':'ALC1737','sourcePageDigital':163,'column':'left',
    'visibleStartRaw':'Mozo de edad. Buſca mancebo.','missType':'page_or_column_edge','containingCandidateId':None,
    'linkedArticleIds':['ALC1737-art-000449'],
    'editorialNote':'Fresh selected p163 page-opening article begins before canonical L-001; L-001 starts already in its tail `...cebo.` and then contains selected 000450. Recorded as a known page-top false negative without treating the p162 catchword as a lexical continuation.',
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
    'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of p162 catchword context, canonical p163 geometry/OCR and pre-existing selected direct-collation anchors; no independent human verification','processedAt':None},
}
(OUT/'p163_missed_visible_starts.jsonl').write_text(json.dumps(miss,ensure_ascii=False)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':163,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':49,'left':26,'right':23,
        'classification':{'article':42,'continuation':7,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':31,'oversegmented':6,'undersegmented':5,'merged_articles':0,'ambiguous':0,'not_applicable':7},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000449','ALC1737-art-000463'],
        'articleCandidateRecordsLinked':14,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':1,
        'selectedStartsOutsideCandidateInventory':1,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleIds':['ALC1737-art-000449'],
    },
    'promotion':{'articleCandidatesPendingPromotion':28,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':43,'knownMissedStartRecords':1,'unresolvedCandidateRecords':0,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 42 article candidates plus selected page-top miss 000449 establish at least 43 starts, but the selected layer is non-exhaustive and undersegmented OCR groups may contain additional unanchored starts.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p162-R-019','to':'ALC1737-art-000449','type':'catchword_to_fresh_next_page_article','note':'p162 catchword `Mozo` anticipates fresh p163 selected 000449; it is not a lexical continuation.'},
        {'from':'ALC1737-art-000449','to':'ALC1737-vcand-p163-L-001','type':'missed_page_top_start_then_tail','note':'Canonical L-001 begins in the tail `...cebo.` of selected 000449 and then opens selected 000450.'},
        {'from':'ALC1737-vcand-p163-L-003','to':'ALC1737-vcand-p163-L-004','type':'article_continuation','note':'`Moho como de hierro` continues into L-004.'},
        {'from':'ALC1737-vcand-p163-L-010','to':'ALC1737-vcand-p163-L-011','type':'article_continuation','note':'Selected 000455 `Molendero el que muele. Tuſeme.` continues into L-011.'},
        {'from':'ALC1737-vcand-p163-L-012','to':'ALC1737-vcand-p163-L-013','type':'article_continuation','note':'`Mondar algo...` continues into L-013.'},
        {'from':'ALC1737-vcand-p163-L-022','to':'ALC1737-vcand-p163-L-023','type':'article_continuation','note':'`Morirſe de frío`-like article continues into L-023.'},
        {'from':'ALC1737-vcand-p163-L-026','to':'ALC1737-vcand-p163-R-001','type':'article_continuation_across_columns','note':'`Mosquito, que llaman gegen` continues across the column boundary.'},
        {'from':'ALC1737-vcand-p163-R-004','to':'ALC1737-vcand-p163-R-005','type':'article_continuation','note':'`Mostrar con el dedo. Buſca apuntar` continues into R-005.'},
        {'from':'ALC1737-vcand-p163-R-006','to':'ALC1737-vcand-p163-R-007','type':'article_continuation','note':'`Moverſe, menearſe` continues into R-007.'},
        {'from':'ALC1737-vcand-p163-R-023','to':'ALC1737-vcand-p164-L-001','type':'fresh_page_transition','note':'p164 opens fresh selected 000464 `Nacimiento. Ioleria.`; no p163→p164 lexical continuation is asserted.'},
    ],
    'structuralNotes':[
        'The canonical extractor misses selected 000449 at the page top; L-001 begins in its tail and then opens selected 000450.',
        'L-002, L-003 and L-007 are undersegmented because each starts with continuation material before a fresh lexical start.',
        'Seven canonical rows are continuations rather than fresh starts, including the L-026→R-001 cross-column continuation.',
        'R-023 remains an article boundary with undersegmented page-bottom noise/catchword-like material; p164 opens fresh `Nacimiento`.'
    ],
    'nextPage':{'sourcePageDigital':164,'candidateInventoryTotal':51,'left':29,'right':22,'firstCandidate':'ALC1737-vcand-p164-L-001','firstSelectedArticle':'ALC1737-art-000464','opening':'Nacimiento. Ioleria.'},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP163LayerUsedAsAnchor':True,'p162ReconciliationUsedForOpeningEdge':True,'p164CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and the known page-top miss. OCR-only internal ambiguity is preserved without promotion; metrics remain withheld without an exhaustive visible-start census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p163_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
