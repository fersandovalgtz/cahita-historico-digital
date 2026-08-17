import json, subprocess
from pathlib import Path

ROOT=Path('.')
REC=ROOT/'data/lexicon/reconciliation'
raw=subprocess.check_output(['python','scripts/export_candidate_page.py','--page','174'], text=True)
rows=[json.loads(x) for x in raw.splitlines() if x.strip()]
assert len(rows)==48 and sum(r['column']=='left' for r in rows)==26 and sum(r['column']=='right' for r in rows)==22

links={
'L-001':['ALC1737-art-000615'],'L-002':['ALC1737-art-000616'],'L-004':['ALC1737-art-000617'],
'L-005':['ALC1737-art-000618'],'L-006':['ALC1737-art-000619'],'L-009':['ALC1737-art-000620'],
'L-010':['ALC1737-art-000621'],'L-011':['ALC1737-art-000622'],'L-013':['ALC1737-art-000623'],
'L-014':['ALC1737-art-000624'],'L-016':['ALC1737-art-000625'],'L-017':['ALC1737-art-000626'],
'L-018':['ALC1737-art-000627'],'L-024':['ALC1737-art-000628']}
merged={'L-013','L-024','R-001','R-006','R-011','R-012'}
special={
'L-001':'Aligned to selected 000615 (`Si, conj. Soc.`); selected 000614 (`Si, adv. para afirmar. Hebui.`) precedes this first canonical boundary and is recorded as a page-top missed start.',
'L-013':'`Sobrina, y sobrino`-like start absorbs selected 000623 (`Socorrer. Buſca ayudar.`); the selected internal start is recorded separately as a missed start.',
'L-024':'`Soñar`-like start absorbs selected 000628 (`Soplar. Apuña.`); the selected internal start is recorded separately as a missed start.',
'R-001':'Canonical group begins with `Sorber`-like material and contains adjacent `Sueño`-like material; retained as `merged_articles` without synthesizing or promoting an OCR-only internal article.',
'R-006':'Canonical group visibly contains `Subir algo`-like and `Sudar`-like material; retained as `merged_articles` without OCR-only promotion.',
'R-011':'Canonical group visibly contains `Suelo` plus adjacent `Sufrir`-like material; retained as `merged_articles` without OCR-only promotion.',
'R-012':'Canonical group visibly contains `Sumirſe en el agua` plus `Sumirſe en la tierra`-like material; retained as `merged_articles` without OCR-only promotion.'}
prov={'derivedFrom':'canonical-v0.2 candidate inventory; p174 selected article layer; p173 reconciliation edge context; p175 canonical candidates and selected layer','agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted conservative structural reconciliation from canonical geometry/OCR, pre-existing selected direct-collation anchors, and adjacent-page evidence; no independent human verification','processedAt':None}
outs={'left':[],'right':[]}
for r in rows:
    suffix=('L' if r['column']=='left' else 'R')+'-'+r['candidateId'].rsplit('-',1)[-1]
    linked=links.get(suffix,[])
    assessment='merged_articles' if suffix in merged else 'exact'
    if suffix in special:
        note=special[suffix]
    elif linked:
        aid=linked[0].split('-')[-1]
        note=f'Aligned to selected {aid}; selected direct-collation transcription remains authoritative over noisy OCR.'
    else:
        note='Distinct lexical start supported by canonical geometry; retained pending because raw OCR alone is not a sufficient transcription anchor for promotion.'
    obj={'candidateId':r['candidateId'],'sourceId':'ALC1737','sourcePageDigital':174,'column':r['column'],'classification':'article','boundaryAssessment':assessment,'linkedArticleIds':linked,'articleLinkStatus':'linked' if linked else 'pending_promotion','editorialNote':note,'reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':prov}
    outs[r['column']].append(obj)
for col in ['left','right']:
    p=REC/f'p174_{col}_reconciliation.jsonl'
    p.write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in outs[col])+'\n',encoding='utf-8')

miss=[
{'missedStartId':'ALC1737-miss-p174-L-001','sourceId':'ALC1737','sourcePageDigital':174,'column':'left','visibleStartRaw':'Si, adv. para afirmar. Hebui.','missType':'page_or_column_edge','containingCandidateId':None,'linkedArticleIds':['ALC1737-art-000614'],'editorialNote':'Selected 000614 is a fresh page-top start before canonical L-001 (`Si, conj. Soc.`).','reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p174 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None}},
{'missedStartId':'ALC1737-miss-p174-L-002','sourceId':'ALC1737','sourcePageDigital':174,'column':'left','visibleStartRaw':'Socorrer. Buſca ayudar.','missType':'inside_candidate_group','containingCandidateId':'ALC1737-vcand-p174-L-013','linkedArticleIds':['ALC1737-art-000623'],'editorialNote':'Selected 000623 is a distinct start absorbed inside L-013 after the unselected `Sobrina, y sobrino`-like start.','reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p174 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None}},
{'missedStartId':'ALC1737-miss-p174-L-003','sourceId':'ALC1737','sourcePageDigital':174,'column':'left','visibleStartRaw':'Soplar. Apuña.','missType':'inside_candidate_group','containingCandidateId':'ALC1737-vcand-p174-L-024','linkedArticleIds':['ALC1737-art-000628'],'editorialNote':'Selected 000628 is a distinct start absorbed inside L-024 after the unselected `Soñar`-like start.','reviewStatus':'machine_corrected_unverified','humanVerified':False,'provenance':{'agent':'GPT-5.6 Sol machine reconciliation','method':'AI-assisted alignment of canonical p174 geometry with pre-existing selected direct-collation anchors; no independent human verification','processedAt':None}}]
(REC/'p174_missed_visible_starts.jsonl').write_text('\n'.join(json.dumps(x,ensure_ascii=False) for x in miss)+'\n',encoding='utf-8')

preflight={'sourceId':'ALC1737','sourcePageDigital':174,'stage':'preflight_complete','candidateInventory':{'total':48,'left':26,'right':22},'selectedLayer':{'preExistingArticles':15,'articleIdRange':['ALC1737-art-000614','ALC1737-art-000628'],'nonExhaustive':True,'humanVerified':False},'openingEdge':{'previousPage':173,'interpretation':'fresh_page_transition','knownTopMissedStart':'ALC1737-art-000614','firstCanonicalCandidate':'ALC1737-vcand-p174-L-001'},'workingHypothesis':{'article':48,'continuation':0,'knownMissedSelectedStarts':['ALC1737-art-000614','ALC1737-art-000623','ALC1737-art-000628'],'mergedCandidateRegions':['ALC1737-vcand-p174-L-013','ALC1737-vcand-p174-L-024','ALC1737-vcand-p174-R-001','ALC1737-vcand-p174-R-006','ALC1737-vcand-p174-R-011','ALC1737-vcand-p174-R-012']},'nextPage':{'sourcePageDigital':175,'candidateInventoryTotal':35,'left':20,'right':15,'firstCandidate':'ALC1737-vcand-p175-L-001','firstSelectedArticle':'ALC1737-art-000629','firstSelectedOpening':'Tarde. Cuſte.','edgeInterpretation':'fresh_page_transition'},'evidenceLimits':{'directFacsimileInspectedThisPass':False,'selectedLayerNotCoverageExpectation':True,'metricsAllowed':False},'reviewStatus':'machine_corrected_unverified','humanVerified':False}
(REC/'p174_preflight.json').write_text(json.dumps(preflight,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
status={'sourceId':'ALC1737','sourcePageDigital':174,'pageStatus':{'candidateReconciliation':'complete','visibleStartCensus':'known_misses_only_not_exhaustive','promotionLinkage':'partial','technicalClosure':False,'humanVerificationPlanned':False},'candidateInventory':{'total':48,'left':26,'right':22,'classification':{'article':48,'continuation':0,'paratext':0,'false_positive':0,'unresolved':0},'boundaryAssessment':{'exact':42,'oversegmented':0,'undersegmented':0,'merged_articles':6,'ambiguous':0,'not_applicable':0}},'selectedLayer':{'preExistingArticles':15,'articleIdRange':['ALC1737-art-000614','ALC1737-art-000628'],'articleCandidateRecordsLinked':14,'structuredArticlesLinked':15,'continuationCandidateRecordsLinked':0,'selectedStartsInsideMergedCandidate':2,'selectedStartsOutsideCandidateInventory':1,'selectedArticlesUnlinked':0,'knownMissedSelectedArticleIds':['ALC1737-art-000614','ALC1737-art-000623','ALC1737-art-000628']},'promotion':{'articleCandidatesPendingPromotion':34,'newPromotionsThisPass':0,'corpusTotalAfterPass':1045},'visibleStartEvidence':{'exhaustive':False,'knownVisibleStartsMinimum':51,'knownMissedStartRecords':3,'unresolvedCandidateRecords':0,'precision':None,'recall':None,'f1':None,'reasonMetricsWithheld':'The 48 article candidates plus three selected missed starts establish at least 51 starts, but the selected layer is non-exhaustive and merged groups may contain additional unanchored starts.'},'physicalContinuities':[{'from':'ALC1737-vcand-p173-R-022','to':'ALC1737-art-000614','type':'fresh_page_transition_with_top_selected_miss','note':'p174 opens with selected 000614 before canonical L-001; no p173→p174 lexical continuation is asserted.'},{'from':'ALC1737-vcand-p174-R-022','to':'ALC1737-vcand-p175-L-001','type':'fresh_page_transition','note':'p174 ends at `Tapón`; p175 opens with fresh `Tarde. Cuſte.` and no cross-page lexical continuation is asserted.'}],'structuralNotes':['L-013 and L-024 are `merged_articles` with selected internal starts 000623 and 000628 respectively.','R-001, R-006, R-011 and R-012 are `merged_articles` based on multiple visible OCR guide units; OCR-only internal units are not promoted or added to the visible-start minimum without an independent anchor.','No canonical p174 row is classified as a physical continuation.'],'nextPage':{'sourcePageDigital':175,'candidateInventoryTotal':35,'left':20,'right':15,'firstCandidate':'ALC1737-vcand-p175-L-001','firstCandidateOpening':'Tarde. Cuſte.','firstSelectedArticle':'ALC1737-art-000629','firstSelectedOpening':'Tarde. Cuſte.','nextPageTopSelectedMissExpected':False},'evidence':{'canonicalCandidateInventoryVerified':True,'canonicalCandidateInventoryCount':2072,'selectedP174LayerUsedAsAnchor':True,'p173ReconciliationUsedForOpeningEdge':True,'p175CanonicalCandidatesAndSelectedLayerUsedForLowerEdge':True,'directFacsimileAvailableThisPass':False,'policy':'Selected direct collations support demonstrated starts and known misses. OCR-only internal units are preserved structurally without invented lexical transcription or promotion; metrics remain withheld without an exhaustive visible-start census.'},'reviewStatus':'machine_corrected_unverified','humanVerified':False}
(REC/'p174_machine_reconciliation_status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
