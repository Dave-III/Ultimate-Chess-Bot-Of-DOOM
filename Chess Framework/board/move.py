from Chessboard import Chessboard


class Move:

    def __init__ (self, start_pos, end_pos, piece_moved, piece_captured):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.piece_moved = piece_moved
        self.piece_captured = piece_captured

    def move_piece(self, board):
        # Unpack the start and end position tuples
        start_row, start_col = self.start_pos
        end_row, end_col = self.end_pos

        # Move the piece on the board
        board.board[end_row][end_col] = self.piece_moved
        board.board[start_row][start_col] = ' '  # Empty the starting square

        return board
    
