from typing import List, Tuple

from geometry.mesh import Mesh
from geometry.vertex import Vertex
from geometry.edge import Edge
from core.vec4 import Vec4

def create_plane() -> Mesh:
    mesh = Mesh()

    verts: List[Vertex] = [
        Vertex(Vec4(0,0,0)),
        Vertex(Vec4(0.5,0,0)),
        Vertex(Vec4( 0.5,0.5,0)),
        Vertex(Vec4(0,0.5,0))
    ]

    mesh.vertices = verts

    indices: List[Tuple[int, int]] = [
        (0,1),(1,2),(2,3),(3,0)
    ]

    for a, b in indices:
        mesh.edges.append(Edge(verts[a], verts[b]))

    return mesh