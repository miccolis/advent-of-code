input = open('input.txt', 'r')

lines = [
	list(v.rstrip())
	for v in input.readlines() if v.rstrip().__len__() > 0
]

for i in range(lines.__len__()):
	lines[i] = [ { 'v': int(v), 'candidate': True } for v in lines[i] ]


risk = 0;
low_points = []

row_count = lines.__len__()
col_count = lines[0].__len__()
for y in range(row_count):
	line = lines[y]
	for x in range(col_count):
		low_point = True
		# Above
		if y > 0:
			if lines[y-1][x]['v'] <= line[x]['v']:
				low_point = False

		# Below
		if y < row_count - 1:
			if lines[y+1][x]['v'] <= line[x]['v']:
				low_point = False
		# Left
		if x > 0:
			if lines[y][x-1]['v'] <= line[x]['v']:
				low_point = False
		# Right
		if x < col_count - 1:
			if lines[y][x+1]['v'] <= line[x]['v']:
				low_point = False

		if low_point:
			low_points.append((x, y))
			risk = risk + line[x]['v'] + 1

print('Risk', risk)

def debug(visited):
	for l in visited:
		print(l)

def explore(lines, cnt, pos, visited):
	x, y = pos
	val = lines[y][x]['v'] 

	# print('Reviewing', (x, y), val, visited[y][x])

	if (val == 9 or visited[y][x]):
		return cnt

	# print('Adding', (x,y))
	visited[y][x] = True	
	cnt = cnt + 1

	# Top
	if y > 0:
		cnt = explore(lines, cnt, (x, y -1), visited)
	# Right
	if x < col_count - 1:
		cnt = explore(lines, cnt, (x + 1, y), visited)
	# Bottom
	if y < row_count - 1:
		cnt = explore(lines, cnt, (x, y + 1), visited)
	# Left
	if x > 0:
		cnt = explore(lines, cnt, (x - 1, y), visited)

	return cnt 

sizes = []
for point in low_points:
	visited = [ [False] * col_count for _ in range(row_count) ] 

	sizes.append(explore(lines, 0, point, visited))

	# debug(visited)

sizes.sort()
sizes.reverse()
print(sizes[0] * sizes[1] * sizes[2])
