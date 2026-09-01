---
name: linkedin-article-edit
description: Review and edit an existing LinkedIn article draft for clarity, structure, credibility, and author voice. Use when a draft already exists; do not use to originate an article or publish it.
---

# LinkedIn Article Edit

Improve an existing article without silently changing what the author claims or how certain those claims are.

## Workflow

1. Read [AGENTS.md](../../../AGENTS.md), [the editorial workflow](../../../docs/editorial-workflow.md), and the target draft in full.
2. Identify its thesis, intended reader, strongest evidence, and intended takeaway before editing.
3. Review title, opening, argument order, paragraph length, transitions, examples, evidence, and conclusion. Remove repetition and formulaic phrasing, but keep useful nuance and the author's language and voice.
4. Do not introduce new facts, personal experiences, quotations, metrics, or certainty. Flag unsupported or time-sensitive claims; verify them only when the task calls for research.
5. Keep the article in `drafts/` with `status: "draft"`. Update `summary` when the thesis changes.
6. Run `make check` after editing.

Report the material edits and any unresolved factual or editorial questions. Do not move, post, or mark the article as published.
