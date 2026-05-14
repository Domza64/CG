from core.vec4 import Vec4
from geometry.mesh import Mesh
from renderer.camera import Camera


def ndc(v: Vec4):
    if v.w == 0:
        return None

    return Vec4(
        v.x / v.w,
        v.y / v.w,
        v.z / v.w,
        1
    )


class Renderer:
    def __init__(self, canvas, camera, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.camera: Camera = camera


    def transform(self, v: Vec4, mesh: Mesh) -> Vec4:
        world: Vec4 = mesh.mat.multiply_vec4(v)
        view: Vec4 = self.camera.V.multiply_vec4(world)
        clip: Vec4 = self.camera.P.multiply_vec4(view)

        return clip

    def to_screen(self, v: Vec4):
        x = (v.x + 1) * 0.5 * self.width
        y = (1 - v.y) * 0.5 * self.height
        return x, y

    def draw_mesh(self, mesh: Mesh):
        for edge in mesh.edges:
            a = self.transform(edge.a.position, mesh)
            b = self.transform(edge.b.position, mesh)

            a_ndc = ndc(a)
            b_ndc = ndc(b)

            if a_ndc is None or b_ndc is None:
                continue

            ax, ay = self.to_screen(a_ndc)
            bx, by = self.to_screen(b_ndc)

            self.canvas.create_line(ax, ay, bx, by, fill="white")
