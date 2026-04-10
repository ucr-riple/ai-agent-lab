#!/usr/bin/env python3
"""Lab 2 Task 1: Structured JSON output."""

from __future__ import annotations

import json
import os

from dotenv import load_dotenv
from google import genai


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY in .env")
        return 1

    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")
    client = genai.Client(api_key=api_key)

    prompt = (
        "Extract the student's name, major, and year from this bio:\n"
        "'Hey! I'm Sarah, a 3rd-year Biology student. I love hiking and want to join the club.'\n"
        "Return JSON in this format: {\"name\": str, \"major\": str, \"year\": int}"
    )
    # OPTIONAL TODO 1:
    # Replace the bio text above with some created messy bio and compare output quality.
    # Example: include nickname, emoji, mixed casing, or extra unrelated details.

    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config={"response_mime_type": "application/json"},
    )
    # OPTIONAL TODO 2:
    # Expand the schema in the prompt (e.g., add "hobby" or "graduation_year")
    # and verify parsed output still matches your new contract.

    print("Raw model output:")
    print(response.text)

    try:
        parsed = json.loads(response.text)
    except json.JSONDecodeError as err:
        print(f"\nJSON parse failed: {err}")
        return 2

    print("\nParsed object:")
    print(parsed)
    # OPTIONAL TODO 3:
    # Save parsed JSON to file:
    # with open("task1_output.json", "w", encoding="utf-8") as f:
    #     json.dump(parsed, f, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
