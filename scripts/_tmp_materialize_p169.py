import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')
links = {
    'L-001':['ALC1737-art-000539','ALC1737-art-000540','ALC1737-art-000541','ALC1737-art-000542'],
    'L-013':['ALC1737-art-000543'],
    'L-014':['ALC1737-art-000544'],
    'L-015':['ALC1737-art-000545'],
    'L-016':['ALC1737-art-000546'],
    'L-017':['ALC1737-art-000547'],
    'L-018':['ALC1737-art-000548'],
    'L-019':['ALC1737-art-000549'],
    'R-001':['ALC1737-art-000550'],
    'R-002':['ALC1737-art-000551'],
    'R-003':['ALC1737-art-000552'],
    'R-004':['ALC1737-art-000553'],
}
merged={'L-001','R-009','R-016'}
under={'L-002','L-010'}
ambiguous={'R-005'}
continuation={'L-003'}
prov={
    'derivedFrom':'canonical-v0.2 candidate inventory; p169 selected article layer; p168 reconciliation edge context; p170 canonical candidates and selected layer',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}
notes={
    'L-001':'Mega-group opens in the tail `...bajas. Buſca pedernal prieto.` of selected 000539 (`Piedra de que ſe ſacan navajas`), then contains selected starts 000540 (`Piel`), 000541 (`Pino`) and 000542 (`Pinal`) plus several unselected OCR guide units (`Pintar`/`Pintor`/`Pinto`/`Pintura`/`Piña`/`Piojo`-like). Retained `merged_articles`; only selected/direct-collation starts are entered into the missed-start layer.',
    'L-002':'Group begins with a tail-like `huoBi.` fragment and then opens an unselected `Piſar alguna coſa`-like article whose Cahita form continues into L-003. Retained `undersegmented`; continuity is modeled explicitly without inventing a selected article.',
    'L-003':'Form-only `huotle.` continuation of the unselected `Piſar alguna coſa`-like article begun in L-002; not a fresh lexical start.',
    'L-010':'Distinct `Pitahalla órgano`-like start with trailing `huefo.` adjacent/reading-order material; retained `undersegmented` without synthesizing another article.',
    'L-013':'Aligned to selected 000543 (`Planta del pie. Huoc betari.`).',
    'L-014':'Aligned to selected 000544 (`Plantar arboles. Echa.`).',
    'L-015':'Aligned to selected cross-reference 000545 (`Platicar con otro. Buſca parlar.`).',
    'L-016':'Aligned to selected 000546 (`Platica tal. Etchoa.`).',
    'L-017':'Aligned to selected 000547 (`Plata. Teoquita.`).',
    'L-018':'Aligned to selected 000548 (`Plato. Lo miſmo.`). Its historical anaphora remains semantically unresolved in the selected article, but the physical boundary is exact.',
    'L-019':'Aligned to selected cross-reference 000549 (`Placer regocijo. Buſca gozo.`).',
    'R-001':'Aligned to selected cross-reference 000550 (`Plazo poner. Buſca ſeñalar dia.`).',
    'R-002':'Aligned to selected cross-reference 000551 (`Pleyto aver. Buſca pelear.`).',
    'R-003':'Aligned to selected 000552 (`Pluma. Maſa.`).',
    'R-004':'Aligned to selected cross-reference 000553 (`Plumero. Buſca penacho.`).',
    'R-005':'Canonical geometry supports a fresh lexical start between `Plumero` and `Pobre eſtar`, but OCR is too damaged to recover the guide responsibly; retained as `article` with `ambiguous` boundary assessment and no promotion.',
    'R-009':'Canonical group contains distinct `Pocas vezes` and second `poco` guide-like units. Retained `merged_articles`; the unselected internal start is not promoted or counted as a missed start without independent direct-collation support.',
    'R-016':'Large canonical group contains multiple distinct guide-like units (`Polilla`, `Polvos`, `Pollo hijo de gallina`, `Poner`, further `Poner...`, `Ponerſe el capote`, `Por...`, `Por ventura`, etc.). Retained `merged_articles`; no OCR-only internal unit is promoted or added to the missed-start census without selected/direct-collation support.',
}

def make_row(side,n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p169-{key}'
    col='left' if side=='L' else 'right'
    linked=links.get(key,[])
    if key in continuation:
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':169,'column':col,
            'classification':'continuation','boundaryAssessment':'not_applicable','linkedArticleIds':[],
            'articleLinkStatus':'not_applicable','continuationType':'from_previous_line',
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
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':169,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
    }

for side,count,name in [('L',19,'p169_left_reconciliation.jsonl'),('R',16,'p169_right_reconciliation.jsonl')]:
    rows=[make_row(side,i) for i in range(1,count+1)]
    (OUT/name).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

misses=[
    {
        'missedStartId':'ALC1737-miss-p169-L-001','sourceId':'ALC1737','sourcePageDigital':169,'column':'left',
        'visibleStartRaw':'Piedra de que ſe ſacan navajas. Buſca pedernal prieto.','missType':'page_or_column_edge','containingCandidateId':None,
        'linkedArticleIds':['ALC1737-art-000539'],
        'editorialNote':'Fresh selected 000539 begins above/before canonical L-001; L-001 starts only in its tail `...bajas. Buſca pedernal prieto.`. The p168 `Pie-` edge fragment is not treated as lexical continuation.',
    },
    {
        'missedStartId':'ALC1737-miss-p169-L-002','sourceId':'ALC1737','sourcePageDigital':169,'column':'left',
        'visibleStartRaw':'Piel. Buſca pelo.','missType':'inside_candidate_group','containingCandidateId':'ALC1737-vcand-p169-L-001',
        'linkedArticleIds':['ALC1737-art-000540'],
        'editorialNote':'Selected 000540 is a distinct start inside the canonical L-001 mega-group after the tail of 000539.',
    },
    {
        'missedStartId':'ALC1737-miss-p169-L-003','sourceId':'ALC1737','sourcePageDigital':169,'column':'left',
        'visibleStartRaw':'Pino. Huoco.','missType':'inside_candidate_group','containingCandidateId':'ALC1737-vcand-p169-L-001',
        'linkedArticleIds':['ALC1737-art-000541'],
        'editorialNote':'Selected 000541 is a distinct start inside canonical L-001.',
    },
    {
        'missedStartId':'ALC1737-miss-p169-L-004','sourceId':'ALC1737','sourcePageDigital':169,'column':'left',
        'visibleStartRaw':'Pinal. Huocoburii.','missType':'inside_candidate_group','containingCandidateId':'ALC1737-vcand-p169-L-001',
        'linkedArticleIds':['ALC1737-art-000542'],
        'editorialNote':'Selected 000542 is a distinct start inside canonical L-001. Additional OCR-only starts later in the same mega-group are deliberately not added to this census without independent direct-collation anchors.',
    },
]
for m in misses:
    m.update({
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,
        'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p169 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None},
    })
(OUT/'p169_missed_visible_starts.jsonl').write_text('\n'.join(json.dumps(m,ensure_ascii=False) for m in misses)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':169,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':35,'left':19,'right':16,
        'classification':{'article':34,'continuation':1,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':28,'oversegmented':0,'undersegmented':2,'merged_articles':3,'ambiguous':1,'not_applicable':1},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000539','ALC1737-art-000553'],
        'articleCandidateRecordsLinked':12,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsInsideMergedCandidate':3,'selectedStartsOutsideCandidateInventory':1,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleIds':['ALC1737-art-000539','ALC1737-art-000540','ALC1737-art-000541','ALC1737-art-000542'],
        'semanticUnresolvedArticleIds':['ALC1737-art-000548'],
        'note':'Selected 000548 retains historical `Lo miſmo.` semantic anaphora as unresolved; this does not make its physical candidate boundary structurally unresolved.'
    },
    'promotion':{'articleCandidatesPendingPromotion':22,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':37,'knownMissedStartRecords':4,'unresolvedCandidateRecords':0,
        'precision':None,'recall':None,'f1':None,
        'minimumAccountingNote':'The 34 article-classified candidate regions cannot simply be added to four missed starts because L-001 is not itself a fresh boundary; it opens in the tail of selected 000539. Minimum accounting therefore uses 33 other article regions + the four selected starts 000539–000542 = 37. Additional OCR-only starts in L-001/R-009/R-016 are withheld from the minimum without independent selected/direct-collation anchors.',
        'reasonMetricsWithheld':'The selected layer is non-exhaustive and large merged OCR groups contain additional unanchored guide-like units; a complete visible-start denominator is not established.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p168-R-018','to':'ALC1737-vcand-p169-L-001','type':'catchword_or_edge_fragment_to_fresh_article_start_missed_at_page_edge','note':'p168 ends with `Pie-`; selected p169 000539 is a fresh `Piedra...` article whose guide start is missed, while L-001 begins only in its tail.'},
        {'from':'ALC1737-vcand-p169-L-002','to':'ALC1737-vcand-p169-L-003','type':'article_continuation','note':'An unselected `Piſar alguna coſa`-like article begins in L-002 and its Cahita form continues into form-only L-003.'},
        {'from':'ALC1737-vcand-p169-R-016','to':'ALC1737-vcand-p170-L-001','type':'fresh_page_transition_with_next_page_top_miss','note':'p169 R-016 contains several `Por...` entries and ends with `Por ventura`; p170 selected 000554 (`Por donde?`) is a fresh top-of-page start without its own canonical candidate, while p170 L-001 begins 000555 (`Porqué?`). No long p169→p170 continuation is asserted.'},
    ],
    'structuralNotes':[
        'L-001 is a `merged_articles` mega-group. It opens in the continuation tail of selected 000539, contains selected starts 000540–000542 and several additional unselected OCR guide units. Only selected/direct-collation starts are entered into the missed-start layer.',
        'L-002 is `undersegmented` and L-003 is the sole canonical `continuation` row.',
        'L-010 is `undersegmented` because of trailing adjacent `huefo.` material.',
        'R-005 remains an `article` with `ambiguous` boundary assessment because geometry supports a fresh start while OCR does not responsibly recover its guide.',
        'R-009 and R-016 are `merged_articles`; their OCR-only internal units are not promoted or counted as false negatives without independent anchors.',
        'Selected 000548 (`Plato. Lo miſmo.`) is semantically unresolved at the article layer while physical L-018 remains exact.'
    ],
    'nextPage':{'sourcePageDigital':170,'candidateInventoryTotal':48,'left':26,'right':22,'firstCandidate':'ALC1737-vcand-p170-L-001','firstCandidateOpening':'Porqué? Hita bechibuo?','firstSelectedArticle':'ALC1737-art-000554','firstSelectedOpening':'Por donde? Hacumbichaca?','nextPageTopSelectedMissExpected':true},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP169LayerUsedAsAnchor':True,'p168ReconciliationUsedForOpeningEdge':True,'p170CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and known misses. OCR-only internal/adjacent units are preserved structurally without invented lexical transcription or promotion; metrics remain withheld without an exhaustive visible-start census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p169_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
