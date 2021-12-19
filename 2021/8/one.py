# line = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

input = open('input.txt', 'r')
lines = [ v.rstrip() for v in input.readlines() if v.rstrip().__len__() > 0  ]

chars = [0 for _ in range(10)] 

for line in lines:
	_, output = [ v.split() for v in line.split('|')]

	for v in output:
		l = v.__len__()
		
		if l == 2:
			chars[1] = chars[1] + 1
		if l == 3:
			chars[7] = chars[7] + 1
		if l == 4:
			chars[4] = chars[4] + 1
		if l == 7:
			chars[8] = chars[8] + 1

print(sum(chars))
	
