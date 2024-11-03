import gamex as gx

window = gx.create_window('hello world', (800, 600))

delta_time = 1.0 / 60.0

while window.running():
    window.tick(delta_time)
    if gx.key.is_pressed(gx.key.K_ESCAPE):
        print('see you!')
        break
