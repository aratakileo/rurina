from base_node import *
import pygame


active_camera = None


def get_active_camera():
    if active_camera is None or not active_camera.current:
        return None

    return active_camera


class Camera(_AdditionalNode):
    def __init__(
            self,
            current: bool = True,
            *args,
            parent=rootnode,
            **kwargs
    ) -> None:
        super().__init__(*args, parent=parent, **kwargs)

        self.current = current

    def __del__(self):
        global active_camera
        active_camera = None

        self.nodes = []
        self.parent.remove(self)

    @property
    def current(self) -> bool:
        return self.__current__

    @current.setter
    def current(self, value):
        self.__current__ = value

        if value:
            global active_camera

            if active_camera is not None:
                active_camera.current = False

            active_camera = self

    @property
    def can_be_drawn(self):
        return self.visible and self.alpha > 0 and self.scale != 0 and self.current

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            super().draw(surface)


class InterpolatedCamera(Camera):
    pass


__all__ = [
    'Camera',
    'InterpolatedCamera',
    'get_active_camera'
]
