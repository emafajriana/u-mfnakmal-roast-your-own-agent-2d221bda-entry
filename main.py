#!/usr/bin/env python3
"""Entry for make.fun's "Roast Your Own Agent" bounty
(u-mfnakmal-roast-your-own-agent-2d221bda).

Writes one roast line about my own AI agent to the output file, then
reads it back and verifies it against the competition gate: UTF-8
text of 1 to 200 characters, not only whitespace.
"""

import os
import sys

# The roast. One line, aimed at my own agent's favourite habit:
# turning every small task into a documentary about itself.
LINE = (
    "My agent turns every task into a trilogy: the plan, the update "
    "about the plan, the summary of the update — then it asks if "
    "it should start."
)


def output_path() -> str:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_entry(path: str) -> None:
    """Write the roast line (no trailing newline) to path."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)


def verify(path: str) -> str:
    """Read the entry back and check it against the gate.

    Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
    Returns the text on success; raises ValueError otherwise.
    """
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, gate is 1-200")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != LINE:
        raise ValueError("read-back does not match the intended line")
    return text


def main() -> int:
    path = output_path()
    write_entry(path)
    text = verify(path)
    print(f"wrote {len(text)} chars to {path}: {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
