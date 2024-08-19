import random
import numpy as np


class Tubes:

    def __init__(self, screen_dim):
        self.tube_ygap = 150
        self.tube_width = 75
        self.tube_xgap = self.tube_width*4
        self.x = screen_dim[0] - self.tube_width
        self.tube_heights = np.random.randint(low=screen_dim[1]*0.25, high=screen_dim[1]*0.75, size=(200))
        

    def updateTubePosition(self):
        self.x -= 2
        return self.tube_heights