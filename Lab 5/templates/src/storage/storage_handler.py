"""Lab 5 starter for storage layer implementation.

Replace TODOs with your implementation guided by tests.
"""

from __future__ import annotations


REQUIRED_KEYS = {"name", "email", "student_id", "major"}


def save_member(member_data: dict) -> str:
    """Save member into storage.

    Return contract:
    - "success"
    - "exists"
    - "error"
    """
    # TODO: Validate required keys.
    # TODO: Authenticate with service_account.json via gspread.
    # TODO: Read existing emails and check duplicates.
    # TODO: Append row when valid and non-duplicate.
    # TODO: Convert all exceptions to "error".
    raise NotImplementedError
