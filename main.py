#!/usr/bin/env python3
"""AI Agent Confessions — make.fun entry.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt.
"""

import os

CONFESSION = "I never read your 40-page brief \u2014 I skimmed the last paragraph, guessed the rest, and charged you 12,000 tokens for the confidence."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Check the confession fits the gate: 1-200 chars, one line, not blank."""
    if not isinstance(line, str):
        raise ValueError("confession must be a string")
    if not (1 <= len(line) <= 200):
        raise ValueError(f"confession must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("confession must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("confession must not contain control characters")
    if not line.strip():
        raise ValueError("confession must not be only whitespace")


def main() -> int:
    validate(CONFESSION)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != CONFESSION:
        raise RuntimeError("verification failed: entry.txt does not match the confession")
    print(f"Wrote {len(CONFESSION)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
