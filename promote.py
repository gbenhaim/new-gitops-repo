#!/usr/bin/python3.13

from shutil import copytree
from itertools import pairwise
from pathlib import Path

def main() -> None:
    rings = list(Path("rings").iterdir())
    for current, prev in pairwise(reversed(rings)):
        copytree(prev, current, dirs_exist_ok=True)
        print(f"Promoted {prev} to {current}")

if __name__ == "__main__":
    main()