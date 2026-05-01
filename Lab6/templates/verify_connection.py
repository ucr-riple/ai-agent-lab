"""Verify live connection to Google Sheets.

Run from your project root (ucr-club-assistant/):
    python verify_connection.py

Expected output:
    Connected to: ucr-club-assistant-members
    Header row: ['name', 'email', 'student_id', 'major']
    Row count (data only): 0
    Connection OK.
"""

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
SERVICE_ACCOUNT_FILE = "service_account.json"
SHEET_NAME = "ucr-club-assistant-members"


def main():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    spreadsheet = client.open(SHEET_NAME)
    sheet = spreadsheet.sheet1

    print(f"Connected to: {spreadsheet.title}")

    all_values = sheet.get_all_values()
    if not all_values:
        print("Sheet is empty — add the header row before running tests.")
        return

    print(f"Header row: {all_values[0]}")
    print(f"Row count (data only): {len(all_values) - 1}")
    print("Connection OK.")


if __name__ == "__main__":
    main()
