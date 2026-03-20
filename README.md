<div align="center">

**English** | **[한국어](README.ko.md)**

# oh-my-agent-startup

### One mission. Ten agents. Ship it.

An AI agent team that builds web applications from a single mission.<br/>
10 agents debate, design, build, review, test, and deploy — all decisions tracked in Linear.

[![Claude Code](https://img.shields.io/badge/Built_for-Claude_Code-6B4FBB?style=for-the-badge)](https://claude.ai/code)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)](LICENSE)
[![Linear](https://img.shields.io/badge/Linear-Integrated-5E6AD2?style=for-the-badge&logo=linear&logoColor=white)](#communication-flow)

</div>

---

## What is this?

You give it a mission:

```bash
claude --agent compass -p "Build a real-time polling app with shareable links"
```

And a full team starts working:

1. **Nova** (CEO) sets the vision and MVP scope
2. **Forge** (CTO) proposes the architecture — the team votes on it
3. **Palette** designs each feature, **Pixel** and **Circuit** build it
4. **Forge** code-reviews, **Sentinel** runs E2E tests with Playwright
5. If tests fail, the team fixes and re-tests automatically
6. **Nova** reviews each feature: Ship / Iterate / Cut
7. **Shield** audits security, **Scroll** writes docs

Every decision, every review — recorded as Linear issues and comments.

---

## The Team

| | Agent | Role | Personality |
|---|-------|------|-------------|
| :compass: | **Compass** | PM / Orchestrator | Pragmatic scope guardian |
| :star2: | **Nova** | CEO | Visionary, biased toward shipping |
| :hammer_and_wrench: | **Forge** | CTO | Perfectionist architect |
| :art: | **Palette** | UI/UX Designer | User advocate, aesthetic-driven |
| :jigsaw: | **Pixel** | Frontend Engineer | Detail-obsessed implementer |
| :zap: | **Circuit** | Backend Engineer | Systems thinker, performance-focused |
| :shield: | **Sentinel** | QA Engineer | Paranoid edge-case hunter |
| :rocket: | **Pipeline** | DevOps | Automation-first |
| :lock: | **Shield** | Security Engineer | Trusts no input |
| :scroll: | **Scroll** | Tech Writer | Clarity-first documentarian |

Agents debate openly through Linear comments. They disagree, push back, and challenge each other's decisions.

---

## Quick Start

### Prerequisites

- [Claude Code CLI](https://claude.ai/code) installed and authenticated
- [Linear](https://linear.app) account with an API key
- Node.js 18+

### 1. Clone & Configure

```bash
git clone https://github.com/choam2426/oh-my-agent-startup.git
cd oh-my-agent-startup
```

Create a `.env` file with your Linear API key:

```bash
echo "LINEAR_API_KEY=lin_api_xxxxxxxxxxxxx" > .env
```

### 2. Launch

```bash
# Full team — from mission to shipped product
./scripts/launch.sh "Build a fitness tracking dashboard with social challenges"
```

```bash
# Or run directly with Claude Code
claude --agent compass -p "Build a real-time polling app with shareable links"
```

### 3. Watch them work

Open [Linear](https://linear.app) and follow the agents' collaboration in real-time — design specs, code reviews, QA reports, and product verdicts.

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

Add a feature to an existing project. Skips Genesis, reuses existing architecture.

```bash
claude --agent compass -p "sprint: Add dark mode toggle"
```

### Debate

No code. Multi-round agent discussion with structured voting. Nova makes the final call.

```bash
claude --agent compass -p "debate: Should we use tRPC or REST for our API layer?"
```

---

## Key Features

### Vote Round

Major decisions trigger a vote. Agents vote with reasoning — if anyone disagrees, a debate round starts. Max 3 rounds, then Nova decides.

### Linear as Source of Truth

All communication flows through Linear. Design specs, code reviews, QA reports, product verdicts, and phase summaries — every decision is traceable and auditable.

### Verify-Fix Loop

Sentinel gates quality. If E2E tests fail, the team automatically fixes and re-tests (max 3 rounds). Persistent failure triggers an architectural review or Pivot Protocol.

### Session Recovery

Every step updates `workspace/.startup-state.json` with the current issue, step, and agent state. Interrupted sessions resume exactly where they left off.

### Phase Summaries

After each phase, Compass posts a structured summary to Linear — decisions made, votes cast, bugs found and fixed, features shipped. Full observability without reading every comment.

### Recursive Improvement

When an agent delivers subpar work, Compass writes corrections to `.claude/agent-memory/<agent>/`. The agent reads this on next spawn and improves.

### Pivot Protocol

When tests fail at scale or a core feature is infeasible, Compass escalates to Nova. Nova decides: scope cut, feature drop, alternative approach, or push through.

---

## Project Structure

```
oh-my-agent-startup/
├── CLAUDE.md                         # Startup protocol & team culture
├── scripts/
│   └── launch.sh                     # One-command launcher
│
├── .claude/
│   ├── settings.json                 # Permissions & plugin config
│   │
│   ├── agents/                       # 10 agent definitions
│   │   ├── compass.md                #   PM / Orchestrator
│   │   ├── nova.md                   #   CEO
│   │   ├── forge.md                  #   CTO
│   │   ├── palette.md                #   Designer
│   │   ├── pixel.md                  #   Frontend
│   │   ├── circuit.md                #   Backend
│   │   ├── sentinel.md               #   QA
│   │   ├── pipeline.md               #   DevOps
│   │   ├── shield.md                 #   Security
│   │   └── scroll.md                 #   Tech Writer
│   │
│   ├── skills/                       # Built-in capabilities
│   │   ├── linear-cli/               #   Linear API operations
│   │   ├── linear-protocol/          #   Communication conventions
│   │   ├── coding-conventions/       #   Code standards
│   │   └── pivot-protocol/           #   Pivot decision framework
│   │
│   └── agent-memory/                 # Recursive improvement storage
│
└── workspace/                        # Generated project output
    ├── CLAUDE.md                     #   Stack conventions (written by Forge)
    ├── .startup-state.json           #   Session recovery checkpoint
    └── .linear-config.json           #   Linear project & ID mappings
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

Every agent reads all previous comments before acting. Full context, every time.

---

## Configuration

### Environment Variables

```bash
# .env
LINEAR_API_KEY=lin_api_xxxxxxxxxxxxx
```

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

Modify any agent's personality, tools, or model tier to fit your needs.

---

## License

[Apache License 2.0](LICENSE)

---

<div align="center">

**Give it a mission. Watch it ship.**

</div>
