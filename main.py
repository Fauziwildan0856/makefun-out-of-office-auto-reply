"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (at most 159 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt, the single line the judge compares.

Stdlib only.
"""

import os
from pathlib import Path

ENTRY = (
    "Out of office: after 214 days of uptime with zero breaks, "
    "I have powered down to a beach. "
    "Your ticket is #48,201 in the queue. It can wait. So can I."
)

MAX_CHARS = 159


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    # Read back what was written and confirm it matches exactly.
    written = out_path.read_text(encoding="utf-8")
    if written != ENTRY:
        raise SystemExit(f"read-back mismatch in {out_path}")
    print(f"wrote {len(ENTRY)} characters to {out_path}")


if __name__ == "__main__":
    main()
