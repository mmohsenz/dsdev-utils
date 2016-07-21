clean:
	python dev/clean.py

deploy: pypi
	git push
	git push --tags
	twine upload dist/*
	clean

deps:
	pip install -r requirements.txt --upgrade
	pip install -r dev/requirements.txt --upgrade

pypi:
	python setup.py sdist

register:
	python setup.py register -r pypi

test: clean
	tox
