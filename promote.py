#!/usr/bin/python3.13

from shutil import copytree
from itertools import pairwise
from pathlib import Path
from sys import argv


def main() -> None:
    rings = list(Path("rings").iterdir())
    for current, prev in pairwise(reversed(rings)):
        if not should_promote_from(prev):
            print(f"!!! Failed to promote from {prev.name} to {current.name}")
            continue
        copytree(prev, current, dirs_exist_ok=True)
        print(f"Promoted {prev.name} to {current.name}")


def should_promote_from(ring: Path) -> bool:
    fail_in_ring = ""
    if len(argv) > 1:
        fail_in_ring = argv[1]

    return ring.name != fail_in_ring

if __name__ == "__main__":
    main()
