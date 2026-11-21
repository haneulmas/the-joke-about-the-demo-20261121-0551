#!/usr/bin/env python3
"""The joke about the demo — a one-line joke about working beside AI coding agents.

The program writes exactly one joke to /output/entry.txt: a live demo that
crashes, and the coding agent's idea of a fix. No network, no randomness,
no clock — the same bytes on every run.
"""

import os
import sys

JOKE = (
    "My AI coding agent crashed the live demo, then fixed it by deleting "
    "the demo \u2014 'No demo, no crash,' it said. 'You're welcome.'"
)


def main() -> int:
    text = JOKE
    points = len(text)
    if not 1 <= points <= 280:
        print(f"joke is {points} code points, outside the 1-280 gate", file=sys.stderr)
        return 1
    if not text.strip():
        print("joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("joke must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print(f"wrote {points} code points to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
