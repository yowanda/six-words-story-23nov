#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one original six-word story to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when unset). Deterministic, no network.
"""
import os
import sys

STORY = "He proposed; she smiled, then vanished."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(STORY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
