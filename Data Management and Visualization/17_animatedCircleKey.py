import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)


x, y = 5, 5
circle = Circle((x, y), 0.5, color="blue")
ax.add_patch(circle)

dx = 0.05  

def init():
    circle.center = (x, y)
    return circle,

def animate(frame):
    global x
    x += dx


    if x > 9.5:
        x = 0.5

    circle.center = (x, y)
    return circle,


def on_key(event):
    global x, y

    step = 0.3

    if event.key == "left":
        x -= step
    elif event.key == "right":
        x += step
    elif event.key == "up":
        y += step
    elif event.key == "down":
        y -= step

    x = max(0.5, min(9.5, x))
    y = max(0.5, min(9.5, y))

    circle.center = (x, y)
    fig.canvas.draw_idle()

fig.canvas.mpl_connect("key_press_event", on_key)

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=200,
    init_func=init,
    interval=30,
    blit=True
)

plt.show()