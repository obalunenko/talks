---
name: linkedin-article-release
description: Prepare a reviewed LinkedIn article for release, move it into the published-content area, and record publication metadata. Use only when the author says a draft is ready or supplies a LinkedIn publication URL.
---

# LinkedIn Article Release

Finalize repository state for a reviewed article. A repository release and an external LinkedIn publication are separate actions.

## Workflow

1. Read [AGENTS.md](../../../AGENTS.md), [the editorial workflow](../../../docs/editorial-workflow.md), and [the article format](../../../docs/article-format.md).
2. Confirm the author has explicitly said the draft is ready. Resolve placeholders, unsupported claims, broken links, and unfinished notes; do not invent missing publication data.
3. Set `status: "ready"`, move the file from `drafts/` to `articles/`, and run `make check`.
4. If Pandoc is installed, run `make preview FILE=articles/<slug>.md` and inspect the generated page for obvious rendering problems.
5. Publishing to LinkedIn is an external side effect. Do it only when the author explicitly asks for that action and an authorized LinkedIn session or connector is available.
6. After the author provides or confirms the live URL and date, set `status: "published"`, `published_at: "YYYY-MM-DD"`, and the canonical `linkedin_url`, then run `make check` again.

Return the final repository path, status, validation result, and any remaining manual action. Never fabricate a URL or publication date.
