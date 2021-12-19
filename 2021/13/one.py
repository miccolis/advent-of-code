input = open('input.txt', 'r')

lines = [ v.rstrip() for v in input.readlines() ]

def parseInput(lines):
    coords = []
    instructions = []
    isCoords = True

    for line in lines:
        if (len(line) == 0):
            isCoords = False
            continue

        if isCoords:
            coords.append([int(v) for v in line.split(',')])
        else:
            instructions.append(line)

    return instructions, coords

instructions, coords = parseInput(lines)

instruction = instructions[0]

# for instruction in instructions:
axis, pos = instruction[11:len(instruction)].split('=')
pos = int(pos)

j = 0
if (axis == 'y'):
    j = 1

for i in range(len(coords)):
    if coords[i][j] > pos:
        diff = (coords[i][j] - pos) * 2 
        coords[i][j] = coords[i][j] - diff


coords.sort(key=lambda x: x[0])

coords = set([ '{},{}'.format(v[0], v[1]) for v in coords ])

# max_x = max([v[0] for v in coords])
# max_y = max([v[1] for v in coords])
print(len(coords))
# node 799

