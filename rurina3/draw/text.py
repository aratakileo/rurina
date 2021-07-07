from constants import position2dtype, colortype, recttype,\
    GRAVITY_LEFT, GRAVITY_RIGHT, GRAVITY_TOP, GRAVITY_BOTTOM, GRAVITY_CENTER_HORIZONTAL, GRAVITY_CENTER_VERTICAL
from draw.surface import get_default_surface
from typing import Union, Tuple
import pygame


def format(value: str, singleline: bool = True):
    if singleline:
        value = value.replace('\n', ' ')

    return value.replace('\t', '    ')


def write(
        value: str,
        font: pygame.font.Font,
        pos: position2dtype = (0, 0),
        color: colortype = pygame.Color('white'),
        surface: pygame.Surface = ...
) -> pygame.Surface:
    if len(value) > 0:
        get_default_surface(surface).blit(font.render(format(value), True, color), pos)

    return surface


def write_with_gravity(
        value: str,
        font: pygame.font.Font,
        rect: recttype,
        color: colortype = pygame.Color('white'),
        gravity: int = GRAVITY_LEFT | GRAVITY_TOP,
        surface: pygame.Surface = ...
) -> pygame.Surface:
    x, y = rect[:2]

    if gravity == 0:
        return write(value, font, (x, y), color, surface)

    value = format(value)
    tw, th = font.size(value)

    if gravity & GRAVITY_RIGHT:
        x += rect.width - tw
    elif gravity & GRAVITY_CENTER_HORIZONTAL:
        x /= 2

    if gravity & GRAVITY_BOTTOM:
        y += rect.height - th
    elif gravity & GRAVITY_CENTER_VERTICAL:
        y /= 2

    return write(value, font, (x, y), color, surface)


def write_multiline(
        value: str,
        font: pygame.font.Font,
        rect: recttype,
        color: colortype = pygame.Color('white'),
        gravity: int = GRAVITY_LEFT | GRAVITY_TOP,
        linespacing: float = 0.0,
        surface: pygame.Surface = ...
) -> pygame.Surface:
    if '\n' not in value:
        return write_with_gravity(value, font, rect, color, gravity, surface)

    value = format(value)
    tw, th = 0, font.get_height()
    values = value.split('\n')
    x, y = rect[:2]

    for _value in values:
        _tw = font.size(_value)[0]
        if _tw > tw:
            tw = _tw

    if gravity & GRAVITY_RIGHT:
        x += rect.width - tw
    elif gravity & GRAVITY_CENTER_HORIZONTAL:
        x /= 2

    if gravity & GRAVITY_BOTTOM:
        y += rect.height - th
    elif gravity & GRAVITY_CENTER_VERTICAL:
        y /= 2

    for _value in values:
        _tw = font.size(_value)[0]
        write(
            value,
            font,
            (x + (tw - _tw) / 2, y),
            color,
            surface
        )
        y += th + linespacing

    return surface


__all__ = [
    'write',
    'write_with_gravity',
    'write_multiline'
]
