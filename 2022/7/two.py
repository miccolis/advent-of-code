"""2022, day 7, part 2"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def eval_command(line, pos, tree):
    if line == "$ cd /":
        pos = tree
    elif line.startswith("$ cd"):
        target = line[4:].strip()
        if target == "..":
            if not pos[2] is None:
                pos = pos[2]
        elif target in pos[1]:
            pos = pos[1][target]
    elif line.startswith("$ ls"):
        pos[0] = 0  # reset in case thing run twice
        return False, pos
    else:
        print(f"Ignoring unknown command ${line}")

    return True, pos


def test_eval_command():
    root = [0, {}, None]
    mode, pos = eval_command("$ cd /", None, root)
    assert mode is True
    assert pos == root

    root = [0, {}, None]
    root[1]["a"] = [0, {}, root]
    mode, pos = eval_command("$ cd ..", root[1]["a"], root)
    assert mode is True
    assert pos == root

    root = [5, {}, None]
    mode, pos = eval_command("$ ls", root, root)
    assert mode is False
    assert pos == [0, {}, None]


def parse_response(line, pos):
    if line.startswith("$"):
        return True

    if line.startswith("dir"):
        dirname = line[4:]
        if not dirname in pos[1]:
            pos[1][dirname] = [0, {}, pos]
    else:
        [size, _] = line.split(" ")
        # print(size, _)
        pos[0] += int(size)

    return False


def test_parse_response():
    assert parse_response("$ cd a", None) is True

    state = [0, {}, None]
    assert parse_response("dir a", state) is False
    assert state[1]["a"][0] == 0
    assert state[1]["a"][1] == {}
    assert state[1]["a"][2] == state

    state = [0, {}, None]
    assert parse_response("123 foo", state) is False
    assert state == [123, {}, None]


# def sum_files(tree, solution):
#     for key, val in tree[1].items():
#         if len(val[1]) > 0:
#             solution = sum_files(val, solution, depth + 1)
#
#         tree[0] += val[0]
#
#     if tree[0] < 100000:
#         solution += tree[0]
#
#     return solution


def sum_files(tree):
    if len(tree[1]) == 0:
        return tree[0]

    for key, branch in tree[1].items():
        tree[0] += sum_files(branch)

    return tree[0]


def solve(tree, lim, solution):
    if tree[0] >= lim:
        solution.append(tree[0])

    for key, branch in tree[1].items():
        solution = solve(branch, lim, solution)

    return solution


def recur_print(tree, depth):
    padding = " " * depth
    print(f"{padding}{tree[0]}")

    for key, branch in tree[1].items():
        recur_print(branch, depth + 1)


def test_example():
    tree = [0, {}, None]  # size, child_dirs, parent
    pos = tree
    command_mode = True
    for line in get_lines("example-1.txt"):
        if command_mode is False:
            command_mode = parse_response(line, pos)

        if command_mode is True:
            command_mode, pos = eval_command(line, pos, tree)

    sum_files(tree)
    # recur_print(tree, 0)

    free = 70000000 - tree[0]
    needed = 30000000 - free

    solution = min(solve(tree, needed, []))

    assert solution == 24933642


def test_solution():
    tree = [0, {}, None]  # size, child_dirs, parent
    pos = tree
    command_mode = True
    for line in get_lines("input-1.txt"):
        if command_mode is False:
            command_mode = parse_response(line, pos)

        if command_mode is True:
            command_mode, pos = eval_command(line, pos, tree)

    sum_files(tree)
    # recur_print(tree, 0)

    free = 70000000 - tree[0]
    needed = 30000000 - free

    solution = min(solve(tree, needed, []))

    assert solution == None
