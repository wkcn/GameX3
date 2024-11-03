import pygame


def is_key_pressed(key) -> bool:
    return pygame.key.get_pressed()[key]
