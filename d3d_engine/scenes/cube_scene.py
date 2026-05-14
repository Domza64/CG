from typing import List, Tuple

from geometry.mesh import Mesh
from geometry.vertex import Vertex
from geometry.edge import Edge
from core.vec4 import Vec4

def create_cube() -> Mesh:
    mesh = Mesh()

    verts: List[Vertex] = [
        Vertex(Vec4(-1,-1,-1)),
        Vertex(Vec4( 1,-1,-1)),
        Vertex(Vec4( 1, 1,-1)),
        Vertex(Vec4(-1, 1,-1)),

        Vertex(Vec4(-1,-1, 1)),
        Vertex(Vec4( 1,-1, 1)),
        Vertex(Vec4( 1, 1, 1)),
        Vertex(Vec4(-1, 1, 1)),
    ]

    mesh.vertices = verts

    indices: List[Tuple[int, int]] = [
        (0,1),(1,2),(2,3),(3,0),
        (4,5),(5,6),(6,7),(7,4),
        (0,4),(1,5),(2,6),(3,7)
    ]

    for a, b in indices:
        mesh.edges.append(Edge(verts[a], verts[b]))

    return mesh