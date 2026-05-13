## Phase 1: Google Sheets Live Setup

### Step 1: Create a Google Cloud Project (or reuse existing)

1. Go to https://console.cloud.google.com/.
2. Click the project selector → **New Project** → name it `ucr-club-assistant`.
3. Click **Create**.

### Step 2: Enable Required APIs

1. In the Cloud Console, go to **APIs & Services → Library**.
2. Search for and enable **Google Sheets API**.
3. Search for and enable **Google Drive API**.

### Step 3: Create a Service Account

1. Go to **APIs & Services → Credentials**.
2. Click **Create Credentials → Service Account**.
3. Name: `storage-agent` → click **Create and Continue** → **Done**.
4. Click the new service account → **Keys → Add Key → Create new key → JSON**.
5. Download the file and rename it `service_account.json`.
6. Move it into your project root (`ucr-club-assistant/`).

Security note:
- Add `service_account.json` to your `.gitignore` immediately.
- Never commit this file to version control.
- The `"client_email"` field inside the file is the identity you will share with your sheet.

### Step 4: Create Your Google Sheet

1. Go to https://sheets.google.com/ and create a new spreadsheet.
2. Name it exactly: `ucr-club-assistant-members`.
3. In Row 1, add the column headers that match `CONTRACT.md`:

```
name    email    student_id    major
```

### Step 5: Share the Sheet with Your Service Account

1. Open the spreadsheet → click **Share**.
2. Paste the `"client_email"` value from `service_account.json` into the email field.
3. Set permission to **Editor** and click **Send**.

---

## 4. Phase 2: Verify Live Connectivity

Copy and run the verification script from your `ucr-club-assistant/` root:

```bash
cp ../Lab6/templates/verify_connection.py .
python verify_connection.py
```

Expected output:
```
Connected to: ucr-club-assistant-members
Header row: ['name', 'email', 'student_id', 'major']
Row count (data only): 0
Connection OK.
```

If you see an error, check:
- `service_account.json` is in the project root.
- The spreadsheet was shared with the service account email (Editor permission).
- Both APIs are enabled in your Cloud project.