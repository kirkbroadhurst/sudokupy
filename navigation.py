"""
functions that identify/retrieve positions and values on sudoku board    
"""

from itertools import groupby, chain

def places():
    """ all the positions on a board """
    return ((x,y) for x in range(9) for y in range(9))

def squares(game, f=None):
    """ all the positions and values on the board
    f = group the positions according to some function of the (x,y) location (to slice rows, cols, boxes) """ 
    result = ((p, game[p]) for p in places())
    return result if f is None else (list(x[1]) for x in groupby(sorted(result,key=f), f))

def rows(game):    
    """ horizontal groups of squares """
    return squares(game, lambda x: x[0][0])

def cols(game):
    """ vertical groups of squares """
    return squares(game, lambda x: x[0][1])

def boxes(game):
    """ groups of squares in 9-block formation """
    f = lambda x: (int(x[0][0]/3), int(x[0][1]/3))
    return squares(game, f)

def sets(game):
    """ all the groups applicable to a game of sudoku """
    return chain(rows(game), cols(game), boxes(game))    