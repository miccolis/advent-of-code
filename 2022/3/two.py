
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
    

def overlap(lines):
    a = { k: 1 for k in lines[0] }

    deduped = [list(set([v for v in line ])) for line in lines[1:]]
    for l in deduped:
        for v in l:
            if v in a:
                a[v] = a[v] + 1

    return [ k for (k, v) in a.items() if v > 2 ][0]

def test_overlap():
    assert overlap('aacdea') == 'a'

def test_get_priority():
    assert get_priority('a') == 1
    assert get_priority('Z') == 52

def test_example():
    lines = [
        'vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw',
    ]
    group = []
    ret = 0

    for line in lines:
        group.append(line)
        if len(group) == 3:
            ret = ret + get_priority(overlap(group))
            group = []

    assert  ret == 70

def test_solution():
    group = []
    ret = 0
    for line in get_lines('input-1.txt'):
        group.append(line)
        if len(group) == 3:
            ret = ret + get_priority(overlap(group))
            group = []

    assert  ret == None
