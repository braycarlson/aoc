from __future__ import annotations

from almanac import generate
from pathlib import Path


def transform(
    ranges: list[tuple[int, int]],
    almanac: dict[str, list[list[int, int, int]]]
) -> list[tuple[int, int]]:
    transformed = []

    for interval_start, interval_end in ranges:
        is_transformed = False

        for destination_start, source_start, length in almanac:
            source_end = source_start + length

            if source_start <= interval_start < source_end:
                minimum = min(interval_end, source_end) - interval_start

                transform_start = destination_start + (interval_start - source_start)
                transform_end = transform_start + minimum

                pair = (transform_start, transform_end)
                transformed.append(pair)

                if interval_end > source_end:
                    pair = (source_end, interval_end)
                    transformed = transformed + transform([pair], almanac)

                is_transformed = True
                break

        if not is_transformed:
            pair = (interval_start, interval_end)
            transformed.append(pair)

    return transformed


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    with open(path, 'r') as handle:
        seeds, almanac = generate(handle)

    length = len(seeds)

    interval = [
        (seeds[i], seeds[i] + seeds[i + 1])
        for i in range(0, length, 2)
    ]

    for transformation in almanac:
        interval = transform(
            interval,
            almanac[transformation]
        )

    minimum = min(start for start, _ in interval)
    print(minimum)


if __name__ == '__main__':
    main()
