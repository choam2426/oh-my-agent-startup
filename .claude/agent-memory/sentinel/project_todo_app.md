---
name: todo_app_setup
description: Todo app static server setup and known issues from QA run
type: project
---

Vanilla HTML/CSS/JS todo app in workspace/. No build step.

Serve with: `cd workspace && python -m http.server 8080`
URL: http://localhost:8080
ES modules require HTTP (not file://) due to CORS.

Known bug found 2026-03-20: New todos append to bottom of list (oldest-first order). Acceptance criterion MY-26 requires new items at top. store.js uses push() + ascending createdAt sort.

**Why:** store.js getTodos() returns todos in push order (ascending createdAt). renderTodos() iterates in that order.

**How to apply:** When re-testing after Pixel fixes ordering, verify the newest item is at index 0 in the rendered list.
