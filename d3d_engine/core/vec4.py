class Vec4:
    def __init__(self, x=0, y=0, z=0, w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def scale(self, s) -> "Vec4":
        return Vec4(self.x * s, self.y * s, self.z * s, self.w)
