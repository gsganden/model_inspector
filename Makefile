.ONESHELL:
SHELL := /bin/bash
SRC = $(wildcard ./*.ipynb)

all: model_inspector docs

model_inspector: $(SRC)
	nbdev_build_lib
	touch model_inspector

sync:
	nbdev_update_lib

docs_serve: docs
	cd docs && bundle exec jekyll serve

docs: $(SRC)
	nbdev_build_docs
	touch docs

test:
	nbdev_test_nbs

release: pypi
	nbdev_conda_package
	nbdev_bump_version

pypi: dist
	twine upload --config-file=./.pypirc --repository pypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
