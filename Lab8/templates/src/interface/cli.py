"""Lab 8 starter for the interface layer.

The interface is the Presentation Layer (Skin) of the system.

Architecture position:
    interface -> engine -> storage

This module collects user input from the terminal, passes it to
process_request() in the engine layer, and formats the result dict
into a human-readable string for display.

This layer makes no AI calls and does not access storage directly.

Replace every TODO with your implementation guided by the tests.
"""

from __future__ import annotations

# Import process_request at the top so the patch path
# "src.interface.cli.process_request" is valid in tests.
from src.engine.engine import process_request

_WELCOME_BANNER = """
========================================
  UCR Club Registration Assistant
  Type 'quit' or 'exit' to stop.
========================================
"""

_HELP_TEXT = (
    "I can help you:\n"
    "  - Register a new member\n"
    "  - List all registered members\n"
    "  - Delete a member\n"
    "Just describe what you want in plain English."
)


def format_response(result: dict) -> str:
    """Convert an engine result dict to a human-readable string.

    Expected result shapes (from engine.process_request):
        {"status": "success",    "message": str, "data": list | None}
        {"status": "exists",     "message": str, "data": None}
        {"status": "incomplete", "message": str, "missing": list}
        {"status": "unknown",    "message": str, "data": None}
        {"status": "error",      "message": str, "data": None}

    Always returns a plain string — never raises.
    """
    # TODO: Read result["status"] and build a formatted string for each case.
    #
    #   "success"    → start with result["message"]
    #                  if result.get("data") is a non-empty list, append each
    #                  member's name and email indented, e.g.:
    #                      "  - Alice Chen (alice@ucr.edu)"
    #
    #   "exists"     → return result["message"]
    #
    #   "incomplete" → return result["message"] + "\n  Missing: " +
    #                  ", ".join(result["missing"])
    #
    #   "unknown"    → return result["message"] + "\n\n" + _HELP_TEXT
    #
    #   "error" and anything else → return result.get("message", "Unexpected response.")
    raise NotImplementedError


def run_session(process_fn=None):
    """Run a REPL session: read input, call engine, print formatted response.

    Parameters
    ----------
    process_fn:
        Callable that accepts a str and returns a dict.  Defaults to
        process_request from the engine layer.  Pass a mock here in tests
        so the session runs without a live AI or Google Sheets connection.
    """
    if process_fn is None:
        process_fn = process_request

    print(_WELCOME_BANNER)

    # TODO: Loop:
    #   1. Call input("You: ") to read a line of user input.
    #      Wrap the call in a try/except to catch EOFError — print a goodbye
    #      message and return when it fires.
    #   2. Strip whitespace from the line; skip it (continue) if it is empty.
    #   3. If the stripped line equals "quit" or "exit" (case-insensitive),
    #      print a goodbye message and return.
    #   4. Call process_fn(user_input) → result dict.
    #   5. Print "Assistant: " followed by format_response(result).
    #   6. Print a blank line for readability.
    raise NotImplementedError


if __name__ == "__main__":
    run_session()
