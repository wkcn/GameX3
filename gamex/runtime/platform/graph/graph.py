import numpy as np


class Window:
    def __init__(self, title, size):
        raise NotImplementedError('Window.__init__ is not implemented')

    def set_title(self, title):
        raise NotImplementedError('Window.set_title is not implemented')

    def get_surface(self):
        raise NotImplementedError('Window.get_surface is not implemented')

    def running(self) -> bool:
        return True

    def tick(self, delta_time):
        raise NotImplementedError('Window.tick is not implemented')


class Surface:
    def __init__(self, surface):
        raise NotImplementedError('Surface.__init__ is not implemented')

    @staticmethod
    def load(filename):
        raise NotImplementedError('Surface.load_image is not implemented')

    @staticmethod
    def new(size):
        raise NotImplementedError('Surface.new is not implemented')

    def draw(self, surface, pos):
        raise NotImplementedError('Surface.draw is not implemented')

    def size(self):
        raise NotImplementedError('Surface.size is not implemented')

    def resize(self, size, smooth=False):
        raise NotImplementedError('Surface.resize is not implemented')

    def fill(self, color):
        raise NotImplementedError('Surface.fill is not implemented')

    def data(self) -> np.ndarray:
        raise NotImplementedError('Surface.data is not implemented')
