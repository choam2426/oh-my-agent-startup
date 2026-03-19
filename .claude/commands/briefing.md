---
description: Generate a Morning Briefing — structured summary of what the AI startup accomplished
---

Spawn Nova (CEO) to generate a Morning Briefing.

Nova should:
1. Read `workspace/.startup-state.json` for current state
2. Query Linear for all issues and their history
3. Generate a structured briefing with:
   - Mission recap
   - Features completed (with Linear references)
   - Incomplete items and reasons
   - Key decisions made (with confidence scores)
   - Items needing human judgment
   - Recommended next steps
