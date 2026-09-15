#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Build a standalone Linux executable: dist/pinger
#
# Prerequisites (run once, from this folder):
#   python3 -m venv venv
#   venv/bin/pip install -r venv_requirements.txt   # installs PyInstaller
# ---------------------------------------------------------------------------

set -euo pipefail

PYTHON="venv/bin/python"

if [ ! -x "$PYTHON" ]; then
    echo "[build] Project venv not found at $PYTHON."
    echo "[build] Create it with:"
    echo "          python3 -m venv venv && venv/bin/pip install -r venv_requirements.txt"
    exit 1
fi

"$PYTHON" -m PyInstaller --noconfirm --clean --onefile --console --name pinger --specpath build src/main.py
chmod +x dist/pinger

echo
echo "[build] Done. Executable: dist/pinger"
