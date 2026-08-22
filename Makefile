.PHONY: help stats query exports qa-surface qa release-check

help:
	@echo "Cahíta Histórico Digital — comandos de trabajo"
	@echo "  make stats       Estadísticas del corpus canónico"
	@echo "  make query Q=... Consulta conservadora del léxico"
	@echo "  make exports     Genera exportaciones léxicas consolidadas"
	@echo "  make qa-surface  Valida metadatos/documentación pública"
	@echo "  make qa           Ejecuta validadores principales locales"
	@echo "  make release-check Valida el paquete estable v1.0.0"

stats:
	python scripts/query_lexicon.py --stats

query:
	@test -n "$(Q)" || (echo "Use: make query Q='Danzar'" >&2; exit 2)
	python scripts/query_lexicon.py "$(Q)" --field all --limit 20

exports:
	python scripts/export_lexicon_corpus.py

qa-surface:
	python scripts/validate_repository_surface.py

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
	python scripts/validate_v1_contract_freeze.py
	python scripts/validate_v1_data_freeze.py

release-check:
	python scripts/validate_v1_release.py
