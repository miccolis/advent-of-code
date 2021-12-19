input = open('input.txt', 'r')

lines = [ v.rstrip() for v in input.readlines()  ]

#line = '3,4,3,1,2'
line = lines[0]

fish = [int(v) for v in line.split(',')]

counts = [0 for _ in range(9)]

for age in fish:
	counts[age] = counts[age] + 1

for day in range(256):
	new = counts.pop(0)
	counts.append(new)
	counts[6] = counts[6] + new
	# print(counts)

print(sum(counts))

