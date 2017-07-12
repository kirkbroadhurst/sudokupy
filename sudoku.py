from itertools import groupby, chain
import numpy as np

# board = np.zeros((9,9))
board = np.loadtxt('games/003.txt')

valid = [1,2,3,4,5,6,7,8,9]

def places():
	return ((x,y) for x in range(9) for y in range(9))

def squares(game, f):	
	result = ((p, game[p]) for p in places())
	return result if f is None else (list(x[1]) for x in groupby(sorted(result,key=f), f))

def rows(game):	
	return squares(game, lambda x: x[0][0])

def cols(game):
	return squares(game, lambda x: x[0][1])

def boxes(game):
	f = lambda x: (int(x[0][0]/3), int(x[0][1]/3))
	return squares(game, f)

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
		again, possible_moves = play_single_gaps(board)
		if again:
			break
		
		# try to find necessary moves using known possible moves
		moves = resolve_moves(possible_moves)
		if any(moves):
			again = True

		for move in moves:
			make_move(board, move) 

def play_single_gaps(board):
	"""
	puts values in places with only one possible value
	returns (True, None) if it did something
	returns (False, possible_moves) if there were no single value moves
	"""
	possible_moves = []
	for moveset in sets(board):
		moves = find_moves(moveset)
		if moves is None or len(moves) == 0:
			continue
		elif len(moves) == 1:
			make_move(board, moves[0])
			return True, None			
		else:
			possible_moves += [moves]
	return False, possible_moves


def resolve_moves(movesets):
	"""
	input collections of 'possible moves' within groups/sets (rows, cols, boxes) across the board
	resolve which 'possible moves' exist across those collections
	if there is only one possible move across collections then it is a necessary move
	"""
	
	moves = []

	for place in places():
		# get matching moves from movesets that contain this 'place'; keeping them as 'movesets' for now
		sets = [set(m[1] for m in ms if place in m) for ms in movesets if any(place in m for m in ms)]
		if not any(sets):
			continue		
		# print (place, list(sets))
		
		valid_moves = sets[0].intersection(*sets)
		# print (valid_moves)
		if len(valid_moves) == 0:
			raise ValueError(place)
		elif len(valid_moves) == 1:
			moves.append((place, valid_moves.pop()))
			# print (moves)

	# print (moves)
	return moves



print (board)
iterate_moves(board)
print (board)
