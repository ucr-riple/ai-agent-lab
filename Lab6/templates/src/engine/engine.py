"""Lab 6 starter for engine layer implementation.

The engine is the Logic Layer of the system.

Architecture position:
    interface -> engine -> storage

This module receives raw user input, uses the Tool Use pattern to determine
what storage operation to perform, then uses the Reflection pattern to
validate its own interpretation before acting.

Replace every TODO with your implementation guided by the tests.
"""

from __future__ import annotations

import json
import os

from dotenv import load_dotenv

# Import storage functions at the top so tests can patch them via
# "src.engine.engine.save_member" (the path where they are USED).
from src.storage.storage_handler import save_member
from src.storage.storage_handler_extended import delete_member, get_members

load_dotenv()

_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
_MODEL = os.getenv("MODEL_NAME", "gemini-2.5-flash")

# --- Prompts ---

_EXTRACTION_PROMPT = """
You are a Club Registration Engine. Analyze the user request and extract:
- intent: exactly one of "register", "list", "delete", "unknown"
- data: a dict containing any fields mentioned (name, email, student_id, major)

Return strict JSON only — no extra text:
{"intent": "<intent>", "data": {}}
""".strip()

_REFLECTION_PROMPT = """
You are a data completeness validator.

Extracted data and intent:
{extracted}

Validation rules:
- "register" intent requires all four fields: name, email, student_id, major.
- "list", "delete", and "unknown" intents have no required fields.

Return strict JSON only — no extra text:
{{"complete": <true|false>, "missing": ["<field>", ...]}}
""".strip()


def process_request(user_input: str) -> dict:
    """Process a user request using Tool Use and Reflection patterns.

    Return contract (every path returns a dict with "status" and "message"):
    - {"status": "success",    "message": str, "data": list | None}
    - {"status": "exists",     "message": str, "data": None}
    - {"status": "incomplete", "message": str, "missing": list}
    - {"status": "unknown",    "message": str, "data": None}
    - {"status": "error",      "message": str, "data": None}
    """
    try:
        # TODO: Import google.genai and google.genai.types.HttpOptions.
        #       Initialize the client at module level or inside this function:
        #           from google import genai
        #           from google.genai.types import HttpOptions
        #           client = genai.Client(http_options=HttpOptions(api_version="v1"))

        # ----------------------------------------------------------------
        # Step 1 — Tool Use: extract intent and data from user_input
        # ----------------------------------------------------------------
        # TODO: Call the model with _EXTRACTION_PROMPT as system_instruction,
        #       user_input as contents, and response_mime_type="application/json".
        # TODO: Parse the JSON response into a dict (extraction).
        # TODO: Pull out extraction["intent"] and extraction["data"].

        # ----------------------------------------------------------------
        # Step 2 — Reflection: validate completeness before acting
        # ----------------------------------------------------------------
        # TODO: Format _REFLECTION_PROMPT with the extracted JSON string.
        # TODO: Call the model again with the reflection prompt.
        # TODO: Parse the JSON response into a dict (reflection).
        # TODO: If reflection["complete"] is False:
        #       return {
        #           "status": "incomplete",
        #           "message": "Missing required fields.",
        #           "missing": reflection["missing"],
        #       }

        # ----------------------------------------------------------------
        # Step 3 — Dispatch: call the correct storage function
        # ----------------------------------------------------------------
        # TODO: if intent == "register":
        #           result = save_member(data)
        #           if result == "success":
        #               return {"status": "success", "message": "Member registered.", "data": None}
        #           elif result == "exists":
        #               return {"status": "exists", "message": "Member already registered.", "data": None}
        #           else:
        #               return {"status": "error", "message": "Storage error.", "data": None}

        # TODO: elif intent == "list":
        #           members = get_members()
        #           return {"status": "success", "message": f"{len(members)} member(s) found.", "data": members}

        # TODO: elif intent == "delete":
        #           result = delete_member(data.get("email", ""))
        #           if result == "success":
        #               return {"status": "success", "message": "Member deleted.", "data": None}
        #           elif result == "not_found":
        #               return {"status": "not_found", "message": "Member not found.", "data": None}
        #           else:
        #               return {"status": "error", "message": "Storage error.", "data": None}

        # TODO: else:  # unknown intent
        #           return {"status": "unknown", "message": "I can register, list, or delete members.", "data": None}

        raise NotImplementedError

    except NotImplementedError:
        raise
    except Exception as exc:
        return {"status": "error", "message": str(exc), "data": None}
