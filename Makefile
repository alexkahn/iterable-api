.PHONY: clean build publish
default: build

clean:
	rm -fr build
	rm -rf dist

build: clean
	python3 -m build

publish: build
	python3 -m twine upload --repository pypi dist/*
