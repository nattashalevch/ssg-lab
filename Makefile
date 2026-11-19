.PHONY: analyze plot summary generate build serve

analyze:
	python scripts/analyze.py

plot:
	python scripts/plot.py

summary:
	python scripts/summary.py

generate: plot summary

build: generate
	mkdocs build --strict

serve:
	mkdocs serve
