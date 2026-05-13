# Lab 6 Worksheet

Student Name:
Section:
Project Name:
Date:

---

## 1) Current Snapshot of Your Own Project

- Current status (one line):
- Next small step (one line):

## 2) Discussion Questions

### A) Tool Use vs Keyword Matching

Question: Why use an LLM to determine intent instead of checking if the user's message contains specific keywords?

Your answer:


### B) Reflection Value

Question: The Reflection step adds a second LLM call, which costs time and money. When is this cost worth paying, and when might you skip it?

Your answer:


### C) Mock vs Integration Testing

Question: The engine unit tests mock the storage layer. The Lab 6 tests hit a real Google Sheet. Why does the choice of mocking vs. integration testing differ between the engine layer and the storage layer?

Your answer:

---

## 3) Optional Extension: Manual Multi-Turn SDK Tool Calling

Complete this section only if you ran `engine_native_tools.py`.

```bash
cp ../Lab6/templates/src/engine/engine_native_tools.py src/engine/
python -m src.engine.engine_native_tools
```

- [ ] I ran the demo and saw `[Turn 1]`, `[Execute]`, and `[Turn 2]` printed for at least one input.

### Observation 1 — The two turns

For input `"Show me all registered members."`, paste what the terminal printed for each step:

`[Turn 1]  model chose →`

`[Execute] tool returned →`

`[Turn 2]  model synthesized final answer`

Final output string:


### Observation 2 — Incomplete input

Input: `"Register incomplete."`

Did the demo print a `[Turn 1]` / `[Execute]` / `[Turn 2]` sequence, or did it return immediately from Turn 1?

Primary engine output (`engine.py`):

Native multi-turn output (`engine_native_tools.py`):

Which behavior is more reliable for a production system, and why?


### Observation 3 — Return contract

Primary engine returns `{"status": ..., "message": ..., "data": ...}`. The native version returns a plain `str`.

Why does returning an unstructured string make the native version harder to integrate with an interface layer?


### Observation 4 — Dynamic tool list (OPTIONAL TODO 3)

If you completed OPTIONAL TODO 3 (adding `find_member` to the tool list):

What did `_describe_tools` generate for `find_member` without any changes to the function?

Did the model correctly route a "find member" request to it?


### Observation 5 — Your preference

Given the tradeoffs in the comparison table, which approach would you choose for a production feature? Justify in 2-3 sentences.
