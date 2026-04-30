# Lab 6 Worksheet

Student Name:
Section:
Project Name:
Date:

---

## 1) Credential Setup

- [ ] Google Cloud project created with Google Sheets API and Google Drive API enabled.
- [ ] Service account created and `service_account.json` downloaded.
- [ ] `service_account.json` added to `.gitignore`.
- [ ] Google Sheet created with correct header row matching `CONTRACT.md`.
- [ ] Sheet shared with service account email (Editor permission).
- [ ] `verify_connection.py` runs and prints `Connection OK.`

## 2) Lab 5 Baseline (Green State, Live)

- [ ] `test_save_new_member_success` passes with live Google Sheet.
- [ ] `test_duplicate_email_prevention` passes with live Google Sheet.
- [ ] `test_missing_fields_error` passes with live Google Sheet.

## 3) Extended Storage Layer

- [ ] `get_members()` implemented and returns a list of dicts.
- [ ] `delete_member(email)` implemented and returns `"success"`, `"not_found"`, or `"error"`.
- [ ] All 5 extended tests (`test_storage_extended.py`) pass in green state.
- [ ] Full suite `pytest tests/storage/ -v` is all green.

## 4) Current Snapshot

- Current status (one line):
- Next small step (one line):

## 5) Integration Awareness

- [ ] I can explain the difference between a unit test (mock) and an integration test (live data).
- [ ] I know why integration tests require cleanup after each run.
- [ ] I identified which column `get_members()` uses as the key for duplicate detection in my app.

Unique identifier column for my app:

## 6) Discussion Questions

### A) Live vs Mock Testing

Question: What is one advantage and one risk of running tests against a real Google Sheet instead of a mock?

Your answer:


### B) Idempotency

Question: If `test_save_new_member_success` is run twice without cleaning the sheet between runs, what happens on the second run? How would you fix this in a production test suite?

Your answer:


### C) Round-Trip Test Value

Question: Why is a round-trip test (save → get → delete → confirm removal) more valuable than testing each function in isolation?

Your answer:
