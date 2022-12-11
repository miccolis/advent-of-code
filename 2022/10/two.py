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


values, commands = runner(get_lines("input-1.txt"))

for i in range(1, 6):
    for j in range(0, 40):
        pos = j + (i * 40)
        val = values[pos]
        if val - 1 == j or val == j or val + 1 == j:
            print("#", end="")
        else:
            print(".", end="")

    print("")
