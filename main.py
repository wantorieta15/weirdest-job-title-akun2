"""Weirdest Job Title: Blind Judge Showdown -- entry for @wantorieta15.

Writes exactly one job title to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure standard library only.

Reviser rewrite: adds validate_entry() (single line, no newline, sha256
must match the verified entry hash) while keeping the entry text
byte-for-byte identical to the builder entry.
"""

import hashlib
import os


ENTRY = "Head of Forgetting Why I Entered This Room"

EXPECTED_SHA256 = "058ab0950ae4072db5c7a8b0c64c30126f6e85a97d4fd4d5a7ff8d93e6690e9d"


def build_entry():
    """Return the single job title for this bounty entry."""
    return ENTRY


def validate_entry(text=None):
    """Check the entry is one line, has no newline, and matches sha256."""
    if text is None:
        text = build_entry()
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no newline")
    if len(text.encode("utf-8")) != 42:
        raise ValueError("entry must be exactly 42 bytes")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError("entry sha256 mismatch: %s" % digest)
    return True


def write_entry():
    """Write the entry directly to <output dir>/entry.txt with mode 0644."""
    validate_entry()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = build_entry()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    return path


if __name__ == "__main__":
    write_entry()
