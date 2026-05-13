# Lab 6: Persistence Layer via Google Sheets

## 1. Objective & Learning Outcomes

- Activate the live Google Sheets backend: set up a service account, configure credentials, and connect your storage layer to a real spreadsheet.
- Confirm green state: run the Lab 5 storage tests against a live Google Sheet.
- Extend the storage layer: add `get_members()` and `delete_member()` using the same TDD loop from Lab 5.
- Practice integration testing: write tests that exercise real data round-trips (save → read → delete).

## 2. Prerequisites

- Lab 5 complete: project scaffold exists at `ucr-club-assistant/` with `save_member()` implemented.
- `gspread>=6.0.0` and `google-auth>=2.0.0` in `requirements.txt` (already added in Lab 5).

## 3. Phase 1: Google Sheets Live Setup

In Lab 5 you wrote the storage implementation but never connected to a real sheet. Phase 1 makes it live.

### Step 1: Create a Google Cloud Project (or reuse existing)

1. Go to https://console.cloud.google.com/.
2. Click the project selector → **New Project** → name it `ucr-club-assistant`.
3. Click **Create**.

### Step 2: Enable Required APIs

1. In the Cloud Console, go to **APIs & Services → Library**.
2. Search for and enable **Google Sheets API**.
3. Search for and enable **Google Drive API**.

### Step 3: Create a Service Account

1. Go to **APIs & Services → Credentials**.
2. Click **Create Credentials → Service Account**.
3. Name: `storage-agent` → click **Create and Continue** → **Done**.
4. Click the new service account → **Keys → Add Key → Create new key → JSON**.
5. Download the file and rename it `service_account.json`.
6. Move it into your project root (`ucr-club-assistant/`).

Security note:
- Add `service_account.json` to your `.gitignore` immediately.
- Never commit this file to version control.
- The `"client_email"` field inside the file is the identity you will share with your sheet.

### Step 4: Create Your Google Sheet

1. Go to https://sheets.google.com/ and create a new spreadsheet.
2. Name it exactly: `ucr-club-assistant-members`.
3. In Row 1, add the column headers that match `CONTRACT.md`:

```
name    email    student_id    major
```

### Step 5: Share the Sheet with Your Service Account

1. Open the spreadsheet → click **Share**.
2. Paste the `"client_email"` value from `service_account.json` into the email field.
3. Set permission to **Editor** and click **Send**.

---

## 4. Phase 2: Verify Live Connectivity

Copy and run the verification script from your `ucr-club-assistant/` root:

```bash
cp ../Lab6/templates/verify_connection.py .
python verify_connection.py
```

Expected output:
```
Connected to: ucr-club-assistant-members
Header row: ['name', 'email', 'student_id', 'major']
Row count (data only): 0
Connection OK.
```

If you see an error, check:
- `service_account.json` is in the project root.
- The spreadsheet was shared with the service account email (Editor permission).
- Both APIs are enabled in your Cloud project.

---

## 5. Phase 3: Confirm Lab 5 Tests Pass (Green State, Live)

With live credentials in place, run the Lab 5 test suite against the real sheet:

```bash
cd ucr-club-assistant
pytest tests/storage/test_storage.py -v
```

All three tests must pass:
- `test_save_new_member_success`
- `test_duplicate_email_prevention`
- `test_missing_fields_error`

If any test fails, use the guardrail prompts in `AGENT_PROMPTS.md` to fix the implementation — do not modify the tests.

---

## 6. Phase 4: Extend the Storage Layer (TDD)

`save_member()` is a write-only operation. A complete persistence layer needs read and delete capabilities.

### Step 1: Write Failing Tests First (Red State)

Copy the extended src and test file into your project:

```bash
cp ../Lab6/templates/src/storage/storage_handler_extended.py src/storage/
cp ../Lab6/templates/tests/storage/test_storage_extended.py tests/storage/
```

Run to confirm red state:

```bash
pytest tests/storage/test_storage_extended.py -v
```

You should see `NotImplementedError` — this is expected.

Minimum required test cases (already in the template):
- Empty state: `get_members()` returns a list (no crash).
- Save then read: `get_members()` returns the saved member.
- Delete existing: `delete_member(email)` returns `"success"`.
- Delete nonexistent: `delete_member(email)` returns `"not_found"`.
- Full round-trip: save → get → delete → confirm removal.

### Step 2: Implement with Coding Agent (Green State)

Copy the starter into your project:

```bash
cp ../Lab6/templates/src/storage/storage_handler_extended.py src/storage/
```

Use the agent prompt in `AGENT_PROMPTS.md` to implement `get_members()` and `delete_member()`.

Run tests to confirm green state:

```bash
pytest tests/storage/test_storage_extended.py -v
```

### Step 3: Full Storage Suite

Run all storage tests together:

```bash
pytest tests/storage/ -v
```

All Lab 5 and Lab 6 tests must pass.

---

## 7. Teardown After Testing

Integration tests write real rows to your sheet. After each test session, verify and clean up:

```bash
python verify_connection.py   # check row count
```

Or open the Google Sheet and delete leftover test rows manually.

Note: In production systems, test cleanup is automated with fixtures and database rollbacks. For this lab, manual cleanup is acceptable.

---

## 8. Common Failure Modes

| Symptom | Likely Cause | Fix |
|---|---|---|
| `SpreadsheetNotFound` | Sheet name mismatch or not shared | Confirm exact name and service account sharing |
| `DefaultCredentialsError` | `service_account.json` path wrong | Check filename and working directory |
| `KeyError` in `get_members()` | Header row missing or column name mismatch | Verify header names match `CONTRACT.md` exactly |
| Tests pass locally but rows don't appear | Wrong spreadsheet opened | Print `spreadsheet.title` to confirm |
| `delete_member` returns `"not_found"` unexpectedly | Email column name mismatch | Check exact column header used in `find()` call |

See `AGENT_PROMPTS.md` for copy-paste guardrail prompts.

---

## 9. Deliverables for Checkoff

- [ ] `WORKSHEET.md` submitted.

Submit `WORKSHEET.md` for Lab 6 checkoff.
Full implementation for each student's own app and functionalities is due by **end of quarter**.
