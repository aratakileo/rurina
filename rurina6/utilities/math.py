from typing import Union, List, Tuple
from copy import deepcopy
from math import sqrt


_pyi_Vector2Type_type = Union['Vector2Type', Tuple[Union[float, int], Union[float, int]], List[Union[float, int]]]
_pyi_Vector2Type_item_type = Union[_pyi_Vector2Type_type, int, float]


class Vector2Type:
    def __init__(self, value1, value2):
        if not isinstance(value1, (int, float)):
            self._data = [*value1[:]]
            return

        self._data = [value1, value2]

    def __len__(self):
        return 2

    def __bool__(self):
        return self[0] != 0 and self[1] != 0

    def __str__(self):
        return f'<{self.__class__.__name__}({str(self[:])[1:-1]})>'

    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self[:])[1:-1]})>'

    def __eq__(
            self,
            other: _pyi_Vector2Type_item_type
    ) -> bool:
        if isinstance(other, (int, float)):
            return self[0] == other and self[1] == other

        return self[0] == other[0] and self[1] == other[1]

    def __ne__(
            self,
            other: _pyi_Vector2Type_item_type
    ) -> bool:
        return not (self == other)

    def __contains__(self, item: Union[float, int]) -> bool:
        return item in self[:]

    def __getitem__(self, item: Union[slice, int]) -> Union[List[Union[float, int]], float, int]:
        return self._data[item]
    
    def __neg__(self) -> 'Vector2Type':
        return self.__class__(-self[0], -self[1])

    def __abs__(self) -> 'Vector2Type':
        return self.__class__(abs(self[0]), abs(self[1]))

    def __add__(
            self,
            other: _pyi_Vector2Type_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return self.__class__(self[0] + other, self[1] + other)

        return self.__class__(self[0] + other[0], self[1] + other[1])

    def __sub__(
            self,
            other: _pyi_Vector2Type_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return self.__class__(self[0] - other, self[1] - other)

        return self.__class__(self[0] - other[0], self[1] - other[1])

    def __floordiv__(
            self,
            other: _pyi_Vector2Type_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return self.__class__(self[0] // other, self[1] // other)

        return self.__class__(self[0] // other[0], self[1] // other[1])

    def __truediv__(
            self,
            other: _pyi_Vector2Type_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return self.__class__(self[0] / other, self[1] / other)

        return self.__class__(self[0] / other[0], self[1] / other[1])

    def __mul__(
            self,
            other: _pyi_Vector2Type_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return self.__class__(self[0] * other, self[1] * other)

        return self.__class__(self[0] * other[0], self[1] * other[1])

    def __pow__(
            self,
            other: _pyi_Vector2Type_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return self.__class__(self[0] ** other, self[1] ** other)

        return self.__class__(self[0] ** other[0], self[1] ** other[1])

    def __iter__(self):
        return self._data

    def copy(self):
        return deepcopy(self)

    def length(self) -> float:
        return sqrt(self[0] ** 2 + self[1] ** 2)


StaticVector2Type = Vector2Type


class DynamicVector2Type(Vector2Type):
    def __init__(self, *args):
        super().__init__(*args)

    def __setitem__(
            self,
            key: Union[int, slice],
            value: _pyi_Vector2Type_item_type
    ):
        self._data[key] = value


class Vector2(DynamicVector2Type):
    def __init__(self, x: Union[int, float, _pyi_Vector2Type_type] = 0, y: Union[int, float] = 0):
        super().__init__(x, y)

    @property
    def x(self) -> Union[int, float]:
        return self[0]

    @x.setter
    def x(self, value: Union[int, float]):
        self[0] = value

    @property
    def y(self) -> Union[int, float]:
        return self[1]

    @y.setter
    def y(self, value: Union[int, float]):
        self[1] = value


DynamicVector2 = Vector2


class StaticVector2(StaticVector2Type):
    def __init__(self, x: Union[int, float, _pyi_Vector2Type_type] = 0, y: Union[int, float] = 0):
        super().__init__(x, y)

    @property
    def x(self) -> Union[int, float]:
        return self[0]

    @property
    def y(self) -> Union[int, float]:
        return self[1]


def distance(
        pos1: _pyi_Vector2Type_type,
        pos2: _pyi_Vector2Type_type
) -> float:
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def ininterval(
        value: Union[float, int],
        min_value: Union[float, int] = ...,
        max_value: Union[float, int] = ...
) -> bool:
    if min_value in (None, ...):
        min_value = value

    if max_value in (None, ...):
        max_value = value

    return min_value <= value <= max_value


def byinterval(
        value: Union[float, int],
        min_value: Union[float, int] = ...,
        max_value: Union[float, int] = ...
) -> Union[float, int]:
    if min_value in (None, ...):
        min_value = value

    if max_value in (None, ...):
        max_value = value

    if value < min_value:
        return min_value

    if value > max_value:
        return max_value

    return value


__all__ = (
    'Vector2Type',
    'StaticVector2Type',
    'DynamicVector2Type',
    'Vector2',
    'StaticVector2',
    'DynamicVector2',
    'distance',
    'ininterval',
    'byinterval'
)
