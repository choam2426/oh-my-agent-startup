---
name: coding-conventions
description: Coding conventions and tech stack for the AI startup workspace
---

# Coding Conventions

## Tech Stack

- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS + Shadcn/ui
- **Package Manager**: npm
- **Testing**: Playwright

## Project Structure (inside workspace/)

```
workspace/
├── src/
│   ├── app/              # Next.js App Router pages
│   │   ├── layout.tsx    # Root layout
│   │   ├── page.tsx      # Home page
│   │   └── api/          # API routes
│   ├── components/       # React components (PascalCase)
│   │   └── ui/           # Shadcn/ui components
│   ├── lib/              # Utilities and shared logic
│   │   ├── db/           # Database logic
│   │   └── utils.ts      # Helper functions (cn, etc.)
│   └── types/            # TypeScript type definitions
├── public/               # Static assets
├── tests/                # Playwright test files
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── next.config.ts
```

## Conventions

- **Components**: PascalCase file names, one component per file
- **Server Components** by default, `'use client'` only when needed
- **Imports**: use `@/` path alias for `src/`
- **Styling**: Tailwind classes, use `cn()` for conditional classes
- **Types**: prefer `interface` for objects, `type` for unions/intersections
- **Error handling**: try/catch with user-friendly messages
- **No `any`**: always type properly
