input = open('input.txt', 'r')

count = 0
lines = [ v.rstrip() for v in input.readlines() if v.rstrip().__len__() > 0  ]

sums = [ 0 for _ in range(12) ]
count = lines.__len__()

for line in lines:
	for i in range(12):
		sums[i] = sums[i] + int(line[i])

common = ''.join(['1' if v > 500 else '0' for v in sums])
gamma = int(common, 2)

invert = ''.join(['0' if v > 500 else '1' for v in sums])
epsilon = int(invert, 2)

print(gamma * epsilon)
