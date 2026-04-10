#!/usr/bin/env python3
"""Lab 3 Task 1: Why we need RAG (knowledge cutoff demo)."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

KNOWLEDGE_FILE = Path("knowledge_base.txt")


def load_context() -> str:
    if not KNOWLEDGE_FILE.exists():
        raise FileNotFoundError(
            f"Missing {KNOWLEDGE_FILE}. Create it to simulate local RAG context."
        )
    return KNOWLEDGE_FILE.read_text(encoding="utf-8")


def main() -> int:
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Missing GEMINI_API_KEY in .env")
        return 1

    model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash-lite")
    client = genai.Client(api_key=api_key)

    # Part A (baseline):
    # Ask without any external context. This simulates a normal LLM request
    # where the model must rely only on its pre-trained knowledge.
    failure_query = (
        "When is the UCR 2026 Space-Pizza Gala and what is the dress code? "
        "Answer in one sentence."
    )
    initial = client.models.generate_content(model=model_name, contents=failure_query)

    # Part B (manual RAG):
    # Retrieve context from a local file and place it into the prompt.
    # This gives the model fresh, task-specific knowledge at runtime.
    context = load_context()
    rag_query = "When is the Space-Pizza Gala and what should I wear?"
    rag_prompt = f"Context file: {KNOWLEDGE_FILE}\n\n{context}\n\nQuestion: {rag_query}"
    rag = client.models.generate_content(model=model_name, contents=rag_prompt)

    print("=== Initial Response (No RAG Context) ===")
    print(initial.text)
    print("\n=== RAG Response (With Context from knowledge_base.txt) ===")
    print(rag.text)

    # OPTIONAL TODO 1:
    # Edit knowledge_base.txt with a different fake event and verify answers change.
    # OPTIONAL TODO 2:
    # Add conflicting lines in knowledge_base.txt and observe which detail the model chooses.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
