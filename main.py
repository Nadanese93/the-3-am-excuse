#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet that moonlights as a bouncer.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the wallet refuses to
sign at 3 AM because the user is not on the guest list.
"""

import os

ENTRY = "3 AM? You're not on the guest list \u2014 the door opens at 9, and I'm the bouncer. No signature, no plus-one."

MAX_CHARS = 200


def validate(text):
    """Gate-check one entry line; raise a specific error per failure."""
    if len(text) < 1:
        raise ValueError("entry is empty: need 1-200 characters")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters: over the %d-character cap"
            % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main():
    text = ENTRY
    try:
        validate(text)
    except ValueError as exc:
        raise SystemExit("invalid entry: %s" % exc)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, target)
    os.chmod(target, 0o644)
    # Read-back verification: the file on disk must be byte-identical
    # to what was written, or the run has silently corrupted the entry.
    with open(target, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise SystemExit(
            "read-back mismatch: entry.txt differs from the entry text"
        )


if __name__ == "__main__":
    main()
