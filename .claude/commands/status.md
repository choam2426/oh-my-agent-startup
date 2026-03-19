---
description: Check the current startup progress from Linear and checkpoint state
---

Check the current state of the AI startup:

1. Read `workspace/.startup-state.json` for checkpoint data
2. Query Linear for all project issues and their statuses
3. Summarize:
   - Current phase (genesis / mvp / polish / evolve)
   - Issues: total / done / in-progress / blocked
   - Recent decisions made
   - What's next in the pipeline
