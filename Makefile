serve:
	poetry run python3.9 main.py

docs-run:
	pdoc3 nest --html --output-dir docs/api --force && mv docs/api/nest/* docs  && rm -r docs/api

docs-serve:
	python3 -m http.server --directory docs/api/nest