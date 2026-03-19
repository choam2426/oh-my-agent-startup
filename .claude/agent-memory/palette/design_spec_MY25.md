[Palette] Design Spec: Todo List Web App

## Design Spec: Todo List Web App

### User Flow

1. User opens the app — sees the page title, an input form, and either a populated list or an empty state message
2. User types a task into the text input and presses Enter or clicks the Add button
3. New task appears at the top of the list, input clears, focus returns to the input
4. User clicks the checkbox on a task to mark it complete — item receives strikethrough styling, checkbox fills
5. User clicks the delete button on a task — item is removed with no confirmation (destructive but low-stakes)
6. User can filter tasks via three tabs: All / Active / Completed
7. Footer shows a live count of remaining active tasks
8. When the last task is deleted, the list area shows the empty state message

### Layout

Single-column centered layout. Max width 600px. Centered horizontally with auto margins. The app lives within a card-style container with subtle elevation. Page background is a neutral off-white.

Structure top to bottom:
- Page header: app title (h1)
- Add-task form: text input + submit button, full width of card
- Filter tabs: All / Active / Completed, three equal segments
- Todo list: scrollable ul, no max-height on desktop, natural height
- Footer bar: remaining tasks count (left) + clear completed button (right, only shown when completed tasks exist)
- Empty state: centered message inside the list area when list is empty

Mobile (< 480px): card has no border-radius, fills full viewport width, side padding reduced to 16px.
Desktop (>= 480px): card is centered, border-radius 12px, side padding 24px, drop shadow.

### CSS Custom Properties (Design Tokens)

Define all tokens on :root in styles.css. Pixel should wire every color and spacing reference to these variables — no raw hex or pixel values in component rules.

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
  --color-accent: #6366f1;          /* indigo — primary action color */
  --color-accent-hover: #4f46e5;
  --color-accent-light: #eef2ff;    /* checkbox fill, active filter bg */
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
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;

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

### Typography

- App title (h1): `--font-size-xl`, `--font-weight-bold`, `--color-text-primary`, letter-spacing -0.02em
- Section labels / filter tabs: `--font-size-sm`, `--font-weight-medium`
- Todo item text: `--font-size-base`, `--font-weight-normal`
- Completed todo text: same size, `--color-completed-text`, text-decoration line-through, decoration color `--color-completed-line`
- Footer count text: `--font-size-sm`, `--color-text-secondary`
- Empty state text: `--font-size-sm`, `--color-text-secondary`, centered, italic

### Components

#### Page Shell

```
.page-wrapper
  background: var(--color-bg)
  min-height: 100vh
  display: flex, flex-direction: column, align-items: center
  padding: var(--space-8) var(--space-4)

.app-card
  background: var(--color-surface)
  width: 100%, max-width: 600px
  border-radius: var(--radius-lg)   [desktop only; 0 on mobile]
  box-shadow: var(--shadow-card)
  overflow: hidden
```

#### Header

```
.app-header
  padding: var(--space-6) var(--space-6) var(--space-4)

.app-title   (h1)
  font-size: var(--font-size-xl)
  font-weight: var(--font-weight-bold)
  color: var(--color-text-primary)
  margin: 0
```

#### Add Task Form

```
.add-form
  display: flex, gap: var(--space-2)
  padding: 0 var(--space-6) var(--space-4)

.todo-input   (input[type=text])
  flex: 1
  height: 44px
  padding: 0 var(--space-4)
  font-size: var(--font-size-base)
  font-family: var(--font-family)
  color: var(--color-text-primary)
  background: var(--color-surface)
  border: 1.5px solid var(--color-border)
  border-radius: var(--radius-md)
  outline: none
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast)

.todo-input::placeholder
  color: var(--color-text-placeholder)

.todo-input:focus
  border-color: var(--color-border-focus)
  box-shadow: var(--shadow-input-focus)

.todo-input.is-error
  border-color: var(--color-danger)
  animation: shake 200ms ease   [see keyframes below]

.add-button   (button[type=submit])
  height: 44px
  padding: 0 var(--space-4)
  min-width: 44px
  background: var(--color-accent)
  color: #fff
  font-size: var(--font-size-base)
  font-weight: var(--font-weight-medium)
  border: none
  border-radius: var(--radius-md)
  cursor: pointer
  transition: background var(--transition-fast)

.add-button:hover
  background: var(--color-accent-hover)

.add-button:focus-visible
  outline: 3px solid var(--color-border-focus)
  outline-offset: 2px

Button label: "Add" — no icon, keep it explicit for accessibility
```

#### Error shake keyframe

```css
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25%       { transform: translateX(-4px); }
  75%       { transform: translateX(4px); }
}
```

When user submits an empty or whitespace-only input: add `.is-error` class to `.todo-input`, remove after 600ms. No separate error message element needed — the shake + red border communicates the rejection clearly.

#### Filter Tabs

```
.filter-bar
  display: flex
  border-top: 1px solid var(--color-border)
  border-bottom: 1px solid var(--color-border)

.filter-btn   (button)
  flex: 1
  height: 40px
  font-size: var(--font-size-sm)
  font-weight: var(--font-weight-medium)
  color: var(--color-text-secondary)
  background: transparent
  border: none
  cursor: pointer
  transition: color var(--transition-fast), background var(--transition-fast)

.filter-btn:hover
  color: var(--color-text-primary)
  background: var(--color-accent-light)

.filter-btn.is-active
  color: var(--color-accent)
  background: var(--color-accent-light)

.filter-btn:focus-visible
  outline: 3px solid var(--color-border-focus)
  outline-offset: -3px   [inset so it doesn't break the tab bar border]
```

Three buttons: "All", "Active", "Completed". Active state uses aria-pressed="true" in addition to the CSS class.

#### Todo List

```
.todo-list   (ul)
  list-style: none
  margin: 0
  padding: 0
  min-height: 48px   [so empty state has breathing room]

.todo-item   (li)
  display: flex, align-items: center, gap: var(--space-3)
  padding: var(--space-4) var(--space-6)
  border-bottom: 1px solid var(--color-border)
  transition: background var(--transition-fast)

.todo-item:last-child
  border-bottom: none

.todo-item:hover
  background: #fafafa
```

#### Checkbox (complete toggle)

Use a visually styled custom checkbox built from a real `<input type="checkbox">` for accessibility. Do not use a div — the input must be keyboard-operable natively.

```
.todo-checkbox   (input[type=checkbox])
  appearance: none
  width: 20px, height: 20px, flex-shrink: 0
  border: 2px solid var(--color-border)
  border-radius: var(--radius-sm)
  cursor: pointer
  position: relative
  transition: border-color var(--transition-fast), background var(--transition-fast)

.todo-checkbox:checked
  background: var(--color-accent)
  border-color: var(--color-accent)

.todo-checkbox:checked::after
  content: ''
  position: absolute
  left: 4px, top: 1px
  width: 8px, height: 12px
  border: 2px solid #fff
  border-top: none, border-left: none
  transform: rotate(45deg)

.todo-checkbox:focus-visible
  outline: 3px solid var(--color-border-focus)
  outline-offset: 2px
```

#### Todo Item Text

```
.todo-text   (span)
  flex: 1
  font-size: var(--font-size-base)
  color: var(--color-text-primary)
  line-height: var(--line-height-normal)
  word-break: break-word

.todo-item.is-completed .todo-text
  color: var(--color-completed-text)
  text-decoration: line-through
  text-decoration-color: var(--color-completed-line)
```

#### Delete Button

```
.delete-btn   (button)
  width: 32px, height: 32px
  display: flex, align-items: center, justify-content: center
  background: transparent
  border: none
  border-radius: var(--radius-sm)
  color: var(--color-text-secondary)
  cursor: pointer
  opacity: 0
  transition: opacity var(--transition-fast), color var(--transition-fast), background var(--transition-fast)

.todo-item:hover .delete-btn,
.delete-btn:focus-visible
  opacity: 1

.delete-btn:hover
  color: var(--color-danger)
  background: #fee2e2

.delete-btn:focus-visible
  outline: 3px solid var(--color-border-focus)
  outline-offset: 2px
  opacity: 1

Delete button inner content: Unicode multiplication sign × (U+00D7) as text node — no SVG, no img.
aria-label="Delete task" must be present (icon-only button).
```

#### Empty State

```
.empty-state   (p, inside .todo-list when list is empty)
  display: flex, align-items: center, justify-content: center
  padding: var(--space-8) var(--space-6)
  font-size: var(--font-size-sm)
  font-style: italic
  color: var(--color-text-secondary)
  margin: 0
```

Message copy (choose based on active filter):
- All / no tasks ever: "No tasks yet. Add one above."
- Active filter, none active: "No active tasks. You're all done!"
- Completed filter, none completed: "No completed tasks yet."

#### Footer

```
.todo-footer
  display: flex, align-items: center, justify-content: space-between
  padding: var(--space-3) var(--space-6)
  border-top: 1px solid var(--color-border)
  min-height: 44px

.task-count   (span)
  font-size: var(--font-size-sm)
  color: var(--color-text-secondary)

.clear-completed-btn   (button)
  font-size: var(--font-size-sm)
  color: var(--color-text-secondary)
  background: transparent
  border: none
  cursor: pointer
  padding: var(--space-1) var(--space-2)
  border-radius: var(--radius-sm)
  transition: color var(--transition-fast)
  display: none   [hidden when no completed tasks exist]

.clear-completed-btn:hover
  color: var(--color-danger)

.clear-completed-btn:focus-visible
  outline: 3px solid var(--color-border-focus)
  outline-offset: 2px
```

Footer count copy: "N task left" (singular) / "N tasks left" (plural). Zero tasks: "0 tasks left".

### Responsive Behavior

Mobile-first. Base styles target mobile (< 480px). Single media query for desktop.

```css
/* Mobile base (default) */
.app-card {
  border-radius: 0;
  box-shadow: none;
  min-height: 100vh;
}
.app-header,
.add-form,
.todo-item,
.todo-footer {
  padding-left: var(--space-4);
  padding-right: var(--space-4);
}

/* Desktop */
@media (min-width: 480px) {
  .app-card {
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-card);
    min-height: auto;
  }
  .app-header,
  .add-form,
  .todo-item,
  .todo-footer {
    padding-left: var(--space-6);
    padding-right: var(--space-6);
  }
}
```

### States

- **Loading**: Not applicable — localStorage is synchronous. App renders immediately on DOMContentLoaded.
- **Empty list**: `.empty-state` paragraph shown inside the list, context-aware copy based on active filter tab.
- **Error (empty input)**: `.is-error` class on `.todo-input` triggers red border + shake animation. Removed after 600ms. Input receives focus.
- **Completed item**: `.is-completed` on `.todo-item` — strikethrough text, muted color, checkbox filled indigo.
- **Active filter tab**: `.is-active` + `aria-pressed="true"` on the active `.filter-btn`.
- **Clear completed visible**: `.clear-completed-btn` switches from `display:none` to `display:inline-block` only when at least one completed task exists.

### Accessibility

- Semantic HTML structure: `<main>`, `<h1>`, `<form>`, `<ul>`, `<li>`, `<button>`, `<label>`
- Every `<input>` must have an associated `<label>` — use `for`/`id` pairing. The add-task label can be visually hidden with `.sr-only` if the placeholder is sufficient, but the label element must be present in DOM.
- `.sr-only` utility class (include in styles.css): `position:absolute; width:1px; height:1px; padding:0; margin:-1px; overflow:hidden; clip:rect(0,0,0,0); white-space:nowrap; border:0`
- Delete button: `aria-label="Delete task"` required — it has no visible text
- Filter buttons: `aria-pressed="true"/"false"` to communicate active state to screen readers
- Checkbox: native `<input type="checkbox">` — do not intercept keyboard events, let the browser handle it
- Focus order: title → input → add button → filter tabs → todo items (checkbox → delete) → footer buttons. Must be logical top-to-bottom.
- All interactive elements must show a visible `:focus-visible` outline — never `outline: none` without a custom replacement
- Color contrast: `--color-text-primary` (#1a1a1a) on `--color-surface` (#ffffff) = 18.1:1 (AAA). `--color-text-secondary` (#737373) on white = 4.6:1 (AA). `--color-accent` (#6366f1) on white = 3.1:1 — only use for decorative/interactive color, not body text.

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
        <!-- .todo-item elements injected by render.js -->
        <!-- or .empty-state when list is empty -->
      </ul>

      <footer class="todo-footer">
        <span class="task-count" id="task-count" aria-live="polite">0 tasks left</span>
        <button class="clear-completed-btn" id="clear-completed">Clear completed</button>
      </footer>
    </div>
  </div>
</body>
```

Each todo item rendered by render.js:
```html
<li class="todo-item" data-id="{{id}}">
  <input
    class="todo-checkbox"
    type="checkbox"
    aria-label="Mark complete: {{text}}"
    {{checked if completed}}
  />
  <span class="todo-text">{{text}}</span>
  <button class="delete-btn" aria-label="Delete task">&#215;</button>
</li>
```
When completed, add class `is-completed` to the `<li>`.
