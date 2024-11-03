import pygame
from pygame.locals import *
from ...graph import Window as WindowBase, Surface as SurfaceBase


class Window(WindowBase):
    def __init__(self, title, size):
        pygame.init()
        self.set_title(title)

        flags = 0
        self.screen = pygame.display.set_mode(size, flags)
        self._running = True

    def set_title(self, title):
        pygame.display.set_caption(title)

    def get_surface(self):
        return Surface(self.screen)

    def running(self) -> bool:
        return self._running

    def tick(self, delta_time):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._running = False
        pygame.display.update()


class Surface(SurfaceBase):
    def __init__(self, data):
        self.data = data

    @staticmethod
    def load(filename):
        data = pygame.image.load(filename).convert_alpha()
        return Surface(data)

    def draw(self, surface, pos):
        self.data.blit(surface.data, pos)

    def size(self):
        return self.data.get_size()

    def resize(self, size, smooth=False):
        if smooth:
            fn = pygame.transform.smoothscale
        else:
            fn = pygame.transform.scale
        size = (int(size[0]), int(size[1]))
        return Surface(fn(self.data, size).convert_alpha())

    def fill(self, color):
        self.data.fill(color)
