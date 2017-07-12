from itertools import groupby
import numpy as np

# board = np.zeros((9,9))
board = np.loadtxt('games/002.txt')

valid = [1,2,3,4,5,6,7,8,9]

def places(game, f):
	result = [((x,y), game[(x,y)]) for x in range(9) for y in range(9)]
	if f is not None:
		result = [list(x[1]) for x in groupby(sorted(result,key=f), f)]
	return result

def rows(game):	
	return places(game, lambda x: x[0][0])

def cols(game):
	return places(game, lambda x: x[0][1])

def boxes(game):
	f = lambda x: (int(x[0][0]/3), int(x[0][1]/3))
	return places(game, f)

def sets(game):
	return rows(game) + cols(game) + boxes(game)

def fill_empty(moveset):
	missing = [m for m in moveset if m[1] == 0]
	if len(missing) == 1:
		values = [v for v in valid if v not in [m[1] for m in moveset if m[1] != 0]][0]
		return (missing[0][0], values)	

def make_move(board, move):
	board[move[0]] = move[1]

def iterate_moves(board):
	again = True
	while again:
		again = False
		for moveset in sets(board):
			move = fill_empty(moveset)
			if move is not None:
				make_move(board, move)
				again = True
				break

print (board)

iterate_moves(board)

print (board)