from __future__ import annotations

from adjacency import find_adjacent
from math import prod
from pathlib import Path


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    with open(path, 'r') as handle:
        grid = [
            line.strip()
            for line in handle
        ]

        total = 0

        for i, row in enumerate(grid, 0):
            for j, cell in enumerate(row, 0):
                if cell.isdigit() or cell == '.' or cell != '*':
                    continue

                adjacent = find_adjacent(grid, i, j)

                if len(adjacent) == 2:
                    product = prod(adjacent)
                    total = total + product

    print(total)


if __name__ == '__main__':
    main()
