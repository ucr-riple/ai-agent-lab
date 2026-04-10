# Student Worksheet: Lab 2

## Before running

1. `bash setup.sh`
2. `source .venv/bin/activate`
3. Add `GEMINI_API_KEY` in `.env`

## Task 1: Structured Output

Run:
```bash
python lab2_task1.py
```

Checklist:
- JSON string is returned.
- `json.loads(...)` parsing succeeds.
- You can identify `name`, `major`, and `year` in parsed output.

## Task 2: Reasoning Comparison

Run:
```bash
python lab2_task2.py --mode both
```

Checklist:
- You capture baseline JSON output.
- You capture CoT JSON output.
- You compare `math_result` quality across modes.

## Submit

- Screenshots for Task 1 and Task 2 runs.
- Completed answers below.

## Discussion Answers

### 1) Format vs Accuracy

Question: Why can Task 1 fail (or become unreliable) when math/logic is introduced?

Your answer:


### 2) The "thought" Field

Question: How does including a `"thought"` key help debugging and reliability?

Your answer:


### 3) Regex Bonus

Question: Use Python `re` to extract `math_result` from JSON string without using `json`.
Why might this be useful for high-speed parsing?

Your answer:

Code snippet:

```python
# Example placeholder
# import re
# text = '{"thought":"...","name":"Alex","math_result":43}'
# m = re.search(r'"math_result"\s*:\s*(\d+)', text)
# print(int(m.group(1)) if m else None)
```
