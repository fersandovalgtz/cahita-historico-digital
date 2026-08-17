import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')
links = {
    'L-001':['ALC1737-art-000494'],
    'L-002':['ALC1737-art-000495'],
    'L-003':['ALC1737-art-000496','ALC1737-art-000497'],
    'L-004':['ALC1737-art-000498'],
    'L-005':['ALC1737-art-000499'],
    'L-006':['ALC1737-art-000500'],
    'L-007':['ALC1737-art-000501'],
    'L-008':['ALC1737-art-000502'],
    'L-010':['ALC1737-art-000503'],
    'L-011':['ALC1737-art-000504'],
    'L-012':['ALC1737-art-000505'],
    'L-013':['ALC1737-art-000506'],
    'L-014':['ALC1737-art-000507'],
    'L-015':['ALC1737-art-000508'],
}
merged={'L-003'}
under={'L-007','R-008','R-022'}
prov={
    'derivedFrom':'canonical-v0.2 candidate inventory; p166 selected article layer; p165 reconciliation edge context; p167 canonical candidates and selected opening',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}
notes={
    'L-001':'Fresh selected 000494 (`Paga tal. Bebeti.`) after the distinct p165 `Padrino` article; no p165→p166 lexical continuation is asserted.',
    'L-002':'Aligned to selected 000495 (`Paja generalmente. Baſo.`).',
    'L-003':'Merged selected starts 000496 (`Palabra. Noqui.`) and 000497 (`Palma arbol conocido. Taco.`); the second selected start lacks its own canonical boundary and is recorded separately as a known internal miss.',
    'L-004':'Aligned to selected 000498 (`Palma otra. Ilitaco.`).',
    'L-005':'Aligned to selected 000499 (`Palma de la mano. Mambetari.`).',
    'L-006':'Aligned to selected 000500 (`Palo. Cuta.`).',
    'L-007':'Aligned to selected cross-reference 000501 (`Palo para eſcarbar tierra. Buſca coa.`). The OCR group also carries displaced `brazo.` material from the neighboring selected Paletilla region, so the group is retained `undersegmented` without synthesizing another start.',
    'L-008':'Aligned to selected 000502 (`Paletilla del brazo. Hapari.`). Its missing tail/form in this candidate is visible as reading-order leakage elsewhere in the OCR, so the selected direct collation remains the transcription authority.',
    'L-010':'Aligned to selected 000503 (`Paloma torcaz. Huocou.`).',
    'L-011':'Aligned to selected 000504 (`Paloma parda. Meretau.`).',
    'L-012':'Aligned to selected 000505 (`Paloma. Batui.`).',
    'L-013':'Aligned to selected 000506 (`Paloma. Omocoli.`).',
    'L-014':'Aligned to selected 000507 (`Paloma. Cucu.`).',
    'L-015':'Aligned to selected 000508 (`Palomilla. Baeſebela.`).',
    'R-008':'Distinct Partear-like lexical start. The OCR group also contains `tierra` and `Hapari`-like material displaced from selected left-column entries 000501/000502; retained `undersegmented` as reading-order leakage, without extra promotion.',
    'R-009':'Distinct Partir-en-partes-like lexical start; damaged `Buſca olor.`-like trailing material is preserved as OCR uncertainty and is not promoted as an independent article.',
    'R-022':'Distinct damaged Pesar-like lexical start followed by `Paſſo`-like edge/catchword material. P167 L-001 opens fresh selected 000509, so no p166→p167 lexical continuation is asserted.',
}

def row(side,n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p166-{key}'
    col='left' if side=='L' else 'right'
    linked=links.get(key,[])
    if key in merged: assessment='merged_articles'
    elif key in under: assessment='undersegmented'
    else: assessment='exact'
    note=notes.get(key)
    if note is None:
        note='Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':166,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
    }

for side,count,name in [('L',28,'p166_left_reconciliation.jsonl'),('R',22,'p166_right_reconciliation.jsonl')]:
    rows=[row(side,i) for i in range(1,count+1)]
    (OUT/name).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

miss={
    'missedStartId':'ALC1737-miss-p166-L-001','sourceId':'ALC1737','sourcePageDigital':166,'column':'left',
    'visibleStartRaw':'Palma arbol conocido. Taco.','missType':'inside_candidate_group',
    'containingCandidateId':'ALC1737-vcand-p166-L-003','linkedArticleIds':['ALC1737-art-000497'],
    'editorialNote':'Selected 000497 is a distinct historical start absorbed inside canonical L-003 after selected 000496 (`Palabra`). Recorded as a known internal false negative without claiming exhaustive visible-start coverage.',
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
    'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p166 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None},
}
(OUT/'p166_missed_visible_starts.jsonl').write_text(json.dumps(miss,ensure_ascii=False)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':166,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':50,'left':28,'right':22,
        'classification':{'article':50,'continuation':0,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':46,'oversegmented':0,'undersegmented':3,'merged_articles':1,'ambiguous':0,'not_applicable':0},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000494','ALC1737-art-000508'],
        'articleCandidateRecordsLinked':14,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsInsideMergedCandidate':1,'selectedStartsOutsideCandidateInventory':0,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleIds':['ALC1737-art-000497'],
    },
    'promotion':{'articleCandidatesPendingPromotion':36,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':51,'knownMissedStartRecords':1,'unresolvedCandidateRecords':0,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 50 article candidates plus selected internal miss 000497 establish at least 51 starts, but the selected layer is non-exhaustive and OCR reading-order leakage prevents a complete visible-start denominator.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p165-R-027','to':'ALC1737-vcand-p166-L-001','type':'fresh_page_transition','note':'p166 opens fresh selected 000494 `Paga tal. Bebeti.`.'},
        {'from':'ALC1737-vcand-p166-R-022','to':'ALC1737-vcand-p167-L-001','type':'catchword_or_edge_fragment_to_fresh_next_page_article','note':'R-022 ends with `Paſſo`-like edge/catchword material; p167 L-001 opens fresh selected 000509 `Paſſo de las beſtias. Arabuerama.`.'},
    ],
    'structuralNotes':[
        'All 50 canonical p166 rows are retained as article boundaries; no canonical continuation or structurally unresolved row is asserted.',
        'L-003 is `merged_articles` because it contains selected 000496 and selected 000497; 000497 is recorded as the known internal missed start.',
        'L-007 and R-008 preserve cross-column reading-order leakage tied to selected 000501/000502 and are retained `undersegmented` without synthesized articles.',
        'R-022 is `undersegmented` because it contains a distinct damaged Pesar-like start plus a `Paſſo`-like edge/catchword; p167 nevertheless opens fresh.'
    ],
    'nextPage':{'sourcePageDigital':167,'candidateInventoryTotal':55,'left':30,'right':25,'firstCandidate':'ALC1737-vcand-p167-L-001','firstSelectedArticle':'ALC1737-art-000509','opening':'Paſſo de las beſtias. Arabuerama.'},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP166LayerUsedAsAnchor':True,'p165ReconciliationUsedForOpeningEdge':True,'p167CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and the known internal miss. OCR-only adjacent/cross-column leakage is preserved structurally without invented lexical transcription or promotion; metrics remain withheld without an exhaustive visible-start census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p166_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
