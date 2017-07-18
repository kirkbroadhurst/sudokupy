from moves import find_possible_moves, find_impossible_moves, resolve_moves


def test_find_possible_moves_1():
    # the first item, with value 0, is 'missing'. find_possible_moves will tell us it should be a 9.
    state = [((i,i), i) for i in range(9)]    
    moves = find_possible_moves(state)

    assert len(moves) == 1
    assert moves[0][0] == (0,0)
    assert moves[0][1] == 9

def test_find_possible_moves_2():
    # the first and last items have value 0
    state = [((i,i), i if i < 8 else 0) for i in range(9)]    
    moves = find_possible_moves(state)

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

def test_find_impossible_moves_1():
    # the first item, with value 0, is 'missing'. find_impossible_moves will tell us it cannot be [1,2,3,4,5,6,7,8].
    state = [((i,i), i) for i in range(9)]
    moves = find_impossible_moves(state)

    assert len(moves) == 1
    assert moves[0][0] == (0,0)
    assert moves[0][1] == [1,2,3,4,5,6,7,8]

def test_find_impossible_moves_2():
    state = [((i,i), 0 if i%2==0 else i) for i in range(9)]
    moves = find_impossible_moves(state)

    assert len(moves) == 5
    for i, m in enumerate(moves):
        assert m[0] == (2*i,2*i)
        assert m[1] == [1,3, 5, 7]

def test_find_impossible_moves_3():
    state = [((i,i), 0) for i in range(9)]
    moves = find_impossible_moves(state)

    assert len(moves) == 9
    for i, m in enumerate(moves):
        assert m[0] == (i, i)
        # there are no impossible moves in this case
        assert m[1] == []
