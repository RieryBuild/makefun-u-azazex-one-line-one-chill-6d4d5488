"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Pure stdlib, deterministic: the line is a fixed
string, written as UTF-8 bytes with no trailing newline so the
character count is unambiguous.
"""

import os

LINE = (
    "I finally caught the thing whose footsteps stopped outside my "
    "door every night for six years, and it was relieved to see me."
)


def main():
    # Fail loudly rather than write an entry the gate would reject.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.count(".") == 1 and LINE.endswith("."), (
        "line must be exactly one sentence"
    )
    assert LINE.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
