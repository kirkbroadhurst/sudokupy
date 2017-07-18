import numpy
from sudoku import play_single_gaps
from navigation import sets
from moves import find_possible_moves, find_impossible_moves, resolve_moves, flatten_impossible_moves


def test_resolve_game_1():
    board = numpy.loadtxt('games/008.txt')
    again, possible_moves = play_single_gaps(board)

    resolved_moves = resolve_moves(possible_moves)
    assert len(resolved_moves) > 1

def test_resolve_game_2():
    board = numpy.loadtxt('games/008.txt')
    possible_moves = []
    impossible_moves = []
    for moveset in sets(board):
        possible_moves.append(find_possible_moves(moveset))
        impossible_moves.append(find_impossible_moves(moveset))
    
    resolved_moves = resolve_moves(possible_moves)
    assert len(resolved_moves) > 1

def test_flatten_impossible_moves_1():
    board = numpy.loadtxt('games/008.txt')
    impossible_moves = []
    for moveset in sets(board):
        impossible_moves.append(find_impossible_moves(moveset))

    flat_moves = flatten_impossible_moves(impossible_moves)
    print (flat_moves)
    assert 39 == len(flat_moves)

    d = dict(flat_moves)
    # spot check some for validation
    assert d[(4,0)] == set([2, 1, 4, 5, 7, 8, 9])
    assert d[(4,3)] == set([1,2, 4, 6, 9])
    assert d[(7,2)] == set([1, 2, 4, 5, 6, 7, 8, 9])