from __future__ import annotations

from pathlib import Path


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    master = {}

    with open(path, 'r') as handle:
        for index, line in enumerate(handle, 1):
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
            length = len(winning)

            collection = range(index + 1, index + length + 1)
            master[index] = list(collection)

    count = {
        card: 1
        for card in master
    }

    keys = master.keys()

    for key in keys:
        copies = count[key]

        for won in master[key]:
            count[won] = count[won] + copies

    total = count.values()
    total = sum(total)

    print(total)


if __name__ == '__main__':
    main()
