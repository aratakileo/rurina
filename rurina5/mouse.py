from utilities.math import Vector2, _pyi_Vector2_type, _pyi_Vector2_item_type
from constants import MOUSE_MODE_CONFINED, MOUSE_MODE_CAPTURED
from pygame import mouse as _mouse, event, display
from pygame.cursors import Cursor
from typing import List, Union
from types import ModuleType
import sys


_captured = False


class _posVector2(Vector2):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def x(self):
        return _mouse.get_pos()[0]

    @x.setter
    def x(self, value):
        _mouse.set_pos(value, self.y)

    @property
    def y(self):
        return _mouse.get_pos()[1]

    @y.setter
    def y(self, value):
        _mouse.set_pos(self.x, value)

    def copy(self):
        return Vector2(self)


class _relVector2(Vector2):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def x(self):
        return _mouse.get_rel()[0]

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        return _mouse.get_rel()[1]

    @y.setter
    def y(self, value):
        pass

    def copy(self):
        return Vector2(self)


position = _posVector2()
relative = _relVector2()


class Mouse(ModuleType):
    @property
    def position(self) -> Vector2:
        position[:] = _mouse.get_pos()
        return position

    @position.setter
    def position(self, value: _pyi_Vector2_type):
        position.x, position.y = value

    @property
    def cursor(self) -> Union[Cursor]:
        return _mouse.get_cursor()

    @cursor.setter
    def cursor(self, value: Union[Cursor]):
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
    def relative(self) -> Vector2:
        relative[:] = _mouse.get_rel()
        return relative

    @property
    def focused(self):
        return bool(_mouse.get_focused())

    @property
    def left_pressed(self) -> bool:
        return _mouse.get_pressed()[0]

    @property
    def middle_pressed(self) -> bool:
        return _mouse.get_pressed()[1]

    @property
    def right_pressed(self) -> bool:
        return _mouse.get_pressed()[2]

    def __getitem__(self, item: Union[slice, int]) -> Union[List[Union[float, int]], float, int]:
        return self.position[item]

    def __setitem__(self, key: Union[slice, int], value: _pyi_Vector2_item_type):
        self.position.__setitem__(key, value)

    def flip(self):
        if self.focused and _captured:
            size = display.get_window_size()
            self.position = size[0] / 2, size[1] / 2


sys.modules[__name__] = Mouse(__name__)
