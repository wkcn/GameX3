class Window:
    def __init__(self):
        raise NotImplementedError('Window.__init__ is not implemented')

    def set_title(self, title):
        raise NotImplementedError('Window.set_title is not implemented')

    def get_surface(self):
        raise NotImplementedError('Window.get_surface is not implemented')


class Surface:
    def __init__(self):
        raise NotImplementedError('Surface.__init__ is not implemented')

    @staticmethod
    def load(filename) -> Surface:
        raise NotImplementedError('Surface.load_image is not implemented')

    def blit(self, surface, pos):
        raise NotImplementedError('Surface.blit is not implemented')
