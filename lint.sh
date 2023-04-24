#!/bin/bash
set -x

echo "-------BLACK---------"
black --check *.py slashml

echo "----RUNNING FLAKE8---"
flake8 --exclude=__init__.py

# echo "----RUNNING PYLINT---"
# pylint *.py src/*.py
