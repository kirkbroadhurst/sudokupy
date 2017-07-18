"""
functions that analyze positions/values and identify appropriate moves
"""

from navigation import *
from itertools import groupby

valid = [1,2,3,4,5,6,7,8,9]


def find_possible_moves(moveset):
    """ finds any move(s) with value 0 in a single set of squares
        returns a list of potential moves, i.e. ((x,y), value)
    """
    values = [v for v in valid if v not in [m[1] for m in moveset if m[1] != 0]]
    return [(m[0], v) for m in moveset if m[1] == 0 for v in values]

    missing = [m for m in moveset if m[1] == 0]
    if len(missing) == 1:
        values = [v for v in valid if v not in [m[1] for m in moveset if m[1] != 0]][0]
        return [(missing[0][0], values)]


def find_impossible_moves(moveset):
    """ finds empty spaces and reports which values cannot be placed there
    """
    values = [v[1] for v in moveset if v[1] != 0]
    return [(v[0], values) for v in moveset if v[1] == 0]


def flatten_impossible_moves(movesets):
    """ movesets: a collection of items each representing the impossible moves 
        (e.g. (3,3) can't be a 4,5, or 6) for each of the 9-item sets
    
    flattens these by unioning the impossible moves for each location.
    """
    g = groupby(sorted((m for ms in movesets for m in ms), key=lambda x: x[0]), lambda x: x[0])
    return [(x, set([val for yy in y for val in yy[1]])) for (x,y) in g]


def resolve_moves(possible_moves, impossible_moves=[]):
    """
    possible_moves: sets of potentially valid moves within each 9-item set (row/col/box)
    
    resolve which 'possible moves' are valid across those collections
    if there is only one possible move across collections then it is a necessary move
    if there is no possible move across collections then something is wrong
    if there are multiple possible moves, continue

    returns set of necessary moves
    """
    moves = []
    impossible = dict(impossible_moves)

    for place in places():
        # find matching moves from each 9-item set that apply to this 'place'; get the possible values from each (drop the place)
        sets = [set(m[1] for m in ms if place in m) for ms in possible_moves if any(place in m for m in ms)]

        if not any(sets):
            continue        
        
        # find which values would be valid according to each 9-item sets' constraints
        valid_moves = sets[0].intersection(*sets)
        if place in impossible:
            valid_moves = valid_moves - set(impossible[place])

        if len(valid_moves) == 0:
            raise ValueError(place)
        elif len(valid_moves) == 1:
            moves.append((place, valid_moves.pop()))        
            
    return moves

