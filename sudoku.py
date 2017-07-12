from itertools import groupby, chain
import numpy as np

# board = np.zeros((9,9))
board = np.loadtxt('games/003.txt')

valid = [1,2,3,4,5,6,7,8,9]

def places(game, f):
	result = (((x,y), game[(x,y)]) for x in range(9) for y in range(9))
	if f is not None:
		result = (list(x[1]) for x in groupby(sorted(result,key=f), f))
	return result

def rows(game):	
	return places(game, lambda x: x[0][0])

def cols(game):
	return places(game, lambda x: x[0][1])

def boxes(game):
	f = lambda x: (int(x[0][0]/3), int(x[0][1]/3))
	return places(game, f)

def sets(game):
	#return list(rows(game)) + list(cols(game)) + list(boxes(game))
	return chain(rows(game), cols(game), boxes(game))	

def find_moves(moveset):
	""" finds any move(s) with value 0 
		returns a list of potential moves, i.e. ((x,y), value)
	"""

	values = [v for v in valid if v not in [m[1] for m in moveset if m[1] != 0]]
	return [(m[0], v) for m in moveset if m[1] == 0 for v in values]

	missing = [m for m in moveset if m[1] == 0]
	if len(missing) == 1:
		values = [v for v in valid if v not in [m[1] for m in moveset if m[1] != 0]][0]
		return [(missing[0][0], values)]


def make_move(board, move):
	board[move[0]] = move[1]

def iterate_moves(board):
	again = True
	while again:
		again = False
		maybe_moves = []
		for moveset in sets(board):
			moves = find_moves(moveset)
			if moves is None or len(moves) == 0:
				continue
			elif len(moves) == 1:
				make_move(board, moves[0])
				again = True
				break
			else:
				maybe_moves += [moves]
	return maybe_moves



print (board)
result = iterate_moves(board)
print (board)

print (sorted(result))