import json
from pathlib import Path

links = {
    'L-001':['ALC1737-art-000404'],
    'L-003':['ALC1737-art-000405'],
    'L-004':['ALC1737-art-000406'],
    'L-005':['ALC1737-art-000407'],
    'L-006':['ALC1737-art-000408'],
    'L-007':['ALC1737-art-000409'],
    'L-010':['ALC1737-art-000410'],
    'L-014':['ALC1737-art-000411'],
    'R-002':['ALC1737-art-000412'],
    'R-003':['ALC1737-art-000413'],
    'R-004':['ALC1737-art-000414'],
    'R-005':['ALC1737-art-000415'],
    'R-006':['ALC1737-art-000417'],
    'R-022':['ALC1737-art-000418'],
}
continuations = {'L-002'}
undersegmented = {'L-003','R-010'}
oversegmented = {'L-001','R-026'}
provenance = {
    'derivedFrom':'canonical-v0.2 candidate inventory; p160 selected article layer; p159 reconciliation edge context; p161 canonical opening and selected layer',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR and pre-existing selected direct-collation anchors; no independent human verification',
    'processedAt':None,
}
notes = {
    'L-001':'Fresh selected 000404 (`Yr derecho à alguna parte`) after p159 page-edge material. The article is split: its form `Tutula hueye` continues in L-002.',
    'L-002':'Form-only continuation `Tutula hueye` of selected 000404 begun at L-001; not a fresh lexical start.',
    'L-003':'Aligned to selected 000405 (`Yr rodeando. Coorite.`). The same OCR group also contains a distinct guide-like `Yr delante. Buſca andar.` fragment; it remains unpromoted without an independent anchor.',
    'L-004':'Aligned to selected 000406 (`Yr por leña. Quehuye.`); trailing OCR debris is preserved without strengthening additional structure.',
    'L-005':'Aligned by selected order and page position to 000407 (`Yr por agua. Buſca agua traer.`). OCR is severely degraded; the selected direct collation remains the transcription authority.',
    'L-006':'Aligned to selected 000408 (`Yzquierda mano. Micoi.`).',
    'L-007':'Aligned to selected 000409 (`Jubilo. Buſca gozo.`).',
    'L-010':'Aligned to selected 000410 (`Juez. Iaut.`); OCR loses initial glyphs but geometry and selected order support the boundary.',
    'L-014':'Aligned to selected 000411 (`Juntar vna coſa con otra. Nauatoha.`).',
    'R-002':'Aligned to selected 000412 (`Ladera. Itero.`).',
    'R-003':'Aligned to selected 000413 (`Ladino. Iorinoca.`).',
    'R-004':'Aligned to selected 000414 (`Ladrar los perros. Chumchae.`).',
    'R-005':'Aligned to selected 000415 (`Ladrido tal. Hia.`). Selected 000416 (`Ladrona`) occurs after this candidate and before R-006 but has no canonical candidate of its own.',
    'R-006':'Aligned to selected 000417 (`Lagaña. Somaparia.`). A selected `Ladrona. Eet buame.` start is independently documented between R-005 and R-006.',
    'R-010':'Distinct `Lagrima` start, but the same OCR group also contains a clear `Lamer`-like guide/form fragment before fresh R-011. Internal microsegmentation is not promoted without an independent selected/facsimile anchor.',
    'R-022':'Aligned to selected 000418 (`Laguna. Bacoa.`).',
    'R-026':'Distinct `Latir la vena, ò el corazón` article start at the bottom of p160. Its form continues on p161 L-001 (`Qobobohftanhuante`) before fresh p161 L-002 `Lavar`.',
}

def rec(side, n):
    key = f'{side}-{n:03d}'
    cid = f'ALC1737-vcand-p160-{key}'
    col = 'left' if side == 'L' else 'right'
    linked = links.get(key, [])
    if key in continuations:
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':160,'column':col,
            'classification':'continuation','boundaryAssessment':'not_applicable',
            'linkedArticleIds':['ALC1737-art-000404'],'articleLinkStatus':'not_applicable',
            'continuationType':'from_previous_line','editorialNote':notes[key],
            'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
        }
    assessment = 'undersegmented' if key in undersegmented else ('oversegmented' if key in oversegmented else 'exact')
    note = notes.get(key)
    if note is None:
        note = 'Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':160,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
    }

out = Path('data/lexicon/reconciliation')
for side, count, filename in [('L',19,'p160_left_reconciliation.jsonl'),('R',26,'p160_right_reconciliation.jsonl')]:
    rows = [rec(side, i) for i in range(1, count + 1)]
    (out / filename).write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n', encoding='utf-8')

miss = {
    'missedStartId':'ALC1737-miss-p160-R-001','sourceId':'ALC1737','sourcePageDigital':160,'column':'right',
    'visibleStartRaw':'Ladrona. Eet buame.','missType':'between_candidates','containingCandidateId':None,
    'linkedArticleIds':['ALC1737-art-000416'],
    'editorialNote':'Selected 000416 is a distinct historical start ordered between selected 000415 (`Ladrido`) and 000417 (`Lagaña`), corresponding to the interval between canonical R-005 and R-006. It is recorded as a demonstrated known miss without claiming exhaustive visible-start coverage.',
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
    'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p160 geometry with pre-existing selected direct-collation layer; no independent human verification','processedAt':None},
}
(out / 'p160_missed_visible_starts.jsonl').write_text(json.dumps(miss, ensure_ascii=False) + '\n', encoding='utf-8')

status = {
    'sourceId':'ALC1737','sourcePageDigital':160,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':45,'left':19,'right':26,
        'classification':{'article':44,'continuation':1,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':40,'oversegmented':2,'undersegmented':2,'merged_articles':0,'ambiguous':0,'not_applicable':1},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000404','ALC1737-art-000418'],
        'articleCandidateRecordsLinked':14,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':1,
        'selectedStartsOutsideCandidateInventory':1,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleId':'ALC1737-art-000416',
    },
    'promotion':{'articleCandidatesPendingPromotion':30,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':45,'knownMissedStartRecords':1,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 44 article candidates plus selected 000416 outside the candidate inventory establish at least 45 starts. L-003 and R-010 contain additional guide-like material without independent anchors, and the selected layer is non-exhaustive; no complete denominator is asserted.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p159-R-026','to':'ALC1737-vcand-p160-L-001','type':'fresh_page_transition','note':'p160 begins fresh selected `Yr derecho à alguna parte`; it is not a continuation of p159 `Yſlabon` edge material.'},
        {'from':'ALC1737-vcand-p160-L-001','to':'ALC1737-vcand-p160-L-002','type':'article_continuation','note':'Selected 000404 continues into form-only L-002 `Tutula hueye`.'},
        {'from':'ALC1737-vcand-p160-R-026','to':'ALC1737-vcand-p161-L-001','type':'article_continuation','note':'`Latir la vena, ò el corazón` continues into p161 form-only `Qobobohftanhuante`; p161 L-002 begins fresh `Lavar`.'},
    ],
    'structuralNotes':[
        'Selected 000416 (`Ladrona. Eet buame.`) is a demonstrated between-candidate false negative between R-005 and R-006.',
        'L-003 and R-010 contain additional guide-like material but no unanchored internal article is promoted or counted as an exhaustive miss.',
        'R-026 is a p160 article start despite its form being physically continued on p161.'
    ],
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP160LayerUsedAsAnchor':True,'p159ReconciliationUsedForOpeningEdge':True,'p161CandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and the one known missed start. OCR-only internal guide-like material remains unpromoted; cross-page form continuation is modeled separately from article-start classification; metrics remain withheld without exhaustive census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(out / 'p160_machine_reconciliation_status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
