# Editorial workflow

## 1. Capture

Start from the author's own idea, experience, notes, and sources. Define the intended reader, one central claim, and the change in understanding the article should produce.

Create the file with:

```sh
make new SLUG=topic-slug TITLE='Working title' ARTICLE_LANG=en
```

The result stays in `drafts/` with `status: "draft"`.

## 2. Draft

Build the argument around one thesis. A useful LinkedIn article usually benefits from a specific opening, short paragraphs, clear subheadings, concrete reasoning, and an earned conclusion. These are editorial choices, not a fixed formula.

Keep traceable links for factual claims. Do not turn an assumption or personal view into an unattributed fact.

## 3. Edit

Review the draft for clarity, evidence, repetition, pacing, and author voice. Confirm every quotation, number, and externally checkable claim. Remove drafting comments before release.

Run `make check` throughout the process.

## 4. Release in the repository

After the author approves the text, move it to `articles/` and change its status to `ready`. If Pandoc is available, inspect an HTML preview:

```sh
make preview FILE=articles/topic-slug.md
```

This repository action does not publish anything to LinkedIn.

## 5. Record publication

Once the article is live, record the confirmed date and canonical LinkedIn URL, then set `status: "published"` and run `make check` again. The generated site becomes a durable archive of reviewed and published work.
