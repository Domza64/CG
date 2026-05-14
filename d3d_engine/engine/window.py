import tkinter as tk

class Window:
    def __init__(self, width=800, height=600):
        self.root = tk.Tk()

        self.canvas = tk.Canvas(
            self.root,
            width=width,
            height=height,
            bg="black"
        )

        self.canvas.pack()

        self.keys = set()

        keys = ["Left", "Right", "Up", "Down", "w", "a", "s", "d"]

        for key in keys:
            self.root.bind(f"<KeyPress-{key}>", self.on_key_press)
            self.root.bind(f"<KeyRelease-{key}>", self.on_key_release)

    def on_key_press(self, event):
        self.keys.add(event.keysym)

    def on_key_release(self, event):
        self.keys.discard(event.keysym)

    def run(self):
        self.root.mainloop()