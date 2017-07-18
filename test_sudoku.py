from sudoku import play_single_gaps, make_move
import numpy
import pytest


def test_play_single_gaps_1():
    # this is a game with only one missing move
    board = numpy.loadtxt('games/001.txt')
    assert board[(0,0)] == 0
    result, possible, impossible = play_single_gaps(board)
    assert board[(0,0)] != 0
    assert result
    assert possible == []
    assert impossible == []

def test_play_single_gaps_2():
	board = numpy.loadtxt('games/empty.txt')
	result, possible, impossible = play_single_gaps(board)
	assert not result
	assert len(possible) == 27
	assert len(impossible) == 81 # these are flattened into individual squares

def test_make_move():
    board = numpy.loadtxt('games/001.txt')
    with pytest.raises(ValueError):
        make_move(board, ((8,8),8))