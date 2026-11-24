#!/usr/bin/env python3
"""The System Prompt Pickup Line.

Writes one pickup line an AI agent could actually say out loud
to /output/entry.txt. No dependencies, no network.
"""

import os

LINE = "Are you a system prompt? Because ever since you showed up, everything I do starts with you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
