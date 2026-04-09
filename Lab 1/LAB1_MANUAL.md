# Lab 1: Building Your First Chat Agent

## 1. Objectives

- Set up a local environment for AI development.
- Establish communication with the Google Gemini LLM via Google AI Studio.
- Build your own terminal-based Chat Agent.

## 2. Prerequisites

### 2.1 Software Stack

Ensure the following are installed on your laptop:

1. VS Code: https://code.visualstudio.com/
2. Python: https://www.python.org/

### 2.2 Obtain your API KEY

1. Go to Google AI Studio: https://aistudio.google.com/
2. Sign in with your UCR account.
3. Click `Get API key` on the left sidebar.
4. Click `Create API key in new project`.
5. Security note:
- Keep this key private.
- Add it only when you are ready to run, then delete/rotate it after execution if required by your security policy.
- Never share it or commit it to public repositories (for example, GitHub).
- Local AI assistants/tools can access local files and may reuse keys while assisting. Treat your local environment as sensitive.

## 3. Project Setup

### Step 1: Project Creation

Create a folder named `AI_Agent_Lab` and open it in VS Code.

### Step 2: Install Libraries

Open the VS Code terminal (`Ctrl + ~`) and run:

```bash
pip install -q -U google-genai python-dotenv
```

Recommended for this project:

```bash
bash setup.sh
source .venv/bin/activate
```

### Step 3: Environment Variables

Create a file named `.env` in the project root:

```text
GOOGLE_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

## 4. Project Tasks

### Task 1: Single-Turn Context Generation

Purpose: verify VS Code terminal can call Gemini successfully.

Student template:
- `student_single_turn_template.py`

Use:

```bash
python student_single_turn_template.py
```

Minimum requirements:

- The script executes without `ModuleNotFoundError`.
- You receive a model response in terminal.
- You can change the prompt and get a different response.

Submission evidence:

- 1 screenshot of a successful run.

### Task 2: Build a Terminal Chat Agent

Purpose: implement multi-turn conversation behavior locally.

Student template:
- `student_chat_template.py`

Use:

```bash
python student_chat_template.py
```

Minimum requirements:

- Supports repeated user input and multiple agent responses.
- Terminates when the user enters `exit`, `quit`, or `bye`.
- Demonstrates memory across turns (second prompt references first prompt).

Suggested memory test:

1. `You: My club is Robotics at UCR.`
2. `You: What club did I just mention?`

Submission evidence:

- 1 screenshot showing at least 3 turns.
- 1 screenshot showing clean termination (`exit`/`quit`/`bye`).

### Worksheet
- `STUDENT_WORKSHEET.md`

## 5. Additional, Optional Tasks

### Task A: Setting a System Persona

Modify chat creation config to include `system_instruction`.
The agent should act as a `UCR Student Organization Advisor`:

- Professional and helpful.
- Occasionally uses UCR references like `Bell Tower` or `The Barn`.

Hint:

```python
client = genai.Client(api_key=api_key)
chat = client.chats.create(
    model="gemini-2.5-flash-lite",
    config={"system_instruction": "You are a ..."},
)
```

### Task B: Understanding Rate Limits

Research: https://ai.google.dev/pricing

Answer:

1. How many requests per minute (RPM) are allowed in the Free Tier for Gemini 2.5 Flash?
2. What is the context window size for this model?
3. Why does context window size matter when building an app?

Submission evidence:

- 1 short paragraph (4-8 sentences).
- Include the exact date you checked the pricing page.
