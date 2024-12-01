from __future__ import annotations

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

        iterable = zip(
            sorted(first),
            sorted(second),
            strict=True
        )

        distances = [
            max(pair) - min(pair)
            for pair in iterable
        ]

        total = sum(distances)

        print(total)


if __name__ == '__main__':
    main()
