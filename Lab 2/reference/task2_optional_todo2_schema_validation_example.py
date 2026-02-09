#!/usr/bin/env python3
"""Reference answer: Task 2 OPTIONAL TODO 2 (schema/type validation)."""

from __future__ import annotations


def validate_schema(parsed: dict) -> list[str]:
    """Return a list of validation errors; empty list means valid."""
    errors: list[str] = []

    required = {
        "thought": str,
        "name": str,
        "math_result": int,
    }

    for key, expected_type in required.items():
        if key not in parsed:
            errors.append(f"Missing required key: {key}")
            continue
        if not isinstance(parsed[key], expected_type):
            errors.append(
                f"Wrong type for '{key}': expected {expected_type.__name__}, "
                f"got {type(parsed[key]).__name__}"
            )

    return errors


def demo() -> None:
    # Example object that might come from json.loads(response_text)
    parsed = {"thought": "Used pattern.", "name": "Alex", "math_result": 43}

    problems = validate_schema(parsed)
    if problems:
        print("Schema validation failed:")
        for issue in problems:
            print(f"- {issue}")
    else:
        print("Schema validation passed.")


if __name__ == "__main__":
    demo()
