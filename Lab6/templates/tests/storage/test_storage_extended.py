"""Integration tests for extended storage layer (get_members, delete_member).

These tests hit a real Google Sheet — run them with a valid service_account.json
and a properly shared spreadsheet (see LAB6_MANUAL.md Phase 1).

Run:
    pytest tests/storage/test_storage_extended.py -v

Important: integration tests are stateful. Each test cleans up after itself
using delete_member(), so tests are safe to run in any order.
"""

import pytest
from src.storage.storage_handler import save_member
from src.storage.storage_handler_extended import delete_member, get_members

SAMPLE = {
    "name": "Lab6 Tester",
    "email": "lab6tester@ucr.edu",
    "student_id": "600600",
    "major": "CS",
}


# ---------------------------------------------------------------------------
# Test 1: Empty-state safety
# ---------------------------------------------------------------------------
def test_get_members_returns_a_list():
    """get_members must return a list and not raise, regardless of sheet state."""
    result = get_members()
    assert isinstance(result, list)


# ---------------------------------------------------------------------------
# Test 2: Save then read
# ---------------------------------------------------------------------------
def test_get_members_contains_saved_member():
    delete_member(SAMPLE["email"])  # ensure clean starting state

    save_member(SAMPLE)
    members = get_members()
    emails = [m.get("email") for m in members]
    assert SAMPLE["email"] in emails

    delete_member(SAMPLE["email"])  # cleanup


# ---------------------------------------------------------------------------
# Test 3: Delete existing member
# ---------------------------------------------------------------------------
def test_delete_member_success():
    delete_member(SAMPLE["email"])  # ensure clean starting state
    save_member(SAMPLE)

    result = delete_member(SAMPLE["email"])
    assert result == "success"


# ---------------------------------------------------------------------------
# Test 4: Delete nonexistent member
# ---------------------------------------------------------------------------
def test_delete_member_not_found():
    delete_member(SAMPLE["email"])  # ensure absent

    result = delete_member(SAMPLE["email"])
    assert result == "not_found"


# ---------------------------------------------------------------------------
# Test 5: Full round-trip
# ---------------------------------------------------------------------------
def test_round_trip_save_get_delete():
    delete_member(SAMPLE["email"])  # start clean

    # Save.
    save_result = save_member(SAMPLE)
    assert save_result == "success"

    # Read — member must appear.
    members = get_members()
    emails = [m.get("email") for m in members]
    assert SAMPLE["email"] in emails

    # Delete.
    delete_result = delete_member(SAMPLE["email"])
    assert delete_result == "success"

    # Confirm removal — member must be gone.
    members_after = get_members()
    emails_after = [m.get("email") for m in members_after]
    assert SAMPLE["email"] not in emails_after
