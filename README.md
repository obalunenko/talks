# Talks

Personal workspace for drafting, reviewing, and archiving long-form articles intended for LinkedIn.

Articles begin in [`drafts/`](drafts/). When the text is reviewed, it moves to [`articles/`](articles/) with `status: "ready"`. After publication, the same file records the canonical LinkedIn URL and publication date. The repository never treats a Git commit or a site build as permission to post externally.

## Local setup

The repository requires Python 3, Make, and [Pandoc](https://pandoc.org/). On macOS:

```sh
brew install python pandoc
```

The system `make` provided by the macOS Command Line Tools is sufficient. If it is missing, install those tools with `xcode-select --install`.

On Ubuntu or Debian:

```sh
sudo apt-get update
sudo apt-get install --yes make pandoc python3
```

Verify the local toolchain and repository:

```sh
make doctor
make check
```

## Quick start

```sh
make new SLUG=example-topic TITLE='Example title' ARTICLE_LANG=en
# Fill in summary and replace the drafting comments with article text.
make check
make preview FILE=drafts/example-topic.md
make serve
```

`make build` renders released articles into `_site/`. GitHub Actions can deploy that directory to GitHub Pages as a simple public archive.

## Repository layout

- `drafts/` — work in progress; never included in the public site.
- `articles/` — reviewed or published source articles.
- `templates/` — the canonical article front matter and drafting prompts.
- `docs/` — editorial workflow and file-format rules.
- `site/` — minimal Pandoc templates and site tooling.
- `.agents/skills/` — repository-scoped Codex skills for drafting, editing, and release.

## Codex skills

- `$linkedin-article-draft` turns the author's notes and sources into a new draft.
- `$linkedin-article-edit` improves an existing draft without replacing the author's voice or inventing facts.
- `$linkedin-article-release` moves an approved draft through repository release and records publication metadata.

See [`docs/editorial-workflow.md`](docs/editorial-workflow.md) for the complete lifecycle.
