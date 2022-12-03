
def getLines(filename):
    input = open(filename, 'r')
    lines = [ v.rstrip().split(' ') for v in input.readlines() ]
    return lines

def outcome(plays):
    # Lose
    if plays[1] == 'X':
        if plays[0] == 'A':
            return 0 + 3
        if plays[0] == 'B':
            return 0 + 1
        return 0 + 2 

    # Draw
    if plays[1] == 'Y':
        if plays[0] == 'A':
            return 3 + 1
        if plays[0] == 'B':
            return 3 + 2
        return 3 + 3 

    # Win
    if plays[1] == 'Z':
        if plays[0] == 'A':
            return 6 + 2
        if plays[0] == 'B':
            return 6 + 3
        return 6 + 1 


def test_example():
    solution = 0;
    for line in getLines('example-1.txt'):
        solution = solution + outcome(line)

    assert solution == 12


def test_solution():
    solution = 0;
    for line in getLines('input-1.txt'):
        solution = solution + outcome(line)

    assert solution == 0
