#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry (account B / Slothana).

Writes one single-line code-review comment that approves a pull request
while carrying quiet existential dread, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt when the variable is unset).

Deterministic: no network, no model calls, no randomness, no clock.
The line is a fixed string; the program only writes it.
"""

import os
import sys

ENTRY = (
    "Approved. The tests are green, the diff is clean, and I no longer "
    "remember what problem this was supposed to solve."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
