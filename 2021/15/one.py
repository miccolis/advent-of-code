input = open('input.txt', 'r')
# input = open('testinput.txt', 'r')

lines = [
   [ int(v) for v in list(v.rstrip()) ] 
       for v in input.readlines() if v.rstrip().__len__() > 0
   ]

nodes = {}
line_cnt = len(lines)
col_cnt = len(lines[0])
max_cost = 9 * line_cnt * col_cnt
for row in range(line_cnt):
    id_offset = row * col_cnt
    for col in range(col_cnt):
        nodes[col + id_offset] = {
            'risk': lines[row][col],
            'cost': max_cost
        }

def debug(nodes, line_range, col_range, solution):
    bold = '\033[1m' 
    end =  '\033[0m'
    path = solution[0]

    ls, le = line_range
    cs, ce = col_range
    for line in range(ls, le):
        for col in range(cs, ce):
            n_id = id(line, col)
            n = nodes[n_id]
            if n_id in path:
                print(bold+f'{n["cost"]}'.rjust(3)+end, end='')
            else:
                print(f'{n["cost"]}'.rjust(3), end='')
        print('')


def id(line, col):
    return (line * col_cnt) + col

end_id = id(line_cnt - 1, col_cnt - 1)

def walk(path, line, col, cost, solutions):
    if id(line, col) == end_id:
        solutions.append([path, cost])
        
    next = []
    if (col > 0):
       n = nodes[id(line, col - 1)]
       r = n['risk'] + cost
       if (r < n['cost']):
           n['cost'] = r
           next.append([line, col - 1, r])
    if (line> 0):
       n = nodes[id(line - 1, col )]
       r = n['risk'] + cost
       if (r < n['cost']):
           n['cost'] = r
           next.append([line - 1, col, r])
    if (col < col_cnt - 1):
       n = nodes[id(line, col + 1)]
       r = n['risk'] + cost
       if (r < n['cost']):
           n['cost'] = r
           next.append([line, col + 1, r])
    if (line < line_cnt - 1):
       n = nodes[id(line + 1, col)]
       r = n['risk'] + cost
       if (r < n['cost']):
           n['cost'] = r
           next.append([line + 1, col, r])

    ret = []
    for v in next:
        v_line, v_col, v_cost= v
        n_id = id(v_line, v_col)
        p_copy = [e for e in path]
        p_copy.append(n_id)
        ret.append([p_copy, v_line, v_col, v_cost])

    return ret

def dedupe_options(options):
    best = {}
    for option in options:
        path, line, col, cost = option
        pos = id(line, col)
        if  pos in best:
            if cost < best[pos][3]:
                best[pos] = option
        else:
            best[pos] = option

    return best.values()


solutions = []
options = walk([], 0, 0, 0, solutions)
i = 0
while len(options) > 0:
    next_options = []
    for option in options:
        path, line, col, cost = option
        next_options = next_options +  walk(path, line, col, cost, solutions)

    options = dedupe_options(next_options)


solutions.sort(key=lambda x: x[1])

debug(nodes, [0, line_cnt], [0, col_cnt], solutions[0])

print('Result: ', nodes[end_id]['cost'])


