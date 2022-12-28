"""2022, day 15, part 1"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def second_as_int(v):
    return [v[0], int(v[1])]


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def test_manhattan_distance():
    assert manhattan_distance([0, 0], [4, 4]) == 8
    assert manhattan_distance([-4, -4], [4, 4]) == 16


def parse_line(line):
    parts = line.split(" ")

    parsed = [
        int(v.split("=")[1])
        for v in [
            parts[2].strip(","),
            parts[3].strip(":"),
            parts[8].strip(","),
            parts[9],
        ]
    ]

    return [parsed[0:2], manhattan_distance(parsed[0:2], parsed[2:4])]


def test_parse_line():
    assert parse_line("Sensor at x=2, y=18: closest beacon is at x=-2, y=15") == [
        [2, 18],
        7,
    ]


def in_range(beacon, row):
    [x, y], dist = beacon
    if y + dist > row > y - dist:
        return True
    return False


def test_example():
    test_row = 10
    beacons = [parse_line(v) for v in get_lines("example-1.txt")]

    min_x = 0
    max_x = 0
    ranges = []
    for beacon in beacons:
        if in_range(beacon, test_row):
            [x, y], dist = beacon
            delta = abs(test_row - y)

            reach = dist - delta

            local_max = x + reach
            if local_max > max_x:
                max_x = local_max

            local_min = x - reach
            if local_min < min_x:
                min_x = local_min
            ranges.append([local_min, local_max])

    count = 0

    print(ranges)
    for i in range(min_x, max_x):
        for start, end in ranges:
            if start <= i <= end:
                count += 1
                break

    assert count == 26


def test_solution():
    test_row = 2000000
    beacons = [parse_line(v) for v in get_lines("input-1.txt")]

    min_x = 0
    max_x = 0
    ranges = []
    for beacon in beacons:
        if in_range(beacon, test_row):
            [x, y], dist = beacon
            delta = abs(test_row - y)

            reach = dist - delta

            local_max = x + reach
            if local_max > max_x:
                max_x = local_max

            local_min = x - reach
            if local_min < min_x:
                min_x = local_min
            ranges.append([local_min, local_max])

    count = 0

    print(ranges)
    for i in range(min_x, max_x):
        for start, end in ranges:
            if start <= i <= end:
                count += 1
                break

    assert count == 0
