# Lab 3: Knowledge and Action (RAG + Function Calling)

Primary student files:
- `lab3_task1.py` (Eyes-only: knowledge cutoff + manual RAG)
- `knowledge_base.txt` (local document used as RAG context)
- `lab3_task2.py` (Hands-only: function calling with time tool)
- `lab3_task3.py` (Eyes + Hands pipeline for club assistant)
- `club_policy_kb.txt` (local policy document used by Task 3)
- `LAB3_MANUAL.md` (full lab instructions)
- `STUDENT_WORKSHEET.md` (run checklist + deliverables answers)

## Quick start

```bash
bash setup.sh
source .venv/bin/activate
```

Set API key in `.env`:

```text
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

Run:

```bash
python lab3_task1.py
python lab3_task2.py
python lab3_task3.py
```
