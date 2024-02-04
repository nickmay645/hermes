VENV := .venv
VENV_SENTINEL := $(VENV)/.sentinel
VENV_PIP := $(VENV)/bin/pip $(PIP_EXTRA_OPTS)
VENV_PRECOMMIT := $(VENV)/bin/pre-commit
VENV_PYTEST := $(VENV)/bin/pytest
VENV_PYTHON := $(VENV)/bin/python
PYTHON := python3.10

# Deploys generally want to have a clean git state to ensure consistency
.PHONY: ensure_git_clean
ensure_git_clean:
	@echo This target requires a clean git state, please stash or commit your changes if this fails on the next line...
	test -z "$$(git status --porcelain)"

.PHONY: ensure_no_venv
ensure_no_venv:
ifdef VIRTUAL_ENV
	$(error Please deactivate your current virtual environment by running `deactivate`)
endif


.PHONY: $(VENV)
$(VENV):
	@$(MAKE) $(VENV_SENTINEL)


 $(VENV_SENTINEL): requirements.txt requirements-test.txt .pre-commit-config.yaml
	$(MAKE) ensure_no_venv
	rm -rf $(VENV)
	$(PYTHON) -m venv $(VENV)
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements.txt
	$(VENV_PIP) install -r requirements-test.txt
	# $(VENV_PRECOMMIT) install
	@touch $(VENV_SENTINEL)
	

.PHONY: update_requirements
update_requirements:
	$(MAKE) ensure_no_venv
	rm -rf $(VENV)
	$(PYTHON) -m venv $(VENV)
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install -r requirements-loose.txt
	rm -rf requirements.txt
	$(VENV_PIP) freeze >> requirements.txt
	make $(VENV)

.PHONY: pre-commit
pre-commit: $(VENV)
	$(VENV_PRECOMMIT) run -a

.PHONY: clean
${VENV}_clean:
	rm -rf $(VENV)

.PHONY: test
test: $(VENV)
	$(VENV_PYTEST) --cov-report term-missing --junitxml=test-reports/pytest/junit.xml tests

run:
	docker-compose up -d --build 

build:
	docker-compose build

clean:
	docker-compose down --volumes --remove-orphans
	docker system prune -a -f --volumes

createsuperuser:
	docker-compose exec django python manage.py createsuperuser


makemigrations:
	$(MAKE) run
	docker-compose exec django python manage.py makemigrations