import numpy
from sudoku import play_single_gaps
from navigation import sets
from moves import find_moves, resolve_moves


def test_resolve_game_1():
    board = numpy.loadtxt('games/008.txt')
    again, possible_moves = play_single_gaps(board)

    resolved_moves = resolve_moves(possible_moves)

    assert len(resolved_moves) > 1


def test_resolve_game_2():
    board = numpy.loadtxt('games/008.txt')
    movesets = []
    for moveset in sets(board):
        movesets.append(find_moves(moveset))
    
    resolved_moves = resolve_moves(movesets)

    print (resolved_moves[0:5])
    assert len(resolved_moves) > 1