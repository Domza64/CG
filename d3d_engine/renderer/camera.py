import numpy as np
from core.mat4 import Mat4

class Camera:
    def __init__(self):
        self.V: Mat4 = Mat4()  # view
        self.P: Mat4 = Mat4()  # projection


def make_view(x, y, z) -> Mat4:
    m = Mat4()
    m.M = np.array([
        [1, 0, 0, -x],
        [0, 1, 0, -y],
        [0, 0, 1, -z],
        [0, 0, 0, 1],
    ], dtype=float)
    return m

def make_perspective(fov, aspect, near, far) -> Mat4:
    f = 1 / np.tan(np.radians(fov) / 2)

    m = Mat4()
    m.M = np.array([
        [f/aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far+near)/(near-far), (2*far*near)/(near-far)],
        [0, 0, -1, 0],
    ], dtype=float)

    return m