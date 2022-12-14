"""2022, day 12, part 1"""
from queue import Queue


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def get_height_value(char):
    if char == "S":
        return 1
    if char == "E":
        return ord("z") - 96

    return ord(char) - 96


def to_grid(rows):
    return [
        [
            {
                "char": v,
                "value": get_height_value(v),
                "dist": float("inf"),
                "visited": 0,
            }
            for v in row
        ]
        for row in rows
    ]


def get_start(grid):
    for y, row in enumerate(grid):
        for x, loc in enumerate(row):
            if loc["char"] == "S":
                return x, y


def debug_print(grid):
    print("---")
    for row in grid:
        print("")
        for v in row:
            print(f'{v["char"]}:{v["dist"]}', end=" ")


def depth_first_search(grid, x, y, dist):
    x_lim = len(grid[0])
    y_lim = len(grid)

    max_value = grid[y][x]["value"] + 1

    for d_x, d_y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        l_x = x + d_x
        l_y = y + d_y

        if 0 <= l_x < x_lim and 0 <= l_y < y_lim:
            local = grid[l_y][l_x]

            if local["value"] <= max_value and local["dist"] > dist:
                grid[l_y][l_x]["dist"] = dist + 1
                grid[l_y][l_x]["visited"] += 1

                if local["char"] == "E":
                    return dist + 1

                ret = depth_first_search(grid, l_x, l_y, dist + 1)
                if ret > -1:
                    return ret

    return -1


def breadth_first_search(grid, x, y, dist):
    x_lim = len(grid[0])
    y_lim = len(grid)

    grid[y][x]["dist"] = dist

    locations = Queue()
    locations.put((x, y))

    while not locations.empty():
        x, y = locations.get()
        local = grid[y][x]

        if local["char"] == "E":
            return local["dist"]

        max_value = local["value"] + 1

        for d_x, d_y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            l_x = x + d_x
            l_y = y + d_y

            if 0 <= l_x < x_lim and 0 <= l_y < y_lim:
                candidate = grid[l_y][l_x]
                if candidate["char"] == "x":
                    pass

                if (
                    candidate["value"] <= max_value
                    and candidate["dist"] > local["dist"] + 1
                ):
                    grid[l_y][l_x]["dist"] = local["dist"] + 1
                    grid[l_y][l_x]["visited"] += 1
                    locations.put((l_x, l_y))

    return -1


def test_example():
    grid = to_grid(get_lines("example-1.txt"))

    x, y = get_start(grid)
    grid[y][x]["dist"] = 0

    solution = breadth_first_search(grid, x, y, 0)

    assert solution == 31

    solution = depth_first_search(grid, x, y, 0)
    assert solution == 31


def test_solution():
    grid = to_grid(get_lines("input-1.txt"))

    x, y = get_start(grid)
    grid[y][x]["dist"] = 0

    solution = breadth_first_search(grid, x, y, 0)

    assert solution == 0
