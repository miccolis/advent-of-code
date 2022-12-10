"""2022, day 9, part 1"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def follow_instruction(direction, head_pos, tail_pos):
    if direction == "L":
        head_pos[0] -= 1
        if head_pos[0] - tail_pos[0] < -1:
            tail_pos[0] -= 1
            if head_pos[1] != tail_pos[1]:
                tail_pos[1] = head_pos[1]

    elif direction == "U":
        head_pos[1] += 1
        if head_pos[1] - tail_pos[1] > 1:
            tail_pos[1] += 1
            if head_pos[0] != tail_pos[0]:
                tail_pos[0] = head_pos[0]

    elif direction == "R":
        head_pos[0] += 1
        if head_pos[0] - tail_pos[0] > 1:
            tail_pos[0] += 1
            if head_pos[1] != tail_pos[1]:
                tail_pos[1] = head_pos[1]

    elif direction == "D":
        head_pos[1] -= 1
        if head_pos[1] - tail_pos[1] < -1:
            tail_pos[1] -= 1
            if head_pos[0] != tail_pos[0]:
                tail_pos[0] = head_pos[0]

    return head_pos, tail_pos


def test_follow_instruction():
    assert follow_instruction("L", [1, 0], [1, 0]) == ([0, 0], [1, 0])
    assert follow_instruction("L", [1, 0], [0, 0]) == ([0, 0], [0, 0])
    assert follow_instruction("L", [1, 0], [1, 1]) == ([0, 0], [1, 1])
    assert follow_instruction("L", [1, 0], [2, 1]) == ([0, 0], [1, 0])

    # assert follow_instruction("R", [0, 0], [0, 0]) == [1, 0]
    # assert follow_instruction("R", [0, 0], [0, 0]) == [1, 0]
    # assert follow_instruction("R", [0, 0], [0, 1]) == [1, 0]

    assert follow_instruction("U", [0, 1], [1, 0]) == ([0, 2], [0, 1])
    assert follow_instruction("U", [0, 1], [0, 1]) == ([0, 2], [0, 1])
    assert follow_instruction("U", [0, 1], [0, 2]) == ([0, 2], [0, 2])
    assert follow_instruction("U", [0, 1], [0, 0]) == ([0, 2], [0, 1])

    # assert follow_instruction("D", [0, 1], [1, 0]) == ([0, 0], [1, 0])
    # assert follow_instruction("D", [0, 1], [0, 1]) == ([0, 2], [0, 1])
    # assert follow_instruction("D", [0, 1], [0, 2]) == ([0, 2], [0, 2])
    assert follow_instruction("D", [1, 5], [2, 5]) == ([1, 4], [2, 5])


def test_example():
    head_pos = [0, 0]
    tail_positions = [[0, 0]]
    for line in get_lines("example-1.txt"):
        parts = line.split(" ")[0:2]
        d = parts[0]
        count = int(parts[1])
        print(line)
        for i in range(0, count):
            head_pos, tail_pos = follow_instruction(d, head_pos, tail_positions[-1])
            print([head_pos, tail_pos])
            tail_positions.append([v for v in tail_pos])

    print([f"{v[0]},{v[1]}" for v in tail_positions])
    solution = len(set([f"{v[0]},{v[1]}" for v in tail_positions]))
    assert solution == 13


def test_solution():
    head_pos = [0, 0]
    tail_positions = [[0, 0]]
    for line in get_lines("input-1.txt"):
        parts = line.split(" ")[0:2]
        d = parts[0]
        count = int(parts[1])
        print(line)
        for i in range(0, count):
            head_pos, tail_pos = follow_instruction(d, head_pos, tail_positions[-1])
            print([head_pos, tail_pos])
            tail_positions.append([v for v in tail_pos])

    print([f"{v[0]},{v[1]}" for v in tail_positions])
    solution = len(set([f"{v[0]},{v[1]}" for v in tail_positions]))
    assert solution == None
