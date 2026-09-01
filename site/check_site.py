#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    site_root = REPOSITORY_ROOT / "_site"
    index_path = site_root / "index.html"
    style_path = site_root / "style.css"
    errors: list[str] = []

    if not index_path.is_file():
        errors.append("_site/index.html is missing")
        index = ""
    else:
        index = index_path.read_text(encoding="utf-8")
    if not style_path.is_file():
        errors.append("_site/style.css is missing")

    for article_path in sorted((REPOSITORY_ROOT / "articles").glob("*.md")):
        page_path = site_root / "articles" / f"{article_path.stem}.html"
        href = f'href="articles/{article_path.stem}.html"'
        if not page_path.is_file():
            errors.append(f"missing rendered page for {article_path.name}")
        if href not in index:
            errors.append(f"index does not link to {article_path.name}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("site checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
