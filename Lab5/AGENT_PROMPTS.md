# Agent Prompt Pack (Lab 5)

## Core Implementation Prompt
Use this after writing failing tests.

```text
I am implementing the Storage layer for ucr-club-assistant.
Context: Read FUNCTIONALITY.md, CONTRACT.md, and tests/storage/test_storage.py.
Goal: Implement src/storage/storage_handler.py.
Requirements:
1. Use gspread for Google Sheets access.
2. Authentication must use service_account.json (no hardcoded secrets).
3. Implement local duplicate check on the Email column before append.
4. Return types must be exactly: "success", "exists", or "error".
5. If required keys are missing, return "error".
6. Keep logic modular and easy to test.
```

## Guardrail Prompts
- Hardcoded keys issue:
  - `Ensure key names match CONTRACT.md exactly (for example: student_id, not studentID).`
- Missing duplicate check:
  - `Read existing Email values first; do not rely on sheet append errors to detect duplicates.`
- Credential safety issue:
  - `Load credentials from service_account.json; do not embed private keys in source code.`
- Wrong return contract:
  - `Only return one of: "success", "exists", "error".`

## Verification Prompt
```text
Now run tests and explain which test validates each required behavior:
- success path
- duplicate path
- missing-fields error path
If any test fails, update implementation only (do not weaken tests).
```
