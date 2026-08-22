.PHONY: help stats query exports cldf cldf-qa variation variation-qa irregularities irregularities-qa grammar-variety grammar-variety-qa qa-surface qa qa-full release-check

help:
	@echo "Cahíta Histórico Digital — comandos de trabajo"
	@echo "  make stats              Estadísticas del corpus canónico"
	@echo "  make query Q=...        Consulta conservadora del léxico"
	@echo "  make exports            Genera exportaciones léxicas consolidadas"
	@echo "  make cldf               Genera la proyección CLDF Dictionary post-v1"
	@echo "  make cldf-qa            Genera y valida CLDF con pycldf + invariantes CHD"
	@echo "  make variation          Genera el índice histórico de variación post-v1"
	@echo "  make variation-qa       Valida determinismo, schema, cobertura y autoridad"
	@echo "  make irregularities     Genera el derivado post-v1 de irregularidades editoriales"
	@echo "  make irregularities-qa  Valida determinismo, schema e invariantes editoriales"
	@echo "  make grammar-variety    Genera enlaces explícitos gramática ↔ variedad histórica"
	@echo "  make grammar-variety-qa Valida cobertura, determinismo y autoridad de los enlaces"
	@echo "  make qa-surface         Valida metadatos/documentación pública"
	@echo "  make qa                 Ejecuta validadores principales locales"
	@echo "  make qa-full            QA local + Lex-0 externo + v1 publicada (requiere jing)"
	@echo "  make release-check      Reconstruye/valida v1.0.0 desde el tag inmutable"

stats:
	python scripts/query_lexicon.py --stats

query:
	@test -n "$(Q)" || (echo "Use: make query Q='Danzar'" >&2; exit 2)
	python scripts/query_lexicon.py "$(Q)" --field all --limit 20

exports:
	python scripts/export_lexicon_corpus.py

cldf:
	python scripts/generate_cldf_dictionary.py --output build/cldf --force

cldf-qa: cldf
	cldf validate build/cldf/Dictionary-metadata.json
	python scripts/validate_cldf_dictionary.py --cldf-dir build/cldf

variation:
	python scripts/export_historical_variation_index.py --out-dir build/historical-variation-index

variation-qa:
	python scripts/validate_historical_variation_index.py

irregularities:
	python scripts/export_editorial_irregularities.py --out-dir build/editorial-irregularities

irregularities-qa:
	python scripts/validate_editorial_irregularities.py

grammar-variety:
	python scripts/export_grammar_variety_links.py --out-dir build/grammar-variety-links

grammar-variety-qa:
	python scripts/validate_grammar_variety_links.py

qa-surface:
	python scripts/validate_repository_surface.py
	python scripts/validate_documentation_links.py

qa: qa-surface
	python scripts/reconstruct_candidate_inventory.py
	python scripts/validate_lexicon_ids.py
	python scripts/validate_documentation_sync.py
	python scripts/validate_postclosure_exports.py
	python scripts/validate_crossreference_source_reviews.py
	python scripts/validate_crossreference_recollation_queue.py
	python scripts/validate_v1_recollation_disposition.py
	python scripts/validate_lo_mismo_reviews.py
	python scripts/validate_tei_export.py
	python scripts/validate_grammar_exports.py
	python scripts/validate_editorial_irregularities.py
	python scripts/validate_grammar_variety_links.py
	python scripts/validate_v1_contract_freeze.py
	python scripts/validate_v1_data_freeze.py

qa-full: qa
	@command -v jing >/dev/null 2>&1 || (echo "jing is required for make qa-full" >&2; exit 2)
	bash scripts/validate_tei_lex0_external.sh
	python scripts/validate_published_v1.py

release-check:
	python scripts/validate_published_v1.py
