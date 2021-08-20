serve:
	poetry run python3.9 main.py

docs-run:
	pdoc3 nest --html --output-dir docs/api --force

docs-serve:
	python3 -m http.server --directory docs/api/nest