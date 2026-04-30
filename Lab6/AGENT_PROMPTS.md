# Agent Prompt Pack (Lab 6)

## Core Extension Prompt

Use this after copying `storage_handler_extended.py` into your project and writing the failing tests.

```text
I am extending the Storage layer for ucr-club-assistant.
Context: Read FUNCTIONALITY.md, CONTRACT.md, src/storage/storage_handler.py, and tests/storage/test_storage_extended.py.
Goal: Implement get_members() and delete_member(email) in src/storage/storage_handler_extended.py.
Requirements:
1. get_members() returns a list of dicts using the sheet header row as keys. Returns [] for empty sheet.
2. delete_member(email) removes the row where the email column matches the argument.
   Return types must be exactly: "success", "not_found", or "error".
3. Authentication must use service_account.json (no hardcoded secrets).
4. Column key names must match CONTRACT.md exactly.
5. All exceptions must be caught and returned as [] (for get_members) or "error" (for delete_member).
6. Keep logic modular and easy to test.
```

## Guardrail Prompts

- Wrong return type for delete:
  - `Return exactly "success", "not_found", or "error" — no booleans, no raised exceptions.`

- Empty sheet not handled:
  - `If the sheet has no data rows (header only), get_members() must return [] not None.`

- Row index off-by-one:
  - `Row 1 is the header; member data starts at row 2. Account for this offset when deleting by row index.`

- Column key mismatch:
  - `Use the header row from the sheet as dict keys when building records in get_members(), not hardcoded strings.`

- Credential path:
  - `Load credentials from service_account.json relative to the project root; do not embed any key material in source code.`

## Verification Prompt

```text
Now run the extended tests and confirm which test validates each required behavior:
- get_members returns a list in empty state
- get_members contains a saved member
- delete_member success path
- delete_member not_found path
- full round-trip save → get → delete → confirm removal
If any test fails, update the implementation only — do not modify or weaken the tests.
```
