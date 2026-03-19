---
name: linear-protocol
description: How to use Linear in the AI startup — includes actual IDs, CLI commands, and workflow rules
---

# Linear Protocol — AI Startup Communication

All team communication flows through Linear using the `Linear-Agent-Skills` plugin CLI.

## CLI Usage

```bash
# The CLI script path (from project root):
CLI="C:/Users/choam/.claude/plugins/cache/Linear-Agent-Skills/Linear-Agent-Skills/2.0.0/skills/linear-cli/scripts/linear_cli.py"

# IMPORTANT: Always run from project root (A:/oh-my-agent-startup/) so .env is loaded
# The .env file contains LINEAR_API_KEY

# Load env and run:
export $(grep -v '^#' .env | xargs) && python "$CLI" <command> [flags]
```

## Team

| Field | Value |
|-------|-------|
| Name | My-agent-workspace |
| Key | MY |
| ID | `65aa8e95-f699-4393-a853-3ef949cc6a2e` |

## Workflow States

| State | Type | ID |
|-------|------|-----|
| Backlog | backlog | `e5d23a54-7937-4bb3-9efc-cf56a37e058c` |
| Todo | unstarted | `281b0243-c11e-4b51-b7d9-3c04f5348424` |
| In Progress | started | `e96f21fa-d9e4-462b-9bc7-026a14ff5336` |
| Done | completed | `e77572d2-9fcd-42db-a640-f967f4e7750c` |
| Canceled | canceled | `d8cc5115-35d6-43e2-b182-07b96ee214b6` |

**Flow**: Backlog → Todo → In Progress → Done

## Labels

| Label | ID |
|-------|----|
| Feature | `07920b99-d053-4117-957b-035dead57684` |
| Bug | `765a0eb7-8bcd-44be-a323-8a7782eed1c2` |
| Improvement | `60cd2b81-3345-4595-b8a5-2164374467c9` |
| design-spec | `a53439ff-d6cc-4e93-82d7-00cfa10da438` |
| architecture | `dab68384-4fd6-4ab2-bd04-44e902ea475d` |
| review | `420e5cf7-d7bd-4aa5-8b74-7b4bab1d59c1` |
| pivot | `d9e11ed4-9a24-47d5-bc25-a00626733761` |
| blocked | `3dbafa3c-140d-4e4e-9ddc-0af3403002fd` |
| tech-debt | `ddc6bbb4-5ac0-4f2b-8dcb-1d8f9a437d68` |

## Common Commands

### Create an issue
```bash
python "$CLI" create-issue \
  --title "[Feature] User authentication" \
  --team-id "65aa8e95-f699-4393-a853-3ef949cc6a2e" \
  --description "## Context\nUsers need to sign in.\n\n## Acceptance Criteria\n- Login form works\n- Session persists" \
  --priority 2 \
  --label-ids "07920b99-d053-4117-957b-035dead57684" \
  --state-id "281b0243-c11e-4b51-b7d9-3c04f5348424"
```

### Update issue status
```bash
# Move to In Progress
python "$CLI" update-issue --id "MY-5" --input '{"stateId":"e96f21fa-d9e4-462b-9bc7-026a14ff5336"}'

# Move to Done
python "$CLI" update-issue --id "MY-5" --input '{"stateId":"e77572d2-9fcd-42db-a640-f967f4e7750c"}'
```

### Add a comment
```bash
python "$CLI" save-comment --input '{"issueId":"<issue-uuid>","body":"[Compass] Design spec approved. Moving to implementation."}'
```

### List issues
```bash
# All issues in team
python "$CLI" list-issues --team "My-agent-workspace"

# Filter by state
python "$CLI" list-issues --team "My-agent-workspace" --state "In Progress"

# Filter by label
python "$CLI" list-issues --team "My-agent-workspace" --label "Feature"
```

### Create a project
```bash
python "$CLI" save-project --input '{"name":"Fitness Tracker MVP","teamIds":["65aa8e95-f699-4393-a853-3ef949cc6a2e"]}'
```

## Communication Rules

1. **Every task** = Linear issue with title, description, acceptance criteria
2. **Every discussion** = Linear comment on the relevant issue
3. **Prefix comments** with agent codename: `[Compass]`, `[Nova]`, `[Forge]`, etc.
4. **Priority**: 1=Urgent, 2=High, 3=Normal, 4=Low
5. **Always update status** when starting or finishing work on an issue
