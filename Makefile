.PHONY: analyze plot summary generate build serve clean

DATA = data/measurements.csv
PLOT_SCRIPT = scripts/plot.py
SUMMARY_SCRIPT = scripts/summary.py

analyze:
	python scripts/analyze.py

plot: docs/images/engagement.png

docs/images/engagement.png: $(DATA) $(PLOT_SCRIPT)
	python $(PLOT_SCRIPT)

summary: docs/results.md

docs/results.md: $(DATA) $(SUMMARY_SCRIPT)
	python $(SUMMARY_SCRIPT)

generate: plot summary build-info

build: generate
	mkdocs build --strict

serve:
	mkdocs serve

clean:
	rm -f docs/images/engagement.png docs/results.md

.PHONY: build-info

build-info:
	python scripts/build_info.py

