def is_in_bound(grid: list[str], x: int, y: int) -> bool:
    return (
        0 <= x < len(grid) and
        0 <= y < len(grid[0])
    )


def find_adjacent(grid: list[str], i: int, j: int) -> set[int]:
    adjacent = set()

    direction = [
        (dx, dy) for dx in range(-1, 2)
        for dy in range(-1, 2)
    ]

    for delta_x, delta_y in direction:
        neighbour_x = i + delta_x
        neighbour_y = j + delta_y

        condition = (
            is_in_bound(grid, neighbour_x, neighbour_y) and
            grid[neighbour_x][neighbour_y].isdigit()
        )

        if condition:
            number = grid[neighbour_x][neighbour_y]

            left = neighbour_y - 1

            while is_in_bound(grid, neighbour_x, left) and grid[neighbour_x][left].isdigit():
                number = grid[neighbour_x][left] + number
                left = left - 1

            right = neighbour_y + 1

            while is_in_bound(grid, neighbour_x, right) and grid[neighbour_x][right].isdigit():
                number = number + grid[neighbour_x][right]
                right = right + 1

            number = int(number)
            adjacent.add(number)

    return adjacent
