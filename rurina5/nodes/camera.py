from node.nodetype import NodeType, remove as _baseremove
from typing import Union


_active_camera = None


class Camera(NodeType):
    def __init__(self, *args, current: bool = True, **kwargs):
        super().__init__(*args, **kwargs)

        self.current = current

        self.__output_properties__ = (*self.__output_properties__, 'current')

    @property
    def current(self) -> bool:
        return id(_active_camera) == id(self)

    @current.setter
    def current(self, value: bool):
        global _active_camera

        if value:
            _active_camera = self
        elif self.current:
            _active_camera = None

    def __visible__(self) -> bool:
        return super().__visible__() and self.current


def active_camera() -> Union['Camera', None]:
    return _active_camera


def remove(camera: Camera):
    _baseremove(camera)
    if camera.current:
        camera.current = False


__all__ = (
    'Camera',
    'active_camera',
    'remove'
)
