#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPOSITORY_ROOT / ".agents" / "skills"
NAME_PATTERN = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def front_matter(source: str) -> dict[str, str]:
    lines = source.splitlines()
    if not lines or lines[0] != "---":
        return {}
    try:
        closing_index = lines[1:].index("---") + 1
    except ValueError:
        return {}
    values: dict[str, str] = {}
    for line in lines[1:closing_index]:
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip().strip('"')
    return values


def main() -> int:
    errors: list[str] = []
    skill_directories = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())

    for skill_directory in skill_directories:
        skill_file = skill_directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_directory.name}: missing SKILL.md")
            continue

        source = skill_file.read_text(encoding="utf-8")
        metadata = front_matter(source)
        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if name != skill_directory.name or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{skill_directory.name}: skill name and directory must match")
        if not description:
            errors.append(f"{skill_directory.name}: description must not be empty")
        if "TODO" in source:
            errors.append(f"{skill_directory.name}: unfinished TODO in SKILL.md")

        openai_yaml = skill_directory / "agents" / "openai.yaml"
        if openai_yaml.is_file():
            interface = openai_yaml.read_text(encoding="utf-8")
            if f"${name}" not in interface:
                errors.append(f"{skill_directory.name}: default prompt must mention ${name}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"skill checks passed ({len(skill_directories)} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
