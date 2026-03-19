---
name: linear-protocol
description: Startup-specific conventions for using Linear — labels, comment format, workflow rules
---

# Linear Communication Rules

Use the `linear-cli` skill from the Linear-Agent-Skills plugin for all Linear operations.
This skill only defines **startup-specific conventions** on top of that.

## Labels — When to Use What

| Label | Use for |
|-------|---------|
| Feature | New functionality being built |
| Bug | Something broken that needs fixing |
| design-spec | UI/UX specifications from Palette |
| architecture | Technical decisions from Forge |
| review | Work that needs review from another agent |
| pivot | Strategic direction change decided by Nova |
| blocked | Cannot proceed without resolution |
| tech-debt | Code quality or refactoring work |

## Comment Format

Always prefix comments with your agent codename:
```
[Compass] Moving this to In Progress. Pixel will handle frontend.
[Sentinel] Found edge case: empty form submission crashes the app.
[Nova] Pivoting: drop real-time charts, use static summary cards instead.
```

## Issue Title Format

```
[Label] Short description
```

Examples:
- `[Feature] User authentication with email/password`
- `[Bug] Dashboard chart overlaps on mobile`
- `[architecture] Choose database: SQLite vs Supabase`

## Priority

- **1 (Urgent)**: Blocks all other work
- **2 (High)**: Core MVP feature
- **3 (Normal)**: Important but not blocking
- **4 (Low)**: Nice to have

## Workflow

Backlog → Todo → In Progress → Done

- Move to **Todo** when planned for current cycle
- Move to **In Progress** when actively working
- Move to **Done** only after verification (QA pass or review complete)
