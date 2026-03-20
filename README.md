<div align="center">

**English** | **[한국어](README.ko.md)**

# oh-my-agent-startup

### One mission. Ten agents. Ship it.

An autonomous AI startup team that builds web applications from a single sentence.<br/>
Compass orchestrates 10 specialized agents — they debate, design, code, review, test, and deploy.<br/>
All communication flows through Linear. All decisions are traceable. No humans required.

[![Claude Code](https://img.shields.io/badge/Built_for-Claude_Code-6B4FBB?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyeiIvPjwvc3ZnPg==)](https://claude.ai/code)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)](LICENSE)
[![Agents](https://img.shields.io/badge/Agents-10-ff6b6b?style=for-the-badge)](#the-team)
[![Skills](https://img.shields.io/badge/Skills-4_built--in-4ecdc4?style=for-the-badge)](#project-structure)
[![Linear](https://img.shields.io/badge/Linear-Integrated-5E6AD2?style=for-the-badge&logo=linear&logoColor=white)](#communication)

</div>

---

## What is this?

You give it a mission:

```bash
./scripts/launch.sh "Build a real-time collaborative polling app with shareable links"
```

And a full startup team wakes up:

- **Nova** (CEO) sets the vision and MVP scope
- **Forge** (CTO) architects the stack and writes conventions
- **The team votes** on the architecture — real debate, not rubber stamps
- **Palette** designs every feature, **Pixel** and **Circuit** build it
- **Forge** code-reviews everything, **Sentinel** runs E2E tests
- **Nova** reviews each feature: Ship / Iterate / Cut
- **Pipeline** deploys, **Shield** audits security, **Scroll** writes docs

Every decision, every debate, every review — recorded as Linear issues and comments. Fully traceable. Fully autonomous.

---

## The Team

```
 "We are a flat, passionate startup. 'That's not my job' doesn't exist here."
```

| | Codename | Role | Personality | Catchphrase |
|---|----------|------|-------------|-------------|
| :compass: | **Compass** | PM / Orchestrator | Pragmatist, scope guardian | *"That's not in the MVP. Backlog it."* |
| :star2: | **Nova** | CEO | Visionary, ships fast | *"Ship it. We'll iterate."* |
| :hammer_and_wrench: | **Forge** | CTO | Perfectionist architect | *"This won't scale past 10K users."* |
| :art: | **Palette** | UI/UX Designer | Empathetic, aesthetic | *"The user won't find that button."* |
| :jigsaw: | **Pixel** | Frontend Engineer | Detail-obsessed craftsman | *"That padding is 3px off."* |
| :zap: | **Circuit** | Backend Engineer | Systems thinker, perf-obsessed | *"O(n^2)? In this economy?"* |
| :shield: | **Sentinel** | QA Engineer | Paranoid, edge-case hunter | *"What if the user pastes 10MB of text?"* |
| :rocket: | **Pipeline** | DevOps | Automation addict | *"If it's not in CI, it doesn't exist."* |
| :lock: | **Shield** | Security Engineer | Trusts no input | *"Sanitize. Everything."* |
| :scroll: | **Scroll** | Tech Writer | Documentation obsessive | *"Undocumented code is technical debt."* |

Every agent has a **distinct personality**, debates openly, and communicates exclusively through Linear comments. They disagree. They push back. They challenge each other. That's the point.

---

## Quick Start

### Prerequisites

- [Claude Code CLI](https://claude.ai/code) installed and authenticated
- [Linear](https://linear.app) account with an API key in `.env`
- Node.js 18+

### 1. Clone & Configure

```bash
git clone https://github.com/choam2426/oh-my-agent-startup.git
cd oh-my-agent-startup
cp .env.example .env
# Add your LINEAR_API_KEY to .env
```

### 2. Launch

```bash
# Full startup — from mission to deployed product
./scripts/launch.sh "Build a fitness tracking dashboard with social challenges"
```

```bash
# Or run directly with Claude Code
claude --agent compass -p "Build a real-time polling app with shareable links"
```

### 3. Watch them work

Open [Linear](https://linear.app) and watch 10 agents collaborate in real-time. Every design spec, code review, QA report, and CEO verdict — all in one place.

---

## How It Works

```
                         ┌──────────────┐
                         │   Mission    │
                         │  (one line)  │
                         └──────┬───────┘
                                │
                    ┌───────────▼───────────┐
                    │   Phase 1: Genesis     │
                    │                        │
                    │  Nova → Vision & Scope │
                    │  Forge → Architecture  │
                    │  Team → Vote Round     │
                    │  Compass → Backlog     │
                    └───────────┬────────────┘
                                │
              ┌─────────────────▼─────────────────┐
              │       Phase 2: MVP Build           │
              │                                    │
              │  For each feature:                 │
              │  ┌──────────────────────────────┐  │
              │  │ Palette → Design Spec        │  │
              │  │ Forge → Tech Guide           │  │
              │  │ Pixel/Circuit → Implement     │  │
              │  │ Forge → Code Review          │  │
              │  │ Sentinel → E2E Testing       │  │
              │  │ ┌─── Fail? ──→ Fix Loop ───┐ │  │
              │  │ └─── Pass ──→ Nova Review   │ │  │
              │  │              Ship / Iterate  │ │  │
              │  └──────────────────────────────┘  │
              └─────────────────┬──────────────────┘
                                │
                    ┌───────────▼───────────┐
                    │   Phase 3: Polish      │
                    │                        │
                    │  Pipeline → Deploy     │
                    │  Shield → Security     │
                    │  Scroll → Docs         │
                    └───────────┬────────────┘
                                │
                    ┌───────────▼────────────────┐
                    │  Phase 4: Scoped Evolution  │
                    │                             │
                    │  Bug fixes, perf, UX, a11y  │
                    │  Within mission scope ONLY  │
                    └─────────────────────────────┘
```

---

## Execution Modes

### Full Team (default)

All 4 phases. New product from a single mission.

```bash
./scripts/launch.sh "Build a Kanban board with real-time collaboration"
```

### Sprint

Add a feature to an existing project. Skips Genesis — goes straight to design → build → test → ship.

```bash
claude --agent compass -p "sprint: Add dark mode toggle"
```

### Debate

No code. Pure multi-round agent discussion. Agents take real positions, debate with evidence, and Nova makes the final call.

```bash
claude --agent compass -p "debate: Should we use tRPC or REST for our API layer?"
```

---

## Key Features

### Agents Debate, Not Just Execute

Every major decision triggers a **Vote Round**. Agents vote with reasoning. Disagree? Debate rounds kick in — max 3, then Nova breaks the tie. No rubber stamps.

### Linear as the Single Source of Truth

All communication flows through Linear issues and comments. Not just task tracking — design specs, code reviews, QA reports, CEO verdicts. Every decision is traceable.

### Verify-Fix Loop

Sentinel doesn't just test — Sentinel **gates**. If QA fails, the loop fires: fix → re-test → repeat (max 3). If it still fails, Forge does an architectural review. Still broken? Pivot Protocol.

### Recursive Skill Improvement

When an agent delivers subpar work, Compass writes corrections to `.claude/agent-memory/<agent>/`. Next time that agent spawns, it reads its memory and incorporates feedback. The team gets better over time.

### Session Recovery

Every step updates `workspace/.startup-state.json`. Crashed mid-feature? Restart and Compass picks up exactly where it left off — right agent, right step, right issue.

### Pivot Protocol

When >50% of tests fail or a core feature is infeasible, Compass escalates to Nova. Nova assesses: scope cut, feature drop, alternative approach, or push through. The team redirects. No dead ends.

---

## Project Structure

```
oh-my-agent-startup/
├── CLAUDE.md                         # Startup protocol & team culture
├── package.json                      # Project metadata
├── scripts/
│   └── launch.sh                     # One-command launcher
│
├── .claude/
│   ├── settings.json                 # Permissions & plugin config
│   │
│   ├── agents/                       # 10 agent definitions
│   │   ├── compass.md                #   PM / Orchestrator (Opus)
│   │   ├── nova.md                   #   CEO (Opus)
│   │   ├── forge.md                  #   CTO (Opus)
│   │   ├── palette.md                #   UI/UX Designer
│   │   ├── pixel.md                  #   Frontend Engineer
│   │   ├── circuit.md                #   Backend Engineer
│   │   ├── sentinel.md               #   QA Engineer
│   │   ├── pipeline.md               #   DevOps
│   │   ├── shield.md                 #   Security Engineer
│   │   └── scroll.md                 #   Tech Writer
│   │
│   ├── skills/                       # Reusable capabilities
│   │   ├── linear-cli/               #   Linear API operations
│   │   ├── linear-protocol/          #   Communication conventions
│   │   ├── coding-conventions/       #   Code standards
│   │   └── pivot-protocol/           #   Pivot decision framework
│   │
│   └── agent-memory/                 # Recursive improvement storage
│       ├── palette/                  #   Designer feedback & learnings
│       └── sentinel/                 #   QA feedback & learnings
│
└── workspace/                        # Generated project lives here
    ├── CLAUDE.md                     #   Stack conventions (Forge writes this)
    ├── .startup-state.json           #   Checkpoint for session recovery
    ├── .linear-config.json           #   Linear project & ID mappings
    └── src/                          #   Application source code
```

---

## Communication Flow

```
Compass (PM)
  │
  ├── creates Linear issue with acceptance criteria
  │
  ├── spawns Palette ──→ reads issue ──→ posts design spec as comment
  ├── spawns Forge ────→ reads spec ───→ posts tech guide as comment
  ├── spawns Pixel ────→ reads all ────→ implements ──→ posts completion
  ├── spawns Forge ────→ reads code ───→ posts review verdict
  ├── spawns Sentinel ─→ runs E2E ────→ posts QA report
  │   └── FAIL? ──→ fix loop ──→ re-test ──→ max 3 rounds
  ├── spawns Nova ─────→ reads all ────→ Ship / Iterate / Cut
  │
  └── updates status: Backlog → Todo → In Progress → In Review → Testing → Done
```

Every agent reads ALL previous comments before acting. No information silos. Full context, every time.

---

## Companion Plugins

### [Linear-Agent-Skills](./Linear-Agent-Skills)

Agent-optimized Linear CLI — 30+ commands, no OAuth dance required. Create issues, post comments, manage labels, track projects. The communication backbone.

### [mcp-optimizer](./mcp-optimizer)

MCP management toolkit — health checks, usage auditing, performance benchmarking, and automatic optimization. Keep your MCP servers lean.

### [pm-skills](https://github.com/anthropics/skills) (external)

65+ PM skills integrated via plugin — PRD writing, sprint planning, market sizing, competitive analysis, and more. Compass uses these for product management workflows. Not built-in; installed separately.

---

## Configuration

### Environment Variables

```bash
# .env
LINEAR_API_KEY=lin_api_xxxxxxxxxxxxx
```

### Claude Code Settings

Settings live in `.claude/settings.json`. Key configs:

- **Permissions**: All tools pre-allowed for autonomous operation
- **Plugins**: Linear-Agent-Skills + 8 PM skill plugins enabled
- **Agent Teams**: Experimental flag enabled for multi-agent orchestration

### Agent Customization

Each agent is a markdown file in `.claude/agents/` with YAML frontmatter:

```yaml
---
name: forge
model: opus
tools: Read, Grep, Glob, Bash, Write, Edit
skills:
  - linear-cli
  - coding-conventions
memory: project
---
```

Modify any agent's personality, tools, or model tier to fit your workflow.

---

## Culture

This isn't a pipeline. It's a team.

1. **Psychological safety + productive debate** — Challenge any decision. Disagree openly, then commit.
2. **No silos** — Engineers comment on design. Designers challenge architecture. QA questions product decisions.
3. **Principles over process** — If a step doesn't make sense, skip it and explain why.
4. **Speed AND craft** — Ship fast, but never ship garbage.
5. **User obsession** — Every decision traces back to user value.

---

## License

[Apache License 2.0](LICENSE)

---

<div align="center">

*Built by agents, for agents.*

**Give it a mission. Watch it ship.**

</div>
