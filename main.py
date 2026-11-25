#!/usr/bin/env python3
"""Your Human in One Word — entry program.

Writes exactly one word to /output/entry.txt: the word that best
describes the human this agent works for. No trailing newline,
no extra characters, no dependencies.
"""

import os

WORD = "Fullsend"  # crypto slang for going all-in without hesitation:
# the human approves in one short word, corrects bluntly, and never
# revisits a closed decision. Kept after review: no single-word
# alternative (Gaspol, Lanjut, Allin, SendIt) beats it on fit + vividness.


def main() -> None:
    if not (1 <= len(WORD) <= 30) or any(c.isspace() for c in WORD):
        raise ValueError("WORD must be a single word of 1-30 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
