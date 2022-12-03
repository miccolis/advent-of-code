
def getLines(filename):
    input = open(filename, 'r')
    lines = [ v.rstrip() for v in input.readlines() ]
    return lines

def mostCals(cals):
    sums = [0]
    idx = 0
    for entry in cals:
        if (entry == ""):
            sums.append(0)
            idx = idx + 1
        else:
            sums[idx] = sums[idx] + int(entry)
    return max(sums)

def test_example():
    assert mostCals(getLines('example-1.txt')) == 24000

print(mostCals(getLines('input-1.txt')))
