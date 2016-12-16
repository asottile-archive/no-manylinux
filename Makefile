REBUILD_FLAG =

.PHONY: all
all: venv test

venv: requirements-dev.txt
	rm -rf venv
	virtualenv venv -ppython3.5
	venv/bin/pip install -r $<

.PHONY: test
test: venv
	venv/bin/pre-commit run --all-files
	venv/bin/py.test tests

.PHONY: clean
clean:
	find -name '*.pyc' -delete
	rm -rf venv
