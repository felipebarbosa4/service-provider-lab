#!/usr/bin/env python3
"""Perform lightweight, dependency-free validation of the documentation repository."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "README.md",
    ROOT / "diagrams/topology.md",
    ROOT / "labs/bgp/README.md",
    ROOT / "labs/mpls-l3vpn/README.md",
    ROOT / "labs/evpn/README.md",
    ROOT / "troubleshooting/bgp-session-down.md",
    ROOT / "verification/expected-state.md",
]

MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def validate() -> list[str]:
    failures: list[str] = []

    for path in REQUIRED:
        if not path.exists():
            failures.append(f"missing required file: {path.relative_to(ROOT)}")
            continue
        if len(path.read_text(encoding="utf-8").strip()) < 80:
            failures.append(f"file is unexpectedly short: {path.relative_to(ROOT)}")

    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "TODO" in text or "TBD" in text:
            failures.append(f"unfinished marker in {path.relative_to(ROOT)}")
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative_target = target.split("#", 1)[0]
            if not relative_target:
                continue
            resolved = (path.parent / relative_target).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                failures.append(f"link escapes repository in {path.relative_to(ROOT)}: {target}")
            elif not resolved.exists():
                failures.append(f"broken local link in {path.relative_to(ROOT)}: {target}")

    return failures


def main() -> int:
    failures = validate()
    if failures:
        print("Documentation validation FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Documentation validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
