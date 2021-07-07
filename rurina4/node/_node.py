from utilities.math import by_interval
from constants import MAX_ALPHA
from pygame import Surface
from event import Event
from typing import List
from copy import copy


scene = None


class _RootNode:
    def __init__(
            self,
            pos=(0, 0),
            scale=(1.0, 1.0),
            alpha: int = MAX_ALPHA,
            visible: bool = True,
            enabled: bool = True,
            name: str = ...
    ):
        self.pos = pos
        self.scale = scale
        self.alpha = alpha
        self.visible = visible
        self.enabled = enabled
        self.name = name

        if name in (None, ...):
            self.name = self.__class__.__name__

        self.nodes = []

    def __get_visible__(self) -> bool:
        return self._visible and self.alpha != 0 and self.scalex != 0 and self.scaley != 0

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, value):
        self.x, self.y = value

    @property
    def scale(self):
        return self.scalex, self.scaley

    @scale.setter
    def scale(self, value):
        self.scalex, self.scaley = value

    @property
    def fscalex(self):
        return self.scalex

    @fscalex.setter
    def fscalex(self, value):
        self.scalex = value

    @property
    def fscaley(self):
        return self.scaley

    @fscaley.setter
    def fscaley(self, value):
        self.scaley = value

    @property
    def fscale(self):
        return self.fscalex, self.fscaley

    @fscale.setter
    def fscale(self, value):
        self.fscalex, self.fscaley = value

    @property
    def alpha(self) -> int:
        return self._alpha

    @alpha.setter
    def alpha(self, value: int):
        self._alpha = by_interval(abs(value), max=MAX_ALPHA)

    @property
    def falpha(self) -> int:
        return self.alpha

    @property
    def visible(self) -> bool:
        return self.__get_visible__()

    @visible.setter
    def visible(self, value: bool):
        self._visible = value

    @property
    def fx(self):
        return self.x

    @fx.setter
    def fx(self, value):
        self.x = value

    @property
    def fy(self):
        return self.y

    @fy.setter
    def fy(self, value):
        self.y = value

    @property
    def fpos(self):
        return self.fx, self.fy

    @fpos.setter
    def fpos(self, value):
        self.fx, self.fy = value

    def __getitem__(self, item):
        return self.pos[item]

    def __str__(self):
        _dict = self.__dict__.copy()
        del _dict['name']

        for key in list(_dict.keys()):
            if key.startswith('_'):
                del _dict[key]

        _dict['visible'] = self.visible
        _dict['alpha'] = self.alpha

        return f'<{self.__class__.__name__}({self.name} => {_dict})>'

    __repr__ = __str__

    def __len__(self):
        return len(self.nodes)

    def enable(self):
        self.visible = self.enabled = True

    def disable(self):
        self.visible = self.enabled = False

    def input(self, event: List[Event]):
        if self.enabled:
            for node in self.nodes[::-1]:
                node.input(event)

    def draw_nodes(self, surface: Surface = ...):
        for node in self.nodes:
            node.draw(surface)

    def draw(self, surface: Surface = ..., draw_nodes: bool = True):
        if self.visible and draw_nodes:
            self.draw_nodes(surface)


scene = _RootNode(name='scene')


class _Node(_RootNode):
    def __init__(self, *args, parent=scene, **kwargs):
        super().__init__(*args, **kwargs)

        self.parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        try:
            self._parent.nodes.remove(self)
        except AttributeError:
            pass

        value.nodes.append(value)
        self._parent = value

    @property
    def fscalex(self):
        return self.parent.fscalex * self.scalex

    @fscalex.setter
    def fscalex(self, value):
        self.scalex = value / self.parent.fscalex

    @property
    def fscaley(self):
        return self.parent.fscaley * self.scaley

    @fscaley.setter
    def fscaley(self, value):
        self.scaley = value / self.parent.fscaley

    @property
    def falpha(self) -> int:
        return int(self.parent.falpha * self.alpha / MAX_ALPHA)

    @property
    def fx(self):
        return self.x + self.parent.fx

    @fx.setter
    def fx(self, value):
        self.x = value - self.parent.fx

    @property
    def fy(self):
        return self.y + self.parent.fy

    @fy.setter
    def fy(self, value):
        self.y = value - self.parent.fy

    def copy(self):
        return copy(self)

    def __del__(self):
        if self in self.parent.nodes:
            self.parent.nodes.remove(self)


__all__ = (
    '_Node',
    'scene'
)
