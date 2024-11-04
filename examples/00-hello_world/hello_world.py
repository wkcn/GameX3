import gamex
import time

window = gamex.create_window('hello world', (800, 600))

delta_time = 1.0 / 60.0

img = gamex.image.load('./res/MiraiX.png')
se = gamex.audio.load('./res/button.mp3')
screen = window.get_surface()
screen_size = screen.size()

img_size = img.size()
ratio = 0.5
img = img.resize((img_size[0] * ratio, img_size[1] * ratio))
img_size = img.size()

pos = (0.0, 0.0)
move_speed = (1, 1)
accum_time = 0.0

tic = time.time()

def tick(delta_time):
    global pos, move_speed, accum_time
    accum_time += delta_time
    if accum_time > 0.004:
        pos = (pos[0] + move_speed[0], pos[1] + move_speed[1])
        trigger = False
        if pos[0] + img_size[0] > screen_size[0] or pos[0] < 0:
            move_speed = (-move_speed[0], move_speed[1])
            trigger = True
        if pos[1] + img_size[1] > screen_size[1] or pos[1] < 0:
            move_speed = (move_speed[0], -move_speed[1])
            trigger = True
        if trigger:
            se.play()
        accum_time = 0.0

while window.running():
    screen.fill((0, 0, 0))
    screen.draw(img, pos)
    if gamex.key.is_pressed(gamex.key.K_ESCAPE):
        print('see you!')
        break

    toc = time.time()
    delta_time = toc - tic
    tic = toc

    tick(delta_time)
    window.tick(delta_time)
