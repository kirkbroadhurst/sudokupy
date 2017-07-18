from sudoku import play_single_gaps, make_move
import numpy
import pytest


def test_play_single_gaps():
    # this is a game with only one missing move
    board = numpy.loadtxt('games/001.txt')
    assert board[(0,0)] == 0
    play_single_gaps(board)
    assert board[(0,0)] != 0

def test_make_move():
    board = numpy.loadtxt('games/001.txt')
    with pytest.raises(ValueError):
        make_move(board, ((8,8),8))