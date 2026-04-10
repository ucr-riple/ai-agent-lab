# FUNCTIONALITY.md

## Purpose
Define what the system should do, i.e., functionalities.

## Example (Reference)
Use this as a template for level of detail.

### Functionality A: Chatbot FAQ Support
- Input:
  - Free-text user question (for example: "When are meetings?")
- Output:
  - Natural-language answer shown to the user
- Success:
  - Returns an answer relevant to the user question
- Failure/Edge Cases:
  - Unknown question -> return fallback like "I don't have that information yet."
  - Empty input -> prompt user to enter a question

### Functionality B: Member Registration
- Input:
  - Free-text or form submission with member fields (for example: name, email, major, year)
- Output:
  - Submission result message (`success`, `exists`, or `incomplete`)
- Success:
  - Required fields are present and record is saved to the database
- Failure/Edge Cases:
  - Missing required field(s) -> return `incomplete` with missing field list
  - Duplicate email -> return `exists`
  - Invalid formats -> return validation error


Your project should define its own functionality set using the same structure.

## Student TODO 1
1. List your project's top 2-4 core functionalities.
2. For each functionality, define:
   - user input
   - expected output
   - success condition
   - failure/edge cases

## Quality Check
- Each functionality is written from user perspective.
- Success is measurable (not vague words like "works well").
- Failure cases are specific enough to become test cases later.
