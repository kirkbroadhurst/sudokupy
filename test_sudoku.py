from sudoku import find_moves, resolve_moves, play_single_gaps
import numpy

def test_find_moves_1():
	# the first item, with value 0, is 'missing'. find_moves will tell us it should be a 9.
	state = [((i,i), i) for i in range(9)]	
	moves = find_moves(state)

	assert len(moves) == 1
	assert moves[0][0] == (0,0)
	assert moves[0][1] == 9

def test_find_moves_2():
	# the first and last items have value 0
	state = [((i,i), i if i < 8 else 0) for i in range(9)]	
	moves = find_moves(state)

	moves = sorted(moves)
	assert len(moves) == 4
	assert moves[0] == ((0,0), 8)
	assert moves[1] == ((0,0), 9)
	assert moves[2] == ((8,8), 8)
	assert moves[3] == ((8,8), 9)
	
def test_resolve_moves_0():
	possible_moves = [[((0,0), 1)], [((0,0), 1)]]
	moves = resolve_moves(possible_moves)
	assert len(moves) == 1
	assert moves[0] == ((0,0), 1)

def test_resolve_moves_1():
	possible_moves = [[((0,0), 1), ((0,0), 2)], [((0,0), 1), ((0,0), 3)]]
	moves = resolve_moves(possible_moves)
	assert len(moves) == 1
	assert moves[0] == ((0,0), 1)

def test_resolve_moves_2():
	possible_moves = [[((0,0), 1), ((0,0), 2)], [((0,0), 1), ((0,0), 2), ((0,0), 3)]]
	moves = resolve_moves(possible_moves)
	assert len(moves) == 0	

def test_resolve_moves_confounding_0():
	possible_moves = [[((0,0), 1), ((0,0), 2), ((1,1), 1), ((1,1), 2)], [((0,0), 1), ((0,0), 2), ((0,0), 3), ((1,1), 1), ((1,1), 2)]]
	moves = resolve_moves(possible_moves)
	assert len(moves) == 0

def test_play_single_gaps():
	# this is a game with only one missing move
	board = numpy.loadtxt('games/001.txt')
	assert board[(0,0)] == 0
	play_single_gaps(board)
	assert board[(0,0)] != 0