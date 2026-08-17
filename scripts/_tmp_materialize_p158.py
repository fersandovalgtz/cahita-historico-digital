import json
from pathlib import Path

links = {
    'L-001':['ALC1737-art-000374'],'L-002':['ALC1737-art-000375'],'L-003':['ALC1737-art-000376'],
    'L-004':['ALC1737-art-000377'],'L-005':['ALC1737-art-000378'],'L-006':['ALC1737-art-000379'],
    'L-007':['ALC1737-art-000380'],'L-010':['ALC1737-art-000381'],'L-011':['ALC1737-art-000382'],
    'L-013':['ALC1737-art-000383'],'L-014':['ALC1737-art-000384','ALC1737-art-000385'],
    'L-021':['ALC1737-art-000386'],'L-023':['ALC1737-art-000387'],'R-014':['ALC1737-art-000388'],
}
continuations = {'L-020','L-027','L-028'}
assessments = {
    'L-014':'merged_articles','L-019':'oversegmented','L-026':'undersegmented',
    'R-004':'undersegmented','R-025':'undersegmented'
}
provenance = {
    'derivedFrom':'canonical-v0.2 candidate inventory; p158 selected article layer; ALC1737-gap-0001; p159 selected opening for lower-edge context',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, documented source-gap evidence, and next-page selected opening; no independent human verification',
    'processedAt':None,
}
notes = {
    'L-001':'Fresh selected 000374 (`Hallarſe bien en vn lugar. Aam-alaca.`) immediately after documented source gap ALC1737-gap-0001; not a continuation of p157 F-material.',
    'L-002':'Aligned to selected 000375 (`Hallar lo que ſe buſca. Aleac.`).',
    'L-003':'Aligned to selected 000376 (`Hambre. Tebau.`); OCR degrades the initial glyphs/form but the selected direct collation anchors the article.',
    'L-004':'Aligned to selected 000377 (`Hambre tener. Tebaurime.`); OCR is damaged but the boundary remains distinct.',
    'L-005':'Aligned to selected 000378 (`Hambre aver. Tebaurine.`).',
    'L-006':'Aligned to selected 000379 (`Hazer. Aboa.`); OCR is degraded and is not used to strengthen the selected transcription.',
    'L-007':'Aligned to selected 000380 (`Hazedor. Hoame.`).',
    'L-008':'Distinct `Hechizar`-like lexical start supported by geometry; retained pending because raw OCR alone is not a sufficient transcription anchor.',
    'L-009':'Distinct `Hechizero` lexical start supported by geometry; retained pending promotion.',
    'L-010':'Aligned to selected 000381 (`Heder. Huba.`).',
    'L-011':'Aligned to selected 000382 (`Hedor. Hubame.`).',
    'L-012':'Distinct `Hediondo` lexical start; retained pending promotion.',
    'L-013':'Aligned to selected 000383 (`Hembra. Hamu.`).',
    'L-014':'Merged region beginning selected 000384 (`Henchir. Atapunia.`) and absorbing distinct selected 000385 (`Henchimiento. Buſca llenar.`), plus additional damaged H-material. The internal selected start is recorded separately as a known miss.',
    'L-015':'Distinct H-entry after the merged Henchir/Henchimiento region; OCR is severely damaged and the article remains pending promotion.',
    'L-016':'Distinct H-entry supported by geometry in the damaged Hermano/Hermana region; no lexical strengthening is attempted.',
    'L-017':'Distinct `Hermana mayor` article start; the final form is hyphenated/damaged, but the following boundary is fresh rather than a demonstrated continuation.',
    'L-018':'Distinct `Hermanos ser`-like article start supported by geometry; retained pending promotion.',
    'L-019':'Distinct `Herrar poner el hierro` article start whose form continues in L-020.',
    'L-020':'Form-only continuation of the `Herrar poner el hierro` article begun at L-019; not a fresh lexical start.',
    'L-021':'Aligned to selected 000386 (`Hervir. Potec.`).',
    'L-022':'Distinct `Hezes` article start; retained pending promotion.',
    'L-023':'Aligned to selected 000387 (`Hiel. Sicara.`); OCR reads the guide as `Miel` but the selected direct collation remains the transcription authority.',
    'L-024':'Distinct `Hielo` article start; retained pending promotion.',
    'L-025':'Distinct `Hierro metal` article start; retained pending promotion.',
    'L-026':'Distinct `Hilado` start, but the candidate absorbs several additional guide-like fragments (`Hilo de la tierra`, `Hijo, o hija...`) and continues into L-027/L-028. Those internal fragments are not promoted or counted as exhaustive misses without independent anchors.',
    'L-027':'Continuation of the mixed lower-left material begun in L-026; not a fresh candidate article.',
    'L-028':'Continuation of the mixed lower-left material begun in L-026; not a fresh candidate article.',
    'R-001':'Fresh `Hilar` article start at the top of the right column; no continuation from the lower-left mixed region is asserted.',
    'R-004':'Begins a clear `Hinchazón`-like article, but absorbs multiple damaged guide/form fragments. The boundary is real; internal microsegmentation remains unstrengthened.',
    'R-014':'Aligned to selected 000388 (`Holgarſe. Buſca gozarſe.`); OCR is degraded but the selected direct collation anchors the start.',
    'R-025':'Distinct `Hueva` article start at the bottom of p158. Trailing `Huey...` material is preserved as damaged page-edge text; p159 selected evidence opens fresh `Huevo. Totolichaba.`, so no long p158→159 continuation is asserted.',
}

def record(side, n):
    key = f'{side}-{n:03d}'
    cid = f'ALC1737-vcand-p158-{key}'
    column = 'left' if side == 'L' else 'right'
    linked = links.get(key, [])
    if key in continuations:
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':158,'column':column,
            'classification':'continuation','boundaryAssessment':'not_applicable','linkedArticleIds':[],
            'articleLinkStatus':'not_applicable','continuationType':'from_previous_line',
            'editorialNote':notes[key],'reviewStatus':'machine_corrected_unverified',
            'humanVerified':False,'provenance':provenance,
        }
    note = notes.get(key)
    if note is None:
        note = 'Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':158,'column':column,
        'classification':'article','boundaryAssessment':assessments.get(key,'exact'),'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':provenance,
    }

out = Path('data/lexicon/reconciliation')
for side, count, filename in [('L',28,'p158_left_reconciliation.jsonl'),('R',25,'p158_right_reconciliation.jsonl')]:
    rows = [record(side, i) for i in range(1, count + 1)]
    (out / filename).write_text('\n'.join(json.dumps(r, ensure_ascii=False) for r in rows) + '\n', encoding='utf-8')

miss = {
    'missedStartId':'ALC1737-miss-p158-L-001','sourceId':'ALC1737','sourcePageDigital':158,'column':'left',
    'visibleStartRaw':'Henchimiento. Buſca llenar.','missType':'inside_candidate_group',
    'containingCandidateId':'ALC1737-vcand-p158-L-014','linkedArticleIds':['ALC1737-art-000385'],
    'editorialNote':'Selected 000385 is a distinct historical start absorbed inside canonical L-014 after selected 000384. Additional damaged guide-like material in L-014 is not promoted or asserted as an exhaustive miss without stronger anchors.',
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
    'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p158 geometry with pre-existing selected direct-collation layer; no independent human verification','processedAt':None},
}
(out / 'p158_missed_visible_starts.jsonl').write_text(json.dumps(miss, ensure_ascii=False) + '\n', encoding='utf-8')

status = {
    'sourceId':'ALC1737','sourcePageDigital':158,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':53,'left':28,'right':25,
        'classification':{'article':50,'continuation':3,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':45,'oversegmented':1,'undersegmented':3,'merged_articles':1,'ambiguous':0,'not_applicable':3},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000374','ALC1737-art-000388'],
        'articleCandidateRecordsLinked':14,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedArticlesUnlinked':0,'mergedCandidateId':'ALC1737-vcand-p158-L-014',
        'mergedSelectedArticleIds':['ALC1737-art-000384','ALC1737-art-000385'],
    },
    'promotion':{'articleCandidatesPendingPromotion':36,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':51,'knownMissedStartRecords':1,'knownMergedInternalStarts':1,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 50 article candidates plus selected 000385 absorbed inside L-014 establish at least 51 starts. L-026 and R-004 contain additional damaged guide-like material without independent anchors, and the selected layer is non-exhaustive; no complete denominator is asserted.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-gap-0001','to':'ALC1737-vcand-p158-L-001','type':'fresh_sequence_after_source_gap','note':'p158 begins fresh H material after unresolved F/G source loss; L-001 is not a continuation.'},
        {'from':'ALC1737-vcand-p158-L-019','to':'ALC1737-vcand-p158-L-020','type':'article_continuation','note':'`Herrar poner el hierro` continues into form-only L-020.'},
        {'from':'ALC1737-vcand-p158-L-026','to':'ALC1737-vcand-p158-L-027','type':'mixed_region_continuation','note':'Lower-left mixed H-material continues beyond L-026.'},
        {'from':'ALC1737-vcand-p158-L-027','to':'ALC1737-vcand-p158-L-028','type':'mixed_region_continuation','note':'The same lower-left mixed region continues through L-028 before fresh right-column R-001 `Hilar`.'},
        {'from':'ALC1737-vcand-p158-R-025','to':'ALC1737-art-000389','type':'fresh_page_transition','note':'R-025 begins `Hueva` and carries damaged edge material; the p159 selected layer opens fresh `Huevo. Totolichaba.`. No long article continuation is asserted.'},
    ],
    'sourceGapContext':{
        'gapId':'ALC1737-gap-0001','position':'immediately_before_page_158',
        'policy':'The F/G loss remains outside p158 reconstructed coverage; no missing entries are synthesized.'
    },
    'structuralNotes':[
        'L-014 is a merged region containing selected 000384 and 000385; only the selected internal start is recorded as a known missed start.',
        'L-026 absorbs multiple guide-like fragments and continues through L-027/L-028, but unanchored internal starts are not promoted or counted exhaustively.',
        'R-004 is structurally an article start but undersegmented because it absorbs damaged guide/form material.',
        'R-025 retains damaged page-edge material without converting p159 `Huevo` into a continuation.'
    ],
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP158LayerUsedAsAnchor':True,'sourceGapRecordUsed':True,'p159SelectedOpeningUsedForPageEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Source-gap context, selected direct collations, and structural geometry are kept separate from lexical transcription authority. Damaged unanchored internal material remains unpromoted; metrics remain withheld without exhaustive census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(out / 'p158_machine_reconciliation_status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
