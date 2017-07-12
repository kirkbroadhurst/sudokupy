from sudoku import find_moves

def test_find_one_move():
	# the first item, with value 0, is 'missing'. find_moves will tell us it should be a 9.
	state = [((i,i), i) for i in range(9)]	
	moves = find_moves(state)

	assert len(moves) == 1
	assert moves[0][0] == (0,0)
	assert moves[0][1] == 9

def test_find_two_moves():
	# the first and last items have value 0
	state = [((i,i), i if i < 8 else 0) for i in range(9)]	
	moves = find_moves(state)

	moves = sorted(moves)
	assert len(moves) == 4
	assert moves[0] == ((0,0), 8)
	assert moves[1] == ((0,0), 9)
	assert moves[2] == ((8,8), 8)
	assert moves[3] == ((8,8), 9)
	
