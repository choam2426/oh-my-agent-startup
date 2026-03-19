---
name: todo_app_security_review
description: Security review findings for the todo app in workspace/ — no critical issues, two High findings around meta CSP limitations
type: project
---

Reviewed workspace/ todo app (index.html, store.js, render.js, app.js, styles.css). No critical issues found. XSS posture is strong.

**High findings:**
1. CSP delivered as `<meta>` tag — `frame-ancestors` is ignored in meta CSP; clickjacking protection absent. Fix requires server-side HTTP header.
2. Unnecessary `data:` in `img-src` CSP — app has no images; remove it.

**Medium findings:**
- Meta CSP has broader limitations beyond frame-ancestors (no sandbox, no report-uri, late parsing).
- `aria-label` built from `todo.text` via `setAttribute` — no XSS risk but adversarial strings could mislead screen readers.
- Missing `Referrer-Policy` and `Permissions-Policy` headers.

**All High findings are deployment/server-config issues** — Pipeline's domain, not Pixel's code.

**Why:** Meta CSP is a common misunderstanding — developers think it provides the same protection as HTTP headers, but browsers explicitly ignore `frame-ancestors` in meta CSP per the spec.

**How to apply:** In future reviews, always check whether CSP is delivered as a header or meta tag. Meta tag = limited protection. Always flag missing `frame-ancestors` and `X-Frame-Options` as High.
