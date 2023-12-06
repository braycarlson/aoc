from __future__ import annotations

from itertools import groupby
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from io import TextIOWrapper


def generate(handle: TextIOWrapper) -> tuple[list[int], dict[str, list[list[int]]]]:
    text = handle.read().split('\n')
    seeds = text.pop(0).split()

    seeds = [
        int(seed)
        for seed in seeds
        if seed.isdigit()
    ]

    section = [
        list(y)
        for x, y in groupby(text, lambda z: z == '')
        if not x
    ]

    almanac = {
        item[0][:-5]: [
            [int(x) for x in s.split()]
            for s in item[1:]
        ]
        for item in section
    }

    return seeds, almanac

