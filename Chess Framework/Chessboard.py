class ChessBoard:
    def __init__(self):
        self.board = self.create_initial_board()

    def create_initial_board(self):
        # Initialize an 8x8 chess board with pieces in starting positions
        board = [[' ' for _ in range(8)] for _ in range(8)]
        # Place pawns
        for i in range(8):
            board[1][i] = 'P'  # White pawns
            board[6][i] = 'p'  # Black pawns
        # Place rooks
        board[0][0] = board[0][7] = 'R'
        board[7][0] = board[7][7] = 'r'
        # Place knights
        board[0][1] = board[0][6] = 'N'
        board[7][1] = board[7][6] = 'n'
        # Place bishops
        board[0][2] = board[0][5] = 'B'
        board[7][2] = board[7][5] = 'b'
        # Place queens
        board[0][3] = 'Q'
        board[7][3] = 'q'
        # Place kings
        board[0][4] = 'K'
        board[7][4] = 'k'
        return board

    def display(self):
        for row in self.board:
            print(' '.join(row))
        print()

        


# Example usage
if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.display()