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
        return "Node {} : Links {}".format(self.label, self.links)

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

def smallCaveProhibited(path, p):
    if p.isupper():
        return False

    sm = [ v for v in path if v.islower() ]
    ret = sm.__len__() > (set(sm).__len__() + 1)
    return ret

def walk(graph, path, solutions):
    s = path[-1]
    #print('Path', path)

    if s == 'end':
        #print('At end', path)
        solutions.append(path)
        return

    if graph[s].links.__len__() == 0:
        return [ path ]

    for p in graph[s].links:
        # Don't revisit start
        if p == 'start':
            continue

        # Don't revisit more than 1 small cave
        if smallCaveProhibited(path, p):
            continue

        # Don't exit the same way twice
        # revisited = False
        # for visited in range(path.__len__() - 1):
        #     # print('revisit check', s, path)
        #     if path[visited] == s and path[visited + 1] == p:
        #         revisited = True

        # if not revisited:
        #     #print('Trying {} -> {}'.format(path, p))
        #     walk(graph, path + [p], solutions)
        walk(graph, path + [p], solutions)

graph = build_graph(lines)

paths = []
walk(graph, ['start'], paths)

# for v in paths:
#     print(v)
print(paths.__len__())
# not 2844510
