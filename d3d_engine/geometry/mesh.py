from typing import List

from core.mat4 import Mat4
from geometry.edge import Edge
from geometry.vertex import Vertex


class Mesh:
    def __init__(self):
        self.mat: Mat4 = Mat4()
        self.vertices: List[Vertex] = []
        self.edges: List[Edge] = []

    def move(self, mat: Mat4):
        new_pos = self.mat.M @ mat.M
        new_mat = Mat4()
        new_mat.M = new_pos
        self.mat = new_mat

    def rotate(self, mat: Mat4):
        new_pos = self.mat.M @ mat.M
        new_mat = Mat4()
        new_mat.M = new_pos
        self.mat = new_mat