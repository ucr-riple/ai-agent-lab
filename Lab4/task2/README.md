# Task 2: Architecture Worksheet Assignment

## Objective
In this task, we will specifically practice three-layer modularized design:
- `interface`
- `engine`
- `storage`

You will define functionality first, then map responsibilities and interfaces across these three layers.

## Timeline
- Duration: 1 week
- Submission file: `task2/WORKSHEET.md`
- This is a living document: you may revise it in later lab stages when project needs change, and submit the final version at the end of all labs.

## Learn Here (Before Filling Worksheet)
1. Functionality definition:
   - Read `task2/FUNCTIONALITY.md`
2. Interface contracts:
   - Read `task2/CONTRACT.md`

## TODO 1: Define Functionality
Use `task2/FUNCTIONALITY.md` as reference, then fill Part A in `task2/WORKSHEET.md`.

What to complete:
- 2-4 core functionalities
- For each: input, output, success, failure/edge cases

## TODO 2: Define Interfaces and Component Boundaries
Fill Part B and Part C in `task2/WORKSHEET.md`.

Quick check for TODO 2 quality:
- Each responsibility has one clear owner.
- Contracts define both success and failure statuses.
- No UI behavior is placed in `storage`.
- No persistence logic is placed in `interface`.

## Deliverable Checklist
- [ ] `task2/WORKSHEET.md` completed
- [ ] A text file to show that the student can explain why boundaries reduce coupling and improve maintainability

## Notes
- Keep this task design-focused with no implementation required.
- You can update this worksheet later when architecture decisions evolve.
