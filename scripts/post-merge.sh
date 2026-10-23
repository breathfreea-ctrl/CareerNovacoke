#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."

# Reconcile the committed lockfile with Replit's existing Python package tree.
# Do not create a virtual environment or download separate browser binaries.
requirements="$(mktemp)"
trap 'rm -f "$requirements"' EXIT
target="$(python -c 'import sys; print(f".pythonlibs/lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages")')"

uv export --locked --all-groups --no-emit-project --output-file "$requirements" --quiet
uv pip install --python "$(command -v python)" --target "$target" \
  --require-hashes --requirements "$requirements"

python -c 'import flask; from playwright.sync_api import sync_playwright'
python -m compileall -q main.py matching.py models.py survey_questions.py
printf 'Post-merge Python dependencies and source checks completed.\n'
