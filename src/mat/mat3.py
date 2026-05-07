import numpy as np

class Mat3:
    def __init__(self, m):
        if False: # TODO
            raise ValueError("Wrong dimensions")
        self.mat = m

    def matrix(self):
        return np.matrix(self.mat)
    
    def get_inverse(self):
        return Mat3(self.matrix().getI().tolist())