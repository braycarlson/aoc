from __future__ import annotations

from adjacency import find_adjacent
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
                if cell.isdigit() or cell == '.':
                    continue

                adjacent = find_adjacent(grid, i, j)
                total = total + sum(adjacent)

    print(total)


if __name__ == '__main__':
    main()
