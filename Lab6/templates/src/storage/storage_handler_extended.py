"""Lab 6 extension: adds get_members() and delete_member() to the storage layer.

Copy this file into src/storage/ in your project and implement the TODOs
guided by the failing tests in tests/storage/test_storage_extended.py.
"""

from __future__ import annotations

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
SERVICE_ACCOUNT_FILE = "service_account.json"
SHEET_NAME = "ucr-club-assistant-members"


def _open_sheet():
    """Authenticate and return the first sheet of the spreadsheet."""
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    return client.open(SHEET_NAME).sheet1


def get_members() -> list[dict]:
    """Return all member rows as a list of dicts.

    Return contract:
    - List of dicts keyed by the header row column names (e.g. "name", "email").
    - Returns [] when the sheet has no data rows.
    - Returns [] on any exception.
    """
    # TODO: Open the sheet with _open_sheet().
    # TODO: Call sheet.get_all_records() to get rows as dicts.
    # TODO: Return the result (it is already a list; return [] if empty).
    # TODO: Wrap everything in try/except and return [] on any exception.
    raise NotImplementedError


def delete_member(email: str) -> str:
    """Delete the first row whose email column value matches email.

    Return contract:
    - "success"   → matching row found and deleted.
    - "not_found" → no row contains that email value.
    - "error"     → any exception during the operation.
    """
    # TODO: Open the sheet with _open_sheet().
    # TODO: Use sheet.find(email) to locate the cell containing the email value.
    #       If find() raises CellNotFound, return "not_found".
    # TODO: Delete the row at the cell's row index using sheet.delete_rows(cell.row).
    # TODO: Return "success" after deletion.
    # TODO: Catch all other exceptions and return "error".
    raise NotImplementedError
