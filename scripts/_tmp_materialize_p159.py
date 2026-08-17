import json
from pathlib import Path

links = {
    'L-001':['ALC1737-art-000389'],
    'L-002':['ALC1737-art-000390'],
    'L-003':['ALC1737-art-000391'],
    'L-004':['ALC1737-art-000392'],
    'L-006':['ALC1737-art-000393'],
    'L-008':['ALC1737-art-000394'],
    'L-009':['ALC1737-art-000395'],
    'L-011':['ALC1737-art-000396'],
    'L-015':['ALC1737-art-000397'],
    'L-017':['ALC1737-art-000398'],
    'L-023':['ALC1737-art-000399'],
    'L-024':['ALC1737-art-000400'],
    'R-003':['ALC1737-art-000401'],
    'R-021':['ALC1737-art-000402'],
    'R-023':['ALC1737-art-000403'],
}
continuations = {'L-026','R-002','R-004'}
undersegmented = {'L-001','L-003','L-017','R-012','R-022','R-026'}
oversegmented = {'L-025','R-001','R-003'}
provenance = {
    'derivedFrom':'canonical-v0.2 candidate inventory; p159 selected article layer; p158 reconciliation edge context; p160 canonical opening',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR and pre-existing selected direct-collation anchors; no independent human verification',
    'processedAt':None,
}
notes = {
    'L-001':'Fresh selected 000389 (`Huevo. Totolichaba.`), not a continuation of p158 `Hueva`. Candidate also absorbs `Aebole`, the selected form for following 000390 (`Huerfano`).',
    'L-002':'Fresh selected 000390 (`Huerfano. Aebole.`). Its form leaks into L-001 in OCR; selected collation remains the transcription authority.',
    'L-003':'Fresh selected 000391 (`Huir de los contrarios. Abeberim tohutte.`) but candidate also absorbs `Butte`, the selected form for following 000392 (`Huirſe`).',
    'L-004':'Fresh selected 000392 (`Huirſe. Butte.`). OCR guide is severely degraded; selected collation anchors the article.',
    'L-006':'Aligned to selected 000393 (`Humo. Michi.`).',
    'L-008':'Aligned to selected 000394 (`Hurtar. Ethuac.`).',
    'L-009':'Aligned to selected 000395 (`Hurto. Ethubuame.`).',
    'L-011':'Aligned to selected 000396 (`Y. conjunc. Y.`).',
    'L-015':'Aligned to selected 000397 (`Yerno. Monte.`).',
    'L-017':'Aligned to selected 000398 (`Yerva. Huia.`). Candidate also contains an additional guide-like `Yerva ... comestible` fragment; no internal article is promoted or counted as an exhaustive miss without an independent anchor. Selected metadata says right column while canonical geometry places this text in left; mismatch is documented without silent correction.',
    'L-023':'Aligned to selected 000399 (`Yerva mora. Mamiam.`). Selected metadata says right column while canonical geometry places the matching text in left; mismatch is documented without silent correction.',
    'L-024':'Aligned to selected 000400 (`Yerva buena. Lo miſmo.`). OCR preserves an anaphoric-looking fragment. Selected metadata says right column while canonical geometry places the matching text in left; mismatch is documented without silent correction.',
    'L-025':'Distinct `Yerva para quelite` article start whose damaged form appears to continue into L-026.',
    'L-026':'Form-only/damaged continuation of the `Yerva para quelite` region begun at L-025; not treated as a fresh lexical start.',
    'R-001':'Distinct `Yerva de la golondrina` article start whose form continues into R-002.',
    'R-002':'Form-only continuation of R-001; not a fresh lexical start.',
    'R-003':'Aligned to selected 000401 (`Yerva que ſe cria en los arboles. Chibichiam.`) and continues into R-004.',
    'R-004':'Continuation of selected 000401 begun at R-003; not a fresh lexical start.',
    'R-012':'Distinct Yerva article start but candidate also contains a second damaged Yerva-like guide/form fragment; internal microsegmentation is not strengthened without an independent anchor.',
    'R-021':'Aligned to selected 000402 (`Ylvanar. Nataiecha.`).',
    'R-022':'Distinct `Ympedir que no ſe haga alguna coſa` article start. Candidate also contains damaged `...nclmarſe...`-like guide material; no additional article is promoted without stronger evidence.',
    'R-023':'Aligned to selected 000403 (`Yo, pro N. Ne.`).',
    'R-026':'Distinct `Yſlabon. Buſca eſlabon.`-like historical cross-reference start plus a short `I*`/`Y*` page-edge fragment. p160 L-001 begins fresh `Yr derecho à alguna parte`; no long continuation is asserted.',
}

def rec(side, n):
    key = f'{side}-{n:03d}'
    cid = f'ALC1737-vcand-p159-{key}'
    col = 'left' if side == 'L' else 'right'
    linked = links.get(key, [])
    if key in continuations:
        continuation_links = ['ALC1737-art-000401'] if key == 'R-004' else []
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':159,'column':col,
            'classification':'continuation','boundaryAssessment':'not_applicable',
            'linkedArticleIds':continuation_links,'articleLinkStatus':'not_applicable',
            'continuationType':'from_previous_line','editorialNote':notes[key],
            'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
        }
    assessment = 'undersegmented' if key in undersegmented else ('oversegmented' if key in oversegmented else 'exact')
    note = notes.get(key)
    if note is None:
        note = 'Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':159,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
    }

out = Path('data/lexicon/reconciliation')
for side, count, filename in [('L',26,'p159_left_reconciliation.jsonl'),('R',26,'p159_right_reconciliation.jsonl')]:
    rows = [rec(side, i) for i in range(1, count + 1)]
    (out / filename).write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n', encoding='utf-8')

status = {
    'sourceId':'ALC1737','sourcePageDigital':159,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':52,'left':26,'right':26,
        'classification':{'article':49,'continuation':3,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':40,'oversegmented':3,'undersegmented':6,'merged_articles':0,'ambiguous':0,'not_applicable':3},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000389','ALC1737-art-000403'],
        'articleCandidateRecordsLinked':15,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':1,
        'selectedArticlesUnlinked':0,
        'selectedColumnMetadataMismatches':[
            {'articleId':'ALC1737-art-000398','selectedColumn':'right','candidateId':'ALC1737-vcand-p159-L-017','candidateColumn':'left'},
            {'articleId':'ALC1737-art-000399','selectedColumn':'right','candidateId':'ALC1737-vcand-p159-L-023','candidateColumn':'left'},
            {'articleId':'ALC1737-art-000400','selectedColumn':'right','candidateId':'ALC1737-vcand-p159-L-024','candidateColumn':'left'}
        ],
        'columnMetadataCorrectionAppliedThisPass':False,
    },
    'promotion':{'articleCandidatesPendingPromotion':34,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':49,'knownMissedStartRecords':0,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'All 15 selected starts align to candidate starts, but several candidates contain additional damaged guide-like material without independent selected/facsimile anchors. The selected layer is non-exhaustive, so no complete denominator is asserted.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p158-R-025','to':'ALC1737-vcand-p159-L-001','type':'fresh_page_transition','note':'p158 `Hueva` plus damaged edge material does not continue into fresh selected p159 `Huevo. Totolichaba.`.'},
        {'from':'ALC1737-vcand-p159-L-025','to':'ALC1737-vcand-p159-L-026','type':'article_continuation','note':'`Yerva para quelite` region continues into damaged/form-only L-026.'},
        {'from':'ALC1737-vcand-p159-R-001','to':'ALC1737-vcand-p159-R-002','type':'article_continuation','note':'`Yerva de la golondrina` continues into form-only R-002.'},
        {'from':'ALC1737-vcand-p159-R-003','to':'ALC1737-vcand-p159-R-004','type':'article_continuation','note':'Selected 000401 continues into R-004.'},
        {'from':'ALC1737-vcand-p159-R-026','to':'ALC1737-vcand-p160-L-001','type':'fresh_page_transition','note':'R-026 carries a short page-edge/catchword fragment; p160 opens fresh `Yr derecho à alguna parte`, not a continuation of Yſlabon.'},
    ],
    'structuralNotes':[
        'L-001 and L-003 absorb forms belonging to the immediately following selected articles but do not erase those fresh candidate starts.',
        'L-017, R-012 and R-022 contain additional guide-like material that remains unpromoted and is not counted as an exhaustive missed-start layer.',
        'Selected article column metadata for 000398–000400 conflicts with canonical candidate geometry; the mismatch is documented but not silently corrected in this structural pass.',
        'R-026 is a distinct article/cross-reference-like start with edge material; p160 begins a fresh Yr sequence.'
    ],
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP159LayerUsedAsAnchor':True,'p158ReconciliationUsedForOpeningEdge':True,'p160CanonicalOpeningUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Candidate geometry and selected direct collations are used only to support demonstrated starts and continuations. Column-metadata discrepancies and unanchored internal guide-like material remain explicit rather than silently normalized or promoted.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(out / 'p159_machine_reconciliation_status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
