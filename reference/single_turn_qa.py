#!/usr/bin/env python3
"""Week 1 comparison script: single-turn Q/A using google.genai."""

from __future__ import annotations

import argparse
import os

from google import genai
from dotenv import load_dotenv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Single-turn Q/A with Gemini (no persistent chat memory)."
    )
    parser.add_argument(
        "question",
        nargs="+",
        help='Question to ask Gemini, e.g. python single_turn_qa.py "What is an API key?"',
    )
    return parser.parse_args()


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GOOGLE_API_KEY. Add it to .env first.")
        return 1

    args = parse_args()
    question = " ".join(args.question).strip()
    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")
    system_instruction = os.getenv("SYSTEM_INSTRUCTION", "").strip()
    config = None

    if system_instruction:
        config = {"system_instruction": system_instruction}

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=model_name,
            contents=question,
            config=config,
        )
        print(response.text)
    except Exception as err:
        print(f"An error occurred: {err}")
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
