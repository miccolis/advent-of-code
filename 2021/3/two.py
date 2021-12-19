input = open('input.txt', 'r')

lines = [
	'00100',
	'11110',
	'10110',
	'10111',
	'10101',
	'01111',
	'00111',
	'11100',
	'10000',
	'11001',
	'00010',
	'01010'
]

lines = [ v.rstrip() for v in input.readlines() if v.rstrip().__len__() > 0  ]

width = lines[0].__len__()
count = lines.__len__()

o_set = lines
for i in range(width):
	len = o_set.__len__()
	v = sum([int(v[i]) for v in o_set])
	common = '1' if v >= (len /2) else '0'
	o_set = [ v for v in o_set if v[i] == common ]
	if o_set.__len__() == 1:
		break

#print(o_set);
oxygen = int(o_set[0], 2);

c_set = lines
for i in range(width):
	len = c_set.__len__()
	v = sum([int(v[i]) for v in c_set])
	uncommon = '0' if v >= (len / 2) else '1'
	c_set = [ v for v in c_set if v[i] == uncommon ]
	if c_set.__len__() == 1:
		break
#print(c_set);
co2 = int(c_set[0], 2);
 
#print(oxygen, co2)
print(oxygen * co2)
# not 1092896
