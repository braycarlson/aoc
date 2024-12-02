from __future__ import annotations

from itertools import pairwise
from pathlib import Path


def is_valid(level: list[int]) -> bool:
    is_increasing_or_decreasing = (
        level == sorted(level) or
        level == sorted(level, reverse=True)
    )

    is_unique = (len(level) - len(set(level))) <= 1

    pairwises = list(pairwise(level))

    is_in_adjacent_range = (
        len(pairwises) - sum(
            [1 <= max(pair) - min(pair) <= 3 for pair in pairwises]
        ) <= 1
    )

    return (
        is_increasing_or_decreasing and
        is_unique and
        is_in_adjacent_range
    )


def main() -> None:
    path = Path.cwd().joinpath('input/sample.txt')

    with open(path, 'r', encoding='utf-8') as handle:
        lines = handle.read().splitlines()

        levels = [
            [int(number) for number in line.split()]
            for line in lines
        ]

        safe = [is_valid(level) for level in levels]
        total = sum(safe)

        print(total)


if __name__ == '__main__':
    main()
