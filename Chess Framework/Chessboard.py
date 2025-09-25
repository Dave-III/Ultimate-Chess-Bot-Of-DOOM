import constants.py as const

class ChessBoard:
    def __init__(self):
        self.board = self.create_initial_board()

    def create_initial_board(self):
        # Initialize an 8x8 chess board with pieces in starting positions
        board = [[' ' for _ in range(8)] for _ in range(8)]
        # Place pawns
        for i in range(8):
            board[1][i] = 'p'  # Black pawns
            board[6][i] = 'P'  # White pawns
        # Place rooks
        board[0][0] = board[0][7] = 'r'
        board[7][0] = board[7][7] = 'R'
        # Place knights
        board[0][1] = board[0][6] = 'n'
        board[7][1] = board[7][6] = 'N'
        # Place bishops
        board[0][2] = board[0][5] = 'b'
        board[7][2] = board[7][5] = 'B'
        # Place queens
        board[0][3] = 'q'
        board[7][3] = 'Q'
        # Place kings
        board[0][4] = 'k'
        board[7][4] = 'K'
        return board

    def display(self):
        # Print the board in a readable format
        for row in self.board:
            print(' '.join(row))
        print()

    def board_state(self):

        # Create a string representation of the board using piece indices
        board = []

        # Iterate through each row and piece to build the nested list.
        for row in self.board:
            for piece in row:
                board.append(const.PIECE_INDEX[piece])
                    
        return board
    
    def return_position(self, position):
        # Unpack the position tuple
        row, col = position 

        # Checks for valid indices
        if row < 0 or row > 7 or col < 0 or col > 7: 
            return "INVALID POSITION"
        
        # Get the piece at the specified position and return its name
        piece = self.board[row][col]
        return const.PIECE_MAP[piece]

    def board_to_FEN(self):
        # Convert the board to Forsyth-Edwards Notation (FEN)
        fen = ""
        for row in self.board:
            empty_count = 0
            for piece in row:
                if piece == ' ':
                    empty_count += 1
                else:
                    if empty_count > 0:
                        fen += str(empty_count)
                        empty_count = 0
                    fen += piece
            if empty_count > 0:
                fen += str(empty_count)
            fen += '/'
        return fen[:-1]  # Remove the trailing '/'
    


# Example usage
if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.display()
    print(chess_board.board_state()) # Display board state as string of indices

    # Get user input for a position
    print(chess_board.board_to_FEN())
    x = input("Enter row: ")
    y = input("Enter column: ")
    user_input = (int(x), int(y)) # Convert input to tuple of integers
    print(chess_board.return_position((user_input))) # Get piece at user-defined position