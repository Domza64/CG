import tkinter as tk
import math

# Window setup
WIDTH, HEIGHT = 600, 600
root = tk.Tk()
root.title("3D Cube")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Cube vertices
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
]

# Edges connecting vertices
edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

angle_x = 0
angle_y = 0

def rotate(point, ax, ay):
    x, y, z = point

    # Rotate around X axis
    cosx = math.cos(ax)
    sinx = math.sin(ax)
    y, z = y * cosx - z * sinx, y * sinx + z * cosx

    # Rotate around Y axis
    cosy = math.cos(ay)
    siny = math.sin(ay)
    x, z = x * cosy + z * siny, -x * siny + z * cosy

    return [x, y, z]

def project(point):
    x, y, z = point
    distance = 10
    factor = 1000 / (z + distance)
    x = x * factor + WIDTH / 2
    y = -y * factor + HEIGHT / 2
    return (x, y)

def draw():
    global angle_x, angle_y
    canvas.delete("all")

    rotated = [rotate(v, angle_x, angle_y) for v in vertices]
    projected = [project(v) for v in rotated]

    for edge in edges:
        x1, y1 = projected[edge[0]]
        x2, y2 = projected[edge[1]]
        canvas.create_line(x1, y1, x2, y2, fill="white", width=2)

    angle_x += 0.03
    angle_y += 0.02

    root.after(16, draw)

draw()
root.mainloop()