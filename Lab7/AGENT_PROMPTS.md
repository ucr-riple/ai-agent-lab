# Agent Prompt Pack (Lab 7)

## Core Engine Implementation Prompt

Use this after copying the starter file and confirming all five tests are in red state.

```text
I am implementing the Engine layer for ucr-club-assistant.
Context: Read CONTRACT.md, FUNCTIONALITY.md, src/storage/storage_handler.py,
         src/storage/storage_handler_extended.py, and tests/engine/test_engine.py.
Goal: Implement process_request(user_input: str) -> dict in src/engine/engine.py.
Requirements:
1. Step 1 — Tool Use: Initialize an AI model client using _API_KEY and _MODEL from
   engine.py. Call the model with _EXTRACTION_PROMPT as the system instruction and
   user_input as the user message. Enforce JSON output. Parse the response to extract:
   {"intent": "register"|"list"|"delete"|"unknown", "data": {field: value, ...}}
   Load _API_KEY from os.getenv() only; never hardcode it.
2. Step 2 — Reflection: Call the model again with _REFLECTION_PROMPT formatted with
   the extraction result. Enforce JSON output. Parse the response to get
   {"complete": bool, "missing": [...]}.
   If complete is False, return {"status": "incomplete", "message": ..., "missing": [...]}
   immediately — do NOT call any storage function.
3. Step 3 — Dispatch: Based on intent, call:
   - "register" → save_member(data)              returns "success" | "exists" | "error"
   - "list"     → get_members()                  returns list of dicts
   - "delete"   → delete_member(data.get("email")) returns "success" | "not_found" | "error"
   - "unknown"  → return {"status": "unknown", "message": "...", "data": None}
4. Return contract: every code path returns a dict with at least "status" and "message" keys.
5. Import save_member, get_members, delete_member at the top of engine.py
   so the patch paths in tests (src.engine.engine.*) resolve correctly.
6. Wrap all logic in try/except; return {"status": "error", "message": str(e), "data": None}.
```

## Guardrail Prompts

- Incorrect patch target (tests fail despite correct logic):
  - `Import storage functions at the top of engine.py with 'from src.storage...' so tests can patch 'src.engine.engine.save_member' correctly.`

- Reflection not blocking storage call:
  - `When reflection returns complete=False, use an early return immediately — do not fall through to the dispatch block.`

- Missing "message" key in some paths:
  - `Every return statement must include both "status" and "message" keys. Check all branches including "unknown" and "error".`

- Hardcoded API key:
  - `Load _API_KEY from os.getenv() only. Never write the key value in source code.`

- Model response not parseable as JSON:
  - `Both model calls (_EXTRACTION_PROMPT and _REFLECTION_PROMPT) must enforce JSON-only output. Use the structured output option available in the SDK being used (e.g., response_mime_type, response_format, or equivalent).`

## Verification Prompt

```text
Now run the engine tests and confirm which test validates each behavior:
- Test 1: save_member called with correct data, returns success status
- Test 2: save_member returns "exists", engine returns exists status
- Test 3: get_members result is returned in data field
- Test 4: Reflection blocks incomplete input — save_member is never called
- Test 5: Unknown intent returns unknown status without calling any storage function
If any test fails, fix the implementation only — do not modify or weaken the tests.
```
