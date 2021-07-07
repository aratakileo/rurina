from constants import MOUSE_MODE_CONFINED, MOUSE_MODE_CAPTURED
from pygame import mouse as _mouse, event, display
from pygame.cursors import Cursor
from typing import Tuple, Union
from types import ModuleType
import sys


# TODO: time.fps and time.dt


_captured = False


class Mouse(ModuleType):
    @property
    def pos(self) -> Tuple[int, int]:
        return _mouse.get_pos()

    @pos.setter
    def pos(self, value: Tuple[int, int]):
        _mouse.set_pos(value)

    @property
    def x(self) -> int:
        return self.pos[0]

    @x.setter
    def x(self, value: int):
        self.pos = value, self.y

    @property
    def y(self) -> int:
        return self.pos[1]

    @y.setter
    def y(self, value: int):
        self.pos = self.x, value

    @property
    def cursor(self) -> Union[Cursor, int]:
        return _mouse.get_cursor()

    @cursor.setter
    def cursor(self, value: Union[Cursor, int]):
        _mouse.set_cursor(value)

    @property
    def visible(self) -> bool:
        return _mouse.get_visible()

    @visible.setter
    def visible(self, value: bool):
        _mouse.set_visible(value)

    @property
    def mode(self) -> int:
        return (MOUSE_MODE_CONFINED if event.get_grab() else 0) | (MOUSE_MODE_CAPTURED if _captured else 0)

    @mode.setter
    def mode(self, value: int):
        global _captured
        event.set_grab(bool(value & MOUSE_MODE_CONFINED))
        _captured = bool(value & MOUSE_MODE_CAPTURED)

    @property
    def rel(self) -> Tuple[int, int]:
        return _mouse.get_rel()

    @property
    def focused(self):
        return bool(_mouse.get_focused())

    def __getitem__(self, item):
        return self.pos[item]

    def flip(self):
        if self.focused and _captured:
            size = display.get_window_size()
            self.pos = size[0] / 2, size[1] / 2


sys.modules[__name__] = Mouse(__name__)
