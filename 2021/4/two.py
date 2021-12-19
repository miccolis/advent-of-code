input = open('input.txt', 'r')

lines = [ v.rstrip() for v in input.readlines()  ]

draw = lines[0].split(',')

boards = []
board = []

for i in range(2, lines.__len__()):
	if lines[i].__len__() == 0:
		boards.append(board)
		board = []
	else:
	 	board.append(lines[i].split())

boards.append(board)

def search(call, board):
	for x in range(board.__len__()):
		for y in range(board[x].__len__()):
			if board[x][y] == call:
				board[x][y] = 0
				if winner(board, x, y):
					return True


def winner(board, x, y):
	if sum([int(v) for v in board[x]]) == 0:
		# print('row', board)
		return True
	if sum([int(row[y]) for row in board]) == 0:
		# print('col', board)
		return True
	else:
		return False

winners = [ False for i in range(boards.__len__()) ]
lastWinner = -1
lastCall = -1

for call in draw:
	for i in range(boards.__len__()):
		if (not winners[i]) and search(call, boards[i]):
			winners[i] = True
			lastWinner = i;
			lastCall = call;

board = boards[lastWinner]
print(board)

val = sum([
	sum([int(v) for v in board[x]])
 	for x in range(board.__len__())
])
print(val * int(lastCall));
