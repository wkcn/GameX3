import numpy as np
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
    def __init__(self, surface):
        self.surface = surface

    @staticmethod
    def load(filename):
        surface = pygame.image.load(filename).convert_alpha()
        return Surface(surface)

    def draw(self, surface, pos):
        self.surface.blit(surface.surface, pos)

    def size(self):
        return self.surface.get_size()

    def resize(self, size, smooth=False):
        if smooth:
            fn = pygame.transform.smoothscale
        else:
            fn = pygame.transform.scale
        size = (int(size[0]), int(size[1]))
        return Surface(fn(self.surface, size).convert_alpha())

    def fill(self, color):
        self.surface.fill(color)

    def data(self) -> np.ndarray:
        data = pygame.surfarray.pixels3d(self.surface)
        return np.swapaxes(data, 0, 1)
