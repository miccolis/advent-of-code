"""2022, day 4, part 2"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.rstrip() for v in input_file.readlines()]
        return lines


def parse_line(line):
    """Transform input into ranges"""
    return [[int(pos) for pos in v.split("-")] for v in line.split(",")]


def overlaps(parts):
    ret = parts[0][0] <= parts[1][1] and parts[0][1] >= parts[1][0]
    return ret


def test_example():
    count = 0

    for line in get_lines("example-1.txt"):
        [a, b] = parse_line(line)
        len_a = a[1] - a[0]
        len_b = b[1] - b[0]

        if len_a > len_b and overlaps([a, b]):
            count = count + 1
        elif overlaps([b, a]):
            count = count + 1

    assert count == 4


def test_solution():
    count = 0

    for line in get_lines("input-1.txt"):
        [a, b] = parse_line(line)
        len_a = a[1] - a[0]
        len_b = b[1] - b[0]

        if len_a > len_b and overlaps([a, b]):
            count = count + 1
        elif overlaps([b, a]):
            count = count + 1

    assert count == None
