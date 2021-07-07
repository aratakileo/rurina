from utilities.math import _pyi_Vector2Type_type, _pyi_Vector2Type_item_type, Vector2
from utilities.string import class_output, short_class_output
from typing import Union, List, Sequence
from constants import _pyi_Surface_type
from pygame.event import Event
from copy import deepcopy
from event import get


class _RootNode:
    def __init__(
            self,
            position: _pyi_Vector2Type_type = (0, 0),
            visible: bool = True,
            enabled: bool = True,
            name: str = ...
    ):
        self.position = position
        self.visible, self.enabled = visible, enabled
        self.name = name

        self.__output_properties__ = ('position', 'visible')

        self.childnodes = []

    @property
    def position(self) -> Vector2:
        return self._position

    @position.setter
    def position(self, value: _pyi_Vector2Type_type):
        self._position = Vector2(value)

    @property
    def visible(self) -> bool:
        return self.__visible__()

    @visible.setter
    def visible(self, value: bool):
        self._visible = value

    def __getitem__(self, item: Union[slice, int]) -> Union[List[Union[float, int]], float, int]:
        return self.position.__getitem__(item)

    def __setitem__(self, key: Union[slice, int], value: _pyi_Vector2Type_item_type):
        self.position.__setitem__(key, value)

    def __str__(self):
        return class_output(self, self.name, output_properties=self.__output_properties__)

    def __repr__(self):
        return short_class_output(self, self.name)

    def __visible__(self) -> bool:
        return self._visible

    def enable(self):
        self.visible = self.enabled = True

    def disable(self):
        self.visible = self.enabled = False

    def input(self, event: Sequence[Event]):
        if self.enabled:
            for node in self.childnodes[::-1]:
                node.input(event)

    def draw_childnodes(self, surface: _pyi_Surface_type = ...):
        for node in self.childnodes:
            node.draw(surface)

    def draw(self, surface: _pyi_Surface_type = ..., draw_childnodes: bool = True):
        if self.visible and draw_childnodes:
            self.draw_childnodes(surface)


scene = _RootNode(name='scene')


class NodeType(_RootNode):
    def __init__(self, *args, parent: 'NodeType' = scene, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

        self.__output_properties__ = (*self.__output_properties__, 'parent')

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if '_parent' in self.__dir__():
            remove(self)

        if value in (None, ...):
            value = scene

        self._parent = value
        self._parent.childnodes.append(self)

    def copy(self):
        return deepcopy(self)


def remove(node: NodeType):
    node._parent.childnodes.remove(node)


def flip(surface: _pyi_Surface_type = ...):
    scene.input(get(False))
    scene.draw(surface)


__all__ = (
    'NodeType',
    'remove',
    'flip',
    'scene',
)
