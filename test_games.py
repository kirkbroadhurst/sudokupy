from sudoku import play_game, is_complete
import numpy

def test_game_1():
    board = numpy.loadtxt('games/001.txt')
    play_game(board)
    assert is_complete(board)

def test_game_2():
    board = numpy.loadtxt('games/002.txt')
    play_game(board)
    assert is_complete(board)

def test_game_3():
    board = numpy.loadtxt('games/003.txt')
    play_game(board)
    assert is_complete(board)

def test_game_4():
    board = numpy.loadtxt('games/004.txt')
    play_game(board)
    assert is_complete(board)    

def test_game_5():
    board = numpy.loadtxt('games/005.txt')
    play_game(board)
    assert is_complete(board)

def test_game_6():
    board = numpy.loadtxt('games/006.txt')
    play_game(board)
    assert is_complete(board)

'''
def test_game_7():
    board = numpy.loadtxt('games/007.txt')
    play_game(board)
    print(board)
    assert is_complete(board)
'''