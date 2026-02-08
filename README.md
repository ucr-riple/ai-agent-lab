# Lab 1: Building Your First Chat Agent

This folder is organized for students to run two files only.

## Student files (primary)

- `student_single_turn_template.py`: Task 1 (single-turn generation)
- `student_chat_template.py`: Task 2 (multi-turn chat with exit/quit/bye)
- `LAB1_MANUAL.md`: Full lab instructions
- `STUDENT_WORKSHEET.md`: Submission checklist

## Setup

```bash
cd /mnt/AI_Agent_Lab
bash setup.sh
source .venv/bin/activate
```

Set your key in `.env`:

```text
GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

## Run

```bash
python student_single_turn_template.py
python student_chat_template.py
```

## Optional instructor reference

- `reference/single_turn_qa.py`
- `reference/main.py`
