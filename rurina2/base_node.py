from constants import MAX_ALPHA, MAX_SCALE
from prefabs.rmath import move_negativity
import pygame
import group


def get_surface(surface: pygame.Surface):
    if surface is ...:
        surface = pygame.display.get_surface()

    return surface


class _Node:
    def __init__(
            self,
            pos=(0, 0),
            rotation=0.0,
            scale=(MAX_SCALE, MAX_SCALE),
            alpha: int = MAX_ALPHA,
            color=(255, 255, 255),
            visible: bool = True,
            enabled: bool = True,
            auto_draw: bool = True,
            name: str = ...,
            group: group.Group = group.rootgroup,
            parent=None
    ) -> None:
        self.name = name

        if self.name is ...:
            self.name = self.__class__.__name__

        self.nodes = []
        self.parent = parent
        self.x, self.y = pos
        self.rotation = rotation
        self.scale, self.alpha = scale, alpha
        self.visible = visible
        self.enabled = enabled
        self.auto_draw = auto_draw
        self.color = color
        self.group = group

    def __del__(self):
        self.nodes = []
        try:
            self.parent.remove(self)
        except AttributeError:
            pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    @property
    def parent(self):
        return self.__pref__

    @parent.setter
    def parent(self, value):
        self.__pref__ = value
        try:
            value.append(self)
        except AttributeError:
            pass

    @property
    def group(self):
        return self.__group__

    @group.setter
    def group(self, value):
        if value is None:
            try:
                if self.__group__ is not None:
                    self.__group__.remove(self)
            except AttributeError:
                value = group.rootgroup

        value.append(self)

        self.__group__ = value

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, value):
        self.x, self.y = value

    @property
    def fx(self):
        if self.parent is not None:
            return self.x + self.parent.fx
        return self.x

    @fx.setter
    def fx(self, value):
        if self.parent is not None:
            self.x = value - self.parent.fx
        self.x = value

    @property
    def fy(self):
        if self.parent is not None:
            return self.y + self.parent.fy
        return self.y

    @fy.setter
    def fy(self, value):
        if self.parent is not None:
            self.y = value - self.parent.fy
        self.y = value

    @property
    def fpos(self):
        return self.fx, self.fy

    @fpos.setter
    def fpos(self, value):
        self.fx, self.fy = value

    @property
    def scalex(self) -> float:
        return self.scale[0]

    @scalex.setter
    def scalex(self, value):
        self.scale = (value, self.scaley)

    @property
    def scaley(self) -> float:
        return self.scale[1]

    @scaley.setter
    def scaley(self, value):
        self.scale = (self.scalex, value)

    @property
    def flip_h(self) -> bool:
        return self.scalex < 0

    @flip_h.setter
    def flip_h(self, value):
        self.scalex = move_negativity(1 if not value else -1, self.scalex)

    @property
    def flip_v(self) -> bool:
        return self.scaley < 0

    @flip_v.setter
    def flip_v(self, value):
        self.scaley = move_negativity(1 if not value else -1, self.scaley)

    @property
    def flip(self) -> bool:
        return self.flip_h or self.flip_v

    @flip.setter
    def flip(self, value):
        self.flip_h = self.flip_v = value

    @property
    def can_be_drawn(self):
        return self.visible and self.alpha > 0 and self.scale != 0

    def enable(self):
        self.enabled = self.visible = True

    def disable(self):
        self.enabled = self.visible = False

    def append(self, node):
        self.nodes.append(node)
        if id(node.parent) != id(self):
            node.parent = self

    def remove(self, node):
        try:
            self.nodes.remove(node)
        except ValueError:
            pass

    def input(self, event) -> None:
        if self.enabled:
            for node in self.nodes[::-1]:
                node.input(event)

    def draw(self, surface: pygame.Surface = ...) -> None:
        if self.can_be_drawn:
            surface = get_surface(surface)

            for node in self.nodes:
                if node.auto_draw:
                    node.draw(surface)


rootnode = _Node(parent=None, pos=(0, 0))
group.rootgroup.clear()


class _AdditionalNode(_Node):
    def __init__(self, *args, parent=rootnode, **kwargs):
        super().__init__(*args, parent=parent, **kwargs)

    @property
    def next(self):
        if self.group.nodes.index(self) == len(self.group) - 1:
            return self.group.next.nodes[0]
        else:
            return self.group.nodes[self.group.nodes.index(self) + 1]

    @property
    def prev(self):
        if self.group.nodes.index(self) == 0:
            return self.group.prev.nodes[-1]
        else:
            return self.group.nodes[self.group.nodes.index(self) - 1]

    @property
    def ralpha(self) -> int:
        try:
            return int(self.alpha * self.parent.ralpha / MAX_ALPHA)
        except AttributeError:
            return self.alpha

    @property
    def rscale(self):
        try:
            return (
                self.scale[0] * self.parent.rscale[0],
                self.scale[1] * self.parent.rscale[1]
            )
        except AttributeError:
            return self.scale

    @property
    def rscalex(self):
        return self.rscale[0]

    @property
    def rscaley(self):
        return self.rscale[1]


__all__ = [
    '_Node',
    '_AdditionalNode',
    'rootnode',
    'get_surface'
]
