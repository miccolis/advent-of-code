
def getLines(filename):
    input = open(filename, 'r')
    lines = [ v.rstrip() for v in input.readlines() ]
    return lines

def calsSums(cals):
    sums = [0]
    idx = 0
    for entry in cals:
        if (entry == ""):
            sums.append(0)
            idx = idx + 1
        else:
            sums[idx] = sums[idx] + int(entry)
    return sums


sums = calsSums(getLines('input-1.txt'))
sums.sort(reverse=True)
print(sum(sums[0:3]))
