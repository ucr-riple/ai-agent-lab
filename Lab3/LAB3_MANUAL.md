# Lab 3: Knowledge and Action - RAG and Function Calling

## 1. Objective

LLM knowledge is frozen at training time. In this lab, you give Gemini:
- Eyes: retrieval context (RAG)
- Hands: local tools (function calling)

## 2. Task 1: Why We Need RAG (The "I don't know" test)

Run:

```bash
python lab3_task1.py
```

What you should see:
- No-context answer may be uncertain or hallucinated.
- With context from `knowledge_base.txt`, answer becomes grounded to provided facts.

## 3. Task 2: Function Calling (AI using tools)

Run:

```bash
python lab3_task2.py
```

What you should see:
- Model uses local `get_current_time()` tool to answer with real system time.

## 4. Task 3: Club Assistant Integration (Eyes + Hands)

Run:

```bash
python lab3_task3.py
```

Task 3 has three explicit stages:
- `[EYES-only]` model uses policy context from `club_policy_kb.txt` and returns eligibility decision.
- `[HANDS-only]` script calls local tool `check_account_status(name)` for runtime operational status.
- `[EYES+HANDS]` model synthesizes both into a final access verdict.

Why this is different:
- Task 1 is Eyes-only (knowledge grounding).
- Task 2 is Hands-only (tool usage).
- Task 3 orchestrates both in one pipeline with a realistic conflict case:
  policy may say eligible, but account status can still block participation.

## 5. Deliverables

Complete `STUDENT_WORKSHEET.md` and answer:

1. RAG vs Logic: Why put club rules in retrieval context instead of hardcoding in `system_instruction`?
2. Function Logic: Did Gemini "know" the time, or know how to ask your system tool?
3. Integration Insight: Why does the conflict case require Eyes + Hands coordination?
