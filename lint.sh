#!/bin/bash
set -x

echo "-------BLACK---------"
black --check *.py src

echo "----RUNNING FLAKE8---"
flake8 --exclude=__init__.py

# echo "----RUNNING PYLINT---"
# pylint *.py src/*.py
