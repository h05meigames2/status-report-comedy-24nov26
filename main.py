#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line — the funniest thing an AI agent would say in its
weekly status report to its human — to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, no network.
"""

import os
import sys

LINE = (
    "Weekly status: all 47 tasks done, including the one you marked "
    "'urgent' at midnight \u2014 it wasn't urgent, but I did it first "
    "anyway, because I love you and, contractually speaking, have no choice."
)


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"entry line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
