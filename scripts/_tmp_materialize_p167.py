import json
from pathlib import Path

OUT = Path('data/lexicon/reconciliation')
links = {
    'L-001':['ALC1737-art-000509'],
    'L-002':['ALC1737-art-000510'],
    'L-003':['ALC1737-art-000511'],
    'L-004':['ALC1737-art-000512'],
    'L-005':['ALC1737-art-000513'],
    'L-006':['ALC1737-art-000514'],
    'L-007':['ALC1737-art-000515'],
    'L-008':['ALC1737-art-000516'],
    'L-009':['ALC1737-art-000517'],
    'L-010':['ALC1737-art-000518','ALC1737-art-000519'],
    'L-027':['ALC1737-art-000520'],
    'L-028':['ALC1737-art-000521'],
    'L-029':['ALC1737-art-000522'],
    'R-004':['ALC1737-art-000523'],
}
merged={'L-010','R-020'}
under={'R-011','R-013','R-025'}
ambiguous={'L-030'}
continuation={'R-003'}
oversegmented={'R-002'}
prov={
    'derivedFrom':'canonical-v0.2 candidate inventory; p167 selected article layer; p166 reconciliation edge context; p168 canonical candidates and selected layer',
    'agent':'GPT-5.6 Sol machine reconciliation',
    'method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification',
    'processedAt':None,
}
notes={
    'L-001':'Fresh selected 000509 (`Paſſo de las beſtias. Arabuerama.`) after p166 edge/catchword material; no p166→p167 lexical continuation is asserted.',
    'L-002':'Aligned to selected 000510 (`Parto aver. Tuabaſo.`).',
    'L-003':'Aligned to selected 000511 (`Paſmarſe la beſtia. Bahac.`).',
    'L-004':'Aligned to selected 000512 (`Paſſo del Rio. Babaſuapo.`).',
    'L-005':'Aligned to selected 000513 (`Pato de tierra caliente colorado. Bachain.`).',
    'L-006':'Aligned to selected 000514 (`Pato anſar. Sibaro.`).',
    'L-007':'Aligned to selected 000515 (`Pato chico. Iliba chau.`).',
    'L-008':'Aligned to selected 000516 (`Pato. Totbio.`).',
    'L-009':'Aligned to selected 000517 (`Pato. Bapo-moatela.`).',
    'L-010':'Merged selected starts 000518 (`Pato. Tepciabiri.`) and 000519 (`Paxaro generalmente. Moel.`); the second selected start lacks its own canonical boundary and is recorded separately as a known internal miss.',
    'L-027':'Aligned to selected cross-reference 000520 (`Pecado. Buſca ofenſa.`).',
    'L-028':'Aligned to selected cross-reference 000521 (`Pecador. Buſca ofenſor.`).',
    'L-029':'Aligned to selected cross-reference 000522 (`Pecar. Buſca ofender.`).',
    'L-030':'Canonical geometry supports a fresh lexical start after `Pecar` and before right-column `Pedazo`, but the OCR does not responsibly recover the guide; retained as `article` with `ambiguous` boundary assessment and no promotion.',
    'R-002':'Distinct `Pedernal prieto para flechas` article start whose Cahita form continues into form-only R-003.',
    'R-003':'Form-only `Bicam` continuation of the `Pedernal prieto para flechas` article begun in R-002; not a fresh lexical start.',
    'R-004':'Aligned to selected 000523 (`Pedir. Netane.`).',
    'R-011':'Distinct `Peine` article/cross-reference-like start. The OCR group also carries adjacent `Apea`-like material consistent with the following Pelar region; retained `undersegmented` without synthesizing an extra article.',
    'R-013':'Distinct `Pelar Aves deſplumandolas`-like article start; trailing `limpi-` belongs to adjacent reading-order material and is retained as subsegmentation evidence without creating another article.',
    'R-020':'Canonical group begins `Pelo interior. Huiboa.` and contains a second distinct `pelo... Caita chona`-like guide unit. Retained `merged_articles`, but the unselected internal start is not promoted or counted as a missed start without direct-collation support.',
    'R-025':'Distinct `Pena generalmente` article start plus trailing `Pena-` edge/catchword material. P168 L-001 begins a fresh `Penacho` article, so no p167→p168 lexical continuation is asserted.',
}

def make_row(side,n):
    key=f'{side}-{n:03d}'
    cid=f'ALC1737-vcand-p167-{key}'
    col='left' if side=='L' else 'right'
    linked=links.get(key,[])
    if key in continuation:
        return {
            'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':167,'column':col,
            'classification':'continuation','boundaryAssessment':'not_applicable','linkedArticleIds':linked,
            'articleLinkStatus':'not_applicable','continuationType':'from_previous_line',
            'editorialNote':notes[key],
            'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
        }
    if key in merged: assessment='merged_articles'
    elif key in under: assessment='undersegmented'
    elif key in ambiguous: assessment='ambiguous'
    elif key in oversegmented: assessment='oversegmented'
    else: assessment='exact'
    note=notes.get(key)
    if note is None:
        note='Aligned to selected direct-collation article anchor.' if linked else 'Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    return {
        'candidateId':cid,'sourceId':'ALC1737','sourcePageDigital':167,'column':col,
        'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,
        'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,
        'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov,
    }

for side,count,name in [('L',30,'p167_left_reconciliation.jsonl'),('R',25,'p167_right_reconciliation.jsonl')]:
    rows=[make_row(side,i) for i in range(1,count+1)]
    (OUT/name).write_text('\n'.join(json.dumps(r,ensure_ascii=False) for r in rows)+'\n',encoding='utf-8')

miss={
    'missedStartId':'ALC1737-miss-p167-L-001','sourceId':'ALC1737','sourcePageDigital':167,'column':'left',
    'visibleStartRaw':'Paxaro generalmente. Moel.','missType':'inside_candidate_group',
    'containingCandidateId':'ALC1737-vcand-p167-L-010','linkedArticleIds':['ALC1737-art-000519'],
    'editorialNote':'Selected 000519 is a distinct historical start absorbed inside canonical L-010 after selected 000518 (`Pato. Tepciabiri.`). Recorded as a known internal false negative without claiming exhaustive visible-start coverage.',
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
    'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p167 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None},
}
(OUT/'p167_missed_visible_starts.jsonl').write_text(json.dumps(miss,ensure_ascii=False)+'\n',encoding='utf-8')

status={
    'sourceId':'ALC1737','sourcePageDigital':167,
    'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},
    'candidateInventory':{
        'total':55,'left':30,'right':25,
        'classification':{'article':54,'continuation':1,'paratext':0,'false_positive':0,'unresolved':0},
        'boundaryAssessment':{'exact':47,'oversegmented':1,'undersegmented':3,'merged_articles':2,'ambiguous':1,'not_applicable':1},
    },
    'selectedLayer':{
        'preExistingArticles':15,'articleIdRange':['ALC1737-art-000509','ALC1737-art-000523'],
        'articleCandidateRecordsLinked':14,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,
        'selectedStartsInsideMergedCandidate':1,'selectedStartsOutsideCandidateInventory':0,'selectedArticlesUnlinked':0,
        'knownMissedSelectedArticleIds':['ALC1737-art-000519'],
    },
    'promotion':{'articleCandidatesPendingPromotion':40,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},
    'visibleStartEvidence':{
        'exhaustive':False,'knownVisibleStartsMinimum':55,'knownMissedStartRecords':1,'unresolvedCandidateRecords':0,
        'precision':None,'recall':None,'f1':None,
        'reasonMetricsWithheld':'The 54 article candidates plus selected internal miss 000519 establish at least 55 starts, but the selected layer is non-exhaustive and merged/undersegmented OCR groups may contain additional unanchored starts.',
    },
    'physicalContinuities':[
        {'from':'ALC1737-vcand-p166-R-022','to':'ALC1737-vcand-p167-L-001','type':'catchword_or_edge_fragment_to_fresh_next_page_article','note':'p166 carries `Paſſo`-like edge/catchword material; p167 opens fresh selected 000509.'},
        {'from':'ALC1737-vcand-p167-R-002','to':'ALC1737-vcand-p167-R-003','type':'article_continuation','note':'`Pedernal prieto para flechas` continues into form-only `Bicam`.'},
        {'from':'ALC1737-vcand-p167-R-025','to':'ALC1737-vcand-p168-L-001','type':'catchword_or_edge_fragment_to_fresh_next_page_article','note':'R-025 ends with `Pena-`; p168 L-001 begins a fresh `Penacho` article before selected p168 anchor 000524.'},
    ],
    'structuralNotes':[
        'L-010 is `merged_articles` because it contains selected 000518 and selected 000519; 000519 is recorded as the known internal missed start.',
        'R-002 is an article start with an oversegmented form continuation in R-003; R-003 is the sole canonical continuation row.',
        'L-030 remains an `article` with `ambiguous` assessment because geometry supports a fresh start while OCR does not responsibly recover its guide.',
        'R-011, R-013 and R-025 are `undersegmented`; adjacent/catchword material is preserved without synthesized lexical articles.',
        'R-020 is `merged_articles` because it contains a second unselected Pelo-like guide unit; that internal unit is not promoted or counted as a missed start without independent direct-collation support.'
    ],
    'nextPage':{'sourcePageDigital':168,'candidateInventoryTotal':32,'left':14,'right':18,'firstCandidate':'ALC1737-vcand-p168-L-001','firstCandidateOpening':'Penacho, ...','firstSelectedArticle':'ALC1737-art-000524','firstSelectedOpening':'Penca de miſcal. Cuumaicoa.'},
    'evidence':{
        'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,
        'selectedP167LayerUsedAsAnchor':True,'p166ReconciliationUsedForOpeningEdge':True,'p168CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,
        'directFacsimileAvailableThisPass':False,
        'policy':'Selected direct collations support demonstrated starts and the known internal miss. OCR-only internal/adjacent units are preserved structurally without invented lexical transcription or promotion; metrics remain withheld without an exhaustive visible-start census.',
    },
    'reviewStatus':'machine_corrected_unverified','humanVerified':False,
}
(OUT/'p167_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
