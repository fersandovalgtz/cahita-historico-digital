import json
from pathlib import Path

links = {
    'L-002':['ALC1737-art-000419'],
    'L-004':['ALC1737-art-000420'],
    'L-005':['ALC1737-art-000421'],
    'L-006':['ALC1737-art-000422'],
    'L-008':['ALC1737-art-000423'],
    'L-009':['ALC1737-art-000424'],
    'L-010':['ALC1737-art-000425'],
    'L-011':['ALC1737-art-000426'],
    'L-012':['ALC1737-art-000427'],
    'L-013':['ALC1737-art-000428'],
    'R-004':['ALC1737-art-000432'],
    'R-008':['ALC1737-art-000433'],
}
provenance = {
    'derivedFrom':'canonical-v0.2 candidate inventory; p161 selected article layer; p160 reconciliation edge context; p162 canonical opening',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR and pre-existing selected direct-collation anchors; no independent human verification',
    'processedAt':None,
}
notes = {
    'L-001':'Form-only continuation `Qobobohftanhuante` of p160 R-026 (`Latir la vena, ò el corazón`). Not a fresh p161 lexical start.',
    'L-002':'Aligned to selected 000419 (`Lavar. Hipacſia, 1, baſona.`).',
    'L-004':'Aligned to selected 000420 (`Leche. Caibua.`).',
    'L-005':'Aligned to selected 000421 (`Lechuza Ave nocturna. Babuis.`). OCR truncates the form with a hyphen but the next candidate is a fresh `Leer` start, so no continuation candidate is created.',
    'L-006':'Aligned to selected 000422 (`Leer. Hioſiata noca.`).',
    'L-008':'Aligned to selected 000423 (`Lenguaje. Noqui.`).',
    'L-009':'Aligned to selected 000424 (`Legumbres. Buſca frixol, habas, &c.`). OCR reading order is jumbled inside the same cross-reference article.',
    'L-010':'Aligned to selected 000425 (`Lengua. Nini.`).',
    'L-011':'Aligned to selected 000426 (`Leña. Quehuima.`); OCR is severely degraded but the selected collation anchors the start.',
    'L-012':'Aligned to selected 000427 (`Leñar hazer leña. Quehine.`).',
    'L-013':'Aligned to selected 000428 (`Leon. Oujeſ.`).',
    'L-014':'Fresh `Levantar algo del suelo` article start that also absorbs selected 000429 (`Lengua de buey. Buabuaſo.`). The internal selected start is recorded separately as a known missed start.',
    'L-015':'Distinct damaged `Lengua...`-like candidate start after the merged L-014 region; retained pending promotion without lexical strengthening.',
    'L-016':'Distinct damaged `Levantarſe/pararſe`-like article start supported by geometry; retained pending promotion.',
    'L-017':'Distinct `Liar` article start; selected `Libro` and `Limon` occur later at the column transition but lack their own canonical candidates.',
    'R-001':'Distinct top-right lexical start after the left-column `Liar` region. Two selected starts (`Libro`, `Limon`) are known to occur at the column transition before this candidate and are recorded separately as misses.',
    'R-004':'Aligned to selected 000432 (`Loco bolverſe. Buſca enloquecer.`).',
    'R-008':'Aligned to selected 000433 (`Loma. Buſca ladera.`).',
    'R-015':'Canonical geometry supports a fresh bottom-right boundary, but OCR does not preserve a recoverable guide. Retained as article with ambiguous boundary assessment and no promotion.',
    'R-016':'Tiny bottom fragment with no recoverable guide or form. It cannot responsibly be classified as article, continuation, paratext, or false positive; p162 opens fresh `Media coſa la mitad`, so no transpage continuation is asserted.',
}

def rec(side, n):
    key = f'{side}-{n:03d}'
    cid = f'ALC1737-vcand-p161-{key}'
    col = 'left' if side == 'L' else 'right'
    linked = links.get(key, [])
    if key == 'L-001':
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':161,'column':col,
            'classification':'continuation','boundaryAssessment':'not_applicable','linkedArticleIds':[],
            'articleLinkStatus':'not_applicable','continuationType':'from_previous_page',
            'editorialNote':notes[key],'reviewStatus':'machine_corrected_unverified',
            'humanVerified':False,'provenance':provenance,
        }
    if key == 'R-016':
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':161,'column':col,
            'classification':'unresolved','boundaryAssessment':'ambiguous','linkedArticleIds':[],
            'articleLinkStatus':'not_applicable','editorialNote':notes[key],
            'reviewStatus':'unresolved','humanVerified':False,'provenance':provenance,
        }
    assessment = 'merged_articles' if key == 'L-014' else ('ambiguous' if key == 'R-015' else 'exact')
    note = notes.get(key)
    if note is None:
        note = 'Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':161,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
    }

out = Path('data/lexicon/reconciliation')
for side, count, filename in [('L',17,'p161_left_reconciliation.jsonl'),('R',16,'p161_right_reconciliation.jsonl')]:
    rows = [rec(side, i) for i in range(1, count + 1)]
    (out / filename).write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n', encoding='utf-8')

misses = [
    {
        'missedStartId':'ALC1737-miss-p161-L-001','sourceId':'ALC1737','sourcePageDigital':161,'column':'left',
        'visibleStartRaw':'Lengua de buey. Buabuaſo.','missType':'inside_candidate_group',
        'containingCandidateId':'ALC1737-vcand-p161-L-014','linkedArticleIds':['ALC1737-art-000429'],
        'editorialNote':'Selected 000429 is a distinct historical start absorbed inside canonical L-014 after the `Levantar algo del suelo` start. Recorded as a known internal false negative without claiming exhaustive visible-start coverage.',
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,
        'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p161 geometry with pre-existing selected direct-collation layer; no independent human verification','processedAt':None},
    },
    {
        'missedStartId':'ALC1737-miss-p161-L-002','sourceId':'ALC1737','sourcePageDigital':161,'column':'left',
        'visibleStartRaw':'Libro. Lo miſmo.','missType':'page_or_column_edge','containingCandidateId':None,
        'linkedArticleIds':['ALC1737-art-000430'],
        'editorialNote':'Selected 000430 is a distinct historical start after left-column L-017 (`Liar`) and before the first canonical right-column candidate. It is recorded as a column-edge known miss; the anaphoric formula remains unresolved.',
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,
        'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p161 geometry with pre-existing selected direct-collation layer; no independent human verification','processedAt':None},
    },
    {
        'missedStartId':'ALC1737-miss-p161-L-003','sourceId':'ALC1737','sourcePageDigital':161,'column':'left',
        'visibleStartRaw':'Limon. Lo miſmo.','missType':'page_or_column_edge','containingCandidateId':None,
        'linkedArticleIds':['ALC1737-art-000431'],
        'editorialNote':'Selected 000431 is a distinct historical start after `Libro` at the left→right column transition and before canonical R-001. It is recorded as a column-edge known miss; the anaphoric formula remains unresolved.',
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,
        'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p161 geometry with pre-existing selected direct-collation layer; no independent human verification','processedAt':None},
    },
]
(out / 'p161_missed_visible_starts.jsonl').write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in misses) + '\n', encoding='utf-8')

status = {
    'sourceId':'ALC1737','sourcePageDigital':161,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':33,'left':17,'right':16,
        'classification':{'article':31,'continuation':1,'paratext':0,'false_positive':0,'unresolved':1},
        'boundaryAssessment':{'exact':29,'oversegmented':0,'undersegmented':0,'merged_articles':1,'ambiguous':2,'not_applicable':1},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000419','ALC1737-art-000433'],
        'articleCandidateRecordsLinked':12,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsInsideMergedCandidate':1,'selectedStartsOutsideCandidateInventory':2,
        'selectedArticlesUnlinked':0,
    },
    'promotion':{'articleCandidatesPendingPromotion':19,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':34,'knownMissedStartRecords':3,
        'unresolvedCandidateRecords':1,'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 31 article candidates plus three selected starts missing from their own canonical candidates establish at least 34 starts. R-016 remains structurally unresolved and the selected layer is non-exhaustive; no complete denominator is asserted.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p160-R-026','to':'ALC1737-vcand-p161-L-001','type':'article_continuation','note':'`Latir la vena, ò el corazón` continues as form-only `Qobobohftanhuante`.'},
        {'from':'ALC1737-vcand-p161-R-016','to':'ALC1737-vcand-p162-L-001','type':'fresh_page_transition_after_unresolved_fragment','note':'p161 R-016 is fragmentary and unresolved; p162 begins fresh `Media coſa la mitad`, so no long continuation is asserted.'},
    ],
    'structuralNotes':[
        'L-014 is a merged region containing a fresh Levantar article plus selected 000429 (`Lengua de buey`).',
        'Selected 000430 (`Libro`) and 000431 (`Limon`) are demonstrated column-edge false negatives after L-017 and before R-001.',
        'R-015 is retained as an article with ambiguous boundary because geometry supports a fresh start while OCR loses the guide.',
        'R-016 remains unresolved rather than being forced into article/continuation/noise classes.'
    ],
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP161LayerUsedAsAnchor':True,'p160ReconciliationUsedForOpeningEdge':True,'p162CanonicalOpeningUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and known misses. Fragmentary bottom material and anaphoric selected entries remain explicitly unresolved; metrics stay withheld without exhaustive census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(out / 'p161_machine_reconciliation_status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
