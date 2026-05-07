import numpy as np
import math

class Mat3:
    def __init__(self, m):
        if False: # TODO
            raise ValueError("Wrong dimensions")
        self.mat = m

    def matrix(self):
        return np.matrix(self.mat)
    
    def get_inverse(self):
        return Mat3(self.matrix().getI().tolist())
    
def get_scale_matrix(scale_x, scale_y, scale_z):
    return Mat3([
            [scale_x, 0, 0],
            [0, scale_y, 0],
            [0, 0, scale_z]
        ])

def get_rotation_matrix(x_deg, y_deg, z_deg):
    theta_x = math.radians(x_deg)
    theta_y = math.radians(y_deg)
    theta_z = math.radians(z_deg)

    mat_x = np.matrix([
        [1, 0, 0],
        [0, math.cos(theta_x), -math.sin(theta_x)],
        [0, math.sin(theta_x), math.cos(theta_x)]
    ])

    mat_y =  np.matrix([
        [math.cos(theta_y), 0, math.sin(theta_y)],
        [0, 1, 0],
        [-math.sin(theta_y), 0, math.cos(theta_y)]
    ])

    mat_z =  np.matrix([
        [math.cos(theta_z), -math.sin(theta_z), 0],
        [math.sin(theta_z), math.cos(theta_z), 0],
        [0, 0, 1]
    ])

    # Applies Z first, then Y, then X
    return Mat3((mat_x * mat_y * mat_z).tolist())