---
name: pivot-protocol
description: When and how to pivot during product development
---

# Pivot Protocol

## When to Pivot

A pivot is triggered when:
- Sentinel (QA) reports >50% test failure rate on core features
- A core feature is technically infeasible with current stack
- Forge (CTO) identifies a fundamental architecture problem
- The approach is clearly not converging toward the mission

## Pivot Process

1. **Compass escalates to Nova** with full context:
   - What failed and why
   - Current state of the product
   - Options available

2. **Nova decides** from these options:
   - **Scope cut**: remove non-essential features, focus on what works
   - **Feature drop**: replace a broken feature with a simpler alternative
   - **Approach change**: different technical approach to the same goal
   - **Push through**: if the issue is fixable with reasonable effort

3. **Compass restructures** the Linear board:
   - Archive dropped issues
   - Create new issues for the new approach
   - Update priorities
   - Notify relevant agents via Linear comments

4. **Team redirects** and continues from the new plan

## What is NOT a Pivot

- Fixing a minor bug → just fix it
- Refactoring code → normal tech debt work
- Changing a component's appearance → design iteration
- Adding error handling → normal development

A pivot is a **strategic direction change**, not a code fix.
