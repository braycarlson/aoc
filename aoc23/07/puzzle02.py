from __future__ import annotations

from collections import Counter
from itertools import groupby
from pathlib import Path


FACE = {
    'J': 1,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14,
}


def main() -> None:
    path = Path.cwd().joinpath('input/sample.txt')

    with open(path, 'r') as handle:
        text = handle.read().split()

        iterable = zip(text[::2], text[1::2], strict=True)
        pair = list(iterable)

        pair = {
                tuple(
                    FACE[character]
                    if character in FACE
                    else int(character)
                    for character in x
                ):
                int(y)
            for x, y in pair
        }

        mapping = {
            tuple(k): tuple(
                sorted(
                    Counter(k).values(),
                    reverse=True
                )
            )
            for k, v in pair.items()
        }

        groups = {
            key: sorted(
                (item[0] for item in group),
                key=lambda x: x
            )
            for key, group in groupby(
                sorted(mapping.items(), key=lambda item: item[1]),
                key=lambda item: item[1]
            )
        }

        total = 0
        i = 1

        for group in groups.values():
            for hand in group:
                bid = pair[hand]
                total = total + (int(bid) * i)

                i = i + 1

        print(total)


if __name__ == '__main__':
    main()
