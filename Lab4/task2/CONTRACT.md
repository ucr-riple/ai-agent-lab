# CONTRACT.md (Short Teaching Template)

## Purpose
Use this file to map each functionality to component ownership and explicit interfaces.

## 1) Three Components (3 Layers)
- `interface`: collects user input, displays output, no application logic
- `engine`: validates/parses/orchestrates logic, no direct UI rendering
- `storage`: reads/writes data, enforces uniqueness/integrity

## 2) Mapping Functionality to Components
For each functionality from `FUNCTIONALITY.md`, define:
- `interface` responsibility
- `engine` responsibility
- `storage` responsibility (if persistence is needed)

## 3) Example (Reference)

In this example, `response_payload` means a structured return object (for example: `{"status": "...", "data": ...}`). `member_record` means validated member data (for example: `{"name": "...", "email": "...", "major": "...", "year": "..."}`).

### Functionality: Chatbot FAQ
- `interface`: collect user question, display answer/fallback
- `engine`: interpret question and produce answer
- `storage`: none, not required for basic FAQ

`interface -> engine`
- `get_faq_response(user_query: str) -> response_payload`
- Success: `{"status": "success", "data": {"answer": "Club meets every Friday at 5pm."}}`
- Failure: `{"status": "not_found", "message": "I don't have that information yet."}`

### Functionality: Member Registration
- `interface`: form submission for name/email/major/year, then show result message
- `engine`: validate required fields + normalize values using local rules (AI optional helper for messy free-text input)
- `storage`: check duplicate email + save record

`interface -> engine`
- `parse_registration(raw_text: str) -> response_payload`
- Success: `{"status": "success", "data": {"name": "...", "email": "..."}}`
- Failure: `{"status": "incomplete", "missing": ["email"]}`

`engine -> storage`
- `save_member(member_data: member_record) -> response_payload`
- Success: `{"status": "success", "id": "member_123"}`
- Failure: `{"status": "exists", "message": "duplicate email"}`


## 4) Quality Check
- Each responsibility has one owner only.
- Every contract defines success + failure statuses.
- No UI logic in `storage`, no persistence logic in `interface`.
