import json
from pathlib import Path

links = {
    'L-001':['ALC1737-art-000434'],
    'L-003':['ALC1737-art-000435'],
    'L-004':['ALC1737-art-000436'],
    'L-005':['ALC1737-art-000437'],
    'L-006':['ALC1737-art-000438'],
    'L-007':['ALC1737-art-000440'],
    'L-008':['ALC1737-art-000441'],
    'L-009':['ALC1737-art-000442'],
    'L-010':['ALC1737-art-000443'],
    'L-011':['ALC1737-art-000444'],
    'L-012':['ALC1737-art-000445'],
    'L-013':['ALC1737-art-000446'],
    'R-009':['ALC1737-art-000447'],
    'R-016':['ALC1737-art-000448'],
}
provenance = {
    'derivedFrom':'canonical-v0.2 candidate inventory; p162 selected article layer; p161 reconciliation edge context; p163 canonical candidate and selected opening',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR and pre-existing selected direct-collation anchors; no independent human verification',
    'processedAt':None,
}
notes = {
    'L-001':'Fresh selected 000434 (`Media coſa la mitad. Najucu.`) after unresolved p161 bottom fragment; no p161→p162 continuation is asserted.',
    'L-003':'Aligned to selected 000435 (`Medicina, ò medicamento. Hitoa.`).',
    'L-004':'Aligned to selected 000436 (`Medida qualquiera. Hunateria.`).',
    'L-005':'Aligned to selected 000437 (`Medir generalmente. Hunaie.`).',
    'L-006':'Merged region beginning selected 000438 (`Melon. Manari.`) and absorbing distinct selected 000439 (`Memoria. Aubuate.`); the internal start is recorded separately as a known miss.',
    'L-007':'Aligned to selected 000440 (`Menear algo. Hitanaucutia.`). OCR retains additional damaged text but no independent internal start is promoted.',
    'L-008':'Aligned to selected 000441 (`Menear la cabeza. Acoba ioa.`). Additional OCR leakage is retained without synthesizing a separate article.',
    'L-009':'Aligned to selected 000442 (`Mencionar. Harequianoca.`).',
    'L-010':'Aligned to selected 000443 (`Menospreciar. Caitapo-abicha.`).',
    'L-011':'Aligned to selected 000444 (`Mentar à alguno. Buſca mencionar.`).',
    'L-012':'Aligned to selected 000445 (`Mentir. Aranoquichi.`).',
    'L-013':'Aligned to selected 000446 (`Mentira. Aranoquichibuame.`).',
    'L-020':'Distinct `Merecer. Hkamabare` article start supported directly by canonical OCR/geometry; retained pending promotion.',
    'R-006':'Distinct `Meter como en la caxa`-like article start whose canonical OCR group absorbs additional guide/form-like material; retained undersegmented without inventing internal starts.',
    'R-009':'Aligned to selected 000447 (`Miedo. Mahahue.`).',
    'R-010':'Distinct `Miedoſo` article start supported by canonical OCR/geometry; retained pending promotion.',
    'R-011':'Distinct `Miedo tener. Mahabuené` article start supported by canonical OCR/geometry; retained pending promotion.',
    'R-016':'Aligned to selected 000448 (`Mirar. Abicha.`).',
    'R-019':'Distinct `Mirar saliendo de lo obscuro`-like article start. The same OCR group absorbs the page-bottom catchword/reclamo `Mozo`, which anticipates fresh p163 selected 000449 (`Mozo de edad. Buſca mancebo.`); no cross-page article continuation is asserted.',
}

def rec(side, n):
    key = f'{side}-{n:03d}'
    cid = f'ALC1737-vcand-p162-{key}'
    col = 'left' if side == 'L' else 'right'
    linked = links.get(key, [])
    if key == 'L-006':
        assessment = 'merged_articles'
    elif key in {'R-006','R-019'}:
        assessment = 'undersegmented'
    else:
        assessment = 'exact'
    note = notes.get(key)
    if note is None:
        note = 'Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':162,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
    }

out = Path('data/lexicon/reconciliation')
for side, count, filename in [('L',20,'p162_left_reconciliation.jsonl'),('R',19,'p162_right_reconciliation.jsonl')]:
    rows = [rec(side, i) for i in range(1, count + 1)]
    (out / filename).write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n', encoding='utf-8')

miss = {
    'missedStartId':'ALC1737-miss-p162-L-001','sourceId':'ALC1737','sourcePageDigital':162,'column':'left',
    'visibleStartRaw':'Memoria. Aubuate.','missType':'inside_candidate_group',
    'containingCandidateId':'ALC1737-vcand-p162-L-006','linkedArticleIds':['ALC1737-art-000439'],
    'editorialNote':'Selected 000439 is a distinct historical start absorbed inside canonical L-006 after selected 000438 (`Melon`). Recorded as a known internal false negative without claiming exhaustive visible-start coverage.',
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
    'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p162 geometry with pre-existing selected direct-collation layer; no independent human verification','processedAt':None},
}
(out / 'p162_missed_visible_starts.jsonl').write_text(json.dumps(miss, ensure_ascii=False) + '\n', encoding='utf-8')

status = {
    'sourceId':'ALC1737','sourcePageDigital':162,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':39,'left':20,'right':19,
        'classification':{'article':39,'continuation':0,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':36,'oversegmented':0,'undersegmented':2,'merged_articles':1,'ambiguous':0,'not_applicable':0},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000434','ALC1737-art-000448'],
        'articleCandidateRecordsLinked':14,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsInsideMergedCandidate':1,'selectedStartsOutsideCandidateInventory':0,'selectedArticlesUnlinked':0,
    },
    'promotion':{'articleCandidatesPendingPromotion':25,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':40,'knownMissedStartRecords':1,
        'unresolvedCandidateRecords':0,'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 39 article candidates plus selected 000439 absorbed inside L-006 establish at least 40 starts, but the selected layer is non-exhaustive and damaged undersegmented groups may contain additional unanchored starts; no complete denominator is asserted.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p161-R-016','to':'ALC1737-vcand-p162-L-001','type':'fresh_page_transition_after_unresolved_fragment','note':'p161 R-016 remains unresolved; p162 opens fresh selected `Media coſa la mitad. Najucu.`.'},
        {'from':'ALC1737-vcand-p162-R-019','to':'ALC1737-art-000449','type':'catchword_to_fresh_next_page_article','note':'R-019 absorbs bottom catchword `Mozo`; p163 selected 000449 is fresh `Mozo de edad. Buſca mancebo.`. The first canonical p163 candidate begins in the tail `...cebo.` and then contains fresh selected 000450 `Mofar, eſcarnecer`; no p162→p163 article continuation is asserted.'},
    ],
    'structuralNotes':[
        'L-006 is a merged region containing selected 000438 (`Melon`) and 000439 (`Memoria`).',
        'R-006 is retained undersegmented because its OCR group contains additional guide/form-like material without independent selected anchors.',
        'R-011 is a distinct `Miedo tener. Mahabuené` article boundary, not an unresolved form-only fragment.',
        'R-016 links selected 000448 (`Mirar. Abicha.`); R-014 is a separate `Miembro del hombre` candidate and remains pending promotion.',
        'R-019 begins `Mirar saliendo de lo obscuro`-like material and absorbs catchword `Mozo`; the catchword anticipates a fresh p163 article rather than creating a transpage continuation.'
    ],
    'nextPage':{'sourcePageDigital':163,'firstSelectedArticle':'ALC1737-art-000449','firstSelectedOpening':'Mozo de edad. Buſca mancebo.','firstCanonicalCandidate':'ALC1737-vcand-p163-L-001','firstCanonicalCandidateRaw':'cebo. Mofar, eſcarnecer.','edgeInterpretation':'fresh selected page-opening article partly missed by canonical boundary extraction'},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP162LayerUsedAsAnchor':True,'p161ReconciliationUsedForOpeningEdge':True,'p163CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and the one known missed start. Damaged undersegmented groups are not split without independent anchors; metrics stay withheld without exhaustive census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(out / 'p162_machine_reconciliation_status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
