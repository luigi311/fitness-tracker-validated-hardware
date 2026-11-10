#!/usr/bin/env python3
"""Download app screenshots into Zola's static assets before building the site."""

from __future__ import annotations

import sys
import tempfile
import tomllib
from http.client import HTTPException
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "data" / "screenshots.toml"
OUTPUT_DIR = ROOT / "static" / "screenshots"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fetch_screenshots() -> None:
    """Fetch every image before replacing any previously downloaded assets."""
    with MANIFEST_PATH.open("rb") as source:
        manifest = tomllib.load(source)

    source_base_url = manifest["source_base_url"].rstrip("/") + "/"
    filenames = [screenshot["file"] for screenshot in manifest["screenshots"]]
    for filename in filenames:
        if Path(filename).name != filename or Path(filename).suffix != ".png":
            raise ValueError(f"Screenshot filename must be a PNG basename: {filename!r}")

    OUTPUT_DIR.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".screenshots-", dir=OUTPUT_DIR.parent
    ) as temporary:
        staging = Path(temporary)
        for filename in filenames:
            url = source_base_url + quote(filename)
            request = Request(url, headers={"User-Agent": "Fitness-Tracker-Site-Build"})
            try:
                with urlopen(request, timeout=30) as response:
                    image = response.read()
            except (OSError, HTTPException) as error:
                raise RuntimeError(f"Could not download screenshot {filename}: {error}") from error

            if not image.startswith(PNG_SIGNATURE):
                raise ValueError(f"Downloaded screenshot {filename} is not a PNG image")
            (staging / filename).write_bytes(image)
            print(f"Downloaded {filename} ({len(image):,} bytes).")

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        for filename in filenames:
            (staging / filename).replace(OUTPUT_DIR / filename)

    print(f"Prepared {len(filenames)} screenshot(s) in {OUTPUT_DIR.relative_to(ROOT)}.")


def main() -> int:
    try:
        fetch_screenshots()
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        print(f"Screenshot download failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
