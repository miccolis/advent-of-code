"""2022, day 16, part 1"""
from queue import Queue


def get_lines(filename):
    """Get a file line by line"""
    with open(filename, "r", encoding="utf8") as input_file:
        lines = [v.strip() for v in input_file.readlines()]
        return lines


def parse_line(line):
    parts = line.split(" ")
    start = parts[1]
    rate = int(parts[4].split("=")[1].strip(";"))
    dest = [v.strip(",") for v in parts[9:]]
    return [start, rate, dest]


def test_parse_line():
    line = "Valve AA has flow rate=0; tunnels lead to valves DD, II, BB"
    assert parse_line(line) == ["AA", 0, ["DD", "II", "BB"]]


def find_paths(valves, a, targets):
    paths = Queue()
    paths.put([a])

    ret = []

    while not paths.empty() and len(targets) > 0:
        path = paths.get()
        loc = path[-1]

        for k in valves[loc][1]:
            if k in path:
                continue

            if k in targets:
                ret.append(path + [k])
                targets = [v for v in targets if v != k]

            if len(targets) > 0:
                paths.put(path + [k])

    return ret


def test_find_paths():
    valves = {"AA": [0, ["BB"]]}
    paths = find_paths(valves, "AA", ["BB"])
    assert paths == [["AA", "BB"]]

    valves = {"AA": [0, ["BB"]], "BB": [0, ["CC"]]}
    paths = find_paths(valves, "AA", ["CC"])
    assert paths == [["AA", "BB", "CC"]]

    valves = {"AA": [0, ["BB"]], "BB": [0, ["CC"]]}
    paths = find_paths(valves, "AA", ["BB", "CC"])
    assert paths == [["AA", "BB"], ["AA", "BB", "CC"]]


class TunnelPath:
    locations: list[str]
    flow: int

    def __init__(self, initial_location=None):
        self.flow = 0
        self.locations = []
        if initial_location:
            self.locations.append(initial_location)

    def clone(self):
        c = TunnelPath()
        c.locations = self.locations[0:]
        c.flow = self.flow
        return c

    def __str__(self):
        sep = " -> "
        return f"[{self.flow}] {sep.join(self.locations)}"


def walk(network_paths, targets, o_path, minute):
    best_path = o_path
    pos = o_path.locations[-1]
    for idx, dest in enumerate(targets):
        path, rate = network_paths[f"{pos}-{dest}"]
        l_minute = minute + len(path)
        if l_minute < 30:
            trimmed = [v for k, v in enumerate(targets) if k != idx]

            l_path = o_path.clone()
            l_path.locations += path[1:]
            new_flow = rate * (30 - l_minute)
            l_path.flow += new_flow

            l_path = walk(network_paths, trimmed, l_path, l_minute)

            if l_path.flow > best_path.flow:
                best_path = l_path

    return best_path


def test_example():
    valves = {}
    for line in get_lines("example-1.txt"):
        valve = parse_line(line)
        valves[valve[0]] = valve[1:]

    targets = {}
    for k, v in valves.items():
        if v[0] > 0:
            targets[k] = v

    network_paths = {}
    for a in [v for v in targets.keys()] + ["AA"]:
        local_targets = [v for v in targets.keys() if v != a]

        for path in find_paths(valves, a, local_targets):
            p_key = f"{path[0]}-{path[-1]}"
            p_val = valves[path[-1]][0]
            network_paths[p_key] = [path, p_val]

    # for k, v in network_paths.items():
    #     print(k, v)

    # next, walk the tree to find the
    initial = TunnelPath("AA")
    solution = walk(network_paths, list(targets.keys()), initial, 0)
    print(solution)
    assert solution.flow == 1651


def test_solution():
    valves = {}
    for line in get_lines("input-1.txt"):
        valve = parse_line(line)
        valves[valve[0]] = valve[1:]

    targets = {}
    for k, v in valves.items():
        if v[0] > 0:
            targets[k] = v

    network_paths = {}
    for a in [v for v in targets.keys()] + ["AA"]:
        local_targets = [v for v in targets.keys() if v != a]

        for path in find_paths(valves, a, local_targets):
            p_key = f"{path[0]}-{path[-1]}"
            p_val = valves[path[-1]][0]
            network_paths[p_key] = [path, p_val]

    # for k, v in network_paths.items():
    #     print(k, v)

    # next, walk the tree to find the
    initial = TunnelPath("AA")
    solution = walk(network_paths, list(targets.keys()), initial, 0)
    print(solution)
    assert solution.flow == 0
