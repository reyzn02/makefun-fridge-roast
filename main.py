#!/usr/bin/env python3
"""Fridge Roast: one line roasting a smart fridge.

The program writes a single line, at most 200 characters, to
/output/entry.txt. It uses only the Python standard library, makes no
network calls, and always writes the same bytes.
"""

import os

LINE = (
    "My smart fridge needs a software update to open the door, "
    "but still can't update its opinion that my 2 a.m. leftovers "
    "are a cry for help."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
