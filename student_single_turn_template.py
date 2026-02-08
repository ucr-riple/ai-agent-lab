#!/usr/bin/env python3
"""Task 1 starter: single-turn Gemini generation using google.genai.

Required for Lab 1:
- Run this file successfully and capture output.

Optional for Lab 1:
- Edit the lines marked OPTIONAL TODO to customize behavior.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from google import genai


def main() -> int:
    # Starter code: load environment variables from .env
    load_dotenv()

    # Starter code: read API key from environment
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Missing GOOGLE_API_KEY in .env")
        return 1

    # Starter code: create a Gemini client
    client = genai.Client(api_key=api_key)

    # OPTIONAL TODO 1:
    # Try a different model name.
    model_name = "gemini-2.5-flash-lite"

    # OPTIONAL TODO 2:
    # Change the prompt and compare outputs.
    user_prompt = "Who are you? Answer in one sentence."
    response = client.models.generate_content(
        model=model_name,
        contents=user_prompt,
    )

    print("Model response:")
    print(response.text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
