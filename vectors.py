from src.vec.vec3 import Vec3
from src.geometry import distance, angle, are_collinear

a = Vec3(1, 2, 3)
b = Vec3(4, 5, 6)
print(a.add(b))       # (5, 7, 9)

a = Vec3(1, 2, 3)
b = Vec3(4, 5, 6)
print(a.sub(b))       # (-3, -3, -3)

a = Vec3(1, 2, 3)
b = Vec3(4, 5, 6)
print(a.dot(b))       # 32

a = Vec3(1, 2, 3)
b = Vec3(4, 5, 6)
print(a.cross(b))     # (-3, 6, -3)

a = Vec3(1, 2, 3)
print(round(a.length(), 3))  # 3.742

a = Vec3(1, 2, 3)
print(a.normalize())  # ~ (0.27, 0.53, 0.8)

dis = distance(Vec3(0,0,0), Vec3(3,4,0))
print(dis)            # 5

print("-----------")

print(angle(Vec3(2,2,-1), Vec3(5,-3,2))) # ~83,8 degrees
print(angle(Vec3(1,0,0), Vec3(1,0,0))) # 0

print("A:", are_collinear((0,0,0), (-1,-1,-1), (3,3,3))) # True
print("B:", are_collinear((3,3,3), (1,1,1), (1,2,5))) # False
