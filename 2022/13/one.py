"""2022, day 13, part 1"""
from json import loads


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def make_pairs(lines):
    pairs = []
    current = []
    for line in lines:
        if len(line) == 0:
            pass
        elif len(current) == 0:
            current.append(loads(line))
        elif len(current) == 1:
            current.append(loads(line))
            pairs.append(current)
            current = []

    return pairs


SAME = -1
CORRECT = 0
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
    assert compare(0, 0) == -1
    assert compare(1, 0) == WRONG
    assert compare(0, 1) == 0
    assert compare([], []) == 0
    assert compare([0], [1]) == 0
    assert compare([1], [0]) == 1
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
    paris = make_pairs(get_lines("example-1.txt"))
    correct = []
    for idx, pair in enumerate(paris):
        if compare(pair[0], pair[1]) == CORRECT:
            correct.append(idx + 1)

    assert sum(correct) == 13


def test_solution():
    paris = make_pairs(get_lines("input-1.txt"))
    correct = []
    for idx, pair in enumerate(paris):
        if compare(pair[0], pair[1]) == CORRECT:
            correct.append(idx + 1)

    assert sum(correct) == None
