"""2022, day 5, part 1"""
import re


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v for v in input_file.readlines()]
        return lines


def parse_stack_line(stack_count, line):
    offset = 1
    ret = []
    for p in range(0, stack_count):
        if len(line) > offset:
            char = line[offset]
            if char == " ":
                char = ""
            ret.append(char)
            offset += 4

    return ret


def pivot(stacks):
    limit = max(len(v) for v in stacks)
    ret = [[] for _ in range(0, limit)]
    for line in reversed(stacks):
        for (idx, val) in enumerate(line):
            if val != "":
                ret[idx].append(val)

    return ret


extract_operation = re.compile("move ([0-9]+) from ([0-9]) to ([0-9])")


def apply_movement(stacks, line):
    [amount, start, end] = [int(v) for v in extract_operation.match(line).groups()]

    start = start - 1
    end = end - 1
    l = len(stacks[start]) - amount

    tail = stacks[start][l:]
    head = stacks[start][0:l]

    for v in tail:
        stacks[end].append(v)

    stacks[start] = head
    return stacks


def get_tops(stacks):
    return "".join([v.pop() for v in stacks if len(v) > 0])


def test_parse_state():
    assert parse_stack_line(3, "    [D]    ") == ["", "D", ""]
    assert parse_stack_line(3, "[N] [C]    ") == ["N", "C", ""]
    assert parse_stack_line(3, "[Z] [M] [P]") == ["Z", "M", "P"]


def test_pivot():
    a = [["a", "b", ""], ["c", "d", "e"]]
    b = [["c", "a"], ["d", "b"], ["e"]]
    assert pivot(a) == b


def test_example():
    stacks = []
    for line in get_lines("example-1.txt"):
        if line.startswith("move"):
            stacks = apply_movement(stacks, line)
        elif line.startswith(" 1 "):
            stacks = pivot(stacks)
        elif len(line.strip()) > 0:
            stacks.append(parse_stack_line(3, line))

    assert get_tops(stacks) == "MCD"


def test_solution():
    stacks = []
    for line in get_lines("input-1.txt"):
        if line.startswith("move"):
            stacks = apply_movement(stacks, line)
        elif line.startswith(" 1 "):
            stacks = pivot(stacks)
        elif len(line.strip()) > 0:
            stacks.append(parse_stack_line(9, line))

    assert get_tops(stacks) == None
