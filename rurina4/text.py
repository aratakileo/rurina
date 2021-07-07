from constants import (
    GRAVITY_LEFT,
    GRAVITY_TOP,
    GRAVITY_RIGHT,
    GRAVITY_BOTTOM,
    GRAVITY_CENTER_HORIZONTAL,
    GRAVITY_CENTER_VERTICAL
)

from pygame.font import Font as _Font
from pygame import Surface, display
from typing import List, Tuple
from font import Font
import re


def write(
        value: str,
        font: _Font,
        pos=(0, 0),
        color=(255, 255, 255),
        surface: Surface = ...
) -> Surface:
    if surface in (None, ...):
        surface = display.get_surface()

    if isinstance(font, Font):
        font = font._font

    value = value.replace('\n', ' ')

    surface.blit(font.render(value, True, color), pos)

    return surface


def lines(value: str, font: _Font, rect, wrapchar: bool = True) -> List[str]:
    if isinstance(font, Font):
        font = font._font

    _lines = value.replace('\r', '\n').split('\n')

    if not wrapchar:
        return _lines

    __lines = _lines
    _lines = []

    i = -1
    for line in __lines:
        i += 1
        if font.size(line.strip(' '))[0] <= rect[2]:
            _lines.append(line)
            continue

        words = re.split(r'(\s+)', line)
        _line = ''
        k = -1
        for word in words:
            k += 1
            if font.size(word)[0] > rect[2]:
                _word = ''
                for char in word:
                    _word += char

                    if font.size(char)[0] > rect[2]:
                        return _lines

                    if font.size(_word)[0] > rect[2]:
                        _word = _word[:-1]
                        words.insert(k + 1, word[len(_word):])
                        word = _word
                        break

            _line += word

            if font.size(_line.strip(' '))[0] > rect[2]:
                _lines.append(_line[:-len(word)])

                if k + 1 != len(words):
                    if ' ' not in words[k + 1]:
                        words[k + 1] = ''

                __lines.insert(i + 1, ''.join(words[k:]))
                break

    return _lines


def lines_gravity(
        _lines: List[str],
        font: _Font,
        rect,
        gravity: int = GRAVITY_LEFT | GRAVITY_TOP,
        linespacing: int = 0,
        croplines: bool = True
) -> List[Tuple[int, int]]:
    if isinstance(font, Font):
        font = font._font

    positions = []
    h = font.get_height()
    lh = (h + linespacing) * len(_lines) - linespacing
    y = rect[1]

    if croplines and lh > rect[3]:
        count = int((rect[3] + linespacing) // (h + linespacing))
        _lines = _lines[:count]
        lh = (h + linespacing) * len(_lines) - linespacing

    if gravity & (GRAVITY_BOTTOM | GRAVITY_CENTER_VERTICAL):
        y += (rect[3] - lh) / (2 if gravity & GRAVITY_CENTER_VERTICAL else 1)

    for line in _lines:
        x = rect[0]

        if gravity & (GRAVITY_RIGHT | GRAVITY_CENTER_HORIZONTAL):
            x += (rect[2] - font.size(line.strip(' '))[0]) / (2 if gravity & GRAVITY_CENTER_HORIZONTAL else 1)

        positions.append((x, y))

        y += h + linespacing

    return positions


__all__ = (
    'write',
    'lines',
    'lines_gravity'
)
