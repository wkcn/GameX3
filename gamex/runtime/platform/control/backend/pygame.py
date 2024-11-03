import pygame


def is_key_pressed(key) -> bool:
    pygame.event.get()
    return pygame.key.get_pressed()[key]
