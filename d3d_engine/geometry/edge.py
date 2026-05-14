from geometry.vertex import Vertex


class Edge:
    def __init__(self, a: Vertex, b: Vertex):
        self.a = a
        self.b = b