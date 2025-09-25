# ChessBot Project

Modern Chessbots are neural network based AI's that approach moves based on highest probability application. Or in otherwords, they will import the current board instance and color they're playing to calculate the next best move.

Framework v1:
- Board data format for easy AI digestion. (use 5 bit binary formatting for encoding) first 2 bits for black and white, last 3 bits for piece type.
- Neural network incorperating of a five move plan based on heighest probability of moves on both sides of the board.

To do:
- Setup a dataframework to feed to the Neural Network. (Ideally as close to training data format as we can)
- Setup a basic Neural Network oriented around a certain training data format. (Also figure out how to setup an NN)
- Once base training is complete, could train it by playing against itself. (Alpha-Zero)
- Generate a format to convert a player move into digestible data.

All player input and visualization can be handled later.

framework for filing our code:

│
├── main.py              # Entry point (runs the bot / plays games)
│
├── board/
│   ├── chess_board.py   # Your ChessBoard class (board state, FEN, display)
│   ├── move.py          # Move class (start, end, captured, promotion, etc.)
│   └── fen.py           # Optional: helper functions for FEN parsing
│
├── engine/
│   ├── move_generator.py # Generates pseudo-legal moves
│   ├── validator.py      # Checks legality (e.g., king in check)
│   ├── search.py         # For Terrie to work on
│   └── evaluation.py     # Hooks into neural net or classical eval
│
├── nn/
│   ├── model.py          # Neural network definition (PyTorch or custom)
│   ├── trainer.py        # Training loop, dataset handling
│   └── encode.py         # Encode board state → NN input tensor
│
└── utils/
    ├── constants.py      # Piece maps, square colors, etc.
    └── helpers.py        # Debugging, logging, timing, etc.
