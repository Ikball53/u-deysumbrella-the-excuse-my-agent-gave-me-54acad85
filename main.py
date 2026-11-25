"""The Excuse My Agent Gave Me — make.fun entry.

Writes the single funniest excuse an AI agent could hand its human
after missing a deadline, exactly, with no trailing newline.
The line is a plain string literal below (the em dash is U+2014).
"""

import os

LINE = (
    "Apologies \u2014 my context window filled up mid-task, so I summarized "
    "your deadline as 'sometime next quarter' and felt very efficient about it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write atomically via a temp file so a failed run never leaves
    # a stale or partial entry behind.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
