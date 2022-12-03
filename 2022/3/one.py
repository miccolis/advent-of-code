
def get_lines(filename):
    input = open(filename, 'r')
    lines = [ v.rstrip() for v in input.readlines() ]
    return lines


def setPriority():
    items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priority = {}
    for i in range(0, len(items)):
        priority[items[i]] = i + 1

    return priority

pVals = setPriority()

def get_priority(item):
    return pVals[item]
    

def overlap(line):
    l = int(len(line) / 2)

    a = { k: 1 for k in line[0:l] }

    for i in range(l, len(line)):
        if line[i] in a:
            a[line[i]] = 2

    return [ k for (k, v) in a.items() if v > 1 ]

def test_overlap():
    assert overlap('aacdea') == ['a']

def test_get_priority():
    assert get_priority('a') == 1
    assert get_priority('Z') == 52

def test_example():
    ret = 0
    shared = [overlap(v) for v in get_lines('example-1.txt')] 
    for items in shared:
        ret = ret + sum([ get_priority(v) for v in items])

    assert  ret == 157

def test_solution():
    ret = 0
    shared = [overlap(v) for v in get_lines('input-1.txt')] 
    for items in shared:
        ret = ret + sum([ get_priority(v) for v in items])

    assert  ret == None
