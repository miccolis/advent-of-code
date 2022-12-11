"""2022 Day 10, part 2"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def runner(lines):
    x_vals = [1]
    commands = ["INITIAL"]
    for line in lines:
        if line == "noop":
            x_vals.append(x_vals[-1])
            commands.append(line)
        else:
            instruction, value = line.split(" ")
            x_vals.append(x_vals[-1])
            commands.append(f"{line} (1)")
            x_vals.append(x_vals[-1] + int(value))
            commands.append(f"{line} (2)")

    return x_vals, commands


def test_example():
    lines = ["noop", "addx 3", "addx -5"]
    values, _ = runner(lines)

    assert values[-1] == -1
    assert len(values) == 6


def test_longer_example():
    values, commands = runner(get_lines("example-1.txt"))

    # for ln, val in enumerate(values):
    #     print(f"{ln}: {commands[ln]} -> {val}")

    assert 20 * values[20 - 1] == 420
    assert 60 * values[60 - 1] == 1140
    assert 100 * values[100 - 1] == 1800
    assert 140 * values[140 - 1] == 2940
    assert 180 * values[180 - 1] == 2880
    assert 220 * values[220 - 1] == 3960

    solution = 0
    for cycle in range(20, 221, 40):
        solution += values[cycle - 1] * cycle

    assert solution == 13140


def test_solution():
    values, commands = runner(get_lines("input-1.txt"))

    solution = 0
    for cycle in range(20, 221, 40):
        solution += values[cycle - 1] * cycle

    assert solution == None
