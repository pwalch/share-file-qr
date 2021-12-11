#!/bin/bash

set -euo pipefail

LINT_LOCATIONS=(sharefileqr)

echo "Starting linting script"

echo "Linting with black..."
python -m black --target-version py39 --check --diff \
    "${LINT_LOCATIONS[@]}"

echo "Linting with isort..."
python -m isort --check-only "${LINT_LOCATIONS[@]}"

echo "Linting with flake8..."
# F541: f-string without placeholder
python -m flake8 "${LINT_LOCATIONS[@]}"

echo "Linting with mypy"
python -m mypy "${LINT_LOCATIONS[@]}"

echo

echo "No linting violation found!"
