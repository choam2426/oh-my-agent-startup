import subprocess, json, sys

body = r"""[Palette] Design Spec: Todo List Web App

## Design Spec: Todo List Web App

### User Flow

1. User opens the app — sees the page title, an input form, and either a populated list or an empty state message
2. User types a task into the text input and presses Enter or clicks the Add button
3. New task appears at the top of the list, input clears, focus returns to the input
4. User clicks the checkbox on a task to mark it complete — item gets strikethrough styling, checkbox fills indigo
5. User clicks the delete button (×) on a task — item is removed immediately
6. User filters tasks via three tabs: All / Active / Completed
7. Footer shows a live count of remaining active tasks
8. When the last task is deleted, the list area shows a context-aware empty state message

---

### Layout

Single-column centered layout. Max width 600px, centered horizontally. The app sits inside a card-style container with subtle elevation. Page background is a neutral off-white.

Top-to-bottom structure:
- Page header: app title (h1)
- Add-task form: text input + submit button, full width of card
- Filter tabs: All / Active / Completed
- Todo list: scrollable ul, natural height
- Footer bar: remaining task count (left) + clear completed button (right)
- Empty state: centered message inside the list area

**Mobile** (< 480px): card fills full viewport width, no border-radius, reduced side padding (16px).
**Desktop** (>= 480px): card is centered, border-radius 12px, side padding 24px, drop shadow.

---

### CSS Custom Properties (Design Tokens)

All tokens live on `:root` in `styles.css`. Pixel must reference these variables everywhere — no raw hex or px values in component rules.

```css
:root {
  /* Colors */
  --color-bg: #f5f5f0;
  --color-surface: #ffffff;
  --color-border: #e0e0dc;
  --color-border-focus: #6366f1;
  --color-text-primary: #1a1a1a;
  --color-text-secondary: #737373;
  --color-text-placeholder: #a3a3a3;
  --color-accent: #6366f1;
  --color-accent-hover: #4f46e5;
  --color-accent-light: #eef2ff;
  --color-danger: #ef4444;
  --color-danger-hover: #dc2626;
  --color-completed-text: #a3a3a3;
  --color-completed-line: #d4d4d4;

  /* Typography */
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-base: 16px;
  --font-size-lg: 18px;
  --font-size-xl: 24px;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;

  /* Radii */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-card: 0 2px 16px rgba(0, 0, 0, 0.08), 0 1px 4px rgba(0, 0, 0, 0.04);
  --shadow-input-focus: 0 0 0 3px rgba(99, 102, 241, 0.18);

  /* Transitions */
  --transition-fast: 120ms ease;
  --transition-normal: 200ms ease;
}
```

---

### Typography

| Use | Size | Weight | Color |
|-----|------|--------|-------|
| App title (h1) | `--font-size-xl` | bold | `--color-text-primary` |
| Filter tab labels | `--font-size-sm` | medium | `--color-text-secondary` / accent when active |
| Todo item text | `--font-size-base` | normal | `--color-text-primary` |
| Completed todo | `--font-size-base` | normal | `--color-completed-text`, line-through |
| Footer / meta text | `--font-size-sm` | normal | `--color-text-secondary` |
| Empty state | `--font-size-sm` | normal | `--color-text-secondary`, italic |

---

### Component Specs

#### Page Shell

```css
.page-wrapper {
  background: var(--color-bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: var(--space-8) var(--space-4);
}

.app-card {
  background: var(--color-surface);
  width: 100%;
  max-width: 600px;
  border-radius: var(--radius-lg);   /* 0 on mobile */
  box-shadow: var(--shadow-card);    /* none on mobile */
  overflow: hidden;
}
```

#### Add Task Form

- Input height: 44px (touch target minimum)
- Border: `1.5px solid var(--color-border)`
- Focus: border-color switches to `--color-border-focus`, adds `--shadow-input-focus`
- Error state: `.is-error` class → border turns `--color-danger`, input shakes (keyframe below)
- Submit button: 44px height, indigo background, white text, hover darkens to `--color-accent-hover`

```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25%       { transform: translateX(-4px); }
  75%       { transform: translateX(4px); }
}
```

Error handling: add `.is-error` to `.todo-input` on empty submission, auto-remove after 600ms via `setTimeout`. Return focus to input.

#### Filter Tabs

Three equal-width buttons inside `.filter-bar`. Separated from form and list by 1px borders top and bottom.

- Default: muted text, transparent background
- Hover: `--color-accent-light` background, primary text color
- Active (`.is-active`): `--color-accent` text, `--color-accent-light` background
- `aria-pressed="true"` on the active button, `"false"` on others — toggle in JS on click

#### Todo List

- `<ul>` with `list-style: none`
- Each `<li>` is a flex row: `[checkbox] [text] [delete button]`
- `gap: var(--space-3)` between flex children
- Bottom border on each item except last
- Hover background: `#fafafa`

#### Checkbox

Use a real `<input type="checkbox">` styled with `appearance: none`. Do not use a div or span.

- Default: 20×20px, 2px border, `--radius-sm`
- Checked: `--color-accent` fill + border, white checkmark via `::after` pseudo-element (rotated border trick)
- Focus: `outline: 3px solid var(--color-border-focus)`, `outline-offset: 2px`

#### Delete Button

- 32×32px, transparent background, no border
- Inner content: `&#215;` (×) as a text node — no SVG, no img
- Hidden by default (`opacity: 0`), revealed on `.todo-item:hover` and on `:focus-visible`
- Hover: text turns `--color-danger`, light red background (`#fee2e2`)
- `aria-label="Delete task"` required

#### Empty State

`<p class="empty-state">` rendered inside the `<ul>` when the list is empty.
- Centered with flexbox, `padding: var(--space-8) var(--space-6)`
- Italic, `--color-text-secondary`

Context-aware copy:
- All filter, no tasks: "No tasks yet. Add one above."
- Active filter, none active: "No active tasks. You're all done!"
- Completed filter, none completed: "No completed tasks yet."

#### Footer

- Flex row, space-between
- Task count uses `aria-live="polite"` — screen readers announce changes
- "Clear completed" button: hidden (`display: none`) when no completed tasks exist, shown otherwise
- Copy: "N task left" (N=1) / "N tasks left" (N≠1)

---

### Responsive Behavior

Mobile-first. One breakpoint at 480px.

```css
/* Mobile base */
.app-card { border-radius: 0; box-shadow: none; min-height: 100vh; }
.app-header, .add-form, .todo-item, .todo-footer { padding-left: var(--space-4); padding-right: var(--space-4); }

/* Desktop */
@media (min-width: 480px) {
  .app-card { border-radius: var(--radius-lg); box-shadow: var(--shadow-card); min-height: auto; }
  .app-header, .add-form, .todo-item, .todo-footer { padding-left: var(--space-6); padding-right: var(--space-6); }
}
```

---

### States Summary

| State | Treatment |
|-------|-----------|
| Loading | N/A — localStorage is synchronous, renders on DOMContentLoaded |
| Empty list | `.empty-state` paragraph, context-aware copy, shown in list area |
| Empty input error | `.is-error` on input → red border + shake animation, removed after 600ms |
| Completed item | `.is-completed` on `<li>` → strikethrough text, muted color, filled checkbox |
| Active filter tab | `.is-active` + `aria-pressed="true"` on active tab button |
| Clear completed | Button hidden until at least one completed task exists |

---

### Accessibility Requirements

- Semantic HTML: `<main>`, `<h1>`, `<form>`, `<ul>`, `<li>`, `<button>`, `<label>`
- Every `<input>` has an associated `<label>` — visually hidden with `.sr-only` is acceptable
- `.sr-only` utility: `position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0`
- Delete button: `aria-label="Delete task"` — icon-only buttons must have a label
- Filter buttons: `aria-pressed` toggled in JS
- Checkbox: native `<input type="checkbox">` — do not intercept keyboard events
- Task count span: `aria-live="polite"` — announces updates to screen readers
- Focus order: title → input → add button → filter tabs → todo items (checkbox → delete) → footer buttons
- Never suppress `:focus-visible` without a custom visible replacement
- Contrast ratios: primary text (#1a1a1a on white) = 18.1:1 AAA. Secondary text (#737373 on white) = 4.6:1 AA. Accent (#6366f1) only used for interactive elements, not body text.

---

### HTML Structure Reference

```html
<body>
  <div class="page-wrapper">
    <div class="app-card">
      <header class="app-header">
        <h1 class="app-title">My Tasks</h1>
      </header>

      <form class="add-form" id="add-form">
        <label for="todo-input" class="sr-only">New task</label>
        <input
          class="todo-input"
          id="todo-input"
          type="text"
          placeholder="What needs to be done?"
          autocomplete="off"
          maxlength="500"
        />
        <button class="add-button" type="submit">Add</button>
      </form>

      <div class="filter-bar" role="group" aria-label="Filter tasks">
        <button class="filter-btn is-active" data-filter="all" aria-pressed="true">All</button>
        <button class="filter-btn" data-filter="active" aria-pressed="false">Active</button>
        <button class="filter-btn" data-filter="completed" aria-pressed="false">Completed</button>
      </div>

      <ul class="todo-list" id="todo-list" aria-label="Task list">
        <!-- .todo-item li elements injected by render.js -->
        <!-- or .empty-state p when list is empty -->
      </ul>

      <footer class="todo-footer">
        <span class="task-count" id="task-count" aria-live="polite">0 tasks left</span>
        <button class="clear-completed-btn" id="clear-completed">Clear completed</button>
      </footer>
    </div>
  </div>
</body>
```

Each todo item (rendered by `render.js`):
```html
<li class="todo-item [is-completed]" data-id="{{id}}">
  <input
    class="todo-checkbox"
    type="checkbox"
    aria-label="Mark complete: {{text}}"
    [checked]
  />
  <span class="todo-text">{{text}}</span>
  <button class="delete-btn" aria-label="Delete task">&#215;</button>
</li>
```"""

payload = {"issueId": "71461ae1-1f57-488c-b4cf-8a14266d1f7d", "body": body}
result = subprocess.run(
    ["python", r"A:\oh-my-agent-startup\.claude\skills\linear-cli\scripts\linear_cli.py",
     "save-comment", "--input", json.dumps(payload)],
    capture_output=True, text=True
)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("RC:", result.returncode)
