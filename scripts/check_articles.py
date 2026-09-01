#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

from articlelib import (
    LANG_PATTERN,
    REQUIRED_FIELDS,
    SLUG_PATTERN,
    ArticleFormatError,
    has_prose,
    read_article,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
LINKEDIN_URL_PATTERN = re.compile(r"https://(?:www\.)?linkedin\.com/.+")


def validate_article(article_path: Path, area: str) -> list[str]:
    errors: list[str] = []
    relative_path = article_path.relative_to(REPOSITORY_ROOT)

    if not SLUG_PATTERN.fullmatch(article_path.stem):
        errors.append(f"{relative_path}: filename must be a lowercase hyphenated slug")

    try:
        article = read_article(article_path)
    except ArticleFormatError as exc:
        return [f"{relative_path}: {exc}"]

    metadata = article.metadata
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            errors.append(f"{relative_path}: missing front matter field {field!r}")

    if not metadata.get("title", "").strip():
        errors.append(f"{relative_path}: title must not be empty")
    if not metadata.get("summary", "").strip():
        errors.append(f"{relative_path}: summary must not be empty")
    if not LANG_PATTERN.fullmatch(metadata.get("lang", "")):
        errors.append(f"{relative_path}: lang must be a short language tag")
    if not has_prose(article.body):
        errors.append(f"{relative_path}: article body has no prose")

    status = metadata.get("status", "")
    allowed_statuses = {"draft"} if area == "drafts" else {"ready", "published"}
    if status not in allowed_statuses:
        allowed = ", ".join(sorted(allowed_statuses))
        errors.append(f"{relative_path}: status must be one of: {allowed}")

    publication_date = metadata.get("published_at", "")
    linkedin_url = metadata.get("linkedin_url", "")
    if status == "published":
        try:
            dt.date.fromisoformat(publication_date)
        except ValueError:
            errors.append(f"{relative_path}: published_at must use YYYY-MM-DD")
        if not LINKEDIN_URL_PATTERN.fullmatch(linkedin_url):
            errors.append(f"{relative_path}: linkedin_url must be a canonical LinkedIn URL")
    elif publication_date or linkedin_url:
        errors.append(
            f"{relative_path}: publication metadata must stay empty until status is published"
        )

    if area == "articles" and re.search(r"\b(?:TODO|TBD)\b|{{.+?}}", article.body):
        errors.append(f"{relative_path}: released article contains an unfinished placeholder")

    return errors


def main() -> int:
    errors: list[str] = []
    seen_slugs: dict[str, Path] = {}

    for area in ("drafts", "articles"):
        for article_path in sorted((REPOSITORY_ROOT / area).glob("*.md")):
            previous = seen_slugs.get(article_path.stem)
            if previous:
                errors.append(
                    f"{article_path.relative_to(REPOSITORY_ROOT)}: slug duplicates "
                    f"{previous.relative_to(REPOSITORY_ROOT)}"
                )
            else:
                seen_slugs[article_path.stem] = article_path
            errors.extend(validate_article(article_path, area))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"article checks passed ({len(seen_slugs)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
