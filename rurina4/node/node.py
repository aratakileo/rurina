from nodes.camera import get_active_camera
from constants import MAX_ALPHA
from ._node import _Node


class Node(_Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def rscalex(self):
        if get_active_camera():
            return self.fscalex * get_active_camera().fscalex

        return self.fscalex

    @rscalex.setter
    def rscalex(self, value):
        if get_active_camera():
            self.fscalex = value / get_active_camera().fscalex

    @property
    def rscaley(self):
        if get_active_camera():
            return self.fscaley * get_active_camera().fscaley

        return self.fscaley

    @rscaley.setter
    def rscaley(self, value):
        if get_active_camera():
            self.fscaley = value / get_active_camera().fscaley

    @property
    def rscale(self):
        return self.rscalex, self.rscaley

    @property
    def ralpha(self) -> int:
        if get_active_camera():
            return int(get_active_camera().falpha * self.falpha / MAX_ALPHA)

        return self.falpha

    @rscale.setter
    def rscale(self, value):
        self.rscalex, self.rscaley = value

    @property
    def rx(self):
        if get_active_camera():
            return self.fx - get_active_camera().fx

        return self.fx

    @rx.setter
    def rx(self, value):
        if get_active_camera():
            self.fx = value + get_active_camera().fx

    @property
    def ry(self):
        if get_active_camera():
            return self.fy - get_active_camera().fy

        return self.fy

    @ry.setter
    def ry(self, value):
        if get_active_camera():
            self.fy = value + get_active_camera().fy

    @property
    def rpos(self):
        return self.rx, self.ry

    @rpos.setter
    def rpos(self, value):
        self.rx, self.ry = value


__all__ = (
    'Node',
)

