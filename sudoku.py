"""
main module for playing sudoku
"""

import numpy as np
from navigation import *
from moves import find_possible_moves, resolve_moves, valid


def make_move(board, move):
    """ put a piece on the board, LOCK IT IN REGIS """
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
        moves = find_possible_moves(moveset)
        if moves is None or len(moves) == 0:
            continue
        elif len(moves) == 1:
            make_move(board, moves[0])
            return True, possible_moves
        else:
            possible_moves += [moves]
    return False, possible_moves


def is_complete(board):
    """ return True is board is complete and error free """
    valid_set = set(valid)
    for s in sets(board):
        if set(m[1] for m in s) != valid_set:
            return False
    return True


if __name__ == "__main__":
    board = np.loadtxt('games/003.txt')
    print (board)
    play_game(board)
    print (board)
