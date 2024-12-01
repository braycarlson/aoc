from __future__ import annotations

import math

from pathlib import Path


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    with open(path, 'r', encoding='utf-8') as handle:
        file = handle.read().split()

        first = [
            int(line)
            for index, line in enumerate(file)
            if index % 2 == 0
        ]

        second = [
            int(line)
            for index, line in enumerate(file)
            if index % 2 == 1
        ]

        similarity = sum([
            math.prod([element, second.count(element)])
            for element in first
        ])

        print(similarity)


if __name__ == '__main__':
    main()
