#!/usr/bin/env python3
from __future__ import annotations

import html
import subprocess
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from articlelib import read_article  # noqa: E402


def article_timestamp(article_path: Path, published_at: str) -> float:
    if published_at:
        return float(published_at.replace("-", ""))
    result = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%at", "-1", "--", str(article_path)],
        cwd=REPOSITORY_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.stdout.strip().isdigit():
        return float(result.stdout.strip())
    return article_path.stat().st_mtime


def main() -> int:
    records: list[tuple[float, str]] = []
    for article_path in (REPOSITORY_ROOT / "articles").glob("*.md"):
        article = read_article(article_path)
        title = html.escape(article.metadata["title"])
        summary = html.escape(article.metadata["summary"])
        href = f"articles/{html.escape(article_path.stem)}.html"
        item = (
            f'<li><a href="{href}">{title}</a>'
            f'<span class="summary">{summary}</span></li>'
        )
        records.append(
            (article_timestamp(article_path, article.metadata.get("published_at", "")), item)
        )

    records.sort(key=lambda record: record[0], reverse=True)
    article_list = "\n".join(item for _, item in records)
    if not article_list:
        article_list = '<li class="empty">No released articles yet.</li>'

    template = (REPOSITORY_ROOT / "site" / "index-template.html").read_text(
        encoding="utf-8"
    )
    output = template.replace("<!-- ARTICLE_LIST -->", article_list)
    destination = REPOSITORY_ROOT / "_site" / "index.html"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output, encoding="utf-8")
    print(f"wrote {destination.relative_to(REPOSITORY_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
