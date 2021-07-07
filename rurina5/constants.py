from pygame.surface import Surface, SurfaceType
from typing import Union, List, Tuple
from pygame.color import Color

GRAVITY_LEFT = 0
GRAVITY_RIGHT = 1
GRAVITY_TOP = 0
GRAVITY_BOTTOM = 2
GRAVITY_CENTER_HORIZONTAL = 4
GRAVITY_CENTER_VERTICAL = 8

STYLE_NORMAL = 0
STYLE_BOLD = 1
STYLE_ITALIC = 2

MOUSE_MODE_CONFINED = 1
MOUSE_MODE_CAPTURED = 2

_pyi_Color_type = Union[Color, str, Tuple[int, int, int], List[int], int, Tuple[int, int, int, int]]
_pyi_Surface_type = Union[Surface, SurfaceType]

key_long_press_duration = 0.4
key_long_press_timeout_duration = 0.2
