from ..platform.control import is_key_pressed
from ..platform import control


# import all variables whose prefix name is 'K_'
for key in dir(control):
    if key.startswith('K_'):
        globals()[key] = getattr(control, key)


def is_pressed(key):
    return is_key_pressed(key)
