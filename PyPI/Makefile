default: upload

build:
	./setup.py bdist_wheel

upload: build
	twine upload dist/*

clean:
	rm -rf dist
