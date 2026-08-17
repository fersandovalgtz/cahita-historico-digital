import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')
links = {
    'L-001':['ALC1737-art-000569'],
    'L-002':['ALC1737-art-000570'],
    'L-003':['ALC1737-art-000571'],
    'L-004':['ALC1737-art-000572'],
    'L-005':['ALC1737-art-000573'],
    'L-006':['ALC1737-art-000574'],
    'L-007':['ALC1737-art-000575','ALC1737-art-000576','ALC1737-art-000580','ALC1737-art-000581','ALC1737-art-000582'],
}
merged={'L-007','R-003','R-017'}
under={'L-004','L-005'}
ambiguous={'R-015'}
continuation={'R-001'}
prov={
    'derivedFrom':'canonical-v0.2 candidate inventory; p171 selected article layer; p170 reconciliation edge context; p172 canonical candidates and selected layer',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}
notes={
    'L-001':'Aligned to selected 000569 (`Querella. Natebo.`) after p170 `Que-` edge/catchword material; no p170→p171 lexical continuation is asserted.',
    'L-002':'Aligned to selected 000570 (`Quizá. Hane.`). Damaged trailing material is retained within the candidate without synthesizing a new article.',
    'L-003':'Aligned to selected 000571 (`Quien? Habe?`). The OCR retains only the guide reliably, while the selected direct collation supplies the authoritative form.',
    'L-004':'Aligned to selected 000572 (`Quien eres? Habeempo?`). The group carries `Empohabeſa`-like material associated with selected 000573, whose guide boundary remains independently represented at L-005; retained `undersegmented` as reading-order leakage.',
    'L-005':'Aligned to selected 000573 (`Quien ſois. Empohabeſa?`). The group also contains severe cross-column/noise leakage including Raton-like material; retained `undersegmented` without synthesizing extra starts.',
    'L-006':'Aligned to selected 000574 (`Quixada. Taba huaſari.`).',
    'L-007':'Mega-group begins selected 000575 (`Quitarſe la porquería... Bahurina`) and visibly contains selected starts 000576 (`Rabo de animal`), 000580 (`Rajar madera`), 000581 (`Rala coſa`) and 000582 (`Rama de arbol`), plus multiple unselected OCR guide units. Selected 000577–000579 and 000583 occur in the historical selected sequence before the Rastro region but their exact microplacement is not forced from damaged OCR.',
    'R-001':'Form-only `Ahaottua.` at the top of the right column; classified as continuation from previous-column material rather than a fresh Spanish guide start. No selected article assignment is forced.',
    'R-003':'Canonical group begins a `Rastro aver`-like article and visibly contains additional Raton/other guide-like material. Retained `merged_articles`; no OCR-only internal unit is promoted or counted as a missed start without independent direct-collation support.',
    'R-015':'Canonical geometry supports a fresh lexical start in a heavily damaged multi-line block, but the Spanish guide cannot be responsibly recovered from OCR. Retained as `article/ambiguous` without promotion.',
    'R-017':'Canonical group visibly contains multiple fresh guide-like units, including `Rechinar la puerta`, `Rechinar los dientes` and `Recular`. Retained `merged_articles`; internal OCR-only starts are not promoted or censused without independent selected/direct-collation anchors.',
}

def make_row(side,n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p171-{key}'
    col='left' if side=='L' else 'right'
    linked=links.get(key,[])
    if key in continuation:
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':171,'column':col,
            'classification':'continuation','boundaryAssessment':'not_applicable','linkedArticleIds':[],
            'articleLinkStatus':'not_applicable','continuationType':'from_previous_column',
            'editorialNote':notes[key],
            'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
        }
    if key in merged: assessment='merged_articles'
    elif key in under: assessment='undersegmented'
    elif key in ambiguous: assessment='ambiguous'
    else: assessment='exact'
    note=notes.get(key)
    if note is None:
        note='Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':171,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
    }

for side,count,name in [('L',7,'p171_left_reconciliation.jsonl'),('R',17,'p171_right_reconciliation.jsonl')]:
    rows=[make_row(side,i) for i in range(1,count+1)]
    (OUT/name).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

miss_specs=[
    ('ALC1737-miss-p171-L-001',576,'Rabo de animal. Buaſiaota.','inside_candidate_group','ALC1737-vcand-p171-L-007','Selected 000576 is a distinct historical start visibly absorbed inside canonical L-007 after selected 000575.'),
    ('ALC1737-miss-p171-L-002',577,'Raer. Sibha.','between_candidates',None,'Selected 000577 occurs in the selected historical sequence between the L-007 opening region and the later Rastro region, but its exact microplacement is not forced from damaged OCR.'),
    ('ALC1737-miss-p171-L-003',578,'Rayar hazer raya. Abuitia.','between_candidates',None,'Selected 000578 lacks an independent canonical boundary; its exact microplacement is not forced from damaged OCR.'),
    ('ALC1737-miss-p171-L-004',579,'Raiz de arbol. Nahua.','between_candidates',None,'Selected 000579 lacks an independent canonical boundary; its exact microplacement is not forced from damaged OCR.'),
    ('ALC1737-miss-p171-L-005',580,'Rajar madera. Etatia.','inside_candidate_group','ALC1737-vcand-p171-L-007','Selected 000580 is visibly present inside canonical L-007 as a distinct `Rajar madera` start.'),
    ('ALC1737-miss-p171-L-006',581,'Rala coſa. Tapiolai.','inside_candidate_group','ALC1737-vcand-p171-L-007','Selected 000581 is visibly present inside canonical L-007 as a distinct `Rala` start.'),
    ('ALC1737-miss-p171-L-007',582,'Rama de arbol. Ioteme.','inside_candidate_group','ALC1737-vcand-p171-L-007','Selected 000582 is visibly present inside canonical L-007 as a distinct `Rama de arbol` start.'),
    ('ALC1737-miss-p171-L-008',583,'Rana. Batait.','between_candidates',None,'Selected 000583 precedes the Rastro region in the selected historical sequence but has no independent canonical boundary; exact microplacement is not forced from damaged OCR.'),
]
misses=[]
for mid,n,raw,mt,cid,note in miss_specs:
    misses.append({
        'missedStartId':mid,'sourceId':'ALC1737','sourcePageDigital':171,'column':'left',
        'visibleStartRaw':raw,'missType':mt,'containingCandidateId':cid,
        'linkedArticleIds':[f'ALC1737-art-{n:06d}'],'editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,
        'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p171 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None},
    })
(OUT/'p171_missed_visible_starts.jsonl').write_text('\n'.join(json.dumps(m,ensure_ascii=False) for m in misses)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':171,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':24,'left':7,'right':17,
        'classification':{'article':23,'continuation':1,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':17,'oversegmented':0,'undersegmented':2,'merged_articles':3,'ambiguous':1,'not_applicable':1},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000569','ALC1737-art-000583'],
        'declaredColumnDistribution':{'left':15,'right':0},'columnMetadataCorrectionThisPass':False,
        'articleCandidateRecordsLinked':7,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsInsideMergedCandidate':4,'selectedStartsOutsideCandidateInventory':4,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleIds':[f'ALC1737-art-{n:06d}' for n in range(576,584)],
    },
    'promotion':{'articleCandidatesPendingPromotion':16,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':31,'knownMissedStartRecords':8,'unresolvedCandidateRecords':0,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 23 article candidates plus eight selected missed starts establish at least 31 starts, but the selected layer is non-exhaustive and large merged/reading-order-leakage groups contain additional unanchored guide-like units.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p170-R-022','to':'ALC1737-vcand-p171-L-001','type':'catchword_or_edge_fragment_to_fresh_next_page_article','note':'p170 ends with `Que-` edge/catchword material; p171 L-001 opens fresh selected 000569 (`Querella`).'},
        {'from':'ALC1737-vcand-p171-L-007','to':'ALC1737-vcand-p171-R-001','type':'article_continuation_across_columns','note':'R-001 is form-only `Ahaottua.` and is retained as continuation from previous-column material without forcing a selected article assignment.'},
        {'from':'ALC1737-vcand-p171-R-017','to':'ALC1737-vcand-p172-L-001','type':'fresh_next_page_top_selected_start_missed','note':'p172 selected 000584 (`Relampago`) is a fresh top-of-page start without its own candidate; p172 L-001 begins selected 000585 (`Redaño`). No p171→p172 lexical continuation is asserted.'},
    ],
    'structuralNotes':[
        'L-007 is a `merged_articles` mega-group beginning selected 000575 and visibly containing selected 000576, 000580, 000581 and 000582 plus unselected guide-like material.',
        'Selected 000577, 000578, 000579 and 000583 are recorded conservatively `between_candidates`; exact microplacement is not inferred from damaged OCR.',
        'R-001 is the sole canonical continuation row and uses `continuationType: from_previous_column`.',
        'R-003 and R-017 are `merged_articles` based on multiple visible guide-like units; their OCR-only internal units are not promoted or counted as false negatives without independent anchors.',
        'R-015 remains `article/ambiguous` because geometry supports a fresh start while OCR does not responsibly recover its guide.',
        'No selected column metadata is corrected in this pass.'
    ],
    'nextPage':{'sourcePageDigital':172,'candidateInventoryTotal':55,'left':27,'right':28,'firstCandidate':'ALC1737-vcand-p172-L-001','firstCandidateOpening':'Redaño. Tona-aurta.','firstSelectedArticle':'ALC1737-art-000584','firstSelectedOpening':'Relampago. Beroitcme.','nextPageTopSelectedMissExpected':True},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP171LayerUsedAsAnchor':True,'p170ReconciliationUsedForOpeningEdge':True,'p172CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and known misses. OCR-only internal/adjacent units are preserved structurally without invented lexical transcription or promotion; metrics remain withheld without an exhaustive visible-start census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p171_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
