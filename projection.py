import math
from src.vec.vec3 import Vec3
from src.mat.mat3 import get_rotation_matrix


def project_perspective(v: Vec3):
    fov = math.radians(45)
    xp = v.x / (v.z * math.tan(fov/2))
    yp = v.y / (v.z * math.tan(fov/2))
    return round(xp, 3), round(yp, 3)

def project_orthographic(v: Vec3):
    return v.x, v.y

vectors = [Vec3(2,2,3), Vec3(2,0,3), Vec3(0,2,3), Vec3(0,0,3)]

print("Original")
for v in vectors:
    print(project_perspective(v))

print("Rotated 90 deg")
vectors_2 = []
m = get_rotation_matrix(0, 0, 90)
for v in vectors:
    vectors_2.append(v.transform(m))

for v in vectors_2:
    print(project_perspective(v))
