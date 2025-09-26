from Chessboard import Chessboard
from utils import constants as const

class Move:

    def __init__ (self, start_pos, end_pos, piece_moved, piece_captured):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.piece_moved = piece_moved
        self.piece_captured = piece_captured