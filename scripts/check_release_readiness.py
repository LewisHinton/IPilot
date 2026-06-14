#!/usr/bin/env python3
"""Run lightweight release-readiness checks for IPilot.

The checks are intentionally dependency-free so they can run in GitHub Actions,
local shells, and constrained agent environments.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "LICENSE",
    "README.md",
    "README.zh-CN.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "AGENTS.md",
    ".gitignore",
    ".github/workflows/validate.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/use_case.yml",
    "assets/demo/ipilot-demo.gif",
    "examples/README.md",
    "scripts/validate_ip_brief.py",
    "references/human-in-the-loop-dialogue.md",
    "references/confirmation-gates.md",
    "references/reference-image-intake.md",
    "references/ip-consistency-system.md",
]

README_SECTIONS = [
    "Why Star This",
    "Demo GIF",
    "Quick Start",
    "Human-in-the-Loop by Default",
    "How to Install",
    "Ecosystem Support",
    "Application Domains",
    "Community and Trust",
    "中文版",
    "GitHub Release Checklist",
]

MOJIBAKE_MARKERS = [
    "\u9225",
    "\u9215",
    "\u9239",
    "\ufffd",
    "\u95c4",
    "\u951b",
    "\u6d60\u72b2",
    "\u9352\u6d98",
    "\u6d63\u64b3",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def check_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def check_skill_frontmatter() -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8-sig")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md is missing YAML frontmatter")

    frontmatter = match.group(1)
    if not re.search(r"^name:\s*ipilot\s*$", frontmatter, re.MULTILINE):
        fail("SKILL.md frontmatter must include name: ipilot")
    if not re.search(r"^description:\s*\S", frontmatter, re.MULTILINE):
        fail("SKILL.md frontmatter must include a non-empty description")


def check_readme_sections() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
    missing = [section for section in README_SECTIONS if f"## {section}" not in readme]
    if missing:
        fail("README.md missing sections: " + ", ".join(missing))


def check_no_mojibake() -> None:
    problems: list[str] = []
    self_path = Path(__file__).resolve()
    for path in ROOT.rglob("*"):
        if path.is_dir() or path.suffix.lower() not in {".md", ".py", ".yml", ".yaml"}:
            continue
        if path.resolve() == self_path:
            continue
        text = path.read_text(encoding="utf-8-sig")
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                rel = path.relative_to(ROOT)
                problems.append(f"{rel}: contains mojibake marker {marker!r}")
                break

    if problems:
        fail("Mojibake found:\n" + "\n".join(problems))


def check_sample_briefs() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    from validate_ip_brief import validate  # pylint: disable=import-error

    brief_paths = sorted((ROOT / "sample_briefs").glob("*.md"))
    if not brief_paths:
        fail("No sample briefs found")

    failures: list[str] = []
    for brief in brief_paths:
        text = brief.read_text(encoding="utf-8-sig")
        missing_required, _missing_recommended, _empty_fields = validate(text)
        if missing_required:
            rel = brief.relative_to(ROOT)
            failures.append(f"{rel}: missing {', '.join(missing_required)}")

    if failures:
        fail("Sample brief validation failed:\n" + "\n".join(failures))


def main() -> None:
    check_required_files()
    check_skill_frontmatter()
    check_readme_sections()
    check_no_mojibake()
    check_sample_briefs()
    print("IPilot release-readiness checks passed.")


if __name__ == "__main__":
    main()

