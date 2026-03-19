---
name: linear-protocol
description: How to communicate through Linear in the AI startup team
---

# Linear Communication Protocol

All team communication flows through Linear using the Linear-Agent-Skills plugin.

## Issue Creation

Use the linear-cli skill to create issues:
- Title format: `[label] Short description`
- Always include acceptance criteria
- Assign a priority: P0 (must-have), P1 (should-have), P2 (nice-to-have)
- Add appropriate labels: `feature`, `bug`, `design-spec`, `architecture`, `review`, `pivot`, `blocked`, `tech-debt`

## Status Updates

Move issues through the workflow:
- **Backlog**: identified but not yet planned
- **Todo**: planned for current cycle
- **In Progress**: actively being worked on
- **In Review**: completed, awaiting review
- **Done**: reviewed and accepted

## Comments

- Prefix with your agent codename: `[Compass]`, `[Nova]`, `[Forge]`, etc.
- Be specific and actionable
- Reference other issues when relevant
- Include code snippets or specs when applicable

## Labels

| Label | Use for |
|-------|---------|
| `feature` | New functionality |
| `bug` | Something broken |
| `design-spec` | UI/UX specifications |
| `architecture` | Technical decisions |
| `review` | Needs review from another agent |
| `pivot` | Strategic direction change |
| `blocked` | Cannot proceed, needs resolution |
| `tech-debt` | Code quality improvements |
