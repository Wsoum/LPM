.PHONY := mix headers
.DEFAULT_GOAL := mix
LOZA = $(shell which loza)

headers:
	@$(LOZA) scripts/update-headers.loza

test:
	@$(LOZA) tests/run.loza

all: headers test
	-@git status
