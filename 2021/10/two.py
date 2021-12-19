input = open('input.txt', 'r')

lines = [
	list(v.rstrip())
	for v in input.readlines() if v.rstrip().__len__() > 0
]

def opener(c):
	return c == '(' or c =='[' or c == '{' or c == '<'

def expected(o, c):
	if o == '(' and c == ')':
		return True
	elif o == '[' and c == ']':
		return True
	elif o == '{' and c == '}':
		return True
	elif o == '<' and c == '>':
		return True
	return False

def char_score(c):
	if c == '(':
		return 1
	if c == '[':
		return 2
	if c == '{':
		return 3
	if c == '<':
		return 4

scores = []
for line in lines:
	stack = [];
	for char in line:
		if stack.__len__() == 0 and opener(char):
			stack.append(char)

		elif opener(char):
			stack.append(char)

		elif expected(stack[-1], char):
			stack.pop()
		
		else:
			# corrupt 
			stack = []
			break

	if (stack.__len__() != 0):
		score = 0
		stack.reverse()
		for c in stack:
			score = (score * 5) + char_score(c)

		scores.append(score)
		#print('incomplete', stack, score)


scores.sort()
print(scores[int(scores.__len__() / 2)])
