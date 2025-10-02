import torch.nn as nn
import torch.nn.functional as F
from utils import constants as const

class ChessModel(nn.Module):
    def __init__(self):
        super().__init__()
        # Define the neural network layers

        #input consists of 256 values (64 squares * 4 bits per square)
        #layer1 will have 512 connections to the next layer. 512 nodes was chosen
        #to give the model more capacity to learn complex patterns.
        self.layer1 = nn.Linear(256, 512) 

        #layer2 will take 512 values from layer1.
        #layer2 will have 256 connections to the next layer.
        self.layer2 = nn.Linear(512, 256)

        #layer3 will take 256 values from layer2.
        #layer3 will have 1 connection to the output layer, which will be the value fed to the search algorithm.
        self.layer3 = nn.Linear(256, 1)

    #values is the input to the model
    #from the chessboard function board_state().
    def forward(self, values):

        #Apply ReLU activation function after each layer except the last one
        #ReLU was chosen for its efficiency and effectiveness in deep learning
        #models because it helps to mitigate the vanishing gradient problem.
        values = F.relu(self.layer1(values))
        values = F.relu(self.layer2(values))
        return self.layer3(values)