# Lab 7 Worksheet

Student Name:
Section:
Project Name:
Date:

---

## 1) Current Snapshot of Your Own Project

- Current status (one line):
- Next small step (one line):

## 2) Discussion Questions

### A) Dependency Injection

Question: `run_session` accepts a `process_fn` parameter and defaults it to `process_request`.
Why is this better than calling `process_request` directly inside the loop?

Your answer:


### B) Format Contract

Question: `format_response` reads `result["status"]` to decide what to display.
What breaks in the interface if the engine starts returning a plain string instead of a typed dict?

Your answer:


### C) Layer Isolation in Testing

Question: The interface unit tests mock the engine entirely — no LLM API calls are made.
What kinds of bugs would these tests miss, and what would the full system integration test catch that the unit tests cannot?

Your answer:

---

## 3) Optional Extension: Conversation History

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


### Observation 4 — Comparison to Lab 6 Optional

The Lab 6 extension used a two-turn loop **per request** (Turn 1: model decides tool, Turn 2: model synthesizes answer).
The history extension here maintains context **across requests** at the interface level.

What is the fundamental difference between these two approaches? Which problem does each one solve?

Your answer:
