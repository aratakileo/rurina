from key import is_button_pressed, is_button_released
from pygame.constants import BUTTON_LEFT as _btn_left
from pygame.mouse import get_pos as _mouse_position
from node.nodetype import remove as _baseremove
from node.node import Node, get_shape
from pygame.event import Event
from typing import Sequence
from shape import Rect


_focused_control = None
_cursor_buffer = [None, 0]
_active_control = None
_last_pressed = {}


class Control(Node):
    def __init__(self, *args, rect: Rect = Rect(), **kwargs):
        super().__init__(*args, **kwargs)

        self.rect = rect
        self._misspress = self._fixed = False

    @property
    def focused(self) -> bool:
        return id(_focused_control) == id(self)

    @focused.setter
    def focused(self, value: bool):
        global _focused_control

        if value:
            _focused_control = self
        elif self.focused:
            _focused_control = None

    @property
    def isinteractive(self) -> bool:
        return id(_active_control) == id(self) or _active_control is None

    @isinteractive.setter
    def isinteractive(self, value: bool):
        global _active_control

        if value:
            _active_control = self
        elif self.isinteractive:
            _active_control = None

    def input(self, event: Sequence[Event]):
        if self.enabled:
            super().input(event)

            if id(self) not in _last_pressed:
                _last_pressed[id(self)] = False

            _last_pressed[id(self)] = ispressed(self)

            if self.isinteractive:
                if is_button_pressed(_btn_left):
                    if ishovered(self) and not self._misspress:
                        self._fixed = True
                        self.isinteractive = True
                    elif not self._fixed:
                        self._misspress = True
                elif is_button_released(_btn_left):
                    self._misspress = self._fixed = False
                    self.isinteractive = False
            else:
                self._fixed = False


def last_pressed(control: Control) -> bool:
    return id(control) in _last_pressed and _last_pressed[id(control)]


def ishovered(control: Control) -> bool:
    return get_shape(control, True).collidepoint(_mouse_position())


def ispressed(control: Control) -> bool:
    return control._fixed


def isreleased(control: Control) -> bool:
    return not ispressed(control) and last_pressed(control)


def isjustpressed(control: Control) -> bool:
    return ispressed(control) and not last_pressed(control)


def remove(control: Control):
    _baseremove(control)

    if id(control) in _last_pressed:
        del _last_pressed[id(control)]


__all__ = (
    'Control',
    'last_pressed',
    'ishovered',
    'ispressed',
    'isreleased',
    'isjustpressed',
    'remove',
)
