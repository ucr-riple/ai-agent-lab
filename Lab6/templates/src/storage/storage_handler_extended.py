"""Lab 6 extension: adds get_members() and delete_member() to the storage layer."""

from __future__ import annotations

import os
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_SERVICE_ACCOUNT_PATH = _PROJECT_ROOT / "service_account.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

SPREADSHEET_NAME = os.environ.get("SPREADSHEET_NAME", "ucr-club-assistant-members")


def _open_sheet() -> gspread.Worksheet:
    creds = Credentials.from_service_account_file(str(_SERVICE_ACCOUNT_PATH), scopes=SCOPES)
    client = gspread.authorize(creds)
    return client.open(SPREADSHEET_NAME).sheet1


def get_members() -> list[dict]:
    """Return all member rows as a list of dicts keyed by the header row.

    Returns [] when the sheet has no data rows or on any exception.
    """
    try:
        sheet = _open_sheet()
        return sheet.get_all_records()
    except Exception:
        return []


def delete_member(email: str) -> str:
    """Delete the first row whose email column matches email.

    Returns:
        "success"   - matching row found and deleted.
        "not_found" - no row contains that email value.
        "error"     - any exception during the operation.
    """
    try:
        sheet = _open_sheet()
        cell = sheet.find(email, in_column=2)
        if cell is None:
            return "not_found"
        # Guard against accidentally matching the header row.
        if cell.row == 1:
            return "not_found"
        sheet.delete_rows(cell.row)
        return "success"
    except Exception:
        return "error"
