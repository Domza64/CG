import numpy as np
from src.mat.mat2 import Mat2

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def transform(self, m: Mat2):
        transformed = (m.matrix() * self.matrix()).tolist()
        new_x = transformed[0][0]
        new_y = transformed[1][0]
        
        return Vec2(new_x, new_y)

    def matrix(self):
        return np.matrix([[self.x], [self.y]]) 