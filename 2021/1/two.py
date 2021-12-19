input = open('input.txt', 'r')

count = 0
lines = [ int(v.rstrip()) for v in input.readlines() if v.rstrip().__len__() > 0  ]

prev = 100000000

len = lines.__len__() + 1;
 
for p in range(3, len):
	s = p - 3
	if s < 0:
		s = 0
	window = [ lines[i] for i in range(s, p) ]
	val = sum(window)
	if (val > prev):
		count = count + 1
	# print('({} = {}) > {} = {} [{}]'.format(window, val, prev, val > prev, count));
	prev = val
 
print(count)
# 1575
