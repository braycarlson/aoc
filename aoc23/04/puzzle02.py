from __future__ import annotations

from collections import deque
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
    unique = deque(keys)

    while unique:
        card = unique.popleft()
        copies = count[card]

        for won in master[card]:
            if won not in master:
                count[won] = 0
                unique.append(won)

            count[won] = count[won] + copies

    total = count.values()
    total = sum(total)

    print(total)


if __name__ == '__main__':
    main()
