from __future__ import annotations

from pathlib import Path


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    with open(path, 'r') as handle:
        total = 0

        lines = handle.readlines()

        for line in lines:
            digit = [
                character for character in line
                if character.isdigit()
            ]

            string = digit[0] + digit[-1]
            calibration = int(string)

            total = total + calibration

    print(total)


if __name__ == '__main__':
    main()
