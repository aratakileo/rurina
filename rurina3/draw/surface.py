import pygame


def get_default_surface(surface: pygame.Surface = ...) -> pygame.Surface:
    if surface is ...:
        return pygame.display.get_surface()

    return surface


__all__ = [
    'get_default_surface'
]
