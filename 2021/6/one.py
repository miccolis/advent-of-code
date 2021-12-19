input = open('input.txt', 'r')

lines = [ v.rstrip() for v in input.readlines()  ]

#line = '3,4,3,1,2'
line = lines[0]

fish = [int(v) for v in line.split(',')]

for day in range(80):
	for i in range(fish.__len__()):
		if fish[i] == 0:
			fish[i] = 6
			fish.append(8)
		else:
			fish[i] = fish[i] - 1
	# print(fish)
print(fish.__len__())

