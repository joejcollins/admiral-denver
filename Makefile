# Consistent set of make tasks.
.DEFAULT_GOAL:= help  # because it's is a safe task.

clean:  # Remove all build, test, coverage and Python artifacts.
	rm -rf .venv
	rm -rf atlanta_shore.egg-info
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete
	rm -rf .R

docker:  # Build the docker image (takes 6 minutes in a Codespace YMMV).
	docker build \
		--tag ghcr.io/earthroverprogram/erpsoiltools:latest \
		--file .devcontainer/Dockerfile \
		.

.PHONY: help
help: # Show help for each of the makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

lint:  # Lint the code with ruff and sourcery.
	.venv/bin/python -m ruff check ./python_src ./tests
	.venv/bin/sourcery login --token $$SOURCERY_TOKEN
	.venv/bin/sourcery review ./python_src ./tests --check --no-summary
	.venv/bin/python -m mypy ./python_src ./tests

lock:  # Create the lock file and requirements file.
	rm -f requirements.txt
	uv pip compile pyproject.toml --python .venv/bin/python --output-file=requirements.txt  requirements.in

.PHONY: r # because there is a directory called r.
r:  # Run Rstudio server
	sudo su - rstudio -c 'rserver'

rtest: lock  # Run the R tests.
	R -e "devtools::test()"

test:  # Run the unit tests.
	.venv/bin/pytest ./tests --verbose --color=yes
	.venv/bin/pytest --cov=atlanta_shore --cov-fail-under=50

venv:  # Create the virtual environment.
	uv venv .venv
	uv pip install --python .venv/bin/python --requirements requirements.txt

survey-prep:
	.venv/bin/python ./src/data/add_id_to_waypoints.py
