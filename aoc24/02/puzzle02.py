from __future__ import annotations

from itertools import pairwise
from pathlib import Path


def is_valid(report: list[int]) -> bool:
    is_increasing_or_decreasing = (
        report == sorted(report) or
        report == sorted(report, reverse=True)
    )

    is_in_adjacent_range = all(
        1 <= max(pair) - min(pair) <= 3
        for pair in pairwise(report)
    )

    return (
        is_increasing_or_decreasing and
        is_in_adjacent_range
    )


def is_valid_or_saveable(report: list[int]) -> bool:
    length = len(report)

    return is_valid(report) or any(
        is_valid(report[:i] + report[i+1:])
        for i in range(length)
    )


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    with open(path, 'r', encoding='utf-8') as handle:
        lines = handle.read().splitlines()

        reports = [
            [int(number) for number in line.split()]
            for line in lines
        ]

        safe = [
            is_valid_or_saveable(report)
            for report in reports
        ]

        total = sum(safe)
        print(total)


if __name__ == '__main__':
    main()
