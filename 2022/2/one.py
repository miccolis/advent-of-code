
def getLines(filename):
    input = open(filename, 'r')
    lines = [ v.rstrip().split(' ') for v in input.readlines() ]
    return lines

def outcome(plays):
    match = ''.join(plays)
    if (
        match == 'AX' or 
        match == 'BY' or
        match == 'CZ'
    ):
        return 3;

    if (
        match == 'CX' or
        match == 'AY' or
        match == 'BZ'
    ):
        return 6;

    return 0;


score = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def test_example():
    solution = 0;
    for line in getLines('example-1.txt'):
        solution = solution + outcome(line) + score[line[1]]

    assert solution == 15


def test_solution():
    solution = 0;
    for line in getLines('input-1.txt'):
        solution = solution + outcome(line) + score[line[1]]

    assert solution == 0
