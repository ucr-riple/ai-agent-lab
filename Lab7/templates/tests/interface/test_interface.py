"""Unit tests for the interface layer.

The engine layer is mocked — these tests run without a Gemini API key or
Google Sheets credentials.

Run:
    pytest tests/interface/test_interface.py -v

Key concept: run_session accepts process_fn so tests can inject a mock
engine directly, without patching.  format_response is a pure function
and needs no mocking at all.
"""

from src.interface.cli import format_response, run_session


# ---------------------------------------------------------------------------
# Test 1: format_response — success with a member list
# ---------------------------------------------------------------------------
def test_format_success_with_member_list_shows_name_and_email():
    result = {
        "status": "success",
        "message": "2 member(s) found.",
        "data": [
            {"name": "Alice Chen", "email": "alice@ucr.edu", "student_id": "12345", "major": "CS"},
            {"name": "Bob Smith", "email": "bob@ucr.edu", "student_id": "67890", "major": "EE"},
        ],
    }
    output = format_response(result)
    assert "Alice Chen" in output
    assert "alice@ucr.edu" in output
    assert "Bob Smith" in output


# ---------------------------------------------------------------------------
# Test 2: format_response — duplicate registration
# ---------------------------------------------------------------------------
def test_format_exists_shows_duplicate_message():
    result = {"status": "exists", "message": "Member already registered.", "data": None}
    output = format_response(result)
    assert "already registered" in output


# ---------------------------------------------------------------------------
# Test 3: format_response — incomplete registration lists missing fields
# ---------------------------------------------------------------------------
def test_format_incomplete_lists_all_missing_fields():
    result = {
        "status": "incomplete",
        "message": "Missing required fields.",
        "missing": ["email", "student_id"],
    }
    output = format_response(result)
    assert "email" in output
    assert "student_id" in output


# ---------------------------------------------------------------------------
# Test 4: format_response — unknown intent includes help text
# ---------------------------------------------------------------------------
def test_format_unknown_includes_help_text():
    result = {
        "status": "unknown",
        "message": "I can register, list, or delete members.",
        "data": None,
    }
    output = format_response(result)
    # Help text must mention at least one available action so the user knows
    # what to do next.
    assert "register" in output.lower() or "list" in output.lower() or "delete" in output.lower()


# ---------------------------------------------------------------------------
# Test 5: run_session — mocked engine, response appears in stdout
# ---------------------------------------------------------------------------
def test_run_session_prints_formatted_engine_response(monkeypatch, capsys):
    def mock_engine(user_input):
        return {"status": "success", "message": "Member registered.", "data": None}

    # Simulate: one message, then quit.
    inputs = iter(
        ["Register Alice Chen, alice@ucr.edu, student_id 12345, CS major.", "quit"]
    )
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    run_session(process_fn=mock_engine)

    captured = capsys.readouterr()
    assert "Member registered." in captured.out
