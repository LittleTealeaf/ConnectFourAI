import numpy as np

CHECK_DIRECTIONS = [lambda i: right(i), lambda i: down(i), lambda i: down(right(i)), lambda i: down(left(i))]

EMPTY: np.int8 = np.int8(0)
PLAYER1: np.int8 = np.int8(1)
PLAYER2: np.int8 = np.int8(2)
PLAYING: np.int8 = np.int8(3)
DRAW: np.int8 = np.int8(4)

def up(i):
    if i > 5:
        return i - 6
    else:
        return -1
def down(i):
    if i < 30:
        return i + 6
    else:
        return -1
def right(i):
    if i%6 < 5:
        return i + 1
    else:
        return -1
def left(i):
    if i%6 > 0:
        return i - 1
    else:
        return -1


class Game:
    def __init__(self):
        self.values = np.zeros(shape=(36),dtype=np.int8)
        self.player = PLAYER1


    def move(self,position):
        if position >= 0 and position < 36:
            if self.values[position] == EMPTY:
                self.values[position] = self.player
                if self.player == PLAYER1:
                    self.player = PLAYER2
                else:
                    self.player = PLAYER1
                return True
            else:
                return False
        else:
            return False



    # Some optimizations that can improve this function:
    # - Don't check directions cannot go to their extent
    def state(self):
        # Using nditer to iterate with index
        it = np.nditer(self.values,flags=['f_index'])
        # whether a move can still be played
        canPlay = False
        # iterate over the array
        for x in it:
            # set canPlay to true if its an empty spot
            if x == EMPTY:
                canPlay = True
            else:
                # For each check direction
                for dir in CHECK_DIRECTIONS:
                    # Set i to the index
                    i = it.index
                    # Default to a successful run (meaning the loop ended on exhaustion)
                    victory = True
                    for j in range(3):
                        # Step one value forward
                        i = dir(i)
                        # If it hit an edge, or the value is not the same
                        if i == -1 or self.values[i] != x:
                            victory = False
                            break
                    if victory:
                        return x
        if canPlay:
            return PLAYING
        else:
            return DRAW



    def __str__(self):
        return "\n".join(" ".join(str(i) for i in self.values[n:n+6]) for n in range(0,36,6))
