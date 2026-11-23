"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-liner (<= 200 characters) naming a
hilariously useless superpower to /output/entry.txt.
Standard library only.
"""

import os
from pathlib import Path

LINE = "I can stop time for exactly one second a year, and I always spend it blinking."


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-200 chars, one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
