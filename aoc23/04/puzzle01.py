from __future__ import annotations

from pathlib import Path


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    total = 0

    with open(path, 'r') as handle:
        for line in handle:
            line = line.strip()

            _, cards = line.split(': ')
            left, right = cards.split(' | ')

            left, right = left.split(' '), right.split(' ')

            left = {
                int(number)
                for number in left
                if number.isdigit()
            }

            right = {
                int(number)
                for number in right
                if number.isdigit()
            }

            winning = right.intersection(left)

            if not winning:
                continue

            length = len(winning)

            total = (
                total + 1
                if length == 1
                else total + 2 ** (length - 1)
            )

    print(total)


if __name__ == '__main__':
    main()
