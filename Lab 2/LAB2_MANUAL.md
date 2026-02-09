# Lab 2: Structured Data and Chain of Thoughts for Reasoning

## 1. Objective

In this lab, we will move from unstructured, terminal-based chat to software-ready JSON and evaluate why reasoning (CoT) can improve logic-heavy extraction tasks.

## 2. Task 1: The API Contract (Structured Output)

Scenario: You are building a member registration pipeline. The model must convert a messy bio into a structured JSON object.

Run:

```bash
python lab2_task1.py
```

What to observe:
- Output is constrained to JSON (`response_mime_type=application/json`).
- You can parse the result with `json.loads(...)` directly.

Engineering concept:
- The model output now behaves like an API contract between model and downstream code.

## 3. Task 2: Why Reasoning Matters (CoT)

Problem: JSON format alone does not guarantee mathematical correctness.

Run baseline + CoT side by side:

```bash
python lab2_task2.py --mode both
```

Run baseline only:

```bash
python lab2_task2.py --mode baseline
```

Run CoT only:

```bash
python lab2_task2.py --mode cot
```

What to observe:
- Baseline may produce valid JSON but weak math accuracy.
- CoT mode includes a `thought` field and may improve `math_result` reliability.

## 4. Deliverables

Complete `STUDENT_WORKSHEET.md` and answer:

1. Format vs Accuracy: Why can Task 1 fail once logic-heavy math is introduced?
2. Thought Field: How does the `thought` key help you debug model behavior?
3. Regex bonus: Extract `math_result` using `re` without `json` library. Why can this be useful for high-speed parsing?
