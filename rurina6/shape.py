from utilities.math import Vector2, _pyi_Vector2Type_type, DynamicVector2Type, _pyi_Vector2Type_item_type, Vector2Type, StaticVector2, distance
from pygame.rect import Rect as _Rect, RectType as _RectType
from constants import _pyi_Color_type, _pyi_Surface_type
from pygame import Rect as _Rect1, draw as _draw
from utilities.string import class_output
from typing import Sequence, Union, List
from pygame.display import get_surface
from copy import deepcopy


class SizeVector2(DynamicVector2Type):
    def __init__(self, width: Union[int, _pyi_Vector2Type_type] = 100, height: int = 100):
        super().__init__(width, height)

    @property
    def width(self) -> Union[int, float]:
        return self[0]

    @width.setter
    def width(self, value: Union[int, float]):
        self[0] = value

    @property
    def height(self) -> Union[int, float]:
        return self[1]

    @height.setter
    def height(self, value: Union[int, float]):
        self[1] = value


class _ShapeBase:
    def __init__(self):
        self.__output_properties__ = ()

    def __str__(self):
        return class_output(self, output_properties=self.__output_properties__)

    __repr__ = __str__

    def copy(self):
        return deepcopy(self)

    def accommodate_point(self, position: _pyi_Vector2Type_type, only_edge: bool = False) -> Vector2:
        position = Vector2(position)
        return position

    def collide(self, shape: '_ShapeBase') -> bool:
        return False

    def collidelist(self, shapes: Sequence['_ShapeBase']) -> int:
        for i in range(len(shapes)):
            if shapes[i] in (None, ...):
                continue

            if self.collide(shapes[i]):
                return i

        return -1

    def collidepoint(self, position: _pyi_Vector2Type_type) -> bool:
        return False


class ShapeType(_ShapeBase):
    def __init__(self, position: _pyi_Vector2Type_type = (0, 0)):
        super().__init__()

        self.position = position
        self.__output_properties__ = (*self.__output_properties__, 'position')

    @property
    def position(self) -> Vector2:
        return self._position

    @position.setter
    def position(self, value: _pyi_Vector2Type_type):
        self._position = Vector2(value)


_Rect_type = (_Rect, _Rect1, _RectType)


class Rect(ShapeType):
    def __init__(
            self,
            x: Union[int, float, _pyi_Vector2Type_type] = 0,
            y: Union[int, float, _pyi_Vector2Type_type] = 0,
            width: Union[int, float] = 100,
            height: Union[int, float] = 100
    ):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            position = (x, y)
            size = (width, height)
        else:
            position = x

            if y == 0:
                size = (100, 100)

            size = y

        super().__init__(position)

        self.size = size
        self.__output_properties__ = (*self.__output_properties__, 'size')
        self._last_op = -1

    @property
    def size(self) -> SizeVector2:
        return self._size

    @size.setter
    def size(self, value: _pyi_Vector2Type_type):
        self._size = SizeVector2(value)

    @property
    def center(self) -> StaticVector2:
        return StaticVector2(self.position + self.size / 2)

    @property
    def rightbottom(self) -> StaticVector2:
        return StaticVector2(self.position + self.size)

    def __getitem__(self, item: Union[slice, int]) -> List[Union[int, float]]:
        return [*self.position[:], *self.size[:]][item]

    def __setitem__(self, key: Union[slice, int], value: _pyi_Vector2Type_item_type):
        _list = self[:]
        _list[key] = value
        self.position, self.size = _list

    def accommodate_point(self, position: _pyi_Vector2Type_type, only_edge: bool = False) -> Vector2:
        position = Vector2(position)

        if not self.collidepoint(position):
            if position.x > self.rightbottom.x:
                position.x = self.rightbottom.x

            if position.x < self.position.x:
                position.x = self.position.x

            if position.y > self.rightbottom.y:
                position.y = self.rightbottom.y

            if position.y < self.position.y:
                position.y = self.position.y

        return position

    def collide(self, shape: _ShapeBase) -> bool:
        if isinstance(shape, (*_Rect_type, Rect, list, tuple)):
            return self[0] <= (shape[0] + shape[2]) and (self[0] + self[2]) >= shape[0]\
                   and self[1] <= (shape[1] + shape[3]) and (self[1] + self[3]) >= shape[1]
        else:
            shape.collide(self)

    def collidepoint(self, position: _pyi_Vector2Type_type) -> bool:
        return self[0] <= position[0] <= (self[0] + self[2]) \
               and self[1] <= position[1] <= (self[1] + self[3])


_Rect_type = (*_Rect_type, Rect)


class Circle(ShapeType):
    def __init__(self, position: _pyi_Vector2Type_type = (0, 0), radius: int = 50):
        super().__init__(position)

        self.radius = radius

    @property
    def center(self) -> StaticVector2:
        return StaticVector2(self.position + self.radius)

    def __getitem__(self, item: Union[slice, int]) -> List[Union[int, float]]:
        return [*self.position[:], self.radius][item]

    def __setitem__(self, key: Union[slice, int], value: _pyi_Vector2Type_item_type):
        _list = self[:]
        _list[key] = value
        self.position, self.radius = _list

    def accommodate_point(self, position: _pyi_Vector2Type_type, only_edge: bool = False) -> Vector2:
        position = Vector2(position)

        if not self.collidepoint(position) or only_edge:
            d = distance(position, self.center)
            if d != 0:
                return Vector2(
                    self.center.x + (position.x - self.center.x) / d * self.radius,
                    self.center.y + (position.y - self.center.y) / d * self.radius
                )

        return position

    def collide(self, shape: '_ShapeBase') -> bool:
        if isinstance(shape, (Circle, list, tuple)):
            return distance((shape[0], shape[1]), self.position) <= (self.radius + shape[2])
        elif isinstance(shape, Rect):
            return False
        else:
            shape.collide(self)

    def collidepoint(self, position: _pyi_Vector2Type_type) -> bool:
        return distance(self.position, position) <= self.radius


class Polygon(_ShapeBase):
    def __init__(self, points: Sequence[_pyi_Vector2Type_type] = [(0, 0)]):
        super().__init__()
        self.points = points

    @property
    def points(self) -> List[Vector2]:
        return self._points

    @points.setter
    def points(self, value: Sequence[_pyi_Vector2Type_type]):
        self._points = []
        for point in value:
            self._points.append(Vector2(point))

    def __len__(self):
        return len(self.points)

    def __getitem__(self, item: Union[slice, int]) -> Union[Sequence[_pyi_Vector2Type_type], _pyi_Vector2Type_type]:
        return self.points[item]

    def __setitem__(self, key: Union[slice, int], value: Union[Sequence[_pyi_Vector2Type_type], _pyi_Vector2Type_type]):
        self.points[key] = value


def draw(
        shape: Union[_ShapeBase, _pyi_Vector2Type_type],
        surface: _pyi_Surface_type = ...,
        color: _pyi_Color_type = (40, 240, 40),
        *args,
        **kwargs
) -> _pyi_Surface_type:
    if surface in (None, ...):
        surface = get_surface()

    if isinstance(shape, (Vector2Type, Sequence)):
        surface.set_at(shape[:], color)
    elif isinstance(shape, _Rect_type):
        _draw.rect(surface, color, shape[:], *args, **kwargs)
    elif isinstance(shape, Circle):
        _draw.circle(surface, color, shape[:-1], shape.radius)
    elif isinstance(shape, Polygon):
        if len(shape) == 0:
            return surface

        if len(shape) == 1:
            surface.set_at(shape[0][:], color)
        elif len(shape) == 2:
            _draw.line(surface, color, shape[0][:], shape[1][:], *args, **kwargs)
        else:
            _draw.polygon(surface, color, shape[:], *args, **kwargs)

    return surface


__all__ = (
    'Rect',
    'Circle',
    'Polygon',
    'draw'
)
