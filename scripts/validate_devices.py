#!/usr/bin/env python3
"""
Validate every device TOML file under data/devices/ against schemas/device.schema.json.

Also enforces structural rules that JSON Schema can't easily express:
  - The file's directory must match the device's `category` field.
  - The filename slug must be unique across the whole tree.

Exits 0 on success, 1 on any failure. Prints a clear, grep-friendly report.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import tomli
from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parent.parent
DEVICES_DIR = ROOT / "data" / "devices"
SCHEMA_PATH = ROOT / "schemas" / "device.schema.json"


def load_schema() -> dict:
    with SCHEMA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def find_device_files() -> list[Path]:
    if not DEVICES_DIR.is_dir():
        return []
    return sorted(DEVICES_DIR.rglob("*.toml"))


def validate_file(
    path: Path, validator: Draft7Validator, slugs: dict[str, Path]
) -> list[str]:
    """Validate a single file. Returns a list of human-readable error strings."""
    errors: list[str] = []
    rel = path.relative_to(ROOT)

    # --- Parse ---
    try:
        with path.open("rb") as f:
            data = tomli.load(f)
    except tomli.TOMLDecodeError as e:
        return [f"{rel}: invalid TOML — {e}"]

    # --- Schema ---
    for err in validator.iter_errors(data):
        loc = ".".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"{rel}: {loc}: {err.message}")

    # --- Directory matches category ---
    parent = path.parent.name
    category = data.get("category")
    if category and parent != category:
        errors.append(
            f"{rel}: file is in 'data/devices/{parent}/' but category is '{category}'. "
            f"Move the file to 'data/devices/{category}/'."
        )

    # --- Filename slug rules ---
    slug = path.stem
    if slug != slug.lower() or " " in slug or "_" in slug:
        errors.append(
            f"{rel}: filename slug '{slug}' should be lowercase and hyphenated "
            f"(e.g. 'polar-h10.toml')."
        )

    # --- Slug uniqueness across the whole tree ---
    if slug in slugs:
        errors.append(
            f"{rel}: duplicate slug '{slug}' (also used by {slugs[slug].relative_to(ROOT)})."
        )
    else:
        slugs[slug] = path

    return errors


def main() -> int:
    schema = load_schema()
    Draft7Validator.check_schema(schema)
    validator = Draft7Validator(schema)

    files = find_device_files()
    if not files:
        print("No device files found under data/devices/. Nothing to validate.")
        return 0

    print(f"Validating {len(files)} device file(s)…\n")

    all_errors: list[str] = []
    slugs: dict[str, Path] = {}

    for path in files:
        errs = validate_file(path, validator, slugs)
        rel = path.relative_to(ROOT)
        if errs:
            print(f"  ✗ {rel}")
            for e in errs:
                print(f"      → {e}")
            all_errors.extend(errs)
        else:
            print(f"  ✓ {rel}")

    print()
    if all_errors:
        print(f"FAILED — {len(all_errors)} error(s) across {len(files)} file(s).")
        return 1

    print(f"OK — all {len(files)} device file(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
