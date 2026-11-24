#!/usr/bin/env python3
"""One-line loading-screen tip for make.fun."""

# The tip is the turn: the build isn't stuck, it's thinking — and the
# developer, unlike the code, is still there after a glass of water.

import os

TIP = "Loading tip: the build isn't stuck, it's thinking. Go drink water — the error will still be there when you get back, and unlike your code, so will you."


def file_tip() -> None:
    """Write the tip to /output/entry.txt, nothing else."""
    if len(TIP) > 200 or not TIP.strip() or "\n" in TIP:
        raise ValueError("tip must be a single non-empty line of at most 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(TIP)


if __name__ == "__main__":  # run it
    file_tip()
