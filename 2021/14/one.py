input = open('input.txt', 'r')

lines = [ v.rstrip() for v in input.readlines() ]

def parseInput(lines):
    template = lines[0]
    rules = []

    for line in lines[2:]:
        rules.append(line.split(' -> '))

    return template, rules 

template, rules = parseInput(lines)


# template = 'NBCCNBBBCBHCB'
#print(template)
# for rule in rules[12:13]:
#    print(rule)

for _ in range(10):
    mods = []
    for rule in rules:
        target, add = rule
        #for match in re.finditer(target, template):
            # p = match.start() + 1
        p = template.find(target) + 1
        adj = p
        #print('outer search', template, target, p)
        while p > 0:
            # if (add == 'N'):
            #    print(target, add, 1)
            mods.append([adj, add])
            p = template[adj:].find(target) + 1
            adj = adj + p

    mods.sort(key=lambda v: v[0])
    #print(mods)

    adj = 0
    for mod in mods:
        p, add = mod
        p = p + adj
        template = template[:p] + add  + template[p:]
        adj = adj + 1

    #print(template)

#        'N B C C N B BB C B H C B'
# thiers: NBBBCNCCNBBNBNBBCHBHHBCHB
# mine:   NBBBCNCCNBBNB BBCHBHHBCHB
#         NBBBCNCCNBBNBNBBCHBHHBCHB

# theirs: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
# mine:   NBBNB BBCCNBCNCCNBBNBBNBB NBB B CBHCBHHNHCBBCBHCB
#         NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

# print(len(template))

counts = {}
for char in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    counts[char] = 0

for char in list(template):
    counts[char] = counts[char] + 1

counts = ([ v for v in counts.items() if v[1] > 0 ])

counts.sort(key=lambda x: x[1])
print(counts)

print(counts[-1][1] - counts[0][1])




