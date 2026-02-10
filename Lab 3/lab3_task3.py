#!/usr/bin/env python3
"""Lab 3 Task 3: Eyes + Hands coordination for a club decision."""

from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

POLICY_FILE = Path("club_policy_kb.txt")


# Teaching note:
# This is a LOCAL tool in your script. The model cannot read this data source directly.
def check_account_status(name: str) -> str:
    """Returns account status from a simulated student system."""
    registry = {
        "Alice": "Active",
        "Bob": "On Hold",
        "Charlie": "Active",
    }
    return registry.get(name, "Unknown")


def load_policy_context() -> str:
    return POLICY_FILE.read_text(encoding="utf-8")


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY in .env")
        return 1

    client = genai.Client(api_key=api_key)
    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")

    # For demo purposes
    # Bob is a CS major (policy-eligible) but account is On Hold (operationally blocked).
    policy_context = load_policy_context()
    student = {"name": "Bob", "major": "CS"}

    # [EYES-only] Policy evaluation from RAG context.
    eyes_prompt = (
        "Use ONLY the policy context below.\n"
        f"Policy Context:\n{policy_context}\n\n"
        f"Student Profile: {student}\n"
        "Return strict JSON with keys: "
        "name, major, policy_eligible (bool), policy_reason"
    )
    eyes_response = client.models.generate_content(
        model=model_name,
        contents=eyes_prompt,
        config={"response_mime_type": "application/json"},
    )
    eyes_data = json.loads(eyes_response.text)

    # [HANDS-only] Local system lookup.
    status = check_account_status(student["name"])

    # [EYES+HANDS] Final coordinated decision.
    combined_prompt = (
        "You are a Club Assistant. Make a final enrollment decision using BOTH signals.\n"
        f"Policy decision JSON: {json.dumps(eyes_data)}\n"
        f"Account status tool result for {student['name']}: {status}\n"
        "Output 2-3 sentences and include final verdict: ALLOW or DENY."
    )
    final_response = client.models.generate_content(
        model=model_name,
        contents=combined_prompt,
    )

    print("=== [EYES-only] Policy Decision (JSON) ===")
    print(json.dumps(eyes_data, indent=2))
    print("\n=== [HANDS-only] Local Account Status ===")
    print(f"check_account_status('{student['name']}') -> {status}")
    print("\n=== [EYES+HANDS] Coordinated Final Decision ===")
    print(final_response.text)

    # OPTIONAL TODO 1:
    # Change student to Alice and compare final verdict.
    # OPTIONAL TODO 2:
    # Set Bob to "Active" in check_account_status and rerun.
    # OPTIONAL TODO 3:
    # Modify one policy line in club_policy_kb.txt and observe impact.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
