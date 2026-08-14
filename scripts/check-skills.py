#!/usr/bin/env python3
"""Check the links and metadata that keep the skills tree usable."""

from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
ROUTED_SKILLS = (
    "live",
    "state",
    "because",
    "drafts",
    "challenge",
    "compile",
    "jstack-stale",
    "unslop",
)
FORBIDDEN = {
    "\u2014": "em dash",
    "\u2013": "en dash",
    "\u2018": "curly single quote",
    "\u2019": "curly single quote",
    "\u201c": "curly double quote",
    "\u201d": "curly double quote",
}
LINK_RE = re.compile(r"\]\(([^)\s]+)")


def tracked_files():
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        path = ROOT / raw_path.decode()
        if path.is_file():
            yield path


def read_text(path):
    return path.read_text(encoding="utf-8", errors="replace")


def check_links(path, text, errors):
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip("<>")
        if target.startswith("#") or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
            continue
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link {target}")


def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    values = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip().strip("\"'")
    return values


def check_skill_metadata(path, text, errors):
    if path.name != "SKILL.md" or path.parent.parent.name != "skills":
        return
    values = frontmatter(text)
    expected_name = path.parent.name
    if values.get("name") != expected_name:
        errors.append(
            f"{path.relative_to(ROOT)}: frontmatter name must be {expected_name}"
        )
    if not values.get("description", "").strip():
        errors.append(f"{path.relative_to(ROOT)}: frontmatter description is empty")


def check_agent_metadata(path, text, errors):
    if path.parent != ROOT / "agents" or path.suffix != ".md":
        return
    values = frontmatter(text)
    expected_name = path.stem
    if values.get("name") != expected_name:
        errors.append(
            f"{path.relative_to(ROOT)}: frontmatter name must be {expected_name}"
        )
    if not values.get("description", "").strip():
        errors.append(f"{path.relative_to(ROOT)}: frontmatter description is empty")


def check_forbidden(path, text, errors):
    for character, name in FORBIDDEN.items():
        if character in text:
            errors.append(f"{path.relative_to(ROOT)}: contains {name}")


def check_routed_skills(errors):
    mode_path = ROOT / "skills" / "jstack-mode" / "SKILL.md"
    if not mode_path.is_file():
        errors.append("skills/jstack-mode/SKILL.md: routed skill source is missing")
        return
    for skill_name in ROUTED_SKILLS:
        target = ROOT / "skills" / skill_name / "SKILL.md"
        if not target.is_file():
            errors.append(
                f"skills/jstack-mode/SKILL.md: routed skill is missing {skill_name}"
            )


def main():
    errors = []
    for path in tracked_files():
        text = read_text(path)
        check_links(path, text, errors)
        check_skill_metadata(path, text, errors)
        check_agent_metadata(path, text, errors)
        check_forbidden(path, text, errors)
    check_routed_skills(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("skills checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
