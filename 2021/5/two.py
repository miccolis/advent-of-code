input = open('input.txt', 'r')

lines = [ v.rstrip() for v in input.readlines()  ]

def parse_coord(v):
	points = v.split(',')
	return [int(points[0]), int(points[1])]

vents = [
	[parse_coord(v[0]), parse_coord(v[2])]
	for v in [
		line.split() for line in lines
	]
]

x_vals = [
	[v[0][0], v[1][0]]
	for v in vents
]
max_x = max([x for x_line in x_vals for x in x_line])

y_vals = [
	[v[0][1], v[1][1]]
	for v in vents
]
max_y = max([y for y_line in y_vals for y in y_line])

ocean = [
	[ 0 for _ in range(max_y + 1) ]
	for _ in range(max_x + 1)
]


for vent in vents:
	x_delta  = vent[1][0] - vent[0][0]
	y_delta =  vent[1][1] - vent[0][1]
	# print('vent', vent)

	if (y_delta == 0):
		y = vent[0][1]
		inc = 1 if x_delta > 0 else -1
		# print('horizontal', y, x_delta)
		for x in range(vent[0][0], vent[1][0] + inc, inc):
			# print([x, y])
			ocean[x][y] = ocean[x][y] + 1

	elif (x_delta == 0):
		x = vent[0][0]
		inc = 1 if y_delta > 0 else -1
		# print('vertical', x, y_delta)
		for y in range(vent[0][1], vent[1][1] + inc, inc):
			# print([x, y])
			ocean[x][y] = ocean[x][y] + 1

	else:
		print('slant', vent[0], x_delta, y_delta)
		x_inc = 1 if x_delta > 0 else -1
		y_inc = 1 if y_delta > 0 else -1
		for p in range(0, abs(x_delta) + 1):
			x = vent[0][0] + (p * x_inc)
			y = vent[0][1] + (p * y_inc)
			# print(p, [x, y])
			ocean[x][y] = ocean[x][y] + 1

pnts = 0
for depth in ocean:
	for loc in depth:
		if loc > 1:
			pnts = pnts + 1

print(pnts)
# not 20251
