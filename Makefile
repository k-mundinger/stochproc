.PHONY: help requirements install format 
UNAME_S := $(shell uname -s)

PROJECTNAME=stochproc

help:
	@echo "Available commands:"
	@echo "requirements       compile all requirements."
	@echo "install            install dev requirements."
	@echo "format             install dev requirements."


requirements:
	cd requirements && \
		pip-compile requirements.in
	cd requirements && \
		pip install -r requirements.txt

install:
	pip install --upgrade pip wheel pip-tools
	pip install -e .

format:
	yapf -i --recursive $(PROJECTNAME)
	isort -rc --atomic $(PROJECTNAME)
	docformatter -i -r $(PROJECTNAME)

