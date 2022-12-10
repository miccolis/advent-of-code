"""2022, day 9, part 2"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def follow_instruction(direction, head_pos):
    if direction == "L":
        head_pos[0] -= 1
    elif direction == "U":
        head_pos[1] += 1
    elif direction == "R":
        head_pos[0] += 1
    elif direction == "D":
        head_pos[1] -= 1

    return head_pos


def update_segment(head_pos, tail_pos):
    dx = head_pos[0] - tail_pos[0]
    dy = head_pos[1] - tail_pos[1]
    if dx < -1:
        tail_pos[0] -= 1
        if dy > 0:
            tail_pos[1] += 1
        if dy < 0:
            tail_pos[1] -= 1

    elif dx > 1:
        tail_pos[0] += 1
        if dy > 0:
            tail_pos[1] += 1
        if dy < 0:
            tail_pos[1] -= 1

    elif dy > 1:
        tail_pos[1] += 1
        if dx > 0:
            tail_pos[0] += 1
        if dx < 0:
            tail_pos[0] -= 1

    elif dy < -1:
        tail_pos[1] -= 1
        if dx > 0:
            tail_pos[0] += 1
        if dx < 0:
            tail_pos[0] -= 1

    return tail_pos


def test_update_segment():
    assert update_segment([1, 1], [1, 1]) == [1, 1]
    assert update_segment([0, 1], [0, 0]) == [0, 0]
    assert update_segment([1, 0], [0, 0]) == [0, 0]
    assert update_segment([2, 0], [0, 0]) == [1, 0]
    assert update_segment([0, 2], [0, 0]) == [0, 1]
    assert update_segment([0, 2], [0, 0]) == [0, 1]

    assert update_segment([1, 0], [0, 0]) == [0, 0]
    assert update_segment([1, 1], [0, 0]) == [0, 0]
    assert update_segment([1, 2], [0, 0]) == [1, 1]


def debug_print(line, positions):
    print("")
    print("-" * 26)
    print("")
    print(line)
    print("")

    for y_idx in range(0, 21):
        y = abs(y_idx - 21) - 6
        for x_idx in range(0, 26):
            x = x_idx - 11
            pos = [i for i, v in enumerate(positions) if v[0] == x and v[1] == y]

            if len(pos) == 0:
                print(".", end="")
            elif x == 0 and y == 0:
                print("s", end="")
            else:
                output_char = "#"
                if len(positions) <= 10:
                    output_char = pos[0]
                if output_char == 0:
                    output_char = "H"

                print(output_char, end="")
        print("")


def solve(positions, lines):
    tail_positions = [[0, 0]]
    # debug_print("initial", positions)

    for line in lines:
        parts = line.split(" ")[0:2]
        d = parts[0]
        count = int(parts[1])
        for i in range(0, count):
            positions[0] = follow_instruction(d, positions[0])
            for j in range(1, len(positions)):
                positions[j] = update_segment(positions[j - 1], positions[j])

            tail_positions.append([v for v in positions[-1]])

        # debug_print(line, positions)

    # debug_print("Tail positions", tail_positions)
    # print([f"{v[0]},{v[1]}" for v in tail_positions])
    return len(set([f"{v[0]},{v[1]}" for v in tail_positions]))


def test_example_one():
    positions = [[0, 0] for _ in range(0, 10)]
    solution = solve(positions, get_lines("example-1.txt"))
    assert solution == 1


def test_example_two():
    positions = [[0, 0] for _ in range(0, 10)]
    solution = solve(positions, get_lines("example-2.txt"))
    assert solution == 36


def test_solution():
    positions = [[0, 0] for _ in range(0, 10)]
    solution = solve(positions, get_lines("input-1.txt"))
    assert solution == None
