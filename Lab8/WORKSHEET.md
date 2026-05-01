# Lab 8 Worksheet

Student Name:
Section:
Project Name:
Date:

---

## 1) Setup Checklist

- [ ] `src/interface/__init__.py` and `src/interface/cli.py` created.
- [ ] `tests/interface/__init__.py` and `tests/interface/test_interface.py` created.
- [ ] Lab 7 engine tests still pass after copying interface files.

## 2) Test Results

- [ ] All five unit tests in `test_interface.py` pass with mocked engine.
- [ ] Full system integration test runs end-to-end from CLI to Google Sheets.
- [ ] Full suite `pytest tests/ -v` is all green (storage + engine + interface).

## 3) Current Snapshot

- Current status (one line):
- Next small step (one line):

## 4) Architecture Awareness

- [ ] I can describe in one sentence what `format_response` is responsible for.
- [ ] I can explain why `run_session` accepts `process_fn` instead of calling `process_request` directly.
- [ ] I can identify which layer is responsible for AI calls, which for persistence, and which for display.
- [ ] I know why `pytest tests/interface/` passes without `GEMINI_API_KEY` or `service_account.json`.

Agent prompt used (paste or summarize):

```
[paste here]
```

## 5) Discussion Questions

### A) Dependency Injection

Question: `run_session` accepts a `process_fn` parameter and defaults it to `process_request`.
Why is this better than calling `process_request` directly inside the loop?

Your answer:


### B) Format Contract

Question: `format_response` reads `result["status"]` to decide what to display.
What breaks in the interface if the engine starts returning a plain string instead of a typed dict?

Your answer:


### C) Layer Isolation in Testing

Question: The interface unit tests mock the engine entirely — no Gemini API calls are made.
What kinds of bugs would these tests miss, and what would the full system integration test catch that the unit tests cannot?

Your answer:

---

## 6) Optional Extension: Conversation History

Complete this section only if you implemented the history buffer in `run_session`.

- [ ] I modified `run_session` to maintain a `history` list and prepend prior turns to each engine call.

### Observation 1 — Follow-up turns

Register a member across multiple turns (provide one field per message).
At what turn did the engine accept the registration?

Turn 1 input / engine status:

Turn 2 input / engine status:

Turn 3 input / engine status:

Turn 4 (if needed) input / engine status:


### Observation 2 — Reflection with history

Did the Reflection step correctly track which fields were still missing across turns, or did it lose earlier fields?

Describe what happened:


### Observation 3 — History depth limit

What happened when the history grew beyond 4 turns? Did response quality change?

Your observation:


### Observation 4 — Comparison to Lab 7 Optional

The Lab 7 extension used a two-turn loop **per request** (Turn 1: model decides tool, Turn 2: model synthesizes answer).
The history extension here maintains context **across requests** at the interface level.

What is the fundamental difference between these two approaches? Which problem does each one solve?

Your answer:
