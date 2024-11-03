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
        return self.screen


class Surface(SurfaceBase):
    def __init__(self, img):
        self.img = img

    @staticmethod
    def load(filename):
        img = pygame.image.load(filename).convert_alpha()
        return Surface(img)

    def blit(self, surface, pos):
        surface.blit(self.img, pos)
