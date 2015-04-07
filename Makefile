help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  dev		=> to install all needed dev tools"
	@echo "  clean		=> to clean clean all automatically generated files"
	@echo "  coverage	=> to run coverage"
	@echo "  check		=> to check code for smells"
	@echo "  test		=> to run all tests"


dev:
	pip install -r requirements.txt
	pip install coverage ipython pudb flake8

clean:
	find  -name \*.pyc -delete
	find  -name \*__pycache__ -delete

rm-migrations:
	find -name \*migrations*0*.py

coverage:
	coverage run python manage.py test
	coverage report -m --fail-under=100

check:
	flake8 .

serve:
	python manage.py runserver

test:
	python manage.py test

superuser:
	python manage.py createsuperuser

migrate:
	- python manage.py makemigrations
	- python manage.py migrate || true
