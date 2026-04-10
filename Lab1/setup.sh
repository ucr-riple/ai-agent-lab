#!/usr/bin/env bash
set -euo pipefail

echo "[1/4] Creating virtual environment (.venv)"
python3 -m venv .venv

echo "[2/4] Upgrading pip"
.venv/bin/python -m pip install -U pip

echo "[3/4] Installing dependencies"
.venv/bin/python -m pip install -U -r requirements.txt

if [[ ! -f .env ]]; then
  echo "[4/4] Creating .env from template"
  cp .env.example .env
else
  echo "[4/4] .env already exists; leaving it unchanged"
fi

echo ""
echo "Setup complete."
echo "Next:"
echo "  source .venv/bin/activate"
echo "  python student_single_turn_template.py"
echo "  python student_chat_template.py"
