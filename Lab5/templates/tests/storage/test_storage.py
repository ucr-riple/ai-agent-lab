import pytest
from src.storage.storage_handler import save_member


# Test 1: Happy Path
def test_save_new_member_success():
    sample_data = {
        "name": "Alice",
        "email": "alice@ucr.edu",
        "student_id": "111",
        "major": "CS",
    }
    result = save_member(sample_data)
    assert result == "success"


# Test 2: Conflict Path (Duplicate)
def test_duplicate_email_prevention():
    sample_data = {
        "name": "Alice",
        "email": "alice@ucr.edu",
        "student_id": "111",
        "major": "CS",
    }
    save_member(sample_data)
    result = save_member(sample_data)
    assert result == "exists"


# Test 3: Error Path (Incomplete Data)
def test_missing_fields_error():
    incomplete_data = {"name": "Bob"}  # Missing email, id, major
    result = save_member(incomplete_data)
    assert result == "error"
