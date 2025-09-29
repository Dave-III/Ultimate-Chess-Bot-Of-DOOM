from board.Chessboard import ChessBoard

def main():
    chess_board = ChessBoard()
    chess_board.display()
    print(chess_board.board_state())
    print(chess_board.board_to_FEN())

if __name__ == "__main__":
    main()