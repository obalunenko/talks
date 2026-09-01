from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


SLUG_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
LANG_PATTERN = re.compile(r"[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*")
REQUIRED_FIELDS = (
    "title",
    "summary",
    "lang",
    "status",
    "published_at",
    "linkedin_url",
)


class ArticleFormatError(ValueError):
    pass


@dataclass(frozen=True)
class Article:
    path: Path
    metadata: dict[str, str]
    body: str


def _decode_scalar(raw_value: str, line_number: int) -> str:
    value = raw_value.strip()
    if value == "":
        return ""
    if value.startswith('"'):
        try:
            decoded = json.loads(value)
        except json.JSONDecodeError as exc:
            raise ArticleFormatError(
                f"line {line_number}: invalid double-quoted value"
            ) from exc
        if not isinstance(decoded, str):
            raise ArticleFormatError(f"line {line_number}: value must be a string")
        return decoded
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def read_article(article_path: Path) -> Article:
    try:
        source = article_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise ArticleFormatError("file is not valid UTF-8") from exc

    lines = source.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ArticleFormatError("missing opening YAML front matter delimiter")

    try:
        closing_index = next(
            index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---"
        )
    except StopIteration as exc:
        raise ArticleFormatError("missing closing YAML front matter delimiter") from exc

    metadata: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, separator, raw_value = line.partition(":")
        key = key.strip()
        if not separator or not re.fullmatch(r"[a-z][a-z0-9_]*", key):
            raise ArticleFormatError(f"line {line_number}: expected a simple key: value field")
        if key in metadata:
            raise ArticleFormatError(f"line {line_number}: duplicate field {key!r}")
        metadata[key] = _decode_scalar(raw_value, line_number)

    body = "\n".join(lines[closing_index + 1 :]).strip()
    return Article(path=article_path, metadata=metadata, body=body)


def has_prose(body: str) -> bool:
    without_comments = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    return bool(without_comments.strip())
