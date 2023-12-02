from __future__ import annotations

from math import prod
from pathlib import Path


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    history = {}

    table = str.maketrans(';', '\n')

    with open(path, 'r') as handle:
        for index, line in enumerate(handle, 1):
            cut = len(f"Game {index}:")

            line = line.strip()
            line = line[cut:]

            games = line.translate(table).split('\n')

            history[index] = {'red': 0, 'green': 0, 'blue': 0}

            for game in games:
                cubes = game.split(', ')

                for cube in cubes:
                    amount, color = cube.strip().split(' ')
                    amount = int(amount)

                    if amount > history[index][color]:
                        history[index][color] = amount

    total = sum(
        prod(power.values())
        for power in history.values()
    )

    print(total)


if __name__ == '__main__':
    main()
