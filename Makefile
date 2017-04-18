.PHONY: clean dist

help:
	@echo "clean   - remove all build and dist artifacts"
	@echo "lint    - check style with flake8"
	@echo "docs    - generate docs wth Gitbook"
	@echo "dist    - package as a wheel"
	@echo "release - package and upload a release"
	@echo "install - install the package to the active Python's site-packages"


clean:
	rm -Rf build/
	rm -Rf dist/
	rm -Rf opendc.egg-info/

lint:
	flake8 setup.py opendc

docs:

dist: clean
	./setup.py sdist bdist_wheel

release: clean
	./setup.py sdist upload
	./setup.py bdist_wheel upload 