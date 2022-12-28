"""2022, day 15, part 2"""


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


def test_example_brute_force():
    beacons = [parse_line(v) for v in get_lines("example-1.txt")]

    count = 0
    solution = 0

    for test_row in range(0, 20):
        ranges = []
        for beacon in beacons:
            if in_range(beacon, test_row):
                [x, y], dist = beacon
                delta = abs(test_row - y)
                reach = dist - delta
                local_max = x + reach
                local_min = x - reach
                ranges.append([local_min, local_max])

        for test_col in range(0, 20):
            allowed = True

            for span in ranges:
                start, end = span

                if start <= test_col <= end:
                    allowed = False
                    break

            if allowed:
                count += 1
                solution = test_col * 4000000 + test_row
                break

    assert count == 1
    assert solution == 56000011


def test_example():
    beacons = [parse_line(v) for v in get_lines("example-1.txt")]

    solution = 0

    for test_row in range(0, 20):
        ranges = []
        for beacon in beacons:
            if in_range(beacon, test_row):
                [x, y], dist = beacon
                delta = abs(test_row - y)
                reach = dist - delta
                local_max = x + reach
                local_min = x - reach
                if local_min < 0:
                    local_min = 0
                ranges.append([local_min, local_max])

        ranges.sort(key=lambda v: v[0])

        covered = [0, 0]

        for span in ranges:
            if covered[0] <= span[0] <= covered[1]:
                if covered[0] <= span[1] <= covered[1]:
                    # fully contained in known coverage, continue
                    continue
                elif span[1] > covered[1]:
                    # Extends coverage
                    covered[1] = span[1]
                    continue
            if span[1] + 1 == span[0]:
                # Immediatly adjacent, expand coverage
                covered[1] = span[1]
            else:
                print(["solution", span[0] - 1, test_row])
                solution = (span[0] - 1) * 4000000 + test_row
                break

        if solution != 0:
            break

    assert solution == 56000011


def test_solution():
    beacons = [parse_line(v) for v in get_lines("input-1.txt")]

    solution = 0

    for test_row in range(0, 4000000):
        ranges = []
        for beacon in beacons:
            if in_range(beacon, test_row):
                [x, y], dist = beacon
                delta = abs(test_row - y)
                reach = dist - delta
                local_max = x + reach
                local_min = x - reach
                if local_min < 0:
                    local_min = 0
                ranges.append([local_min, local_max])

        ranges.sort(key=lambda v: v[0])

        covered = [0, 0]

        for span in ranges:
            if covered[0] <= span[0] <= covered[1]:
                if covered[0] <= span[1] <= covered[1]:
                    # fully contained in known coverage, continue
                    continue
                elif span[1] > covered[1]:
                    # Extends coverage
                    covered[1] = span[1]
                    continue
            if span[1] + 1 == span[0]:
                # Immediatly adjacent, expand coverage
                covered[1] = span[1]
            else:
                print(["solution", span[0] - 1, test_row])
                solution = (span[0] - 1) * 4000000 + test_row
                break

        if solution != 0:
            break

    assert solution == 0
