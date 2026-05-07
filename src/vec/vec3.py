from math import sqrt

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other_vector):
        self.x += other_vector.x
        self.y += other_vector.y
        self.z += other_vector.z
        return self

    def sub(self, other_vector):
        self.x -= other_vector.x
        self.y -= other_vector.y
        self.z -= other_vector.z
        return self

    def mul(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self

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

    def length(self): # Also called magnitute or norm
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        len = self.length()
        return Vec3(self.x/len, self.y/len, self.z/len)
    
    def is_zero(self, eps=1e-9):
        return self.length() < eps

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"