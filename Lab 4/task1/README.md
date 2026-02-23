# Task 1: Agent Smoke Test

## Objective
Verify each student's coding agent works end-to-end before project architecture work begins.

## A. Test Setup
1. Open the folder where you will run the Bubble Sort smoke test.
2. Open your coding agent.

## B. Agent Test Prompt (Bubble Sort + Tests)
Paste this prompt into your agent:

```text
Create a Python implementation of Bubble Sort and complete pytest test coverage.

Requirements:
1. Create `bubble_sort.py` with function:
   - `def bubble_sort(values: list[int]) -> list[int]`
2. Behavior:
   - Returns a NEW sorted list in ascending order.
   - Does not mutate the input list.
   - Works with empty lists, one element, duplicates, negative numbers, and already sorted input.
3. Create `test_bubble_sort.py` with clear pytest unit tests covering:
   - empty list
   - single element
   - already sorted list
   - reverse-sorted list
   - duplicates
   - negative values
   - input immutability check
4. Keep code modular and readable.
5. Print the exact commands to run the tests.
```

## C. Pass Criteria
- Agent generates both implementation and test files.
- Tests run locally and all pass.
- Student can explain what each test verifies.

## Deliverable
- Screenshot or terminal log showing passing tests.
