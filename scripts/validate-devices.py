#!/usr/bin/env python3
"""
validate-devices.py
Validates frontmatter on all device .md files.
Used by CI — exits with code 1 if any file fails.
"""

import os
import re
import sys
from pathlib import Path

DEVICES_DIR = Path(__file__).parent.parent / "devices"

REQUIRED_FIELDS = ["name", "brand", "model", "category", "protocols", "status"]
VALID_STATUSES  = {"validated", "community-tested", "untested", "broken"}
VALID_CATEGORIES = {"heart-rate-monitors", "foot-pods", "bike-trainers", "treadmills"}

def parse_frontmatter(text):
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1]
            value = [v.strip().strip('"').strip("'") for v in inner.split(",") if v.strip()]
        else:
            value = value.strip('"').strip("'")
        data[key] = value
    return data

errors = []

for md_file in sorted(DEVICES_DIR.rglob("*.md")):
    if md_file.name.lower() == "readme.md":
        continue

    rel = md_file.relative_to(DEVICES_DIR.parent)
    text = md_file.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if not fm:
        errors.append(f"{rel}: missing frontmatter block")
        continue

    for field in REQUIRED_FIELDS:
        if field not in fm or not fm[field]:
            errors.append(f"{rel}: missing required field '{field}'")

    if fm.get("status") and fm["status"] not in VALID_STATUSES:
        errors.append(f"{rel}: invalid status '{fm['status']}' — must be one of {VALID_STATUSES}")

    if fm.get("category") and fm["category"] not in VALID_CATEGORIES:
        errors.append(f"{rel}: invalid category '{fm['category']}' — must be one of {VALID_CATEGORIES}")

    # Filename convention: lowercase + hyphens only
    if not re.match(r"^[a-z0-9][a-z0-9\-]*\.md$", md_file.name):
        errors.append(f"{rel}: filename should be lowercase-with-hyphens.md (got '{md_file.name}')")

if errors:
    print("❌  Validation failed:\n")
    for e in errors:
        print(f"  • {e}")
    sys.exit(1)
else:
    print(f"✅  All device files valid ({sum(1 for _ in DEVICES_DIR.rglob('*.md') if _.name.lower() != 'readme.md')} checked).")
