input = open('input.txt', 'r')

lines = [
   [ int(v) for v in list(v.rstrip()) ] 
       for v in input.readlines() if v.rstrip().__len__() > 0
   ]

# lines = [
#     [ 1, 1, 1, 1, 1 ],
#     [ 1, 9, 9, 9, 1 ],
#     [ 1, 9, 1, 9, 1 ],
#     [ 1, 9, 9, 9, 1 ],
#     [ 1, 1, 1, 1, 1 ]
# ]

rows = lines.__len__()
cols = lines[0].__len__()

def debug(i, m):
    print('---', i, '---')
    for row in m:
        print(''.join(map(str, row)))

def increment(m):
    flashers = []
    for i in range(rows):
        for j in range(cols):
            m[i][j] = m[i][j] + 1
            if m[i][j] > 9:
                flashers.append((i, j))

    return flashers

def flash(m, pos):
    i, j = pos

    j_range = [0]
    if j > 0:
        j_range.append(-1)
    if j < rows - 1:
        j_range.append(1)

    # Above
    if i > 0:
        for j_adj in j_range:
            v = m[i-1][j+j_adj]
            m[i-1][j+j_adj] = v + 1
            if v == 9:
                flash(m, (i-1, j+j_adj))

    # Same row 
    for j_adj in j_range:
        if j_adj != 0:
            v = m[i][j+j_adj]
            m[i][j+j_adj] = v + 1
            if v == 9:
                flash(m, (i, j+j_adj))

    # Below
    if i < cols - 1:
        for j_adj in j_range:
            v = m[i+1][j+j_adj]
            m[i+1][j+j_adj] = v + 1
            if v == 9:
                flash(m, (i+1, j+j_adj))
    
def reset(m):
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            if m[i][j] > 9:
                cnt = cnt + 1
                m[i][j] = 0
    return cnt


total = 0
debug(0, lines)

for iteration in range(100):
    flashers = increment(lines)
    # print(flashers)
    for pos in flashers: 
        flash(lines, pos)
    total = total + reset(lines)
    debug(iteration + 1, lines)

print(total)
