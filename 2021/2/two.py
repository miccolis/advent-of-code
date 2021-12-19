input = open('input.txt', 'r')

count = 0
lines = [ v.rstrip() for v in input.readlines() if v.rstrip().__len__() > 0  ]

x = 0
y = 0
aim = 0

for line in lines:
	v = line.split(' ')
	command = v[0]
	value = int(v[1])
	if command == 'down':
		aim = aim + value
	elif command == 'up':
		aim = aim - value
	elif command == 'forward':
		x = x + value
		y = y + (value * aim)

print(x * y)
# not 536563918513
