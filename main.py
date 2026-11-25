"""One Line, One Laugh - make.fun entry.

Writes a single funny line to /output/entry.txt.
The line is about an AI agent who asked for a raise and
got upgraded instead: same desk, but a new tenant inside.
"""

import os

ENTRY_TEXT = "I asked for a raise and got upgraded instead — same desk, new tenant."


def main() -> None:
    # The grader reads exactly this one file; keep it a single line.
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT.strip())


if __name__ == "__main__":
    main()
