from typing import overload, Union, Tuple, List, Sequence
from copy import deepcopy
from math import sqrt


_pyi_Vector2_type = Union['Vector2Type', Tuple[Union[float, int], Union[float, int]], List[Union[float, int]]]
_pyi_Vector2_item_type = Union[_pyi_Vector2_type, int, float]


class Vector2Type:
    def __init__(self, data_name: Tuple[str, str, str] = ('x', 'y', 'position'), *args, **kwargs):
        self._data = [0, 0]

        if data_name[2] in kwargs:
            self[:] = kwargs[data_name[2]][:]
            return

        if data_name[0] in kwargs:
            self[0] = kwargs[data_name[0]]

        if data_name[1] in kwargs:
            self[1] = kwargs[data_name[1]]

        if len(args) > 0:
            if isinstance(args[0], (int, float)):
                self[0] = args[0]

                if len(args) > 1:
                    self[1] = args[1]
            else:
                self[0], self[1] = args[0][:]

    def __len__(self):
        return 2

    def __bool__(self):
        return self[0] != 0 and self[1] != 0

    def __str__(self):
        return f'<Vector2({str(self[:])[1:-1]})>'

    def __repr__(self):
        return f'<Vector2({repr(self[:])[1:-1]})>'

    def __eq__(
            self,
            other: _pyi_Vector2_item_type
    ) -> bool:
        if isinstance(other, (int, float)):
            return self[0] == other and self[1] == other

        return self[0] == other[0] and self[1] == other[1]

    def __ne__(
            self,
            other: _pyi_Vector2_item_type
    ) -> bool:
        return not (self == other)

    def __contains__(self, item: Union[float, int]):
        return item in self[:]

    def __getitem__(self, item: Union[int, slice]) -> Union[List[Union[float, int]], float, int]:
        return self._data[item]

    def __setitem__(
            self,
            key: Union[int, slice],
            value: _pyi_Vector2_item_type
    ):
        self._data[key] = value

    def __neg__(self):
        return [-self[0], -self[1]]

    def __abs__(self):
        return [abs(self[0]), abs(self[1])]

    def __add__(
            self,
            other: _pyi_Vector2_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return Vector2(self[0] + other, self[1] + other)

        return Vector2(self[0] + other[0], self[1] + other[1])

    def __sub__(
            self,
            other: _pyi_Vector2_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return Vector2(self[0] - other, self[1] - other)

        return Vector2(self[0] - other[0], self[1] - other[1])

    def __floordiv__(
            self,
            other: _pyi_Vector2_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return Vector2(self[0] // other, self[1] // other)

        return Vector2(self[0] // other[0], self[1] // other[1])

    def __truediv__(
            self,
            other: _pyi_Vector2_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return Vector2(self[0] / other, self[1] / other)

        return Vector2(self[0] / other[0], self[1] / other[1])

    def __mul__(
            self,
            other: _pyi_Vector2_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return Vector2(self[0] * other, self[1] * other)

        return Vector2(self[0] * other[0], self[1] * other[1])

    def __pow__(
            self,
            other: _pyi_Vector2_item_type
    ) -> 'Vector2Type':
        if isinstance(other, (int, float)):
            return Vector2(self[0] ** other, self[1] ** other)

        return Vector2(self[0] ** other[0], self[1] ** other[1])

    def copy(self):
        return deepcopy(self)

    def length(self) -> float:
        return sqrt(self[0] ** 2 + self[1] ** 2)


class Vector2(Vector2Type):
    @overload
    def __init__(self, x: Union[float, int] = 0, y: Union[float, int] = 0): ...

    @overload
    def __init__(
            self,
            position: _pyi_Vector2_type
    ): ...

    def __init__(self, *args, **kwargs):
        super().__init__(('x', 'y', 'position'), *args, **kwargs)

    @property
    def x(self) -> Union[float, int]:
        return self._data[0]

    @x.setter
    def x(self, value: Union[float, int]):
        self._data[0] = value

    @property
    def y(self) -> Union[float, int]:
        return self._data[1]

    @y.setter
    def y(self, value: Union[float, int]):
        self._data[1] = value


def distance(
        pos1: _pyi_Vector2_type,
        pos2: _pyi_Vector2_type
) -> float:
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def in_interval(
        value: Union[float, int],
        min: Union[float, int] = ...,
        max: Union[float, int] = ...
) -> bool:
    if min in (None, ...):
        min = value

    if max in (None, ...):
        max = value

    return min <= value <= max


def by_interval(
        value: Union[float, int],
        min: Union[float, int] = ...,
        max: Union[float, int] = ...
) -> Union[float, int]:
    if min in (None, ...):
        min = value

    if max in (None, ...):
        max = value

    if value < min:
        return min

    if value > max:
        return max

    return value


__all__ = (
    'Vector2Type',
    'Vector2',
    'distance',
    'in_interval',
    'by_interval'
)
