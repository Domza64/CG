from typing import List

from core.mat4 import translate, rotate
from engine.window import Window
from geometry.mesh import Mesh
from renderer.camera import Camera, make_view, make_perspective
from renderer.renderer import Renderer
from scenes.cube_scene import create_cube
from scenes.plane_scene import create_plane

WIDTH = 800
HEIGHT = 600

def main():
    window = Window(WIDTH, HEIGHT)
    camera = Camera()

    camera.V = make_view(4, 1, -4)
    camera.P = make_perspective(45, WIDTH / HEIGHT, 1, 10)

    renderer = Renderer(
        window.canvas,
        camera,
        WIDTH,
        HEIGHT
    )

    cube: Mesh = create_cube()
    plane: Mesh = create_plane()

    plane.move(translate(0, 0, 5))
    plane.rotate(rotate(0, 1, 0))
    cube.move(translate(0, 0, 5))

    meshes: List[Mesh] = [cube, plane]

    def handle_input():
        if "Left" in window.keys:
            cube.move(translate(-0.1, 0, 0))
        elif "Right" in window.keys:
            cube.move(translate(0.1, 0, 0))
        elif "Up" in window.keys:
            cube.move(translate(0, 0, 0.1))
        elif "Down" in window.keys:
            cube.move(translate(0, 0, -0.1))
        elif "w" in window.keys:
            cube.move(translate(0, -0.1, 0))
        elif "s" in window.keys:
            cube.move(translate(0, 0.1, 0))
        elif "d" in window.keys:
            cube.rotate(rotate(0,-0.05,0))
        elif "a" in window.keys:
            cube.rotate(rotate(0,0.05,0))

    def update():
        handle_input()
        window.canvas.delete("all")

        for mesh in meshes:
            renderer.draw_mesh(mesh)

        window.root.after(16, update)

    update()
    window.run()


if __name__ == "__main__":
    main()