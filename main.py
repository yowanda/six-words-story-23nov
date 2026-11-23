#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one original six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when unset). Deterministic, no network.
"""
import os
import sys

STORY = "He proposed; she smiled, then vanished."


def main() -> int:
    # Runtime validation: the entry must be exactly six words, 1-60 chars.
    words = STORY.split()
    if len(words) != 6:
        raise SystemExit(f"invalid story: expected 6 words, got {len(words)}")
    if not 1 <= len(STORY) <= 60:
        raise SystemExit(f"invalid story: length {len(STORY)} outside 1-60 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Deterministic byte write: exact bytes, single trailing newline.
    with open(path, "wb") as f:
        f.write((STORY + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
