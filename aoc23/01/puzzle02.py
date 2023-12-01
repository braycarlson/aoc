from __future__ import annotations

from pathlib import Path


STRING = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]


def find_calibration(line: str) -> int:
    length = len(line)

    integer_position = {
        index
        for index, character in enumerate(line)
        if character.isdigit()
    }

    string_position = {
        index
        for string in STRING
        if string in line
        for index in range(length)
        if line.startswith(string, index)
    }

    first_index = min(integer_position | string_position)
    last_index = max(integer_position | string_position)

    if first_index in integer_position:
        first_value = line[first_index]
    else:
        for string in STRING:
            if line.startswith(string, first_index):
                first_value = str(STRING.index(string) + 1)
                break

    if last_index in integer_position:
        last_value = line[last_index]
    else:
        for string in STRING:
            if line.startswith(string, last_index):
                last_value = str(STRING.index(string) + 1)
                break

    return int(first_value + last_value)


def main() -> None:
    path = Path.cwd().joinpath('input/input.txt')

    with open(path, 'r') as handle:
        total = 0

        lines = handle.readlines()

        for line in lines:
            calibration = find_calibration(line)
            total = total + calibration

    print(total)


if __name__ == '__main__':
    main()
