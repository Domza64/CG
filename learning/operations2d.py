from src.mat.mat2 import Mat2
from src.vec.vec2 import Vec2
from src.draw2d import draw
import math

v1 = Vec2(3,2)
m1 = Mat2([[2,0], [0,2]])

def get_scale_matrix(scale_x, scale_y):
    return Mat2([[scale_y, 0], [0, scale_x]])

def get_rotation_matrix(degrees):
    theta = math.radians(degrees)
    return Mat2([
        [math.cos(theta), -math.sin(theta)],
        [math.sin(theta), math.cos(theta)]
    ])

m2 = get_scale_matrix(2,5)

print("V1:", v1)

v2 = v1.transform(m2)

print("V2:", v2)

# Should be same as v1
v3 = v2.transform(m2.get_inverse())
print("V3:", v3)

m3 = get_rotation_matrix(-90)
v4 = v1.transform(m3)

draw(v2, v3, v4)