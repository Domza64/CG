import numpy as np

from core.vec4 import Vec4


class Mat4:
    def __init__(self):
        self.M = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ], dtype=float)

    def multiply_vec4(self, v: Vec4):
        vec = np.array([v.x, v.y, v.z, v.w], dtype=float)
        new_vec = self.M @ vec
        return Vec4(*new_vec)


def translate(tx, ty, tz) -> "Mat4":
    m = Mat4()
    m.M = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1],
    ], dtype=float)
    return m

def scale(sx, sy, sz) -> "Mat4":
    m = Mat4()
    m.M = np.array([
        [sx, 0,  0,  0],
        [0,  sy, 0,  0],
        [0,  0,  sz, 0],
        [0,  0,  0,  1],
    ], dtype=float)
    return m

def rotate(x, y, z) -> "Mat4":
    # TODO: Finish for other axies, make matrice for each and then multiply
    c = np.cos(y)
    s = np.sin(y)

    m = Mat4()
    m.M = np.array([
        [ c, 0, s, 0],
        [ 0, 1, 0, 0],
        [-s, 0, c, 0],
        [ 0, 0, 0, 1],
    ], dtype=float)
    return m