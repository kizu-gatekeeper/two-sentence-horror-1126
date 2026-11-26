"""Entry for make.fun bounty: Two-Sentence Horror.

Writes a horror story in exactly two sentences (at most 400 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

LINE = "For a week the baby monitor kept playing my own voice singing my daughter to sleep, so last night I hid in her room to catch whoever was imitating me. At midnight the singing started from the monitor in my hands, my daughter opened eyes that were not hers, and she smiled with my mouth and whispered, 'You found me.'"
MAX_CHARS = 400


def write_entry(out_dir: str) -> Path:
    assert LINE and LINE.strip() == LINE, "entry must be non-empty text"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    assert LINE.count(".") == 2 and "!" not in LINE and "?" not in LINE, (
        "entry must be exactly two sentences"
    )
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    path = out / "entry.txt"
    path.write_text(LINE, encoding="utf-8")
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
