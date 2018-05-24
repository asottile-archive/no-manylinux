.PHONY: all
all: venv test

venv: requirements-dev.txt
	rm -rf venv
	virtualenv venv -ppython3.6
	venv/bin/pip install -r $<

.PHONY: test
test: venv
	venv/bin/pre-commit run --all-files
	venv/bin/pytest tests

.PHONY: clean
clean:
	find -name '*.pyc' -delete
	rm -rf venv
