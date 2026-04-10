#!/usr/bin/env python3
"""Lab 3 Task 2: Function calling (AI uses a local tool)."""

from __future__ import annotations

import datetime
import os

from dotenv import load_dotenv
from google import genai


# Teaching note:
# This function is a LOCAL tool provided by your Python script.
# The model cannot directly access your computer clock by itself.
# Instead, the model decides when it needs this tool, and your script
# executes the function call and returns the result back to the model.
def get_current_time() -> str:
    """Returns the current date and time of this system."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY in .env")
        return 1

    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")
    client = genai.Client(api_key=api_key)

    question = (
        "Use the get_current_time tool, then answer with the exact current "
        "timestamp in one sentence."
    )
    response = client.models.generate_content(
        model=model_name,
        contents=question,
        config={"tools": [get_current_time]},
    )

    print("=== Function Calling Response ===")
    print(response.text)

    # OPTIONAL TODO 1:
    # Add another tool (e.g., get_current_weekday) and test when the model uses which tool.
    # Example tool list extension:
    # config={"tools": [get_current_time, get_current_weekday]}
    # OPTIONAL TODO 2:
    # Ask for both date and time in one question and verify the response contains both.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
