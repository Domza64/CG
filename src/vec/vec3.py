from math import sqrt
import numpy as np
from src.mat.mat3 import Mat3

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vec3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def sub(self, other):
        return Vec3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def mul(self, scalar):
        return Vec3(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    def dot(self, other_vector):
        dot = 0
        dot += self.x * other_vector.x
        dot += self.y * other_vector.y
        dot += self.z * other_vector.z
        return dot

    def cross(self, other_vector):
        cross_x = self.y * other_vector.z - self.z * other_vector.y
        cross_y = self.z * other_vector.x - self.x * other_vector.z
        cross_z = self.x * other_vector.y - self.y * other_vector.x

        return Vec3(cross_x, cross_y, cross_z)
    
    def transform(self, m: Mat3):
        transformed = (m.matrix() * self.matrix()).tolist()
        new_x = transformed[0][0]
        new_y = transformed[1][0]
        new_z = transformed[2][0]
        
        return Vec3(new_x, new_y, new_z)
    
    def matrix(self):
        return np.matrix([[self.x], [self.y], [self.z]])

    def length(self): # Also called magnitute or norm
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        leng = self.length()
        return Vec3(self.x/leng, self.y/leng, self.z/leng)
    
    def is_zero(self, eps=1e-9):
        return self.length() < eps

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"