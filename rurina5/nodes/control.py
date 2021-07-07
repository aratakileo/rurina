from node.nodetype import remove as _baseremove
from nodes.collisionshape import get_shape
from input import haveaction, setkey, is_action_pressed, is_action_released
from pygame.cursors import Cursor
from pygame.event import Event
from error import UrsinaError
from typing import Sequence
from node.node import Node
from typing import Union
from shape import Rect
import mouse


FOCUS_CLICK = 1
FOCUS_KEYS = 2


_focused_control = None
_cursor_buffer = [None, 0]
_active_control = None


class FocusSystem:
    next: 'Control' = None
    prev: 'Control' = None
    neighbour_left: 'Control' = None
    neighbour_top: 'Control' = None
    neighbour_right: 'Control' = None
    neighbour_bottom: 'Control' = None

    def __init__(self, mode: int = FOCUS_CLICK | FOCUS_KEYS):
        self.mode = mode

        if not get_init():
            raise UrsinaError('control not initialized')


class Control(Node):
    hovered: bool = False
    pressed: bool = False
    last_pressed: bool = False
    focused_cursor: Union[int, Cursor] = 0
    focus_system: FocusSystem

    def __init__(self, *args, rect: Rect = Rect(), **kwargs):
        super().__init__(*args, **kwargs)

        self.rect = rect
        self.focus_system = FocusSystem()
        self._misspress = self._fixed = False

        self.__output_properties__ = (*self.__output_properties__, 'focused')

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
        self.last_pressed = self.pressed
        self.hovered = self.pressed = False

        if self.enabled:
            global _cursor_buffer

            super().input(event)

            if get_shape(self, True).collidepoint(mouse.position):
                self.hovered = True

            if self.hovered:
                if _cursor_buffer[0] is None:
                    _cursor_buffer = [self, mouse.cursor]

                if id(_cursor_buffer[0]) == id(self):
                    mouse.cursor = self.focused_cursor
            elif id(_cursor_buffer[0]) == id(self):
                mouse.cursor = _cursor_buffer[1]
                _cursor_buffer[0] = None

            if self.isinteractive:
                if is_action_pressed('ui_mouse_left'):
                    if self.hovered and not self._misspress:
                        self._fixed = True
                        self.isinteractive = True
                    elif not self._fixed:
                        self._misspress = True
                elif is_action_released('ui_mouse_left'):
                    self._misspress = self._fixed = False
                    self.isinteractive = False

                self.pressed = self._fixed


def get_init() -> bool:
    return haveaction('ui_tab') and haveaction('ui_left') and haveaction('ui_up') and haveaction('ui_right')\
           and haveaction('ui_down') and haveaction('ui_mouse_left')


def init():
    setkey('ui_tab', 'tab')
    setkey('ui_left', 'arrow left')
    setkey('ui_left', 'arrow left', True)
    setkey('ui_up', 'arrow up')
    setkey('ui_up', 'arrow up', True)
    setkey('ui_right', 'arrow right')
    setkey('ui_right', 'arrow right', True)
    setkey('ui_down', 'arrow down')
    setkey('ui_down', 'arrow down', True)
    setkey('ui_mouse_left', 'mouse left')


def remove(control: Control):
    _baseremove(control)

    control.focused = False
    control.isinteractive = False

    if id(_cursor_buffer[0]) == id(control):
        mouse.cursor = _cursor_buffer[1]
        _cursor_buffer[0] = None


__all__ = (
    'Control',
    'FocusSystem',
    'FOCUS_CLICK',
    'FOCUS_KEYS',
    'get_init',
    'init',
    'remove'
)
