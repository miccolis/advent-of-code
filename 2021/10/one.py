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
	if c == ')':
		return 3
	if c == ']':
		return 57
	if c == '}':
		return 1197 
	if c == '>':
		return 25137

score = 0
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
			#print(char_score(char))
			score = score + char_score(char)
			break

print('Score', score)
			
