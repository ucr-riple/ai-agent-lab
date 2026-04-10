# Lab 1: Building Your First Chat Agent

This folder is organized for students to run two files only.

## Student files (primary)

- `student_single_turn_template.py`: Task 1 (single-turn generation)
- `student_chat_template.py`: Task 2 (multi-turn chat with exit/quit/bye)
- `STUDENT_WORKSHEET.md`: Submission checklist
- `LAB1_MANUAL.md`: Full lab instructions
- `WINDOWS_SETUP.md`: Windows setup instructions

## Setup

If you are using Linux or macOS:
```bash
bash setup.sh
source .venv/bin/activate
```

Set your key as an environment variable to avoid mistakenly submitting it:

```bash
export GOOGLE_API_KEY=<YOUR_ACTUAL_API_KEY_HERE>
```

If you are using Windows, see [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for the exact commands.

## Run

```bash
python student_single_turn_template.py
python student_chat_template.py
```

## Optional instructor reference

- `reference/single_turn_qa.py`
- `reference/main.py`
