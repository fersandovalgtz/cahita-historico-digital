import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')
links = {
    'L-002':['ALC1737-art-000524'],
    'L-003':['ALC1737-art-000525'],
    'L-004':['ALC1737-art-000526'],
    'L-005':['ALC1737-art-000527'],
    'L-006':['ALC1737-art-000529'],
    'L-007':['ALC1737-art-000532','ALC1737-art-000533'],
    'L-009':['ALC1737-art-000534'],
    'L-010':['ALC1737-art-000535'],
    'L-011':['ALC1737-art-000536'],
    'L-013':['ALC1737-art-000537'],
    'L-014':['ALC1737-art-000538'],
}
merged={'L-007','L-013','R-009'}
under={'L-006','L-012','L-014','R-011','R-018'}
prov={
    'derivedFrom':'canonical-v0.2 candidate inventory; p168 selected article layer; p167 reconciliation edge context; p169 canonical candidates and selected layer',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}
notes={
    'L-001':'Fresh unselected `Penacho` article after p167 edge/catchword `Pena-`; no p167→p168 lexical continuation is asserted.',
    'L-002':'Aligned to selected 000524 (`Penca de miſcal. Cuumaicoa.`).',
    'L-003':'Aligned to selected 000525 (`Penſar. Ea.`).',
    'L-004':'Aligned to selected 000526 (`Penſamiento. Ehuame.`).',
    'L-005':'Aligned to selected 000527 (`Peñaſco. Teſo.`). Selected 000528 (`Pepita generalmente`) occurs before L-006 but lacks its own canonical boundary and is recorded separately as a known miss.',
    'L-006':'Aligned to selected 000529 (`Pequeño. Ilichi.`). The group also carries `...tuc-bochi`-like material consistent with selected 000531 (`Perderſe en el camino. Chituc-bochi.`); retained `undersegmented` while 000530 and 000531 are recorded as selected starts lacking independent candidate boundaries.',
    'L-007':'Merged selected starts 000532 (`Perdon. Nehiocore.`) and 000533 (`Perdonar la injuria. Ahiocore.`); 000533 is recorded separately as a known internal miss.',
    'L-009':'Aligned to selected 000534 (`Pereza. Olie.`).',
    'L-010':'Aligned to selected 000535 (`Perezoſo ſer. Obeme.`).',
    'L-011':'Aligned to selected 000536 (`Permanecer la coſa. Calulute.`).',
    'L-012':'Distinct `Permitirle. Buſca conſentimiento`-like lexical start with additional damaged adjacent material; retained `undersegmented` without synthesizing another article.',
    'L-013':'Begins selected 000537 (`Perſona. Ioreme.`) and visibly contains a second `Pertenecer...`-like guide unit. Retained `merged_articles`; the unselected internal unit is not promoted or counted as a missed start without independent direct-collation support.',
    'L-014':'Begins selected 000538 (`Peſada coſa. Beete.`) and carries additional `Buſca penar`-like adjacent material; retained `undersegmented` without synthesizing another article.',
    'R-009':'Canonical group visibly contains at least two distinct `Pescado` guide units (`Ruafo`-like and `Tenchihert`-like forms); retained `merged_articles`, but the internal unselected start is not promoted or added to the missed-start census without an independent anchor.',
    'R-011':'Distinct damaged `Pescuezo`/`cerviz`-like lexical start plus `Calulute`-like reading-order leakage from selected left-column 000536; retained `undersegmented` without creating an extra article.',
    'R-018':'Distinct `Pie de animal` lexical start plus trailing `Pie-` edge/catchword material. P169 selected 000539 begins a fresh `Piedra de que ſe ſacan navajas` article; canonical p169 L-001 starts only in its tail, so no p168→p169 lexical continuation is asserted.',
}

def row(side,n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p168-{key}'
    col='left' if side=='L' else 'right'
    linked=links.get(key,[])
    if key in merged: assessment='merged_articles'
    elif key in under: assessment='undersegmented'
    else: assessment='exact'
    note=notes.get(key)
    if note is None:
        note='Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':168,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
    }

for side,count,name in [('L',14,'p168_left_reconciliation.jsonl'),('R',18,'p168_right_reconciliation.jsonl')]:
    rows=[row(side,i) for i in range(1,count+1)]
    (OUT/name).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

misses=[
    {
        'missedStartId':'ALC1737-miss-p168-L-001','sourceId':'ALC1737','sourcePageDigital':168,'column':'left',
        'visibleStartRaw':'Pepita generalmente. Tepſia.','missType':'between_candidates','containingCandidateId':None,
        'linkedArticleIds':['ALC1737-art-000528'],
        'editorialNote':'Selected direct collation places 000528 between 000527 and 000529, but no canonical candidate represents its guide start. Precise microplacement is not forced beyond the selected sequence.',
    },
    {
        'missedStartId':'ALC1737-miss-p168-L-002','sourceId':'ALC1737','sourcePageDigital':168,'column':'left',
        'visibleStartRaw':'Perder generalmente. Ataru.','missType':'between_candidates','containingCandidateId':None,
        'linkedArticleIds':['ALC1737-art-000530'],
        'editorialNote':'Selected 000530 occurs after selected 000529 and before 000531/000532 without an independent canonical guide boundary. Recorded conservatively as between candidates.',
    },
    {
        'missedStartId':'ALC1737-miss-p168-L-003','sourceId':'ALC1737','sourcePageDigital':168,'column':'left',
        'visibleStartRaw':'Perderſe en el camino. Chituc-bochi.','missType':'between_candidates','containingCandidateId':None,
        'linkedArticleIds':['ALC1737-art-000531'],
        'editorialNote':'Selected 000531 has no independent canonical guide boundary; a `...tuc-bochi`-like tail is displaced into L-006, but the guide start is not forced into that candidate.',
    },
    {
        'missedStartId':'ALC1737-miss-p168-L-004','sourceId':'ALC1737','sourcePageDigital':168,'column':'left',
        'visibleStartRaw':'Perdonar la injuria. Ahiocore.','missType':'inside_candidate_group','containingCandidateId':'ALC1737-vcand-p168-L-007',
        'linkedArticleIds':['ALC1737-art-000533'],
        'editorialNote':'Selected 000533 is a distinct historical start absorbed inside canonical L-007 after selected 000532 (`Perdon`).',
    },
]
for m in misses:
    m.update({
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,
        'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p168 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None},
    })
(OUT/'p168_missed_visible_starts.jsonl').write_text('\n'.join(json.dumps(m,ensure_ascii=False) for m in misses)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':168,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':32,'left':14,'right':18,
        'classification':{'article':32,'continuation':0,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':24,'oversegmented':0,'undersegmented':5,'merged_articles':3,'ambiguous':0,'not_applicable':0},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000524','ALC1737-art-000538'],
        'articleCandidateRecordsLinked':11,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsInsideMergedCandidate':1,'selectedStartsOutsideCandidateInventory':3,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleIds':['ALC1737-art-000528','ALC1737-art-000530','ALC1737-art-000531','ALC1737-art-000533'],
    },
    'promotion':{'articleCandidatesPendingPromotion':21,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':36,'knownMissedStartRecords':4,'unresolvedCandidateRecords':0,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 32 article candidates plus four selected missed starts establish at least 36 starts, but the selected layer is non-exhaustive and merged/undersegmented OCR groups may contain additional unanchored starts.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p167-R-025','to':'ALC1737-vcand-p168-L-001','type':'catchword_or_edge_fragment_to_fresh_next_page_article','note':'p167 ends with `Pena-` edge/catchword material; p168 L-001 opens a fresh `Penacho` article.'},
        {'from':'ALC1737-vcand-p168-R-018','to':'ALC1737-vcand-p169-L-001','type':'catchword_or_edge_fragment_to_fresh_next_page_article','note':'p168 R-018 ends with `Pie-`; p169 selected 000539 is a fresh `Piedra de que ſe ſacan navajas` article whose canonical L-001 begins in the tail `...bajas. Buſca pedernal prieto.`.'},
    ],
    'structuralNotes':[
        'All 32 canonical p168 rows are retained as article boundaries; no canonical continuation or structurally unresolved row is asserted.',
        'Four selected starts lack independent canonical boundaries: 000528, 000530, 000531 and 000533; only 000533 is demonstrably inside L-007, while the other three are recorded conservatively between candidates.',
        'L-007, L-013 and R-009 are `merged_articles`; only the selected internal start 000533 is added to the missed-start census.',
        'L-006, L-012, L-014, R-011 and R-018 are `undersegmented` because of selected-tail leakage, adjacent OCR material or page-edge/catchword content.',
        'No OCR-only internal unit is promoted or counted as a false negative without selected/direct-collation support.'
    ],
    'nextPage':{'sourcePageDigital':169,'candidateInventoryTotal':35,'left':19,'right':16,'firstCandidate':'ALC1737-vcand-p169-L-001','firstCandidateOpening':'...bajas. Buſca pedernal prieto. Piel...','firstSelectedArticle':'ALC1737-art-000539','firstSelectedOpening':'Piedra de que ſe ſacan navajas. Buſca pedernal prieto.'},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP168LayerUsedAsAnchor':True,'p167ReconciliationUsedForOpeningEdge':True,'p169CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and known misses. OCR-only internal/adjacent units are preserved structurally without invented lexical transcription or promotion; metrics remain withheld without an exhaustive visible-start census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p168_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
