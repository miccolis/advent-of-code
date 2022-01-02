import math

input = open('input.txt', 'r')
lines = [ eval(v.rstrip()) for v in input.readlines()  ]

def explode(context, path):
    explode_left(context, path)
    explode_right(context, path)
    setAt(context, path, 0)

def pathValue(path):
    return float(('0.'+ ''.join([str(v) for v in path])))

def explode_left(context, path):
    add = valueAt(context, path)[0]
    start = pathValue(path + [0])

    target = in_order(context, start, 'left', [])
    if target:
        local = valueAt(context, target)
        setAt(context, target, local + add)

def explode_right(context, path):
    add = valueAt(context, path)[1]

    start = pathValue(path + [1])

    target = in_order(context, start, 'right', [])
    if target:
        local = valueAt(context, target)
        setAt(context, target, local + add)

def in_order(node, start, cmp, path):
    pv = pathValue(path)

    if type(node) is int:
        if cmp == 'left' and pv > start:
            return
        if cmp == 'right' and pv < start:
            return
        if pv != start:
            return path
        else:
            return None

    fs = 0
    ss = 1
    if cmp == 'left':
        fs = 1
        ss = 0

    first_search = in_order(node[fs], start, cmp, path + [fs])
    if first_search:
        return first_search
    else:
        return in_order(node[ss], start, cmp, path + [ss])



def explode_search(context, path):
    modified = False
    if len(path) == 4:
        explode(context, path)
        return True
    else:
        local = valueAt(context, path)
        for i in range(len(local)):
            if type(local[i]) is list:
                 if explode_search(context, path + [i]) == True:
                     return True

def split(value):
    v = value / 2
    return [math.floor(v), math.ceil(v)]

def split_search(context, path):
        local = valueAt(context, path)
        for i in range(len(local)):
            if type(local[i]) is list:
                if split_search(context, path + [i]) == True:
                    return True
            elif type(local[i]) is int and local[i] > 9:
                local[i] = split(local[i])
                return True

def reduce(context):
    while explode_search(context, []):
        pass

    if split_search(context, []):
        reduce(context)


def valueAt(context, path):
    if len(path) == 0: 
        return context
    else:
        local = context[:]
        for i in path:
            local = local[i]

        return local

def setAt(context, path, value):
    local = context
    plen = len(path)
    plim = plen - 1
    for ii in range(plen):
        if (ii == plim):
            local[path[ii]] = value
        else:
            local = local[path[ii]]

def magnitude(context):
    if type(context[0]) is int:
        left = 3 * context[0]
    else:
        left = 3 * magnitude(context[0])

    if type(context[1]) is int:
        right = 2 * context[1]
    else:
        right = 2 * magnitude(context[1])

    return left + right


from itertools import permutations
from copy import deepcopy

c_max = 0

for a, b in permutations(lines, 2):
    local = [deepcopy(a), deepcopy(b)]
    reduce(local)
    l_max = magnitude(local)
    if l_max > c_max:
        c_max = l_max
    

print(c_max)

# 4651 is too low

