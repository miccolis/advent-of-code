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

for instruction in instructions:
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

coords = [
    [ int(vv) for vv in v.split(',') ]
    for v in
    list(set([ '{},{}'.format(v[0], v[1]) for v in coords ]))
]

max_x = max([v[0] for v in coords])
max_y = max([v[1] for v in coords])
print(len(coords), max_x, max_y)

display = [ ['.']*(max_y+1) for _ in range(max_x+1) ]

for coord in coords:
    display[coord[0]][coord[1]] = '#'

for y in range(max_y + 1):
    print()
    for x in range(max_x + 1):
        print(display[x][y], end='')

