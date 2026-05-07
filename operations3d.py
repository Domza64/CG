from src.mat.mat3 import get_rotation_matrix, get_scale_matrix
from src.vec.vec3 import Vec3

v1 = Vec3(1,2,3)
m1 = get_scale_matrix(2,2,2)
m2 = get_rotation_matrix(90, 0, 0)

print(v1.transform(m1)) # -> (2,4,6)
print(v1.transform(get_rotation_matrix(0, 90, 0))) # -> (3,2,-1)
print(v1.transform(get_rotation_matrix(0, 0, 90))) # -> (-2,1,3)