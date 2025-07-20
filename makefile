
install-deps:
	@ poetry install

dev:
	@docker compose -f local.yml up --build -d --remove-orphans

.PHONY: install-deps dev