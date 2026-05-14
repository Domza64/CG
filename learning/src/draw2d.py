import matplotlib.pyplot as plt

def draw(*vectors):
    plt.figure(figsize=(6,6))

    # draw axes
    plt.axhline(0)
    plt.axvline(0)

    # draw vectors
    for v in vectors:
        x, y = v.x, v.y
        
        plt.quiver(
            0, 0,
            x, y,
            angles='xy',
            scale_units='xy',
            scale=1
        )

    # limits
    plt.xlim(-15, 15)
    plt.ylim(-15, 15)

    # keep aspect ratio square
    plt.gca().set_aspect('equal')

    plt.grid()
    plt.show()