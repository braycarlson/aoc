from __future__ import annotations

from almanac import generate
from pathlib import Path


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    with open(path, 'r') as handle:
        seeds, almanac = generate(handle)

    location = []

    for seed in seeds:
        for sections in almanac.values():
            for section in sections:
                destination, source, length = section

                if source <= seed < (source + length):
                    seed = seed - source + destination
                    break

        location.append(seed)

    minimum = min(location)
    print(minimum)


if __name__ == '__main__':
    main()
