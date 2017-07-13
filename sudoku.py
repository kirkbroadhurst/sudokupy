from navigation import *
import numpy as np

# board = np.zeros((9,9))
board = np.loadtxt('games/003.txt')

valid = [1,2,3,4,5,6,7,8,9]

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
	""" put a piece on the board, LOCK IT IN REBUS """
	if board[move[0]] == 0:
		board[move[0]] = move[1]
	else:
		raise ValueError(move)


def play_game(board):
	""" loops through the board trying to make moves """
	again = True
	while again:
		again, possible_moves = play_single_gaps(board)
		if again:
			continue
		
		# try to find necessary moves using known possible moves
		moves = resolve_moves(possible_moves)
		if any(moves):
			again = True

		for move in moves:
			make_move(board, move) 


def play_single_gaps(board):
	"""
	completes 9-value sets (rows, cols, boxes) with one missing value by putting the missing value into the empty space	
	returns (was_move_made, possible_moves) 
	was_move_made is True if a move was made
	possible moves is a list of potentially valid moves within each 9-item set
	"""
	possible_moves = []
	for moveset in sets(board):
		moves = find_moves(moveset)
		if moves is None or len(moves) == 0:
			continue
		elif len(moves) == 1:
			make_move(board, moves[0])
			return True, possible_moves
		else:
			possible_moves += [moves]
	return False, possible_moves


def resolve_moves(possible_moves):
	"""
	possible_moves: sets of valid moves within each 9-item set (row/col/box)
	
	resolve which 'possible moves' are valiid across those collections
	if there is only one possible move across collections then it is a necessary move
	if there is no possible move across collections then something is wrong
	if there are multiple possible moves, continue

	returns set of necessary moves
	"""
	
	moves = []
	for place in places():
		# find matching moves from each 9-item set that apply to this 'place'; get the possible values from each (drop the place)
		sets = [set(m[1] for m in ms if place in m) for ms in possible_moves if any(place in m for m in ms)]

		if not any(sets):
			continue		
		
		# find which values would be valid according to each 9-item sets' constraints
		valid_moves = sets[0].intersection(*sets)
		
		if len(valid_moves) == 0:
			raise ValueError(place)
		elif len(valid_moves) == 1:
			moves.append((place, valid_moves.pop()))		
			
	return moves


def is_complete(board):
	""" return True is board is complete and error free """
	valid_set = set(valid)
	for s in sets(board):
		if set(m[1] for m in s) != valid_set:
			return False
	return True



print (board)
play_game(board)
print (board)
