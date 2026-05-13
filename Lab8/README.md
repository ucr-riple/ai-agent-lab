# Lab 8: Quality Assurance and Documentation

## 1. Objective & Learning Outcomes

- Write a user-facing `README.md` for your own project using a coding agent.
- Add docstrings to all public functions and verify they match your `CONTRACT.md`.
- Audit test coverage across all three layers and fill identified gaps.
- Perform a final end-to-end walkthrough to confirm your system matches `FUNCTIONALITY.md`.

## 2. Prerequisites

- Lab 7 complete: all three layers (`storage`, `engine`, `interface`) are implemented and tests pass.
- `pytest-cov` installed for coverage reporting:

```bash
echo "pytest-cov>=4.0.0" >> requirements.txt
pip install -r requirements.txt
```

---

## 3. Phase 1: Project README

Your project needs a user-facing `README.md` that explains what your app does and how to run it. This is different from lab instruction files — it is written for a user, not a student.

Use the agent prompt in `AGENT_PROMPTS.md` to generate a draft, then review and edit it.

Minimum sections:
- **What it does** — one paragraph describing the app and its core capabilities.
- **Setup** — dependencies, credentials, and any one-time configuration steps.
- **How to run** — the exact command to start the app.
- **Usage examples** — 2–3 example inputs and their expected outputs.

Place this file at the root of your project (not inside `src/`).

---

## 4. Phase 2: Docstring Coverage

Public functions should have docstrings that describe what they do, their parameters, and their return contract. This makes the code self-documenting and helps the coding agent in future tasks.

### Step 1: Identify undocumented functions

```bash
python -m pydoc -w src   # generates HTML docs; missing docstrings appear as empty
```

Or simply review each public function across `storage_handler.py`, `storage_handler_extended.py`, `engine.py`, and `cli.py`.

### Step 2: Add docstrings with coding agent

Use the docstring prompt in `AGENT_PROMPTS.md` for each function that needs one.

Quality check: every docstring must describe:
- What the function does (one line).
- Parameters and their types.
- Return value and all possible return values (for functions with string status contracts).

### Step 3: Verify docstrings match CONTRACT.md

Cross-check each function's docstring against the `engine → storage` and `interface → engine` contracts in `CONTRACT.md`. If a docstring describes behavior that differs from the contract, update the docstring — or update `CONTRACT.md` if the implementation has legitimately evolved.

---

## 5. Phase 3: Test Coverage Audit

### Step 1: Run coverage report

```bash
pytest --cov=src --cov-report=term-missing tests/
```

The `--cov-report=term-missing` flag shows exactly which lines are not reached by any test.

### Step 2: Identify gaps

Review the report and note:
- Any public function with 0% coverage.
- Any branch (`if`/`elif`/`else`) that is never exercised.
- Edge cases in `FUNCTIONALITY.md` that have no corresponding test (e.g., empty input, API error paths).

### Step 3: Fill gaps with coding agent

Use the test-gap prompt in `AGENT_PROMPTS.md` to generate new test cases. Add them to the appropriate test file (`tests/storage/`, `tests/engine/`, or `tests/interface/`).

Target: every public function covered; all status return values exercised at least once.

Run the full suite after adding tests to confirm everything still passes:

```bash
pytest --cov=src --cov-report=term-missing tests/ -v
```

---

## 6. Phase 4: Final End-to-End Walkthrough

Run your app from the CLI and manually exercise every functionality defined in `FUNCTIONALITY.md`.

```bash
python -m src.interface.cli
```

For each functionality:
1. Enter a request that exercises the happy path.
2. Enter a request that triggers each failure/edge case.
3. Note whether the system behaves as described in `FUNCTIONALITY.md`.

Document any gap between the design spec and actual behavior. Update `FUNCTIONALITY.md` or the implementation to close the gap.

---

## 7. Common Failure Modes

| Symptom | Likely Cause | Fix |
|---|---|---|
| Coverage report shows 0% for a module | Module not inside `src/` | Check `--cov=src` path matches your package structure |
| Docstring says `"success" | "error"` but function can also return `"exists"` | Docstring written before implementation was complete | Update to match the actual return contract |
| New test fails on a path that was never tested | Latent bug exposed by coverage work | Fix the implementation; do not weaken the test |
| `FUNCTIONALITY.md` describes behavior the system doesn't implement | Feature was planned but not built | Either implement it or update `FUNCTIONALITY.md` to reflect current scope |

---

## 8. Deliverables for Checkoff

- [ ] `WORKSHEET.md` submitted.

Submit `WORKSHEET.md` for Lab 8 checkoff.
Full implementation for each student's own app and functionalities is due by **end of quarter**.
