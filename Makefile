
install:
	poetry install

lint:
	poetry run flake8 .

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=./ --cov-report=xml
