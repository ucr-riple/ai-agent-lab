# Lab 8: Presentation Layer & System Integration

## 1. Objective & Learning Outcomes

- Build the **interface layer** (`src/interface/cli.py`) to complete the three-tier architecture: `interface → engine → storage`.
- Practice **dependency injection** — `run_session` accepts `process_fn` so the engine can be swapped for a test double.
- Understand **format contracts**: the interface depends on the engine's typed `dict` return to format output reliably.
- Run a **full system integration test** with all three layers active simultaneously.

## 2. Prerequisites

- Lab 7 complete: all five engine tests pass and integration smoke test runs.
- `service_account.json` in project root and storage layer working.
- `.env` with `GEMINI_API_KEY` set.

No new dependencies are required for this lab.

---

## 3. The Interface Layer

The interface is the **Presentation Layer** (Skin) of the system. It is responsible only for:

1. Collecting raw text input from the user.
2. Passing that text to `process_request()` in the engine layer.
3. Formatting the response dict into a human-readable string and printing it.

```
user → run_session() → engine.process_request() → storage
                     ←──────────── result dict ──────────
                     → format_response(result) → terminal
```

The interface layer has **no AI calls** and **no storage access**. It delegates all logic to the engine and all persistence to storage.

This separation makes the interface layer independently testable: in unit tests the engine is replaced with a mock, so the interface tests never make a real API call or touch Google Sheets.

---

## 4. Phase 1: Add Interface Skeleton

Create the interface module in your project:

```bash
mkdir -p src/interface tests/interface
cp ../Lab8/templates/src/interface/cli.py src/interface/
cp ../Lab8/templates/tests/interface/test_interface.py tests/interface/
```

---

## 5. Phase 2: Write Failing Tests (Red State)

Run the interface tests immediately after copying:

```bash
pytest tests/interface/test_interface.py -v
```

You should see `NotImplementedError` on all five tests — this is expected.

Minimum required test cases (already in the template):
- **Format success with data**: `"success"` result with a member list includes each member's name and email.
- **Format exists**: `"exists"` result output includes the duplicate message.
- **Format incomplete**: `"incomplete"` result output lists every missing field name.
- **Format unknown**: `"unknown"` result output includes help text with available actions.
- **Run session**: `run_session()` with a mocked engine prints the formatted response to stdout.

---

## 6. Phase 3: Implement with Coding Agent (Green State)

Use the agent prompt in `AGENT_PROMPTS.md` to implement `format_response()` and `run_session()`.

Run tests to confirm green state:

```bash
pytest tests/interface/test_interface.py -v
```

All five tests must pass.

Key implementation note — dependency injection:

`run_session` accepts an optional `process_fn` parameter. When `process_fn is None`, it defaults to `process_request` imported at the top of `cli.py`. Inside the loop, always call `process_fn(user_input)` — never call `process_request` directly — so tests can inject a mock without patching.

If you need to patch for other reasons, the correct patch path is `"src.interface.cli.process_request"` (where it is **used**, not where it is defined).

---

## 7. Phase 4: Full System Integration Test

After unit tests pass, run the CLI with the full stack active:

```bash
python -m src.interface.cli
```

Test each engine capability in sequence:

1. Register a new member: `Register Test User, test8@ucr.edu, student_id 8001, CS major.`
2. List all members: `Show me all registered members.`
3. Try an incomplete registration: `Register Bob.`
4. Delete the test member: `Delete test8@ucr.edu.`
5. Try an off-topic message: `What is the weather today?`

Verify that:
- The new member appears in your Google Sheet after step 1.
- The member is listed in the output for step 2.
- Step 3 returns an `"incomplete"` message with the specific missing fields.
- The member row is removed from the sheet after step 4.
- Step 5 returns an `"unknown"` response with the help text.

Type `quit` or `exit` to stop the session.

---

## 8. Phase 5: Full Project Suite

Run all tests across every layer:

```bash
pytest tests/ -v
```

All storage, engine, and interface tests must pass. This confirms the complete `interface → engine → storage` chain is working correctly end to end.

---

## 9. Common Failure Modes

| Symptom | Likely Cause | Fix |
|---|---|---|
| `format_response` wrong for `"success"` with data | Member list not iterated | Check `result.get("data")` is a list and iterate each item |
| `test_run_session_...` hangs | Loop not using built-in `input()` | Ensure the loop calls `input(...)`, not `sys.stdin.readline()` |
| `test_run_session_...` assertion fails | Formatted string missing the expected substring | Match your format string to the test's `assert ... in captured.out` check |
| `NotImplementedError` on all tests | Skeleton not yet modified | Complete the implementation before running tests |
| Full suite fails on engine or storage tests | Earlier layer incomplete | Complete Labs 5–7 first |

See `AGENT_PROMPTS.md` for copy-paste guardrail prompts.

---

## 10. Deliverables for Checkoff

- [ ] All five interface unit tests pass (`pytest tests/interface/ -v`).
- [ ] Full system integration test runs end-to-end from CLI to Google Sheets.
- [ ] Full suite `pytest tests/ -v` is all green.
- [ ] `WORKSHEET.md` submitted.

Submit `WORKSHEET.md` for Lab 8 checkoff.
Full implementation for each student's own app and functionalities is due by **end of quarter**.

---

## 11. Optional Extension: Conversation History

The current CLI treats each user message independently — `process_request` receives only the current turn's text. This extension adds a **conversation history buffer** so the engine sees prior context when answering follow-up messages.

Modify `run_session` to maintain a `history` list of `{"role": str, "text": str}` dicts. Before each engine call, build a context string from the last N turns and prepend it to `user_input`:

```python
context = "\n".join(f"{h['role']}: {h['text']}" for h in history[-4:])
augmented_input = f"{context}\nUser: {user_input}" if context else user_input
result = process_fn(augmented_input)
```

Then append each user turn (and the engine's status) to `history` after the call.

### What to test

1. Ask to register a member but provide only the name.
2. In the next turn, add `"My email is bob@ucr.edu"` — a follow-up without repeating the name.
3. Continue adding fields one turn at a time until the engine accepts the registration.

### What to notice

1. **Context window growth** — at what history depth does the engine start to lose earlier fields?
2. **Reflection with context** — does the Reflection step correctly identify which fields are still missing even when they appear in prior turns?
3. **Return contract dependency** — can `run_session` use `result["status"]` to decide whether to append a turn to history (e.g., skip appending on `"error"`), or is it safer to store all turns unconditionally?
4. **Comparison to Lab 7 Optional** — the Lab 7 extension used a two-turn SDK loop per request. How does session-level history in the interface differ from per-request multi-turn in the engine?
