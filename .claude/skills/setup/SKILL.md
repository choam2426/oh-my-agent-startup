---
name: setup
description: First-time setup — validate Linear API key, check dependencies, generate .env file.
---

# Setup

Run this before your first mission to configure the environment.

## Steps

1. **Ask the user for their Linear API key**
   - Direct them to https://linear.app/settings/api to create one
   - The key should start with `lin_api_`

2. **Validate the API key**
   - Run: `python skills/linear-cli/scripts/linear_cli.py list-teams` with the key set as `LINEAR_API_KEY` env var
   - If it returns teams, the key is valid
   - If it errors, tell the user the key is invalid

3. **Check Python**
   - Run: `python3 --version` (or `python --version` on Windows)
   - Require Python 3.6+
   - If missing, direct user to https://python.org

4. **Check Node.js**
   - Run: `node --version`
   - Require Node.js 18+
   - If missing, direct user to https://nodejs.org

5. **Create .env file**
   - Write `LINEAR_API_KEY=<user's key>` to `.env` at project root
   - Do NOT overwrite if `.env` already exists — ask first

6. **Show available Linear teams**
   - List teams from the API response
   - Tell the user which team will be used

7. **Report results**
   ```
   Setup complete:
   - Linear API key: valid (Team: <team name>)
   - Python: <version>
   - Node.js: <version>
   - .env: created

   Ready! Run: claude --agent compass -p "your mission here"
   ```

## If something fails
- Missing Python: "Install Python 3.6+ from https://python.org"
- Missing Node.js: "Install Node.js 18+ from https://nodejs.org"
- Invalid API key: "Check your key at https://linear.app/settings/api"
