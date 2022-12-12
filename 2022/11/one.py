"""2022, day 11, part 1"""


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3


class Monkey:
    items: list[int]
    review_criteria: int
    actions: dict
    inspect_count: int
    operation: list[str]

    def __init__(self):
        self.items = []
        self.review_criteria = 0
        self.actions = {}
        self.inspect_count = 0

    def __str__(self):
        return f"Monkey [{self.review_criteria} -> {self.actions}] has: " + ", ".join(
            [str(v) for v in self.items]
        )

    def add_item(self, item):
        self.items.append(item)

    def set_operation(self, val):
        self.operation = val.split(" ")

    def set_review_criteria(self, val):
        self.review_criteria = val

    def set_true_action(self, if_true):
        self.actions[True] = if_true

    def set_false_action(self, if_false):
        self.actions[False] = if_false

    def review_items(self, neighbors):
        for item in self.items:
            self.inspect_count += 1
            # print(f"Monkey inspects an item with a worry level of {item}")
            worry_level = int(run_operation(item, self.operation) / 3)
            dest = self.actions[(worry_level % self.review_criteria) == 0]
            # print(f"Item with worry level {worry_level} is thrown to monkey {dest}")
            neighbors[dest].add_item(worry_level)

        self.items = []


def run_operation(val, operation):
    input_vals = [operation[0], operation[2]]
    operator = operation[1]
    parts = [0, 0]
    for idx in range(0, 2):
        if input_vals[idx] == "old":
            parts[idx] = val
        else:
            parts[idx] = int(input_vals[idx])

    if operator == "+":
        return sum(parts)
    elif operator == "*":
        return parts[0] * parts[1]
    else:
        print("warning unsupported operator " + operator)
        return val


def test_run_operation():
    assert run_operation(5, ["old", "*", "old"]) == 25
    assert run_operation(2, ["old", "*", "19"]) == 38
    assert run_operation(2, ["old", "+", "3"]) == 5
    assert run_operation(2, ["5", "+", "old"]) == 7


def parse_input(lines):
    monkeys: list[Monkey] = []

    for line in lines:
        if line.startswith("Monkey"):
            # Assumes monkeys are always given in order
            current = Monkey()
            monkeys.append(current)
        elif line.startswith("Starting items:"):
            for val in line[16:].split(","):
                current.add_item(int(val))
        elif line.startswith("Operation: new = "):
            current.set_operation(line[17:])
        elif line.startswith("Test:"):
            current.set_review_criteria(int(line[19:]))
        elif line.startswith("If true:"):
            current.set_true_action(int(line[25:]))
        elif line.startswith("If false:"):
            current.set_false_action(int(line[25:]))
        elif len(line) == 0:
            pass

    return monkeys


def test_parse_input():
    lines = [
        "Monkey 0:",
        "Starting items: 79, 98",
        "Operation: new = old * 19",
        "Test: divisible by 23",
        "If true: throw to monkey 2",
        "If false: throw to monkey 3",
    ]
    out = parse_input(lines)
    assert str(out[0]) == "Monkey [23 -> {True: 2, False: 3}] has: 79, 98"


def test_example():
    monkeys = parse_input(get_lines("example-1.txt"))

    for _ in range(0, 20):
        for idx, m in enumerate(monkeys):
            # print("")
            # print(f"Monkey {idx}")
            m.review_items(monkeys)

    # print("")
    # for m in monkeys:
    #     print(m)
    #     print(m.inspect_count)
    top = sorted([v.inspect_count for v in monkeys], reverse=True)[0:2]
    solution = top[0] * top[1]

    assert solution == 10605


def test_solution():
    monkeys = parse_input(get_lines("input-1.txt"))

    for _ in range(0, 20):
        for idx, m in enumerate(monkeys):
            m.review_items(monkeys)

    top = sorted([v.inspect_count for v in monkeys], reverse=True)[0:2]
    solution = top[0] * top[1]

    assert solution == 0
