# Agent Prompt Pack (Lab 8)

## Core Interface Implementation Prompt

Use this after copying the starter file and confirming all five tests are in red state.

```text
I am implementing the Interface layer for ucr-club-assistant.
Context: Read CONTRACT.md, FUNCTIONALITY.md, src/engine/engine.py, and tests/interface/test_interface.py.
Goal: Implement format_response(result: dict) -> str and run_session(process_fn=None)
      in src/interface/cli.py.
Requirements:
1. format_response: Read result["status"] and return a formatted string for each case:
   - "success"    → start with result["message"]; if result.get("data") is a non-empty
                    list, append each member's name and email on an indented line,
                    e.g., "  - {name} ({email})".
   - "exists"     → return result["message"].
   - "incomplete" → return result["message"] + "\n  Missing: " +
                    ", ".join(result["missing"]).
   - "unknown"    → return result["message"] + "\n\n" + _HELP_TEXT.
   - "error" and all other statuses → return result.get("message", "Unexpected response.").
   Do not raise; always return a string.
2. run_session: Loop calling input("You: ") to read one line at a time.
   - Skip blank lines (after strip).
   - Exit cleanly (print a goodbye message and return) when the line equals "quit"
     or "exit" (case-insensitive), or when EOFError is raised.
   - For all other input, call process_fn(user_input) to get a result dict,
     then print "Assistant: " followed by format_response(result).
   - Print a blank line after each response for readability.
3. process_fn defaults to process_request imported from src.engine.engine at the
   top of cli.py. Inside run_session, always call process_fn(user_input) —
   never call process_request directly — so tests can inject a mock.
4. Import process_request at the top of cli.py:
       from src.engine.engine import process_request
   This ensures the patch path "src.interface.cli.process_request" is valid if needed.
5. Do not modify or weaken any tests.
```

## Guardrail Prompts

- `format_response` raises instead of returning:
  - `Every code path in format_response must return a string. Remove any raise statements from the implementation and add a default case that returns result.get("message", "Unexpected response.").`

- `run_session` does not use `process_fn` parameter:
  - `Replace any direct calls to process_request inside the loop with calls to process_fn. The process_fn parameter exists specifically so tests can inject a mock engine.`

- Member list not appearing in format output:
  - `When result["status"] == "success" and result.get("data") is a non-empty list, iterate over the list and append each item's "name" and "email" to the output string on a new indented line.`

- Session loop does not exit on "quit":
  - `Compare user_input.strip().lower() against "quit" and "exit" at the top of the loop body, before calling process_fn.`

## Verification Prompt

```text
Now run the interface tests and confirm which test validates each behavior:
- Test 1: format_response with success + data list — member name and email appear in output
- Test 2: format_response with exists — duplicate message appears in output
- Test 3: format_response with incomplete — each missing field name appears in output
- Test 4: format_response with unknown — help text with available actions appears in output
- Test 5: run_session with mocked engine — formatted engine response appears in stdout
If any test fails, fix the implementation only — do not modify or weaken the tests.
```
