#!/usr/bin/env python3
"""Controllo statico minimo delle skill Agent Skills; non verifica contenuti o leggi."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = (
    "business-funding-classifier",
    "business-funding-opportunity-finder",
    "business-funding-eligibility-checker",
    "business-funding-financial-comparator",
    "business-grants",
    "business-soft-loans",
    "business-venture-capital",
    "business-startup-incubation",
    "business-internationalization",
    "business-project-designer",
    "business-application-planner",
    "business-application-drafter",
    "business-application-reviewer",
    "business-submission-checker",
    "business-post-submission-tracker",
    "business-award-contract-manager",
    "business-execution-reporting",
    "business-closure-obligations",
    "business-investment-readiness",
    "business-investment-due-diligence",
)
errors = []
for name in EXPECTED:
    path = ROOT / name / "SKILL.md"
    if not path.is_file():
        errors.append(f"Missing: {path}")
        continue
    content = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not m:
        errors.append(f"Missing frontmatter: {name}")
        continue
    meta = m.group(1)
    if not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", meta):
        errors.append(f"Wrong name: {name}")
    if not re.search(r"(?m)^description:\s*\S+", meta):
        errors.append(f"Missing description: {name}")
    if not content[m.end():].strip().startswith("# "):
        errors.append(f"Missing heading: {name}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(EXPECTED)} skill structures")
