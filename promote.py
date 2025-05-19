#!/usr/bin/python3.13

from shutil import copytree
from itertools import pairwise
from pathlib import Path
from sys import argv

def main() -> None:
    fail_in_ring = ""
    if len(argv) > 1:
        fail_in_ring = argv[1]

    rings = list(Path("rings").iterdir())
    for current, prev in pairwise(reversed(rings)):
        if fail_in_ring == prev.name:
            print(f"!!! Failed to promote from {prev} to {current}")
            continue
        copytree(prev, current, dirs_exist_ok=True)
        print(f"Promoted {prev} to {current}")

if __name__ == "__main__":
    main()
