---
name: linkedin-article-draft
description: Create a new LinkedIn article draft from the author's notes, outline, or source material. Use for starting or substantially drafting an article; do not use for polishing an existing draft or recording a publication.
---

# LinkedIn Article Draft

Turn the author's own ideas and evidence into a Markdown draft that is ready for editorial review.

## Workflow

1. Read [AGENTS.md](../../../AGENTS.md), [the article format](../../../docs/article-format.md), and [the canonical template](../../../templates/linkedin-article.md).
2. Establish the topic, intended reader, central claim, desired reader outcome, language, and available notes or sources. Ask only when a missing answer would materially change the article; otherwise make a conservative assumption and state it.
3. Separate supplied facts, personal observations, opinions, and claims that require verification. Never invent experience, metrics, quotations, sources, or results. Research current or uncertain claims when needed and retain traceable links.
4. Create `drafts/<lowercase-hyphen-slug>.md`, preferably with `make new SLUG=<slug> TITLE='<title>' ARTICLE_LANG=<lang>`.
5. Write one clear thesis. Prefer a specific opening, short paragraphs, descriptive subheadings, concrete reasoning, and a conclusion that earns its takeaway. Use lists only when the material is genuinely list-shaped.
6. Preserve the author's requested language and natural level of technical detail. Avoid engagement bait, generic motivational filler, fabricated anecdotes, excessive emojis, and hashtag blocks.
7. Complete the front matter, keeping `status: "draft"`, and run `make check`.

Return the draft path, the central claim, and a short list of facts or sources that still need author confirmation. Do not publish or move the file to `articles/`.
