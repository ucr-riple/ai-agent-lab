"""Storage layer: persists member records to Google Sheets via gspread."""

from __future__ import annotations

import os
from pathlib import Path

import gspread

REQUIRED_KEYS = {"name", "email", "student_id", "major"}

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_SERVICE_ACCOUNT_PATH = _PROJECT_ROOT / "service_account.json"

# Sheet header order; must match the actual spreadsheet column layout.
_COLUMNS = ["name", "email", "student_id", "major"]
# Column position (1-indexed) of the Email field.
_EMAIL_COL = _COLUMNS.index("email") + 1

SPREADSHEET_NAME = os.environ.get("SPREADSHEET_NAME", "ucr-club-assistant-members")


def _get_worksheet() -> gspread.Worksheet:
    client = gspread.service_account(filename=str(_SERVICE_ACCOUNT_PATH))
    return client.open(SPREADSHEET_NAME).sheet1


def _existing_emails(worksheet: gspread.Worksheet) -> set[str]:
    all_values = worksheet.col_values(_EMAIL_COL)
    return {v.strip().lower() for v in all_values[1:] if v}  # skip header row


def save_member(member_data: dict) -> str:
    """Persist a member record to Google Sheets.

    Returns:
        "success"  - record appended.
        "exists"   - email already present; no write performed.
        "error"    - missing required fields or any unexpected exception.
    """
    if not REQUIRED_KEYS.issubset(member_data):
        return "error"

    try:
        worksheet = _get_worksheet()

        if member_data["email"].strip().lower() in _existing_emails(worksheet):
            return "exists"

        worksheet.append_row([member_data[col] for col in _COLUMNS])
        return "success"

    except Exception:
        return "error"
