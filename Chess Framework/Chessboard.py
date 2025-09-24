class ChessBoard:
    #dictionary used for returning piece names
    PIECE_MAP = {' ': "EMPTY", 'R': "WHITE_ROOK",'N': "WHITE_KNIGHT",'B': "WHITE_BISHOP",'Q': "WHITE_QUEEN",
                 'K': "WHITE_KING",'P': "WHITE_PAWN",'r': "BLACK_ROOK",'n': "BLACK_KNIGHT",
                 'b': "BLACK_BISHOP",'q': "BLACK_QUEEN",'k': "BLACK_KING",'p': "BLACK_PAWN"}

    #dictionary used for board state representation
    PIECE_INDEX = {' ': "0",'R': "1",'N': "2",'B': "3",'Q': "4",
                   'K': "5",'P': "6",'r': "7",'n': "8",
                   'b': "9",'q': "10",'k': "11",'p': "12"}
    
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
        # Print the board in a readable format
        for row in self.board:
            print(' '.join(row))
        print()

    def board_state(self):

        # Create a string representation of the board using piece indices
        board = ""

        # Iterate through each row and piece to build the string
        for row in self.board:
            for piece in row:
                board += self.PIECE_INDEX[piece]
                board += " "
        
        return board
    
    def return_position(self, position):
        # Unpack the position tuple
        row, col = position 

        # Checks for valid indices
        if row < 0 or row > 7 or col < 0 or col > 7: 
            return "INVALID POSITION"
        
        # Get the piece at the specified position and return its name
        piece = self.board[row][col]
        return self.PIECE_MAP[piece]

# Example usage
if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.display()
    print(chess_board.board_state()) # Display board state as string of indices

    # Get user input for a position
    x = input("Enter row: ")
    y = input("Enter column: ")
    user_input = (int(x), int(y)) # Convert input to tuple of integers
    print(chess_board.return_position((user_input))) # Get piece at user-defined position