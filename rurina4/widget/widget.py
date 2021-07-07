from nodes.collisionshape import _CollisionShape, CollisionShape, CollisionRect
from pygame import mouse
from event import Event
from typing import List


# TODO: upgrade code with help 'input' module


active_widget = None

active_events = [
    False
]
last_active_events = active_events.copy()


class _RectWidget(CollisionRect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class _InteractiveWidget(_CollisionShape):
    def __init__(self, *args, change_mousecursor: bool = True, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_mousecursor = change_mousecursor
        self.hovered = self.pressed = self.released = False
        self._misspress = False
        self._fixed = False

    def input(self, event: List[Event]):
        self.hovered = self.pressed = self.released = False
        if self.enabled:
            super().input(event)

            if can_interactive(self):
                self.hovered = self.collidepoint(*mouse.get_pos())

                if active_events[0]:
                    if self.hovered and not self._misspress:
                        self._fixed = True
                        set_interactive(self)
                    elif not self._fixed:
                        self._misspress = True
                elif last_active_events[0]:
                    self.released = self._fixed
                    self._misspress = self._fixed = False
                    set_interactive(None)

                self.pressed = active_events[0] and self._fixed


class Widget(CollisionShape):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RectWidget(_RectWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InteractiveWidget(CollisionShape, _InteractiveWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InteractiveRectWidget(_RectWidget, _InteractiveWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def can_interactive(widget) -> bool:
    return is_interactive(widget) or active_widget is None


def is_interactive(widget) -> bool:
    return id(widget) == id(active_widget)


def set_interactive(widget):
    if can_interactive(widget) or widget is None:
        global active_widget
        active_widget = widget


def flip():
    global last_active_events
    last_active_events = active_events.copy()

    active_events[0] = mouse.get_pressed()[0]


__all__ = (
    'Widget',
    'RectWidget',
    'InteractiveWidget',
    'InteractiveRectWidget',
    'can_interactive',
    'is_interactive',
    'set_interactive',
    'flip'
)
