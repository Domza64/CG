import numpy as np

class Mat2:
    def __init__(self, m):
        self.m = m

    def matrix(self):
        return np.matrix(self.m)
    
    def get_inverse(self):
        return Mat2(np.matrix(self.m).getI().tolist())