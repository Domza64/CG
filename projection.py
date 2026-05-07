import math
from src.vec.vec3 import Vec3
from src.mat.mat3 import get_rotation_matrix
from src.draw_vertices import draw

FOV = 45
CAMERA_DISTANCE = 10

def project_perspective(v: Vec3):
    fov = math.radians(FOV)
    xp = v.x / (v.z * math.tan(fov/2))
    yp = v.y / (v.z * math.tan(fov/2))
    # print("Projected: ", round(xp, 3), round(yp, 3))
    return round(xp, 3), round(yp, 3)

cube = [Vec3(-2, 2, -2), Vec3(2, 2, -2), 
           Vec3(-2, -2, -2), Vec3(2, -2, -2),
           
           Vec3(-2, 2, 2), Vec3(2, 2, 2), 
           Vec3(-2, -2, 2), Vec3(2, -2, 2)
           ]

piramid = [Vec3(0, 1, 0), Vec3(-1.2, -0.8, 0), 
           Vec3(1.2, -0.8, 0), Vec3(0, 0, 2)
           ]

def get_vertices():
    m = get_rotation_matrix(0.5, 2.5, 1.5)
    projected = []

    for vec in cube:
        rotated = vec.transform(m)
        vec.x = rotated.x
        vec.y = rotated.y
        vec.z = rotated.z
        projected.append(rotated)

    for vec in projected:
        vec.z -= CAMERA_DISTANCE

    return [project_perspective(v) for v in projected]

draw(get_vertices)