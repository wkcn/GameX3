import pygame
from ...graph import Window as WindowBase, Surface as SurfaceBase


class Window(WindowBase):
    def __init__(self, title, size):
        pygame.init()
        self.set_title(title)

        flags = 0
        self.screen = pygame.display.set_mode(size, flags)

    def set_title(self, title):
        pygame.display.set_caption(title)

    def get_surface(self):
        return Surface(self.screen)

    def tick(self, delta_time):
        pygame.event.get()
        pygame.display.update()


class Surface(SurfaceBase):
    def __init__(self, data):
        self.data = data

    @staticmethod
    def load(filename):
        data = pygame.image.load(filename).convert_alpha()
        return Surface(data)

    def blit(self, surface, pos):
        self.data.blit(surface.data, pos)

    def size(self):
        return self.data.get_size()
