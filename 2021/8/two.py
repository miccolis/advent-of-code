# lines = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

input = open('input.txt', 'r')
lines = [ v.rstrip() for v in input.readlines() if v.rstrip().__len__() > 0  ]

def solve(glyphs):
	map = {
		'a': None,
		'b': None,
		'c': None,
		'd': None,
		'e': None,
		'f': None,
		'g': None
	}

	chars = [ [] for _ in range(10) ]

	for glyph in glyphs:
		as_list = list(glyph)
		as_list.sort()
		glyph = ''.join(as_list)
		l = glyph.__len__()
		if l == 2:
			chars[1].append(glyph)
		if l == 3:
			chars[7].append(glyph)
		if l == 4:
			chars[4].append(glyph)
		if l == 5:
			chars[2].append(glyph)
			chars[3].append(glyph)
			chars[5].append(glyph)
		if l == 6:
			chars[0].append(glyph)
			chars[6].append(glyph)
			chars[9].append(glyph)
		if l == 7:
			chars[8].append(glyph)
	
	chars = [ list(set(v)) for v in chars ]

	# diff between 1 & 7 must be the top line
	map['a'] = (set(list(chars[7][0])) - set(list(chars[1][0]))).pop()

	# the 1 part that isn't present in 0, 6 & 9 is top right
	# ..other part of 1 is bottom 
	one_parts = list(chars[1][0])
	counts = { c: 0 for c in one_parts }
	for v in chars[0]:
		for c in one_parts:
			if c in v:
				counts[c] = counts[c] + 1

	for (c, count) in counts.items():
		if count == 2:
			map['c'] = c
		if count == 3:
			map['f'] = c
	
	# remove 4 & top from the 5 segment glyphs...
	# 2 => 2 segments (bottom left, bottom), 3 & 5 => 1 segment (bottom)
	mask = set(list(chars[4][0]))
	mask.add(map['a'])
	for v in chars[2]:
		diff = (set(v) - mask)
		l = diff.__len__()
		if l == 1:
			map['g'] = diff.pop();
		elif l == 2:
		  two_diff = diff

	map['e'] = (two_diff - set(map['g'])).pop()


	# diff between 4 & 7 are the middle and far left
	# middle only exists in 2 of the 6 segment glyphs
	remains = set(list(chars[4][0])) - set(list(chars[7][0]))
	for c in remains:
		count = sum([1 for v in chars[0] if c in v])
		if count == 2:
			map['d'] = c
		if count == 3:
			map['b'] = c

	return { v: k for (k, v) in map.items() }

def decode(mapping, glyph):
	segments = [ mapping[v] for v in list(glyph) ]
	segments.sort()
	s = ''.join(segments)

	if s == 'abcefg':
		return '0'
	if s == 'cf':
		return '1'
	if s == 'acdeg':
		return '2'
	if s == 'acdfg':
		return '3'
	if s == 'bcdf':
		return '4'
	if s == 'abdfg':
		return '5'
	if s == 'abdefg':
		return '6'
	if s == 'acf':
		return '7'
	if s == 'abcdefg':
		return '8'
	if s == 'abcdfg':
		return '9'
	
vals = []

for line in lines:
	input, output = [ v.split() for v in line.split('|')]
	combinations = list(set(input + output))

	mapping = solve(combinations)
	vals.append(int(''.join([ decode(mapping, glyph) for glyph in output])))

print(vals)
print(sum(vals))

