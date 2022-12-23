"""2022, day 13, part 2"""
from json import loads
from functools import cmp_to_key


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def make_packets(lines):
    current = []
    for line in lines:
        if len(line) == 0:
            pass
        else:
            current.append(loads(line))

    return current


SAME = 0
CORRECT = -1
WRONG = 1


def compare(a, b):
    a_type = type(a)
    b_type = type(b)

    if a_type == b_type:
        if a_type == int:
            if a == b:
                return SAME

            if a < b:
                return CORRECT

            return WRONG
        if a_type == list:
            a_len = len(a)
            b_len = len(b)
            b_lim = b_len - 1
            for i in range(0, a_len):
                if i > b_lim:
                    return WRONG
                cmp = compare(a[i], b[i])
                if cmp != SAME:
                    return cmp

            return CORRECT

    if a_type == int:
        return compare([a], b)

    if b_type == int:
        return compare(a, [b])

    return CORRECT


def test_compare():
    assert compare(0, 0) == SAME
    assert compare(1, 0) == WRONG
    assert compare(0, 1) == CORRECT
    assert compare([], []) == CORRECT
    assert compare([0], [1]) == CORRECT
    assert compare([1], [0]) == WRONG
    assert compare([1], []) == WRONG
    assert compare([], [1]) == CORRECT
    assert compare([1, 1, 3, 1, 1], [1, 1, 5, 1, 1]) == CORRECT
    assert compare([[1], [2, 3, 4]], [[1], 4]) == CORRECT
    assert compare(9, 8) == WRONG
    assert compare([9], [8, 7, 6]) == WRONG
    assert compare([9], [[8, 7, 6]]) == WRONG
    assert compare([[4, 4], 4, 4], [[4, 4], 4, 4, 4]) == CORRECT
    assert compare([7, 7, 7, 7], [7, 7, 7]) == WRONG
    assert compare([[[]]], [[]]) == WRONG
    assert (
        compare(
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
        )
        == WRONG
    )


def test_examples():
    packets = make_packets(get_lines("example-1.txt"))
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare))
    decoders = []
    for idx, v in enumerate(packets):
        print(v)
        if type(v) == list and len(v) == 1:
            if type(v[0]) == list and len(v[0]) == 1:
                if v[0][0] == 2 or v[0][0] == 6:
                    decoders.append(idx + 1)

    assert decoders[0] * decoders[1] == 140


def test_solution():
    packets = make_packets(get_lines("input-1.txt"))
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(compare))
    decoders = []
    for idx, v in enumerate(packets):
        if type(v) == list and len(v) == 1:
            if type(v[0]) == list and len(v[0]) == 1:
                if v[0][0] == 2 or v[0][0] == 6:
                    decoders.append(idx + 1)

    solution = decoders[0] * decoders[1]
    assert solution == 0
