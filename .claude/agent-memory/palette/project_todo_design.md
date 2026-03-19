---
name: todo_app_design_spec
description: Design spec for MY-25 todo list app — Vanilla HTML/CSS/JS, no frameworks, CSS custom properties for theming
type: project
---

Created design spec for MY-25 covering: color palette (CSS custom properties), typography (system font stack), layout (single-column centered), component specs (form, todo items, empty state, filters), responsive behavior, and accessibility.

**Why:** Tech stack is Vanilla HTML/CSS/JS with no CSS frameworks — all design must use CSS custom properties and semantic class names, not utility classes.

**How to apply:** Any future design work for this project must avoid Tailwind/Bootstrap conventions. Use CSS custom property tokens defined in :root. Semantic class names only (e.g., .todo-item, not .flex.gap-4).
