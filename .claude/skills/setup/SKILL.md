---
name: setup
description: First-time setup — validate Linear API key, check dependencies, configure Linear workspace, generate config files.
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

6. **Select Linear team**
   - List teams from the API response
   - If only 1 team → auto-select it
   - If multiple teams → ask the user to choose (show numbered list)
   - Tell the user which team was selected

7. **Initialize Linear workspace structure**
   Using the selected team, run these steps:

   a. **Check existing labels** (`list-issue-labels --team <team-name>`)
      - Create missing type labels: `feature`, `bug`, `design-spec`, `architecture`, `review`, `tech-debt`, `blocked`, `pivot`, `improvement`
      - Create missing area labels: `frontend`, `backend`, `infra`
      - Create missing role labels: `needs-review`, `needs-qa`
      - Use `create-issue-label --name <name> --team-id <UUID>` for each missing label
      - Report: count created vs already existed

   b. **Check existing workflow states** (`list-issue-statuses --name <team-name>`)
      - Verify these exist: Backlog, Todo, In Progress, In Review, Testing, Done, Canceled
      - Create `Waiting` if missing (type: `unstarted`, color: `#f59e0b`)
      - Use `save-issue-status --input '{"name":"Waiting","teamId":"<UUID>","type":"unstarted","color":"#f59e0b"}'` if needed
      - Report: count configured

8. **Save startup config**
   - Write `.claude/startup-config.json`:
   ```json
   {
     "team": { "id": "<UUID>", "name": "<team name>", "key": "<team key>" }
   }
   ```
   - This file is gitignored (user-specific)
   - Compass will read this on future runs to skip team selection

9. **Report results**
   ```
   Setup complete:
   - Linear API key: valid
   - Team: <team name> (selected)
   - Python: <version>
   - Node.js: <version>
   - .env: created
   - Labels: <count> configured (<new> created, <existing> already existed)
   - Workflow states: <count> configured
   - Config: .claude/startup-config.json saved

   Ready! Run: claude --agent compass -p "your mission here"
   ```

## If something fails
- Missing Python: "Install Python 3.6+ from https://python.org"
- Missing Node.js: "Install Node.js 18+ from https://nodejs.org"
- Invalid API key: "Check your key at https://linear.app/settings/api"
