# Contributing

We welcome contributions! Please use **Pull Requests** and follow the guidelines below.

## How to add content
1. Create a new branch
2. Edit or add Markdown files in `/docs`
3. Use fenced code blocks for commands: \`\`\`bash
4. Prefer **read‑only** diagnostics; when using risky commands, add a warning block:

```markdown
!!! warning "⚠️ SAFETY — high‑risk operation"
    Explain impact, pre-checks, and rollback.
```

5. Open a Pull Request; tag reviewers

## Style
- Use sentence case headings
- Keep commands runnable (no trailing spaces)
- Prefer short paragraphs and bullet lists

## Risky commands
If you must include risky operations (e.g., `killall -9`, `isi_test_thread`, or panic triggers), link to **Risky Commands (Read First)** and add a **warning** callout.
