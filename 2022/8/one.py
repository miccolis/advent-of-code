"""2022, day 8, part 1"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def visibility_scan(row):
    ret = set()
    ret.add(0)
    ret.add(len(row) - 1)
    hw = row[0]
    for idx, val in enumerate(row):
        if val > hw:
            ret.add(idx)
            hw = val

    hw = row[-1]
    for idx, val in reversed(list(enumerate(row))):
        if val > hw:
            ret.add(idx)
            hw = val

    return ret


def test_visibility_scan():
    assert visibility_scan([5, 1, 1, 5]) == set([0, 3])
    assert visibility_scan([5, 7, 1, 5]) == set([0, 1, 3])
    assert visibility_scan([5, 7, 6, 5]) == set([0, 1, 2, 3])


def test_example():
    rows = []
    for line in get_lines("example-1.txt"):
        rows.append([int(v) for v in line])

    max_y = len(rows)
    max_x = len(rows[0])

    visible = []
    for y in range(0, max_y):
        visible.append(visibility_scan(rows[y]))

    for x in range(0, max_x):
        for idx in visibility_scan([v[x] for v in rows]):
            visible[idx].add(x)

    solution = sum([len(v) for v in visible])
    assert solution == 21


def test_solution():
    rows = []
    for line in get_lines("input-1.txt"):
        rows.append([int(v) for v in line])

    max_y = len(rows)
    max_x = len(rows[0])

    visible = []
    for y in range(0, max_y):
        visible.append(visibility_scan(rows[y]))

    for x in range(0, max_x):
        for idx in visibility_scan([v[x] for v in rows]):
            visible[idx].add(x)

    solution = sum([len(v) for v in visible])
    assert solution == None
