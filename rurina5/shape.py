from utilities.math import Vector2, Vector2Type, _pyi_Vector2_type
from constants import _pyi_Color_type, _pyi_Surface_type
from typing import Sequence, overload, Union, List
from pygame import Rect as pygRect, draw as _draw
from pygame.rect import Rect as mRect, RectType
from utilities.string import class_output
from pygame.display import get_surface
from copy import deepcopy


class SizeVector2(Vector2Type):
    @overload
    def __init__(self, width: int = 0, height: int = 0): ...

    @overload
    def __init__(
            self,
            size: _pyi_Vector2_type
    ): ...

    def __init__(self, *args, **kwargs):
        super().__init__(('width', 'height', 'size'), *args, **kwargs)

    @property
    def width(self) -> int:
        return self._data[0]

    @width.setter
    def width(self, value: int):
        self._data[0] = value

    @property
    def height(self) -> int:
        return self._data[0]

    @height.setter
    def height(self, value: int):
        self._data[0] = value


class ShapeType:
    def __init__(self, position: _pyi_Vector2_type = (0, 0)):
        self.position = position
        self.__output_properties__ = ('position',)

    def __str__(self):
        return class_output(self, output_properties=self.__output_properties__)

    __repr__ = __str__

    @property
    def position(self) -> Vector2:
        return self._position

    @position.setter
    def position(self, value: _pyi_Vector2_type):
        self._position = Vector2(value)

    def copy(self):
        return deepcopy(self)

    def collide(self, shape: 'ShapeType') -> bool:
        return False

    def collidelist(self, shapes: Sequence['ShapeType']) -> int:
        for i in range(len(shapes)):
            if shapes[i] in (None, ...):
                continue

            if self.collide(shapes[i]):
                return i

        return -1

    def collidepoint(self, position: _pyi_Vector2_type) -> bool:
        return False


_Rect_type = (mRect, pygRect, RectType)


class Rect(ShapeType):
    @overload
    def __init__(self, x: Union[float, int], y: Union[float, int], width: int, height: int): ...

    @overload
    def __init__(self, position: _pyi_Vector2_type = (0, 0), size: _pyi_Vector2_type = (100, 100)): ...

    def __init__(self, *args, **kwargs):
        self.size = (100, 100)
        position = [0, 0]

        if len(args) > 0:
            if isinstance(args[0], (int, float)):
                position[0] = args[0]
            else:
                position = args[0]

            if len(args) > 1:
                if isinstance(args[1], (int, float)):
                    position[1] = args[1]
                else:
                    self.size = args[1]

                if len(args) > 2:
                    self.size[0] = args[2]

                    if len(args) > 3:
                        self.size[1] = args[3]

        if len(kwargs) > 0:
            if 'position' in kwargs:
                position = kwargs['position']

            if 'size' in kwargs:
                self.size = kwargs['size']

            if 'x' in kwargs:
                position[0] = kwargs['x']

            if 'y' in kwargs:
                position[1] = kwargs['y']

            if 'width' in kwargs:
                self.size[0] = kwargs['width']

            if 'height' in kwargs:
                self.size[1] = kwargs['height']

        super().__init__(position)
        self.__output_properties__ = (*self.__output_properties__, 'size', 'center')

    @property
    def position(self) -> Vector2:
        if (self._position + self.size / 2) != self._center:
            print((self._position + self.size / 2), self._center)
            self._position = self._center - self.size / 2
            exit(self)

        return self._position

    @position.setter
    def position(self, value: _pyi_Vector2_type):
        self._position = Vector2(value)
        self.center = self._position + self.size / 2

    @property
    def size(self) -> SizeVector2:
        return self._size

    @size.setter
    def size(self, value: _pyi_Vector2_type):
        self._size = SizeVector2(value)

    @property
    def center(self) -> SizeVector2:
        if (self._position + self.size / 2) != self._center:
           self._center = self._position + self.size / 2

        return self._center

    @center.setter
    def center(self, value: _pyi_Vector2_type):
        self._center = SizeVector2(value)

    def __getitem__(self, item: Union[slice, int]) -> List[Union[int, float]]:
        return [*self.position[:], *self.size[:]][item]

    def collide(self, shape: 'ShapeType') -> bool:
        if isinstance(shape, (*_Rect_type, Rect, list, tuple)):
            return self[0] <= (shape[0] + shape[2]) and (self[0] + self[2]) >= shape[0]\
                   and self[1] <= (shape[1] + shape[3]) and (self[1] + self[3]) >= shape[1]
        else:
            shape.collide(self)

    def collidepoint(self, position: _pyi_Vector2_type) -> bool:
        return self[0] <= position[0] <= (self[0] + self[2]) \
               and self[1] <= position[1] <= (self[1] + self[3])


_Rect_type = (*_Rect_type, Rect)


def draw(
        shape: Union[Vector2Type, ShapeType],
        color: _pyi_Color_type = (40, 40, 240),
        surface: _pyi_Surface_type = ...,
        collideborder: bool = False,
        *args,
        **kwargs
) -> _pyi_Surface_type:
    if surface in (None, ...):
        surface = get_surface()

    if isinstance(shape, Vector2Type):
        surface.set_at(shape[:], color)
    elif isinstance(shape, _Rect_type):
        if collideborder:
            _draw.rect(surface, color, shape[:], 1, *args, **kwargs)
        else:
            _draw.rect(surface, color, shape[:], *args, **kwargs)

    return surface


__all__ = (
    'Rect',
    'draw',
)
