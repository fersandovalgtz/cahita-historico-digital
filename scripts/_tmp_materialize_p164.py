import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')
links = {
    'L-001':['ALC1737-art-000464'],
    'L-003':['ALC1737-art-000465'],
    'L-004':['ALC1737-art-000466'],
    'L-005':['ALC1737-art-000467'],
    'L-007':['ALC1737-art-000468'],
    'L-009':['ALC1737-art-000469'],
    'L-010':['ALC1737-art-000470'],
    'L-011':['ALC1737-art-000471'],
    'L-012':['ALC1737-art-000472'],
    'L-013':['ALC1737-art-000473'],
    'L-014':['ALC1737-art-000474'],
    'L-016':['ALC1737-art-000475'],
    'L-023':['ALC1737-art-000476'],
    'R-001':['ALC1737-art-000477'],
    'R-002':['ALC1737-art-000478'],
}
merged={'R-018','R-020','R-022'}
prov={
    'derivedFrom':'canonical-v0.2 candidate inventory; p164 selected article layer; p163 reconciliation edge context; p165 canonical candidates and selected opening',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}
notes={
    'L-001':'Fresh selected 000464 (`Nacimiento. Ioleria.`) after p163 bottom material; no p163→p164 lexical continuation is asserted.',
    'L-003':'Aligned to selected 000465 (`Nada ninguna coſa. Caita.`).',
    'L-004':'Aligned to selected 000466 (`Nadar. Bapume.`).',
    'L-005':'Aligned to selected 000467 (`Nadie por ninguno. Cahabe.`).',
    'L-007':'Aligned to selected 000468 (`Nariz. Ieca.`).',
    'L-009':'Aligned to selected 000469 (`Natura de macho. Hui.`).',
    'L-010':'Aligned to selected 000470 (`Natura de hembra. Coi.`).',
    'L-011':'Aligned to selected cross-reference 000471 (`Neceſſidad tener de alguna coſa. Buſca meneſter ſer.`).',
    'L-012':'Aligned to selected 000472 (`Negociar. Hinenca.`).',
    'L-013':'Aligned to selected 000473 (`Negociacion. Hinenguiapo.`).',
    'L-014':'Aligned to selected 000474 (`Negro color. Chuculi.`).',
    'L-016':'Aligned to selected 000475 (`Nervio. Iate.`).',
    'L-023':'Aligned to selected cross-reference 000476 (`Ninguna coſa. Buſca nada.`).',
    'R-001':'Aligned to selected 000477 (`Noez, y nogal. Lo miſmo.`). Its historical anaphora remains semantically unresolved in the selected article, but the physical boundary is exact.',
    'R-002':'Aligned to selected cross-reference 000478 (`Nombrar, poner nombre. Buſca llamar.`).',
    'R-018':'Canonical group begins a `Nudo` article and also contains a distinct `O. adv. para llamar`-like guide. It is structurally `merged_articles`, but the unselected internal start is not promoted or entered into the missed-start census without direct-collation support.',
    'R-020':'Canonical group contains distinct `Obediente` and `Obediencia` guide-like units. It is retained `merged_articles`; no internal article object is synthesized from raw OCR.',
    'R-022':'Canonical group begins `Obligación`, contains a distinct `Obrar algo`-like guide, and ends with `Obr...` edge/catchword material. It is `merged_articles`; p165 nevertheless opens a fresh selected `Obra aſſi, hechura` article, so no long p164→p165 continuation is asserted.',
}

def row(side,n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p164-{key}'
    col='left' if side=='L' else 'right'
    linked=links.get(key,[])
    assessment='merged_articles' if key in merged else 'exact'
    note=notes.get(key)
    if note is None:
        note='Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':164,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
    }

for side,count,name in [('L',29,'p164_left_reconciliation.jsonl'),('R',22,'p164_right_reconciliation.jsonl')]:
    rows=[row(side,i) for i in range(1,count+1)]
    (OUT/name).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':164,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'non_exhaustive_selected_anchor_only','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':51,'left':29,'right':22,
        'classification':{'article':51,'continuation':0,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':48,'oversegmented':0,'undersegmented':0,'merged_articles':3,'ambiguous':0,'not_applicable':0},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000464','ALC1737-art-000478'],
        'articleCandidateRecordsLinked':15,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsOutsideCandidateInventory':0,'selectedArticlesUnlinked':0,
        'semanticUnresolvedArticleIds':['ALC1737-art-000477'],
        'note':'Selected 000477 retains historical `Lo miſmo.` semantic anaphora as unresolved; this does not make its physical candidate boundary structurally unresolved.'
    },
    'promotion':{'articleCandidatesPendingPromotion':36,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':51,'knownMissedStartRecords':0,'unresolvedCandidateRecords':0,
        'unanchoredInternalGuideLikeRegions':['ALC1737-vcand-p164-R-018','ALC1737-vcand-p164-R-020','ALC1737-vcand-p164-R-022'],
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'All 51 canonical candidates are compatible with article starts, but three merged OCR groups contain additional guide-like material without independent selected/direct-collation anchors. The selected layer is non-exhaustive, so no complete visible-start denominator is asserted.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p163-R-023','to':'ALC1737-vcand-p164-L-001','type':'fresh_page_transition','note':'p164 opens fresh selected `Nacimiento. Ioleria.`; no p163→p164 lexical continuation is asserted.'},
        {'from':'ALC1737-vcand-p164-R-022','to':'ALC1737-vcand-p165-L-001','type':'catchword_or_edge_fragment_to_fresh_next_page_article','note':'R-022 ends with `Obr...` after `Obligación` and `Obrar algo`-like material; p165 opens fresh selected `Obra aſſi, hechura. Chupari.`.'},
    ],
    'structuralNotes':[
        'All 51 canonical p164 rows are retained as article boundaries; there are no continuation or structurally unresolved candidate rows.',
        'R-018, R-020 and R-022 are `merged_articles` because each OCR group visibly contains more than one guide-like unit.',
        'Those unselected internal units are not promoted and are not counted as missed visible starts without independent direct-collation anchors.',
        'Selected 000477 (`Noez, y nogal. Lo miſmo.`) is semantically unresolved at the article level, while its physical boundary remains exact.',
    ],
    'nextPage':{'sourcePageDigital':165,'candidateInventoryTotal':56,'left':29,'right':27,'firstCandidate':'ALC1737-vcand-p165-L-001','firstSelectedArticle':'ALC1737-art-000479','opening':'Obra aſſi, hechura. Chupari.'},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP164LayerUsedAsAnchor':True,'p163ReconciliationUsedForOpeningEdge':True,'p165CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated article links. OCR-only internal guide-like units in merged candidates are preserved as structural notes without promotion or census inflation; metrics remain withheld without exhaustive visible-start coverage.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p164_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
