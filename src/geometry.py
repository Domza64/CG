
from src.vec.vec3 import Vec3
from math import sqrt, acos, degrees

def distance(a: Vec3, b: Vec3):
    return sqrt((a.x-b.x)**2 + (a.y-b.y)**2 + (a.z-b.z)**2)

def angle(a: Vec3, b: Vec3, eps=1e-9):
    la = a.length()
    lb = b.length()

    if la < eps or lb < eps:
        return 0.0

    dot = a.dot(b)

    # Cosine inverse of dot prodiuct devided by lengths gives angle between vectors
    cos = dot / (la * lb)
    cos = max(-1.0, min(1.0, cos))
    rad = acos(cos)
    return degrees(rad)

def are_collinear(a, b, c):
    va = Vec3(a[0], a[1], a[2])
    vb = Vec3(b[0], b[1], b[2])
    vc = Vec3(c[0], c[1], c[2])
    
    va.sub(vc)
    vb.sub(vc)

    cross = va.cross(vb)

    return cross.is_zero()