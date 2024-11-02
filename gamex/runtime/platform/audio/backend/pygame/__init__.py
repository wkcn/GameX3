import pygame
from ...audio import Sound as SoundBase


class Sound(SoundBase):
    def __init__(self, filename):
        self.filename = filename
        self.sound = pygame.mixer.Sound(self.filename)

    def play(self, loops=0, fade_ms=0):
        self.sound.play(loops=loops, fade_ms=fade_ms)

    def stop(self):
        self.sound.stop()
