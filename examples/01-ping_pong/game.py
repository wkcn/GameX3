import gamex
import time
import numpy as np

WIDTH, HEIGHT = 800, 600
window = gamex.create_window('ping pong!', (WIDTH, HEIGHT))
boundary_width = 10
boundary_interval = 15
boundary_img = np.zeros((HEIGHT, boundary_width, 3), dtype=np.uint8)
boundary_img.reshape((-1, 2, boundary_interval, boundary_width, 3))[:, 0] = 255

screen = window.get_surface()

delta_time = 1.0 / 60.0

def draw_boundary(screen):
    data = screen.data()
    x = (WIDTH - boundary_width) // 2
    data[:, x:x+boundary_width] = boundary_img


tic = time.time()

while window.running():
    screen.fill((0, 0, 0))
    draw_boundary(screen)

    toc = time.time()
    delta_time = toc - tic
    tic = toc

    window.tick(delta_time)
