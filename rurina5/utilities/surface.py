from typing import Union, Tuple, List, Sequence, overload
from constants import _pyi_Color_type, _pyi_Surface_type
from utilities.math import Vector2Type, by_interval
from pygame.transform import smoothscale
from pygame.display import get_surface
from pygame.constants import SRCALPHA
from pygame.surface import Surface
from pygame import Color
from shape import Rect


@overload
def AlphaSurface(
        size: Union[Tuple[float, float], List[float], Vector2Type] = (100, 100),
        flags: int = 0
) -> _pyi_Surface_type: ...


@overload
def AlphaSurface(surface: Surface, flags: int = 0, alpha: int = 255) -> _pyi_Surface_type: ...


def AlphaSurface(*args, **kwargs) -> _pyi_Surface_type:
    flags = SRCALPHA
    size = (100, 100)
    alpha = None
    surface = None

    if len(args) > 0:
        if isinstance(args[0], Surface):
            surface = args[0]
        else:
            size = args[0]

        if len(args) > 1:
            flags |= args[1]

            if len(args) > 2:
                alpha = by_interval(abs(args[2]), 0, 255)

    if len(kwargs) > 0:
        if 'surface' in kwargs:
            surface = kwargs['surface']

        if 'size' in kwargs:
            size = kwargs['size']

        if 'flags' in kwargs:
            flags |= kwargs['flags']

        if 'alpha' in kwargs:
            alpha = by_interval(abs(kwargs['alpha']), 0, 255)

    if surface is not None:
        size = surface.get_size()
        returned_surface = Surface(size, flags, 32)

        for x in range(size[0]):
            for y in range(size[1]):
                color = Color(surface.get_at((x, y)))

                if alpha is not None:
                    color.a = alpha

                returned_surface.set_at((x, y), color)

        return returned_surface

    return Surface(size[:], flags, 32)


def gradient(
        rect: Union[Rect, Tuple[Union[int, float], Union[int, float], int, int], List[float]] = (0, 0, 100, 100),
        colors: Sequence[_pyi_Color_type] = [(40, 240, 40), (40, 40, 240)],
        horizontal: bool = True,
        surface: _pyi_Surface_type = ...,
        offset: int = 1
) -> _pyi_Surface_type:
    if surface in (None, ...):
        surface = get_surface()

    offset = by_interval(abs(offset), 1)

    if len(colors) == 0:
        return surface

    size = offset * len(colors)

    if not horizontal:
        _gradient = Surface((1, size))

        for i in range(size):
            _gradient.set_at((0, i), colors[i])
    else:
        _gradient = Surface((size, 1))

        for i in range(size):
            _gradient.set_at((i, 0), colors[int(i / offset)])

    surface.blit(smoothscale(_gradient, rect[2:]), rect[:2])

    return surface


def mask(origin_surface: _pyi_Surface_type, mask_surface: _pyi_Surface_type) -> _pyi_Surface_type:
    if origin_surface.get_size() != mask_surface.get_size():
        raise ValueError('All of got surfaces should have equal sizes')

    returned_surface = AlphaSurface(origin_surface.get_size())

    for x in range(returned_surface.get_size()[0]):
        for y in range(returned_surface.get_size()[1]):
            _color = Color(mask_surface.get_at((x, y)))
            if _color.a != 0:
                color = Color(origin_surface.get_at((x, y)))
                color.a = _color.a
                returned_surface.set_at((x, y), color)

    return returned_surface


__all__ = (
    'AlphaSurface',
    'gradient',
    'mask',
)
