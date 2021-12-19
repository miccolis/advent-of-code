input = open('input.txt', 'r')

lines = [ v.rstrip() for v in input.readlines() ]

def parseInput(lines):
    template = lines[0]
    rules = []

    for line in lines[2:]:
        rules.append(line.split(' -> '))

    return template, rules 



template, rules = parseInput(lines)

counts = {}
for char in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    counts[char] = 0

pairs = {}
counts[template[-1]] = counts[template[-1]] + 1
for i in range(len(template) - 1):
    counts[template[i]] = counts[template[i]] + 1
    pair = template[i:i+2]
    pairs.setdefault(pair, 0)
    pairs[pair] = pairs[pair] + 1

# print(pairs)
# print([ v for v in counts.items() if v[1] > 0 ])

for _ in range(40):
    # print(pairs)
    mods = []
    for target, add in rules:
        if target in pairs:
            # if add == 'N':
            #    print(target, add, pairs[target])
            mods.append([target, -pairs[target]])
            mods.append([target[0] + add, pairs[target]])
            mods.append([add + target[1], pairs[target]])
            counts[add] = counts[add] + pairs[target] 

    for target, adj in mods:
        if target not in pairs:
            pairs[target] = adj
        else:
            pairs[target] = pairs[target] + adj 


counts = ([ v for v in counts.items() if v[1] > 0 ])

counts.sort(key=lambda x: x[1])
# print(counts)
print(counts[-1][1] - counts[0][1])
# 10x is 2003

# 1917714787558 is too low
 



