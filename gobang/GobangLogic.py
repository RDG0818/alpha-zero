import numpy as np
'''
Author: Ryan Goodwin
Date: Feb 6, 2025
Board class, implemented with numpy.
Board data:
  1=white, -1=black, 0=empty
  first dim is column , 2nd is row:
     pieces[1, 7] is the square in column 2,
     at the opposite end of the board in row 8.

'''
class Board():
    def __init__(self, n):
        "Set up initial board configuration."
        self.n = n
        # Create the empty board array.
        self.pieces = np.zeros((n, n), dtype=np.int32)

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black
        """
        empty_positions = np.argwhere(self.pieces == 0)  # Returns a list of (row, col) indices
        return [tuple(pos) for pos in empty_positions]  # Convert to list of tuples

    def has_legal_moves(self):
        """Returns True if has legal move else False
        """
        # Get all empty locations.
        return np.any(self.pieces == 0)

    def execute_move(self, move, color):
        """Places a piece of the given color on the board at the specified move position."""
        x, y = move
        assert self.pieces[x, y] == 0, "Invalid move: Position already occupied."
        self.pieces[x, y] = color

