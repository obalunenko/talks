# Repository instructions

This repository is an authoring workspace for LinkedIn articles.

## Content integrity

- Treat the author's notes, explicitly supplied sources, and confirmed experience as the source of truth.
- Never invent personal anecdotes, measurements, quotations, credentials, outcomes, or citations.
- Distinguish opinion from verifiable fact. Verify current or uncertain factual claims when they materially affect the article.
- Preserve the requested language and the author's natural technical level.
- The `dzyanis/articles` repository is structural inspiration only. Do not copy its article prose, examples, arguments, claims, or topic material.

## Repository workflow

- Required local commands are `python3`, `make`, and `pandoc`; run `make doctor` before the first build.
- New work belongs in `drafts/<lowercase-hyphen-slug>.md` with `status: "draft"`.
- Reviewed work moves to `articles/` with `status: "ready"` only after the author says it is ready.
- Use `status: "published"` only with a confirmed `published_at` date and canonical `linkedin_url`.
- Do not publish to LinkedIn or any other external service without an explicit request for that external action.
- Follow `docs/article-format.md` and run `make check` after content or tooling changes. Installation commands live in `README.md`.

Use the matching repository skill under `.agents/skills/` for drafting, editing, or release work.
