"""Lab 6 Optional Extension: Hand-Rolled Multi-Turn Tool Calling.

Shows how LLM-decided tool calling works by implementing it from scratch
instead of using the SDK's built-in tools=[...] parameter.

The SDK feature (tools=[...]) does exactly what this file does — just
automatically and invisibly. Here every step is explicit Python:

  _describe_tools   Inspect function signatures and docstrings → build the
                    tool description text that goes into the Turn 1 prompt.
  Turn 1            Prompt the model with available tools. It outputs a JSON
                    tool-call decision: {"tool": "<name>", "args": {...}}.
  _dispatch         Look the chosen function up in a name → fn table.
                    Use inspect.signature to call it correctly (no args,
                    single dict arg, or keyword args).
  Turn 2            Send the tool result back in a plain prompt.
                    Model reads it and writes a final natural-language answer.

Compare to engine.py:

  engine.py (primary)            this file
  ───────────────────────        ─────────────────────────────────────────────
  Structured JSON extraction     JSON tool-call decision via prompt
  Explicit Reflection call       No validation step (model's judgment)
  Hardcoded dispatch if/elif     _dispatch() driven by inspect + name table
  Tool list baked in             Tool list passed in by the caller
  Returns typed dict             Returns natural-language string

Run the demo:
    python -m src.engine.engine_native_tools
"""

from __future__ import annotations

import inspect
import json
import os
from collections.abc import Callable

from dotenv import load_dotenv
from google import genai

from src.storage.storage_handler import save_member
from src.storage.storage_handler_extended import delete_member, get_members

load_dotenv()

_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
_MODEL = os.getenv("MODEL_NAME", "gemini-2.5-flash")

# {tool_descriptions} is filled dynamically by _describe_tools().
# {user_input} is filled at call time.
_TURN1_TEMPLATE = """
You are a Club Registration Engine. You have these tools available:

{tool_descriptions}

Read the user request and decide which tool to call.
Respond with ONLY a JSON object — no extra text:
  {{"tool": "<tool_name>", "args": {{<key>: <value>, ...}}}}

If no tool is appropriate, respond with:
  {{"tool": null, "args": {{}}}}

User request: {user_input}
""".strip()

_TURN2_TEMPLATE = """
The user asked: {user_input}

You decided to call `{tool_name}` and it returned: {tool_result}

Write a short, friendly natural-language response to the user
summarizing what happened. Do not repeat raw data structures.
""".strip()


# ---------------------------------------------------------------------------
# Dynamic tool description — replaces the hardcoded list in the prompt
# ---------------------------------------------------------------------------

def _describe_tools(fns: list[Callable]) -> str:
    """Build the tool-list section of the Turn 1 prompt from function objects.

    For each function, inspect.signature extracts the parameter names and
    annotations; the first line of __doc__ provides a plain-English summary.

    Example output:
      save_member(member_data: dict)  — Save member into storage.
      get_members()                   — Return all member rows as a list of dicts.
      delete_member(email: str)       — Delete the first row whose email matches.
    """
    lines = []
    for fn in fns:
        sig = inspect.signature(fn)
        params_str = ", ".join(
            f"{name}: {p.annotation.__name__}"
            if p.annotation is not inspect.Parameter.empty
            else name
            for name, p in sig.parameters.items()
        )
        first_doc_line = (fn.__doc__ or "no description").strip().splitlines()[0]
        lines.append(f"  {fn.__name__}({params_str})  — {first_doc_line}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Dynamic dispatch — replaces hardcoded if/elif
# ---------------------------------------------------------------------------

def _dispatch(table: dict[str, Callable], name: str, args: dict):
    """Call the function named `name` from `table` with the model's args.

    Calling convention is inferred from inspect.signature:
      - No parameters          → fn()
      - One dict-annotated param → fn(args)        e.g. save_member(member_data)
      - One or more other params → fn(**args)       e.g. delete_member(email=...)
    """
    fn = table.get(name)
    if fn is None:
        return f"unknown_tool:{name}"

    params = list(inspect.signature(fn).parameters.values())

    if not params:
        return fn()

    first = params[0]
    if len(params) == 1 and first.annotation is dict:
        return fn(args)          # pass the whole args dict as one argument

    return fn(**args)            # unpack args as keyword arguments


# ---------------------------------------------------------------------------
# Main function
# ---------------------------------------------------------------------------

def process_request_native(user_input: str, tools: list[Callable]) -> str:
    """Two-turn LLM-decided tool calling loop.

    Args:
        user_input: Raw natural-language request from the caller.
        tools:      List of Python callables the model may choose from.
                    _describe_tools() reads their signatures and docstrings
                    to build the prompt section; _dispatch() uses their
                    signatures to call them correctly.

    Returns the model's final natural-language answer as a plain string.
    """
    client = genai.Client(api_key=_API_KEY)
    tool_table = {fn.__name__: fn for fn in tools}

    # ── Turn 1: describe tools via prompt, ask model to pick one ─────────────
    turn1_prompt = _TURN1_TEMPLATE.format(
        tool_descriptions=_describe_tools(tools),
        user_input=user_input,
    )

    turn1 = client.models.generate_content(
        model=_MODEL,
        contents=turn1_prompt,
        config={"response_mime_type": "application/json"},
    )

    decision = json.loads(turn1.text)
    tool_name = decision.get("tool")
    tool_args = decision.get("args", {})

    print(f"  [Turn 1]  model chose → {tool_name}({tool_args})")

    if not tool_name:
        # Model decided no tool is needed — ask it to answer directly.
        fallback = client.models.generate_content(
            model=_MODEL,
            contents=user_input,
        )
        return fallback.text

    # ── Execute: call the chosen function via our dispatch table ──────────────
    tool_result = _dispatch(tool_table, tool_name, tool_args)

    print(f"  [Execute] tool returned → {tool_result!r}")

    # ── Turn 2: send result back, get the model's synthesized answer ──────────
    turn2_prompt = _TURN2_TEMPLATE.format(
        user_input=user_input,
        tool_name=tool_name,
        tool_result=tool_result,
    )

    turn2 = client.models.generate_content(
        model=_MODEL,
        contents=turn2_prompt,
    )

    print(f"  [Turn 2]  model synthesized final answer")
    return turn2.text


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

_TOOLS = [save_member, get_members, delete_member]

if __name__ == "__main__":
    demo_inputs = [
        "Show me all registered members.",
        "Register Demo User, demo_native@ucr.edu, student_id 9999, CS major.",
        "Register incomplete.",             # missing fields — watch model behavior
        "What is the capital of France?",  # off-topic — tool should be null
    ]

    for prompt in demo_inputs:
        print(f"\nInput : {prompt}")
        output = process_request_native(prompt, tools=_TOOLS)
        print(f"Output: {output}")

    # OPTIONAL TODO 1:
    # Add a delete call for demo_native@ucr.edu after the registration above.
    # The model must extract the email from plain English — watch tool_args.

    # OPTIONAL TODO 2:
    # Run "Register incomplete." through both process_request (engine.py) and
    # process_request_native (this file) and compare outputs:
    #   engine.py  → {"status": "incomplete", "missing": [...]}  (typed, consistent)
    #   this file  → model's judgment (may vary between runs)
    # Which is safer in production?

    # OPTIONAL TODO 3:
    # Add a new tool — for example a lookup function:
    #
    #   def find_member(email: str) -> dict:
    #       """Find a single member by email. Returns {} if not found."""
    #       members = get_members()
    #       return next((m for m in members if m.get("email") == email), {})
    #
    # Pass it in: process_request_native(prompt, tools=_TOOLS + [find_member])
    # _describe_tools will pick it up automatically — no other changes needed.
    # This shows why the dynamic approach is better than hardcoded if/elif.
