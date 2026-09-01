#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from articlelib import LANG_PATTERN, SLUG_PATTERN


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = REPOSITORY_ROOT / "templates" / "linkedin-article.md"


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a LinkedIn article draft.")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--lang", default="en")
    args = parser.parse_args()

    if not SLUG_PATTERN.fullmatch(args.slug):
        parser.error("--slug must contain lowercase letters, digits, and single hyphens")
    if not args.title.strip():
        parser.error("--title must not be empty")
    if not LANG_PATTERN.fullmatch(args.lang):
        parser.error("--lang must be a short language tag such as en, ru, or en-GB")

    destination = REPOSITORY_ROOT / "drafts" / f"{args.slug}.md"
    if destination.exists():
        parser.error(f"draft already exists: {destination.relative_to(REPOSITORY_ROOT)}")

    rendered = TEMPLATE_PATH.read_text(encoding="utf-8")
    rendered = rendered.replace("{{TITLE_YAML}}", json.dumps(args.title.strip(), ensure_ascii=False))
    rendered = rendered.replace("{{LANG_YAML}}", json.dumps(args.lang, ensure_ascii=False))
    destination.write_text(rendered, encoding="utf-8")
    print(f"created {destination.relative_to(REPOSITORY_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
