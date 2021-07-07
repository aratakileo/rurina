from constants import MAX_ALPHA, MAX_SCALE
import pygame


def set_alpha(surface: pygame.Surface, alpha: int = MAX_ALPHA) -> pygame.Surface:
    surface.set_alpha(alpha)
    return surface


def set_scale(surface: pygame.Surface, scale=(MAX_SCALE, MAX_SCALE)) -> pygame.Surface:
    surface = pygame.transform.flip(surface, scale[0] < 0, scale[1] < 0)

    scale = abs(scale[0]), abs(scale[1])

    sw, sh = surface.get_size()
    sw, sh = int(sw * scale[0]), int(sh * scale[1])
    return pygame.transform.scale(surface, (sw, sh))


def set_alpha_scale(surface: pygame.Surface, alpha: int = MAX_ALPHA, scale=(MAX_SCALE, MAX_SCALE)) -> pygame.Surface:
    return set_alpha(set_scale(surface, scale), alpha)


def get_pos_of_difference(pos, old_surface: pygame.Surface, new_surface: pygame.Surface):
    ow, oh = old_surface.get_size()
    nw, nh = new_surface.get_size()
    return pos[0] - (nw - ow) / 2, pos[1] - (nh - oh) / 2


def blit(
        place: pygame.Surface,
        placeable: pygame.Surface,
        pos=(0, 0),
        alpha: int = MAX_ALPHA,
        scale=(MAX_SCALE, MAX_SCALE)
):
    _placeable = set_alpha_scale(placeable, alpha, scale)
    place.blit(_placeable, get_pos_of_difference(pos, placeable, _placeable))


__all__ = [
    'set_alpha',
    'set_scale',
    'set_alpha_scale',
    'get_pos_of_difference',
    'blit'
]
