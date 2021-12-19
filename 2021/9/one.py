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
