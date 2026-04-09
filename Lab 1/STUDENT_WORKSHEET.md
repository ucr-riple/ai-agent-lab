# Student Worksheet (Run First, Then Optional Edits)

Use these template files:

- `student_single_turn_template.py` for Task 1
- `student_chat_template.py` for Task 2

## Before running

1. `bash setup.sh` (Linux / macOS) or `bash setup_windows.sh` (Windows Git Bash)
2. `source .venv/bin/activate` (Linux / macOS) or `source .venv/Scripts/activate` (Windows Git Bash)
3. Confirm `.env` has `GOOGLE_API_KEY=...`

## Task 1: Single-Turn Generation

File:
- `student_single_turn_template.py`

Required:
- Run the file as-is and confirm one valid model response.

Optional edits:
- `OPTIONAL TODO 1`: change model name.
- `OPTIONAL TODO 2`: change prompt text and compare output.

Run:
```bash
python student_single_turn_template.py
```

Pass criteria:
- Script runs without import errors.
- Prints one Gemini response.

## Task 2: Multi-Turn Chatbot

File:
- `student_chat_template.py`

Required:
- Run the file as-is.
- Demonstrate at least 3 turns.
- Terminate with `exit`/`quit`/`bye`.

Optional edits:
- `OPTIONAL TODO 1`: try another model.

Run:
```bash
python student_chat_template.py
```

Pass criteria:
- Supports multiple turns.
- Exits on `exit`, `quit`, or `bye`.
- Preserves memory within the same run.

## Submission checklist

- Screenshot for Task 1 successful output.
- Screenshot for Task 2 with at least 3 turns.
- Screenshot showing clean exit.
- Short note: what you changed (if any optional edits were done).
