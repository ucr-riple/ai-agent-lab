#!/usr/bin/env python3
"""Lab 2 Task 2: Why reasoning (CoT) improves structured extraction."""

from __future__ import annotations

import argparse
import json
import os

from dotenv import load_dotenv
from google import genai

CHALLENGE_PROMPT = "I'm Alex. 3^12345 mod 100 is the key."
# OPTIONAL TODO 1:
# Try alternative logic-heavy prompts and compare baseline vs CoT.
# Example: "I'm Alex. 7^222 mod 40 is the key."

SYSTEM_PROMPT = """
You are a Club Registrar.
1. Use the 'thought' field to solve math or logic step-by-step.
2. Use pattern recognition for modular arithmetic when needed.
3. Output strictly in this JSON format:
{"thought": "...", "name": "...", "math_result": int}
""".strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare baseline JSON extraction vs CoT-enabled extraction."
    )
    parser.add_argument(
        "--mode",
        choices=["baseline", "cot", "both"],
        default="both",
        help="Which run mode to execute (default: both).",
    )
    return parser.parse_args()


def run_once(client: genai.Client, model_name: str, use_cot: bool) -> str:
    config = {"response_mime_type": "application/json"}
    if use_cot:
        config["system_instruction"] = SYSTEM_PROMPT

    response = client.models.generate_content(
        model=model_name,
        contents=CHALLENGE_PROMPT,
        config=config,
    )
    return response.text


def print_result(label: str, text: str) -> None:
    print(f"\n=== {label} ===")
    print(text)
    try:
        parsed = json.loads(text)
        print(f"math_result -> {parsed.get('math_result')}")
    except json.JSONDecodeError:
        print("Could not parse JSON response.")
    # OPTIONAL TODO 2:
    # Add a simple schema check after json parsing.
    # Verify required keys exist and have expected types:
    # - "thought": str
    # - "name": str
    # - "math_result": int
    # If validation fails, print a clear warning for debugging.


def main() -> int:
    load_dotenv()
    args = parse_args()

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY in .env")
        return 1

    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")
    client = genai.Client(api_key=api_key)

    if args.mode in {"baseline", "both"}:
        baseline = run_once(client, model_name, use_cot=False)
        print_result("Baseline (No CoT)", baseline)

    if args.mode in {"cot", "both"}:
        cot = run_once(client, model_name, use_cot=True)
        print_result("CoT (With 'thought' field)", cot)
    # OPTIONAL TODO 3:
    # Run each mode multiple times (e.g., 5 trials) and count how often math_result is correct.

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
