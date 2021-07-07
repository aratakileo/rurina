from constants import GRAVITY_RIGHT, GRAVITY_BOTTOM, GRAVITY_CENTER_HORIZONTAL, GRAVITY_CENTER_VERTICAL
from shape import *
import pygame


def fix_by_min_max_size(target, min_size=None, max_size=None, by_width: bool = True, by_height: bool = True):
    size = Rect(0, 0, *get_size(get_shape(target)))

    if min_size is not None:
        if by_width and size.width < min_size[0]:
            size.width = min_size[0]

        if by_height and size.height < min_size[1]:
            size.height = min_size[1]

    if max_size is not None:
        if by_width and size.width > max_size[0]:
            size.width = max_size[0]

        if by_height and size.height > max_size[1]:
            size.height = max_size[1]

    set_size(get_shape(target), *size.size)


def fix_size(target, parent, size_fraction=(1, 1), min_size=None, max_size=None, by_width: bool = True, by_height: bool = True):
    tsize = Rect(0, 0, *get_size(get_shape(target)))
    psize = Rect(0, 0, *get_size(get_shape(parent)))

    if by_width:
        tsize.width = psize.width // size_fraction[0]

    if by_height:
        tsize.height = psize.height // size_fraction[1]

    set_size(get_shape(target), *tsize.size)
    fix_by_min_max_size(target, min_size, max_size, by_width, by_height)


def fix_size_by_window(target, size_fraction=(1, 1), min_size=None, max_size=None, by_width: bool = True, by_height: bool = True):
    ww, wh = pygame.display.get_window_size()
    size = Rect(0, 0, *get_size(get_shape(target)))

    if by_width:
        size.width = ww // size_fraction[0]

    if by_height:
        size.height = wh // size_fraction[1]

    set_size(get_shape(target), *size.size)
    fix_by_min_max_size(target, min_size, max_size, by_width, by_height)


def set_margin(target, parent, margin=(0, 0, 0, 0)):
    tsize = Rect(0, 0, *get_size(get_shape(target)))
    psize = Rect(0, 0, *get_size(get_shape(parent)))

    tsize.size = psize.width - margin[2] - margin[0], psize.height - margin[3] - margin[1]
    target.pos = margin[:2]

    set_size(get_shape(target), *tsize.size)


def set_margin_by_window(target, margin=(0, 0, 0, 0)):
    size = Rect(0, 0, *get_size(get_shape(target)))
    ww, wh = pygame.display.get_window_size()

    size.size = ww - margin[2] - margin[0], wh - margin[3] - margin[1]
    target.pos = margin[:2]

    set_size(get_shape(target), *size.size)


def set_padding(target, child, padding=(0, 0, 0, 0)):
    set_margin(child, target, padding)


def set_gravity(target, parent, gravity: int = 0):
    tsize = Rect(0, 0, *get_size(get_shape(target)))
    psize = Rect(0, 0, *get_size(get_shape(parent)))

    if gravity & GRAVITY_RIGHT:
        target.x = psize.width - tsize.width

    if gravity & GRAVITY_CENTER_HORIZONTAL:
        target.x = (psize.width - tsize.width) / 2

    if gravity & GRAVITY_BOTTOM:
        target.y = psize.height - tsize.height

    if gravity & GRAVITY_CENTER_VERTICAL:
        target.y = (psize.height - tsize.height) / 2

    set_size(get_shape(target), *tsize.size)


def accommodate_by_horizontal(targets, parent, offset: int = 0):
    offset_score = parent.rx + offset

    for target in targets:
        target.rx = offset_score
        offset_score = target.rx + get_size(get_shape(target))[0] + offset


def accommodate_by_vertical(targets, parent, offset: int = 0):
    offset_score = parent.ry + offset

    for target in targets:
        target.ry = offset_score
        offset_score = target.ry + get_size(get_shape(target))[1] + offset


__all__ = [
    'fix_by_min_max_size',
    'fix_size',
    'fix_size_by_window',
    'set_margin',
    'set_margin_by_window',
    'set_padding',
    'set_gravity',
    'accommodate_by_horizontal',
    'accommodate_by_vertical'
]
