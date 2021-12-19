input = open('input.txt', 'r')

lines = [ v.rstrip() for v in input.readlines()  ]
line = lines[0]

#line = '16,1,2,0,4,2,7,1,2,14'

crabs = [int(v) for v in line.split(',')]

max_pos = max(crabs)

counts = [0 for _ in range(max_pos + 1)]

for pos in crabs:
	counts[pos] = counts[pos] + 1

#costs = [sum(range(i+1)) for i in range(counts.__len__())]
costs = [(n*(n+1))/2 for n in range(counts.__len__())]

# print(counts)
fuel = [0 for _ in counts]
for i in range(counts.__len__()):
	fuel[i] = sum([
		# sum(range(abs(i - p)+1)) * counts[p] # TODO memoize
		costs[abs(i - p)] * counts[p] 
		for p in range(counts.__len__())
	])

# print(fuel)
print(min(fuel))

