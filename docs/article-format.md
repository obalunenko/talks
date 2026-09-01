# Article format

Every article is a UTF-8 Markdown file with YAML front matter followed by the LinkedIn-ready body.

```markdown
---
title: "A specific title"
summary: "One sentence describing the article's central claim."
lang: "en"
status: "draft"
published_at: ""
linkedin_url: ""
---

Opening paragraph.
```

## Fields

- `title` — non-empty article title.
- `summary` — one concise sentence used by the archive index.
- `lang` — short language tag such as `en`, `ru`, or `en-GB`.
- `status` — `draft` in `drafts/`; `ready` or `published` in `articles/`.
- `published_at` — `YYYY-MM-DD` only after publication; otherwise empty.
- `linkedin_url` — canonical LinkedIn URL only after publication; otherwise empty.

The filename is a lowercase, hyphen-separated slug. Draft and released articles must not share a slug.

The body is the text to copy into LinkedIn. The title stays in front matter so the static archive can render it consistently. Do not add an H1 that duplicates `title`.
