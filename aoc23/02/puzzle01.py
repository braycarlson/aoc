from __future__ import annotations

from collections import deque
from pathlib import Path


CONFIGURATION = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    table = str.maketrans(
        '',
        '',
        ';:,'
    )

    with open(path, 'r') as handle:
        game = {}

        for i, line in enumerate(handle, 1):
            game[i] = []

            line = deque(
                line
                .strip()
                .translate(table)
                .split(' ')
            )

            line.popleft()
            line.popleft()

            for j in range(0, len(line), 2):
                amount = line[j]
                amount = int(amount)

                color = line[j + 1]
                limit = CONFIGURATION[color]

                game[i].append(amount <= limit)

        valid = [
            k
            for k, v in game.items()
            if all(valid is True for valid in v)
        ]

        total = sum(valid)
        print(total)


if __name__ == '__main__':
    main()
