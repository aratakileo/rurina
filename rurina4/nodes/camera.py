from utilities.string import printwarning
from node._node import _Node
from event import Event
from typing import List


# TODO: Complete InterpolatedCamera


active_camera = None


def get_active_camera():
    return active_camera


class Camera(_Node):
    def __init__(self, *args, current: bool = True, **kwargs):
        super().__init__(*args, **kwargs)

        self.current = current

    @property
    def current(self) -> bool:
        return id(active_camera) == id(self)

    @current.setter
    def current(self, value: bool):
        global active_camera

        if value:
            active_camera = self
        elif self.current:
            active_camera = None

    def __get_visible__(self) -> bool:
        return super().__get_visible__() and self.current


class InterpolatedCamera(Camera):
    def __init__(self, *args, target=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.target = target

        printwarning(f'Warning: Object \'{self.__class__.__name__}\' is incomplete')

    def input(self, event: List[Event]):
        if self.enabled:
            super().input(event)

            if self.target not in (None, ...):
                pass


__all__ = (
    'Camera',
    'InterpolatedCamera',
    'get_active_camera'
)
