"""2022, day 8, part 2"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def hw_test(hw, val):
    if val > hw:
        return val
    else:
        return hw


def visibility_scan(rows, pos):
    x = pos[0]
    y = pos[1]

    max_y = len(rows) - 1
    max_x = len(rows[0]) - 1

    hw = rows[y][x]

    # top
    cnt = 0
    for i in reversed(range(0, y)):
        y_loc = i
        # print(f"{x},{y_loc} T {rows[y_loc][x]}")
        if rows[y_loc][x] < hw:
            cnt += 1
        else:
            cnt += 1
            break
    # print(f"T {cnt}")
    top_score = cnt

    # right
    cnt = 0
    for i in range(x, max_x):
        x_loc = i + 1
        # print(f"{x_loc},{y} R {rows[y][x_loc]}")
        if rows[y][x_loc] < hw:
            cnt += 1
        else:
            cnt += 1
            break

    # print(f"R {cnt}")
    right_score = cnt

    # bottom
    cnt = 0
    for i in range(y, max_y):
        y_loc = i + 1
        # print(f"{x},{y_loc} B {rows[y_loc][x]}")
        if rows[y_loc][x] < hw:
            cnt += 1
        else:
            cnt += 1
            break

    # print(f"B {cnt}")
    bottom_score = cnt

    # left
    cnt = 0
    for i in reversed(range(0, x)):
        x_loc = i
        # print(f"{x_loc},{y} L {rows[y][x_loc]}")
        if rows[y][x_loc] < hw:
            cnt += 1
        else:
            cnt += 1
            break

    # print(f"L {cnt}")
    left_score = cnt

    # print([top_score, right_score, bottom_score, left_score])
    return top_score * right_score * bottom_score * left_score


def test_visibility_scan():
    # assert visibility_scan([[3, 4, 1, 2]], [2, 0]) == 0
    # assert visibility_scan([[3], [4], [1], [2]], [0, 2]) == 0

    rows = []
    for line in get_lines("example-1.txt"):
        rows.append([int(v) for v in line])

    assert visibility_scan(rows, [2, 1]) == 4
    assert visibility_scan(rows, [2, 3]) == 8


def test_example():
    rows = []
    for line in get_lines("example-1.txt"):
        rows.append([int(v) for v in line])

    hw = 0
    max_y = len(rows) - 1
    max_x = len(rows[0]) - 1
    for y in range(0, max_y):
        for x in range(0, max_x):
            score = visibility_scan(rows, [x, y])
            # print([x, y, score])
            if score > hw:
                hw = score

    assert hw == 8


def test_solution():
    rows = []
    for line in get_lines("input-1.txt"):
        rows.append([int(v) for v in line])

    hw = 0
    max_y = len(rows) - 1
    max_x = len(rows[0]) - 1
    for y in range(0, max_y):
        for x in range(0, max_x):
            score = visibility_scan(rows, [x, y])
            # print([x, y, score])
            if score > hw:
                hw = score

    assert hw == None
