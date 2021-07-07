from camera import get_active_camera
from base_node import *


class Node(_AdditionalNode):
    def __init__(
            self,
            *args,
            **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)

    @property
    def rx(self):
        if get_active_camera() is not None:
            return self.fx + get_active_camera().fx

        return self.fx

    @rx.setter
    def rx(self, value):
        if get_active_camera() is not None:
            self.fx = value - get_active_camera().fx

    @property
    def ry(self):
        if get_active_camera() is not None:
            return self.fy + get_active_camera().fy

        return self.fy

    @ry.setter
    def ry(self, value):
        if get_active_camera() is not None:
            self.fy = value - get_active_camera().fy

    @property
    def rpos(self):
        return self.rx, self.ry

    @rpos.setter
    def rpos(self, value):
        self.rx, self.ry = value


__all__ = [
    'Node'
]
