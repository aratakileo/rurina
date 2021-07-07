from constants import GRAVITY_RIGHT, GRAVITY_BOTTOM, GRAVITY_CENTER_HORIZONTAL, GRAVITY_CENTER_VERTICAL
from base_node import get_surface
from shape import Rect
import pygame


def write(
        value: str,
        font: pygame.font.Font,
        pos=(0, 0),
        color: pygame.Color = pygame.Color('white'),
        surface: pygame.Surface = ...
) -> pygame.Surface:
    surface = get_surface(surface)

    if len(value) > 0:
        value = value.replace('\t', '   ').replace('\n', ' ')
        surface.blit(font.render(value, True, color), pos)

    return surface


def write_gravity(
        value: str,
        font: pygame.font.Font,
        rect: Rect,
        color: pygame.Color = pygame.Color('white'),
        gravity: int = 0,
        surface: pygame.Surface = ...
) -> pygame.Surface:
    if gravity == 0:
        return write(value, font, rect.rpos, color, surface)

    vw, vh = font.size(value)
    x, y = rect.rpos

    x += rect.width - vw if gravity & GRAVITY_RIGHT else (
        (rect.width - vw) / 2 if gravity & GRAVITY_CENTER_HORIZONTAL else 0
    )
    y += rect.height - vh if gravity & GRAVITY_BOTTOM else (
        (rect.height - vh) / 2 if gravity & GRAVITY_CENTER_VERTICAL else 0
    )

    return write(value, font, (x, y), color, surface)


def write_multiline(
        value: str,
        font: pygame.font.Font,
        rect: Rect,
        color: pygame.Color = pygame.Color('white'),
        gravity: int = 0,
        surface: pygame.Surface = ...,
        linespacing: int = 0
) -> pygame.Surface:
    surface = get_surface(surface)

    if len(value) > 0:
        value = value.replace('\t', '   ')
        lines = value.split('\n')

        vw, vh = 0, font.get_height()
        ww, wh = rect.size

        for line in lines:
            _vw = font.size(line)[0]

            if _vw > vw:
                vw = _vw

        lsw = (vh + linespacing) * len(lines) - linespacing
        y_off = 0

        if gravity & GRAVITY_BOTTOM:
            y_off = wh - lsw
        elif gravity & GRAVITY_CENTER_VERTICAL:
            y_off = (wh - lsw) / 2

        del lsw

        for i in range(len(lines)):
            line = lines[i]

            surface.blit(
                font.render(line, True, color),
                (
                    rect.rx + (
                        ww - font.size(line)[0] if gravity & GRAVITY_RIGHT else
                        (ww - font.size(line)[0]) / 2 if gravity & GRAVITY_CENTER_HORIZONTAL else 0
                    ),
                    rect.ry + y_off + (vh + linespacing) * i
                )
            )

    return surface


def write_autoline(
        value: str,
        font: pygame.font.Font,
        rect: Rect,
        color: pygame.Color = pygame.Color('white'),
        gravity: int = 0,
        surface: pygame.Surface = ...,
        linespacing: int = 0
) -> pygame.Surface:
    surface = get_surface(surface)

    if '\n' in value:
        surface = write_multiline(
            value,
            font,
            rect,
            color,
            gravity,
            surface,
            linespacing
        )
    elif len(value) > 0:
        surface = write_gravity(value, font, rect, color, gravity, surface)

    return surface


__all__ = [
    'write',
    'write_gravity',
    'write_multiline',
    'write_autoline'
]
