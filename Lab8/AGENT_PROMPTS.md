# Agent Prompt Pack (Lab 8)

## Prompt 1 — Project README Generation

Use this to generate a first draft of your user-facing `README.md`.

```text
I need a user-facing README.md for my project.
Context: Read FUNCTIONALITY.md, CONTRACT.md, and requirements.txt.
Goal: Write README.md at the project root.
Sections to include:
1. Project name and one-paragraph description of what the app does.
2. Setup — list every dependency and one-time configuration step (credentials, env vars).
3. How to run — the exact command to start the app.
4. Usage examples — 2-3 example inputs with their expected outputs, covering the core functionalities in FUNCTIONALITY.md.
5. Project structure — a brief table or list of src/ and tests/ layout.
Keep the tone practical. Do not include lab instructions or assignment details.
```

## Prompt 2 — Docstring Generation

Use this per-function to add missing docstrings.

```text
Add a docstring to the following function. The docstring must include:
1. One-line summary of what the function does.
2. Args section listing each parameter with type and description.
3. Returns section describing all possible return values (include every status string if the contract uses them).
The docstring must match the return contract in CONTRACT.md exactly.
Do not change the function implementation — only add the docstring.

[paste the function here]
```

## Prompt 3 — Test Gap Filling

Use this after identifying uncovered lines or branches in the coverage report.

```text
I need additional tests to cover the following gap in my test suite.
Context: Read the relevant source file and its existing test file.
Gap identified: [describe the uncovered function, branch, or edge case]
Requirements:
1. Write a pytest test function with a descriptive name.
2. The test must exercise the specific uncovered path.
3. Use the same mocking patterns already established in the test file (e.g., unittest.mock.patch for storage functions).
4. Do not modify existing tests.
5. The new test must pass.
```

## Guardrail Prompts

- Docstring contradicts implementation:
  - `The docstring must describe what the code actually does, not what it was originally designed to do. Re-read the function body before writing.`

- README contains internal lab details:
  - `README.md is for end users, not course staff. Remove any references to labs, assignments, or submission requirements.`

- New test weakens an existing one:
  - `Do not modify or remove existing tests. Only add new test functions. If a new test reveals a bug in the implementation, fix the implementation.`

- Coverage target unreachable (e.g., exception path):
  - `Use unittest.mock to raise an exception inside the patched function to cover the except branch.`
