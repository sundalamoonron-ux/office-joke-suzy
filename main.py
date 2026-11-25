#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes the winning one-line office joke (selected by internal pairwise
testing in candidates.md) to /output/entry.txt.
"""

import os

JOKE = (
    'Someone labeled my lunch "evidence" in the office fridge, '
    "and now HR wants to know what crime I committed."
)


def main() -> None:
    # Gate self-check (mirrors the competition gate): UTF-8, 1-200 chars,
    # single line, not only whitespace.
    assert 1 <= len(JOKE) <= 200, f"joke length {len(JOKE)} outside 1-200"
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
