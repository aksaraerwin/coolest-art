#!/usr/bin/env python3
"""make.fun coolest-art-01 entry: "Two Moons".

The artwork ships in this repository as artwork.b64: the PNG's bytes
base64-encoded as one line of text, so the repository holds only text
files. When the grader runs this program it decodes the base64 back to
the exact PNG bytes and writes them to $MAKEFUN_OUTPUT_DIR/entry.png
(default output directory: /output).

Decoding fixed data is deliberate: the program runs twice and both
runs must produce byte-identical output, which fixed input guarantees.
"""

import base64
import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "artwork.b64"
OUTPUT_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


MAX_BYTES = 1_048_576  # competition limit: at most 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"


def load_artwork() -> bytes:
    """Decode the shipped base64 text back to the artwork's exact bytes."""
    return base64.b64decode(SOURCE.read_text(encoding="ascii").strip(), validate=True)


def check_output(destination: Path, expected: bytes) -> None:
    """Fail loudly if the written file is not a complete, in-limit image."""
    data = destination.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"{destination} is {len(data)} bytes, over the 1 MiB limit")
    if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
        raise SystemExit(f"{destination} is neither a PNG nor a JPEG image")
    if data != expected:
        raise SystemExit(f"{destination} differs from the shipped artwork")


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / OUTPUT_NAME
    artwork = load_artwork()
    destination.write_bytes(artwork)
    check_output(destination, artwork)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
