# Lab 1: Building Your First Chat Agent

This folder is organized for students to run two files only.

## Student files (primary)

- `student_single_turn_template.py`: Task 1 (single-turn generation)
- `student_chat_template.py`: Task 2 (multi-turn chat with exit/quit/bye)
- `STUDENT_WORKSHEET.md`: Submission checklist
- `LAB1_MANUAL.md`: Full lab instructions

## Setup

For Linux or macOS:
```bash
bash setup.sh
source .venv/bin/activate
```

For Windows Git Bash:
```bash
bash setup_windows.sh
source .venv/Scripts/activate
```

Set your key as an environment variable to avoid mistakenly submitting it:

```bash
export GOOGLE_API_KEY=<YOUR_ACTUAL_API_KEY_HERE>
```

## Run

```bash
python student_single_turn_template.py
python student_chat_template.py
```

## Optional instructor reference

- `reference/single_turn_qa.py`
- `reference/main.py`
