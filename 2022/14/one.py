"""2022, day 14, part 1"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def parse_path(line):
    corners = line.split(" -> ")
    return [[int(vv) for vv in v.split(",")] for v in corners]


def test_parse_path():
    assert parse_path("498,4 -> 498,6 -> 496,6") == [[498, 4], [498, 6], [496, 6]]


def widen(cols, lim):
    for _ in range(len(cols), lim):
        cols.append([])
    return cols


def deepen(cols, x, y):
    for _ in range(len(cols[x]), y):
        cols[x].append(0)
    return cols


def extend(surface, x, y):
    if x + 1 > len(surface):
        surface = widen(surface, x + 1)

    if y + 1 > len(surface[x]):
        surface = deepen(surface, x, y + 1)

    return surface


def range_step(delta):
    if delta < 0:
        return -1
    return 1


def set_location(surface, x, y):
    surface = extend(surface, x, y)
    surface[x][y] = 1
    return surface


def build_surface(paths):
    surface = []
    for path in paths:
        [x, y] = path[0]

        for [c_x, c_y] in path[1:]:
            if x == c_x:
                y_diff = c_y - y
                step = range_step(y_diff)
                for y_delta in range(0, y_diff + step, step):
                    surface = set_location(surface, x, y + y_delta)
            else:
                x_diff = c_x - x
                step = range_step(x_diff)
                for x_delta in range(0, x_diff + step, step):
                    surface = set_location(surface, x + x_delta, y)

            y = c_y
            x = c_x

    return surface


def test_build_surface():
    assert build_surface([[[2, 2], [2, 4]]]) == [[], [], [0, 0, 1, 1, 1]]
    assert build_surface([[[2, 2], [4, 2]]]) == [
        [],
        [],
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1],
    ]


def print_surface(surface):
    depth = max([len(col) for col in surface])
    width = len(surface)
    print("")
    for y in range(0, depth):
        for x in range(0, width):
            if len(surface[x]) > y:
                char = "."
                if surface[x][y] == 1:
                    char = "#"
                elif surface[x][y] == 2:
                    char = "o"
                elif surface[x][y] == 3:
                    char = "+"
                print(char, end="")
            else:
                print(".", end="")
        print("")

    print("")


def drop_sand(surface, x, y):
    try:
        if surface[x][y + 1] == 0:
            return drop_sand(surface, x, y + 1)
        elif surface[x - 1][y + 1] == 0:
            return drop_sand(surface, x - 1, y + 1)
        elif surface[x + 1][y + 1] == 0:
            return drop_sand(surface, x + 1, y + 1)
        else:
            surface[x][y] = 2
            return True
    except IndexError:
        return False


def test_example():
    surface = build_surface([parse_path(v) for v in get_lines("example-1.txt")])
    surface[500][0] = 3
    # print_surface(surface[494:])

    units = 0
    while drop_sand(surface, 500, 0):
        units += 1

    # print_surface(surface[494:])
    assert units == 24


def test_solution():
    surface = build_surface([parse_path(v) for v in get_lines("input-1.txt")])
    surface[500][0] = 3

    units = 0
    while drop_sand(surface, 500, 0):
        units += 1

    # print_surface(surface[494:])
    assert units == 0
