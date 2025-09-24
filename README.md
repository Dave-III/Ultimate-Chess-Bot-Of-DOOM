# ChessBot Project

Modern Chessbots are neural network based AI's that approach moves based on highest probability application. Or in otherwords, they will import the current board instance and color they're playing to calculate the next best move.

Framework v1:
- Board data format for easy AI digestion.
- Neural network incorperating of a five move plan based on heighest probability of moves on both sides of the board.

To do:
- Setup a dataframework to feed to the Neural Network. (Ideally as close to training data format as we can)
- Setup a basic Neural Network oriented around a certain training data format. (Also figure out how to setup an NN)
- Once base training is complete, could train it by playing against itself. (Alpha-Zero)
- Generate a format to convert a player move into digestible data.

All player input and visualization can be handled later.
