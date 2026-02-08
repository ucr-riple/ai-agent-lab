#!/usr/bin/env python3
"""Task 2 starter: multi-turn terminal chat with Gemini using google.genai.

Required for Lab 1:
- Run this file successfully and demonstrate chat + termination.

Optional for Lab 1:
- Edit lines marked OPTIONAL TODO for customization.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from google import genai


def main() -> int:
    # Starter code: load .env and read GOOGLE_API_KEY
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GOOGLE_API_KEY in .env")
        return 1

    # Starter code: create a Gemini client
    client = genai.Client(api_key=api_key)

    # OPTIONAL TODO 1:
    # Try another flash model.
    model_name = "gemini-2.5-flash-lite"

    # Starter code: start a chat session with memory
    chat = client.chats.create(model=model_name)

    print("--- Student Chat Agent Started ---")
    print("Type exit, quit, or bye to stop.\n")

    while True:
        user_msg = input("You: ").strip()

        # Starter code: termination condition
        # OPTIONAL TODO 2:
        # Try another termination conditions.
        if user_msg.lower() in {"exit", "quit", "bye"}:
            print("Agent: Goodbye!")
            break

        if not user_msg:
            continue

        try:
            # Starter code: send message using chat memory
            response = chat.send_message(user_msg)
            print(f"Agent: {response.text}")
        except Exception as err:
            print(f"An error occurred: {err}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
