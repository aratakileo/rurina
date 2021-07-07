from typing import Union, Tuple, List
from pygame.math import Vector2
from pygame import Color, Rect


position2dtype = Union[
    Vector2,
    Tuple[int, int],
    Tuple[float, float],
    Tuple[int, float],
    Tuple[float, int],
    List[int, int],
    List[float, float],
    List[int, float],
    List[float, int],
]
colortype = Union[
    Color,
    Tuple[int, int, int],
    Tuple[int, int, int, int],
    List[int, int, int],
    List[int, int, int, int]
]
recttype = Union[
    Rect,
    Tuple[Vector2, int, int],
    List[Vector2, int, int],
    Tuple[float, float, int, int],
    List[float, float, int, int],
    Tuple[int, int, int, int],
    List[int, int, int, int]
]


GRAVITY_LEFT = 0
GRAVITY_RIGHT = 1
GRAVITY_TOP = 0
GRAVITY_BOTTOM = 2
GRAVITY_CENTER_HORIZONTAL = GRAVITY_RIGHT | 4
GRAVITY_CENTER_VERTICAL = GRAVITY_BOTTOM | 8
