# Lab 7: Logic Layer — Tool Use & Reflection Design Patterns

## 1. Objective & Learning Outcomes

- Understand two agentic design patterns: **Tool Use** (AI dispatches to Python functions) and **Reflection** (AI validates its own output before acting).
- Implement the engine layer (`src/engine/engine.py`) using TDD + coding agents.
- Complete the `interface → engine → storage` chain defined in Lab 4.

## 2. Prerequisites

- Lab 6 complete: live Google Sheets connected, all storage tests green.
- `service_account.json` in project root and storage layer working.
- `.env` with `GEMINI_API_KEY` set (from Lab 1 setup).

Add `google-genai` to your project's `requirements.txt` and install it:

```bash
echo "google-genai>=1.0.0" >> requirements.txt
pip install -r requirements.txt
```

---

## 3. The Two Patterns

### Tool Use

The engine receives raw natural-language input and must decide which storage operation to perform. Rather than hardcoding keyword matching, it delegates this decision to Gemini: the AI extracts a structured intent and any provided fields from the user's message.

```
user_input (str)
    └── Gemini (extraction call)
            └── {"intent": "register", "data": {"name": ..., "email": ...}}
                    └── Python dispatches → save_member(data)
```

The AI "uses a tool" indirectly: it tells the engine which function to call and with which arguments. This is the **Tool Use** pattern.

### Reflection

After the AI extracts intent and data, a second AI call validates whether the extraction is complete before any storage function is called. If required fields are missing, the engine returns `"incomplete"` immediately — the storage layer is never touched.

```
extracted_data
    └── Gemini (reflection call)
            └── {"complete": false, "missing": ["email", "student_id"]}
                    └── return {"status": "incomplete", ...}   ← storage NOT called
```

This is the **Reflection** pattern: the AI critiques its own output to catch errors before they propagate.

---

## 4. Phase 1: Add Engine Skeleton

Create the engine module in your project:

```bash
cp ../Lab7/templates/src/engine/engine.py src/engine/
```

Also create the test folder:

```bash
mkdir -p tests/engine
cp ../Lab7/templates/tests/engine/test_engine.py tests/engine/
```

---

## 5. Phase 2: Write Failing Tests (Red State)

Run the engine tests immediately after copying:

```bash
pytest tests/engine/test_engine.py -v
```

You should see `NotImplementedError` on all five tests — this is expected.

Minimum required test cases (already in the template):
- Register success: storage mock returns `"success"` → engine returns `{"status": "success"}`.
- Register duplicate: storage mock returns `"exists"` → engine returns `{"status": "exists"}`.
- List members: storage mock returns a list → engine returns `{"status": "success", "data": [...]}`.
- Reflection blocks incomplete input: `"Register Bob."` → engine returns `{"status": "incomplete"}` and `save_member` is **never called**.
- Unknown intent: unrelated input → engine returns `{"status": "unknown"}`.

Test 4 is the most important: `mock_save.assert_not_called()` verifies that Reflection actually prevents a bad write.

---

## 6. Phase 3: Implement with Coding Agent (Green State)

Use the agent prompt in `AGENT_PROMPTS.md` to implement `process_request()`.

Run tests to confirm green state:

```bash
pytest tests/engine/test_engine.py -v
```

All five tests must pass.

Key implementation note — mock patch target:

When `engine.py` imports `save_member` with:
```python
from src.storage.storage_handler import save_member
```
the correct patch path is `"src.engine.engine.save_member"` (where it is **used**, not where it is defined). Make sure your implementation imports storage functions at the top of `engine.py` so the patch targets are predictable.

---

## 7. Phase 4: Integration Smoke Test

After unit tests pass, run a quick end-to-end test with real storage:

```bash
python -c "
from src.engine.engine import process_request
result = process_request('Show me all registered members.')
print(result)
"
```

Expected: `{'status': 'success', 'message': ..., 'data': [...]}` with live data from your Google Sheet.

Then test a registration:

```bash
python -c "
from src.engine.engine import process_request
result = process_request('Register Test User, test7@ucr.edu, student_id 7001, ECE major.')
print(result)
"
```

Verify the new row appears in your Google Sheet.

Clean up test data from the sheet when done.

---

## 8. Phase 5: Full Project Suite

Run all tests across every layer:

```bash
pytest tests/ -v
```

All storage and engine tests must pass. This confirms the full `engine → storage` chain is working correctly.

---

## 9. Common Failure Modes

| Symptom | Likely Cause | Fix |
|---|---|---|
| `patch` has no effect | Patching the wrong module path | Patch `"src.engine.engine.save_member"`, not `"src.storage.storage_handler.save_member"` |
| `test_incomplete_...` fails | Reflection step not implemented or bypassed | Ensure reflection call happens before any storage dispatch |
| `mock_save.assert_not_called()` fails | Storage called despite incomplete data | Reflection must return early before the dispatch block |
| `status` key missing from return | Not all code paths return a full dict | Every branch must return `{"status": ..., "message": ...}` |
| `GEMINI_API_KEY` error in tests | `.env` not loaded in test context | Add `load_dotenv()` at the top of `engine.py` |

See `AGENT_PROMPTS.md` for copy-paste guardrail prompts.

---

## 10. Deliverables for Checkoff

- [ ] All five engine unit tests pass (`pytest tests/engine/ -v`).
- [ ] Integration smoke test runs and produces a valid response.
- [ ] Full suite `pytest tests/ -v` is all green.
- [ ] `WORKSHEET.md` submitted.

Submit `WORKSHEET.md` for Lab 7 checkoff.
Full implementation for each student's own app and functionalities is due by **end of quarter**.

---

## 11. Optional Extension: Hand-Rolled Multi-Turn Tool Calling

The primary engine uses structured extraction: your Python code extracts intent as JSON, runs Reflection, then dispatches to storage. This is explicit and testable.

This extension builds tool calling from scratch — **no `tools=` config is passed to the SDK**. Two helper functions implement what the SDK automates internally:

- **`_describe_tools(fns)`** — iterates the caller-supplied function list, uses `inspect.signature` to read each function's parameter names and type annotations, takes the first line of `__doc__` as a summary, and returns a formatted string that goes directly into the Turn 1 prompt. The model never sees actual Python callables — only this text.

- **`_dispatch(table, name, args)`** — builds a `{name: fn}` lookup table from the same list, then uses `inspect.signature` to decide the calling convention: no-arg functions get `fn()`, functions with a single `dict`-annotated parameter get `fn(args)`, all others get `fn(**args)`.

```
_describe_tools([save_member, get_members, delete_member])
   → "  save_member(member_data: dict)  — Save member into storage.\n ..."

Turn 1   _TURN1_TEMPLATE.format(tool_descriptions=..., user_input=...)
         → model outputs {"tool": "save_member", "args": {...}}

Execute  _dispatch(tool_table, "save_member", args)
         → inspects signature → fn(args)  → "success" | "exists" | "error"

Turn 2   _TURN2_TEMPLATE.format(tool_result=...) → model writes final answer
```

### Side-by-side comparison

| Property | Primary (`engine.py`) | This file (`engine_native_tools.py`) |
|---|---|---|
| Intent detection | Structured JSON extraction | JSON tool-call decision via prompt |
| Validation | Explicit Reflection call | Model's own judgment |
| SDK tool config | None | None — tools described via `_describe_tools` |
| Dispatch | Hardcoded `if/elif` | `_dispatch()` driven by `inspect` + name table |
| Tool list | Baked into engine | Passed by the caller |
| Return value | Typed `dict` contract | Natural-language `str` |
| Unit-testable | Yes — mock storage functions | Hard — model controls flow |

### Run the demo

```bash
cp ../Lab7/templates/src/engine/engine_native_tools.py src/engine/
python -m src.engine.engine_native_tools
```

The demo prints `[Turn 1]`, `[Execute]`, and `[Turn 2]` for each input so you can follow the two-turn flow.

### What to notice

1. **Turn 1 response** — the model outputs `{"tool": "get_members", "args": {}}` (or similar). This JSON is the model's decision, parsed by your code — not by the SDK.
2. **Null tool** — for off-topic input, the model outputs `{"tool": null, ...}`. Your code handles this branch and asks the model to answer directly.
3. **Incomplete input** (`"Register incomplete."`) — does the model still call `save_member` with partial args, or does it set `tool` to `null`? Compare to what the Reflection step in `engine.py` guarantees every time.
4. **Return type** — the function returns a plain `str`. A downstream interface layer cannot branch reliably on `result["status"]`.

After running this, read the SDK docs for `GenerateContentConfig(tools=[...])`. OPTIONAL TODO 3 in the file asks you to identify what the SDK adds on top of what this hand-rolled version does.
