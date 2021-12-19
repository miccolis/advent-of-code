# lines = [
#     'start-A',
#     'start-b',
#     'A-c',
#     'A-b',
#     'b-d',
#     'A-end',
#     'b-end'
# ]

# lines = [
#     'dc-end',
#     'HN-start',
#     'start-kj',
#     'dc-start',
#     'dc-HN',
#     'LN-dc',
#     'HN-end',
#     'kj-sa',
#     'kj-HN',
#     'kj-dc'
# ]


input = open('input.txt', 'r')

lines = [
    v.rstrip()
    for v in input.readlines() if v.rstrip().__len__() > 0
]

lines = [ v.split('-') for v in lines ]


class Node:

    def __init__(self, label):
        self.label = label
        self.links = []

    def __str__(self):
        return "Node: {} : {} links".format(self.label, self.links.__len__())

    def link(self, node):
        self.links.append(node)

def build_graph(lines):
    nodes = {}

    for line in lines:
        for p in line:
            if p not in nodes:
                nodes[p] = Node(p)

        a, b = line
        nodes[a].link(b)
        nodes[b].link(a)

    return nodes

def walk(graph, path, solutions):
    s = path[-1]

    if s == 'end':
        #print('at end', path)
        solutions.append(path)

    if graph[s].links.__len__() == 0:
        return [ path ]

    for p in graph[s].links:
        # Don't revisit small caves
        if p.islower() and p in path:
            continue

        # Don't exist the same way twice
        revisited = False
        for visited in range(path.__len__() - 1):
            if path[visited] == s and path[visited + 1] == p:
                revisited = True
                break

        if not revisited:
            # print('Trying {} -> {}'.format(s, p))
            walk(graph, path + [p], solutions)

graph = build_graph(lines)

paths = []
walk(graph, ['start'], paths)

print(paths.__len__())
