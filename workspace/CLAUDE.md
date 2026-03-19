# Workspace — Product Code

This directory contains the product being built by the AI startup team.

## Tech Stack

- Next.js 15 (App Router)
- TypeScript (strict)
- Tailwind CSS + Shadcn/ui
- Playwright for E2E testing

## Conventions

- Server Components by default
- `'use client'` only when needed (interactivity, hooks)
- Use `@/` import alias for `src/`
- Components: PascalCase, one per file, in `src/components/`
- API routes: `src/app/api/`, RESTful conventions
- Types: `src/types/` or co-located
- No `any` types
- Always handle loading, error, and empty states
