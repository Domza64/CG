import tkinter as tk

# Window setup
WIDTH, HEIGHT = 600, 600
SCALE = 100
root = tk.Tk()
root.title("Cube")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

r = 2
get_vertices = None

def to_screen(x, y):
    screen_x = WIDTH // 2 + x * SCALE
    screen_y = HEIGHT // 2 - y * SCALE
    return screen_x, screen_y

def start():
    canvas.delete("all")

    # canvas.create_line(x1, y, x2, y, fill="white", width=2)
    for v in (get_vertices()):
        x, y = to_screen(v[0], v[1])
        canvas.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill="white",
            outline=""
        )

    root.after(20, start)

def draw(callback):
    global get_vertices
    get_vertices = callback
    start()
    root.mainloop()

