# Windows Setup

## Step 1

If you are using Windows, we suggest creating the virtual environment manually:

```bash
python3 -m venv .venv
```

## Step 2

Open `.venv` and check whether it contains `Scripts` or `bin`. After that, use the matching commands for your terminal.

### Senario 1: `.venv/Scripts` exists

If you are using Git Bash:
```bash
.venv/Scripts/python.exe -m pip install -U pip
.venv/Scripts/python.exe -m pip install -U -r requirements.txt
cp .env.example .env
source .venv/Scripts/activate
```

If you are using PowerShell:
```powershell
.venv\Scripts\python.exe -m pip install -U pip
.venv\Scripts\python.exe -m pip install -U -r requirements.txt
Copy-Item .env.example .env
.\.venv\Scripts\Activate.ps1
```

### Scenario 2: `.venv/bin` exists

If you are using Git Bash:
```bash
.venv/bin/python.exe -m pip install -U pip
.venv/bin/python.exe -m pip install -U -r requirements.txt
cp .env.example .env
source .venv/bin/activate
```

If you are using PowerShell:
```powershell
.venv\bin\python.exe -m pip install -U pip
.venv\bin\python.exe -m pip install -U -r requirements.txt
Copy-Item .env.example .env
.\.venv\bin\Activate.ps1
```

## Step 3

Now you can set your API key.

If you are using Git Bash:
```bash
export GOOGLE_API_KEY=<YOUR_ACTUAL_API_KEY_HERE>
```

If you are using PowerShell:
```powershell
$env:GOOGLE_API_KEY="<YOUR_ACTUAL_API_KEY_HERE>"
```
