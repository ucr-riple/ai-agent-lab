#!/usr/bin/env python3
"""Week 1 lab starter: terminal chat agent using google.genai."""

from __future__ import annotations

import os

from google import genai
from dotenv import load_dotenv


def build_chat(client: genai.Client):
    """Create a chat session, optionally with system instruction."""
    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")
    system_instruction = os.getenv("SYSTEM_INSTRUCTION", "").strip()
    config = None

    if system_instruction:
        config = {"system_instruction": system_instruction}

    return client.chats.create(model=model_name, config=config)


def start_agent(chat) -> None:
    print("--- UCR Club AI Assistant Initialized (type 'exit' to stop) ---")

    while True:
        user_msg = input("You: ").strip()
        if user_msg.lower() in {"quit", "exit", "bye"}:
            print("Agent: Goodbye! Good luck with your club activities.")
            break
        if not user_msg:
            continue

        try:
            response = chat.send_message(user_msg)
            print(f"Agent: {response.text}")
        except Exception as err:
            print(f"An error occurred: {err}")


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Missing GOOGLE_API_KEY. Add it to .env first.")
        return 1

    client = genai.Client(api_key=api_key)
    chat = build_chat(client)
    start_agent(chat)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
