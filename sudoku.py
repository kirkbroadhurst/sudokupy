from itertools import groupby
import numpy as np

# board = np.zeros((9,9))
board = np.loadtxt('games/001.txt')

def places(game, f):
	result = [((x,y), game[(x,y)]) for x in range(9) for y in range(9)]
	if f is not None:
		result = [list(x[1]) for x in groupby(sorted(result,key=f), f)]
	return result

def rows(game):	
	return places(game, lambda x: x[0][0])

def cols(game):
	return places(game, lambda x: x[0][1])

def boxes(game):
	f = lambda x: (int(x[0][0]/3), int(x[0][1]/3))
	return places(game, f)


#print (board)

#print (rows(board)[0])
#print (cols(board)[0])
print (boxes(board))