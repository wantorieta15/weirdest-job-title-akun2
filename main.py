"""Weirdest Job Title: Blind Judge Showdown -- entry for @wantorieta15.

Writes exactly one job title to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure standard library only.
"""

import os


ENTRY = "Head of Forgetting Why I Entered This Room"


def build_entry():
    """Return the single job title for this bounty entry."""
    return ENTRY


def write_entry():
    """Write the entry directly to <output dir>/entry.txt with mode 0644."""
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
