# Student Worksheet: Lab 3

## Before running

1. `bash setup.sh`
2. `source .venv/bin/activate`
3. Add `GEMINI_API_KEY` in `.env`

## Task 1: RAG Need (Eyes only)

Run:
```bash
python lab3_task1.py
```

Checklist:
- Capture initial no-context response.
- Capture RAG response with provided context.
- Explain difference in one sentence.

## Task 2: Function Calling (Hands only)

Run:
```bash
python lab3_task2.py
```

Checklist:
- Response includes current time.
- You can explain that tool output came from local function.

## Task 3: Club Assistant Integration (Eyes + Hands)

Run:
```bash
python lab3_task3.py
```

Checklist:
- Capture `[EYES-only]` policy decision.
- Capture `[HANDS-only]` account status lookup output.
- Capture `[EYES+HANDS]` coordinated final verdict.
- Explain why the conflict case (policy-eligible + account hold) requires both signals.

## Submit

- Screenshots for Task 1, Task 2, Task 3 stages.
- Completed discussion answers below.

## Discussion Answers

### 1) RAG vs Logic

Why is it better to keep club rules in RAG context instead of putting everything in `system_instruction`?

Your answer:


### 2) Function Logic

In Task 2, did Gemini "know" the current time, or know how to call your tool for the time?
Explain the difference.

Your answer:


### 3) Integration Insight

Task 3 combines `[EYES]` (RAG policy decision) and `[HANDS]` (tool lookup).
Why is this combined pipeline stronger than using only Task 1 style or only Task 2 style?

Your answer:
