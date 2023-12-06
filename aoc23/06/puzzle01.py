from __future__ import annotations

from math import prod
from pathlib import Path


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    with open(path, 'r') as handle:
        text = handle.read().split()

        information = [
            int(x)
            for x in text
            if x.isdigit()
        ]

        middle = len(information) // 2

        races = [
            (information[i], information[middle + i])
            for i in range(middle)
        ]

        error = []

        for race in races:
            time, distance = race

            winnable = 0

            for millisecond in range(0, time, 1):
                potential = 0 if millisecond == 0 else (time - millisecond)
                forward = 0 if millisecond == time - 1 else (potential * millisecond)

                if forward > distance:
                    winnable = winnable + 1

            error.append(winnable)

        total = prod(error)
        print(total)


if __name__ == '__main__':
    main()
