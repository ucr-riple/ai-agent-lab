# Lab 5: Modular Storage & TDD with Coding Agents

## 1. Objective & Learning Outcomes
- Establish physical architecture: transition from Lab 4 design docs to a professional 3-tier project structure.
- Master the agent-TDD loop: use failing tests as the definition of done for coding agents.
- Implement persistence logic: build a modular storage layer with duplicate checks and error handling.
- Practice verification-driven development: use tests to validate AI-generated code.

## 2. Phase 1: Physical Project Scaffolding
Lab 4 was design-only. In Lab 5, create your implementation project root and skeleton.

Run in terminal:
```bash
# 1. Create and enter project root
mkdir ucr-club-assistant && cd ucr-club-assistant

# 2. Create source and test folders
mkdir -p src/storage src/engine src/interface
mkdir -p tests/storage tests/engine tests/interface

# 3. Initialize core files
# Move your Lab 4 FUNCTIONALITY.md and CONTRACT.md into this root.
touch requirements.txt .gitignore
```

Recommended initial `requirements.txt`:
```txt
pytest>=8.0.0
gspread>=6.0.0
google-auth>=2.0.0
```

Dependency note:
- `google-auth` is for Google Sheets authentication used by `gspread` in the **storage layer**.
- `google-genai` is only needed if your project code directly calls Gemini in the **engine/AI layer**.
- Local coding agents (for example, Codex/Cline) do not depend on this project `requirements.txt`.

## 3. Phase 2: Why TDD Before AI?
For coding-agent workflows, tests are your executable specification.

Why this matters:
1. Tests define exact inputs and outputs.
2. Agents must satisfy measurable behavior (red -> green).
3. Tests reduce hallucinated keys, contracts, or return types.

## 4. Phase 3: The Safety Suite (TDD Sequence)
Create `tests/storage/test_storage.py` first (red state).

Reference template: `templates/tests/storage/test_storage.py`

Minimum required test cases:
- Happy path -> returns `"success"`
- Duplicate path -> returns `"exists"`
- Missing fields -> returns `"error"`

Run:
```bash
pytest -q
```
You should first see failures (red state).

## 5. Phase 4: AI-Powered Implementation (Green State)
Then implement `src/storage/storage_handler.py` using your coding agent.

Reference starter: `templates/src/storage/storage_handler.py`

Agent prompt template is in: `AGENT_PROMPTS.md`

Required behaviors:
- Use `gspread`
- Authenticate via `service_account.json` (no hardcoded secrets)
- Check duplicate email with local logic before append
- Return only: `"success"`, `"exists"`, `"error"`
- Validate required keys before write

## 6. Common Failure Modes & Guardrails
See `AGENT_PROMPTS.md` for copy-paste guardrail prompts.

## 7. Deliverables for Checkoff
- [ ] Submit `WORKSHEET.md` (lightweight checkoff: timeline awareness, design/flow awareness, current snapshot)

## Worksheet Submission
- Submit `WORKSHEET.md` for Lab 5 checkoff.
- Full implementation for each student's own app and own functionalities is due by **end of quarter**.
