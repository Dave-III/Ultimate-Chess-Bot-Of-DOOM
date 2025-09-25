    #dictionary used for returning piece names
PIECE_MAP = {' ': "EMPTY", 'R': "WHITE_ROOK",'N': "WHITE_KNIGHT",'B': "WHITE_BISHOP",'Q': "WHITE_QUEEN",
             'K': "WHITE_KING",'P': "WHITE_PAWN",'r': "BLACK_ROOK",'n': "BLACK_KNIGHT",
             'b': "BLACK_BISHOP",'q': "BLACK_QUEEN",'k': "BLACK_KING",'p': "BLACK_PAWN"}

    #dictionary used for returning piece indices represented in binary format (1st digit is color, 2-4 is piece type)
PIECE_INDEX = {' ': [0,0,0,0],'R': [0,0,0,1],'N': [0,0,1,0],'B': [0,0,1,1],'Q': [0,1,0,0],
               'K': [0,1,0,1],'P': [0,1,1,0],'r': [1,0,0,0],'n': [1,0,0,1],'b': [1,0,1,0],
               'q': [1,0,1,1],'k': [1,1,0,0],'p': [1,1,0,1]}
    
#dictionary used for returning square color (1 is white, 0 is black)
SQUARE_MAP = [1,0,1,0,1,0,1,0,
              0,1,0,1,0,1,0,1,
              1,0,1,0,1,0,1,0,
              0,1,0,1,0,1,0,1,
              1,0,1,0,1,0,1,0,
              0,1,0,1,0,1,0,1,
              1,0,1,0,1,0,1,0,
              0,1,0,1,0,1,0,1]