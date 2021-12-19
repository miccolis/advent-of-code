input = open('input.txt', 'r')

count = 0
prev = -1
for line in input.readlines():
	v = line.rstrip()
	if (v.__len__() > 0):
		val = int(v)
		if (prev > -1 and val > prev):
			count = count + 1
		prev = val

print(count)
