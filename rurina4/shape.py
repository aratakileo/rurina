from pygame import draw as _draw, Rect as _Rect, rect, Surface, display, transform
from typing import Tuple, Union, Sequence
from utilities.math import distance
from copy import copy
import math


# TODO: append all shape types


class _Shape:
    def __init__(self):
        pass

    def __str__(self):
        _dict = self.__dict__.copy()

        for key in list(_dict.keys()):
            if key.startswith('_'):
                del _dict[key]

        return f'<{self.__class__.__name__}({_dict})>'

    __repr__ = __str__

    def copy(self):
        return copy(self)

    def collide(self, shape) -> bool:
        return False

    def collidelist(self, shape_list: Sequence) -> int:
        for i in range(len(shape_list)):
            if self.collide(shape_list[i]):
                return i

        return -1

    def collidepoint(self, x: Union[int, float], y: Union[int, float]) -> bool:
        return False


class Point(_Shape):
    def __init__(self, x: Union[int, float] = 0, y: Union[int, float] = 0):
        super().__init__()
        self.pos = x, y

    @property
    def pos(self) -> Tuple[Union[int, float], Union[int, float]]:
        return self.x, self.y

    @pos.setter
    def pos(self, value: Tuple[Union[int, float], Union[int, float]]):
        self.x, self.y = value

    def __getitem__(self, item):
        return self.pos[item]

    def collide(self, shape) -> bool:
        if isinstance(shape, (Point, list, tuple)):
            return self.collidepoint(*shape[:])
        else:
            return shape.collidepoint(*self.pos)

    def collidepoint(self, x: Union[int, float], y: Union[int, float]) -> bool:
        return self.pos == (x, y)


class Rect(Point):
    def __init__(self, x: Union[int, float] = 0, y: Union[int, float] = 0, width: int = 100, height: int = ...):
        super().__init__(x, y)
        self.size = width, height if height not in (None, ...) else width

    @property
    def size(self) -> Tuple[int, int]:
        return self.width, self.height

    @size.setter
    def size(self, value: Tuple[int, int]):
        self.width, self.height = value

    @property
    def right(self) -> Union[int, float]:
        return self.x + self.width

    @right.setter
    def right(self, value: Union[int, float]):
        self.x = value - self.width

    @property
    def bottom(self) -> Union[int, float]:
        return self.y + self.height

    @bottom.setter
    def bottom(self, value: Union[int, float]):
        self.y = value - self.height

    @property
    def centerx(self) -> Union[int, float]:
        return self.x + self.width / 2

    @centerx.setter
    def centerx(self, value: Union[int, float]):
        self.x = value - self.width / 2

    @property
    def centery(self) -> Union[int, float]:
        return self.y + self.height / 2

    @centery.setter
    def centery(self, value: Union[int, float]):
        self.y = value - self.height / 2

    @property
    def center(self) -> Tuple[Union[int, float], Union[int, float]]:
        return self.centerx, self.centery

    @center.setter
    def center(self, value: Tuple[Union[int, float], Union[int, float]]):
        self.centerx, self.centery = value

    def __getitem__(self, item):
        return (*self.pos, *self.size)[item]

    def __str__(self):
        _dict = self.__dict__.copy()

        for key in list(_dict.keys()):
            if key.startswith('_'):
                del _dict[key]

        _dict['right'], _dict['bottom'] = self.right, self.bottom
        _dict['centerx'], _dict['centery'] = self.centerx, self.centery

        return f'<{self.__class__.__name__}({_dict})>'

    __repr__ = __str__

    def collide(self, shape) -> bool:
        if isinstance(shape, (Rect, _Rect, rect.Rect, list, tuple)):
            return self.x <= (shape[0] + shape[2]) \
                   and self.y <= (shape[1] + shape[3]) \
                   and self.right >= shape[0] \
                   and self.bottom >= shape[1]
        else:
            return shape.collide(self)

    def collidepoint(self, x: Union[int, float], y: Union[int, float]) -> bool:
        return self.x <= x <= self.right and self.y <= y <= self.bottom


_Rect_types = (Rect, _Rect, rect.Rect)


class Circle(Point):
    def __init__(self, x: Union[int, float] = 0, y: Union[int, float] = 0, radius: int = 50):
        super().__init__(x, y)
        self.radius = radius

    def __getitem__(self, item):
        return (*self.pos, self.radius)[item]

    @property
    def centerx(self) -> Union[int, float]:
        return self.x + self.radius

    @centerx.setter
    def centerx(self, value: Union[int, float]):
        self.x = value - self.radius

    @property
    def centery(self) -> Union[int, float]:
        return self.y + self.radius

    @centery.setter
    def centery(self, value: Union[int, float]):
        self.y = value - self.radius

    @property
    def center(self) -> Tuple[Union[int, float], Union[int, float]]:
        return self.centerx, self.centery

    @center.setter
    def center(self, value: Tuple[Union[int, float], Union[int, float]]):
        self.centerx, self.centery = value

    def __str__(self):
        _dict = self.__dict__.copy()

        for key in list(_dict.keys()):
            if key.startswith('_'):
                del _dict[key]

        _dict['centerx'], _dict['centery'] = self.centerx, self.centery

        return f'<{self.__class__.__name__}({_dict})>'

    __repr__ = __str__

    def collide(self, shape) -> bool:
        if isinstance(shape, (Circle, list, tuple)):
            return distance(self.center, (shape[0] + shape[2], shape[1] + shape[2])) < (self.radius + shape[2])
        elif isinstance(shape, _Rect_types):
            dx, dy = abs(self.centerx - shape.centerx), abs(self.centery - shape.centery)

            if (dx > (shape.width / 2 + self.radius)) or (dy > (shape.height / 2 + self.radius)):
                return False

            if (dx <= (shape.width / 2)) or (dy <= (shape.height / 2)):
                return True

            dist = (dx - shape.width / 2) ** 2 + (dy - shape.height / 2) ** 2

            return dist <= (self.radius ** 2)
        else:
            return shape.collide(self)

    def collidepoint(self, x: Union[int, float], y: Union[int, float]) -> bool:
        return distance(self.center, (x, y)) < self.radius

    def accommodate_point(
            self,
            x: Union[int, float],
            y: Union[int, float],
            only_edge: bool = False
    ) -> Tuple[Union[float, int], Union[float, int]]:
        if not self.collidepoint(x, y) or only_edge:
            d = math.sqrt((x - self.centerx) ** 2 + (y - self.centery) ** 2)
            if d != 0:
                return self.centerx + (x - self.centerx) / d * self.radius,\
                       self.centery + (y - self.centery) / d * self.radius

            return x, y

        return x, y


class Line(Point):
    def __init__(
            self,
            x: Union[int, float] = 0,
            y: Union[int, float] = 0,
            endx: Union[int, float] = 100,
            endy: Union[int, float] = 100
    ):
        super().__init__(x, y)
        self.endpos = endx, endy

    @property
    def endpos(self):
        return self.endx, self.endy

    @endpos.setter
    def endpos(self, value):
        self.endx, self.endy = value

    @property
    def centerx(self):
        return (self.x + self.endx) / 2

    @centerx.setter
    def centerx(self, value):
        diff = value - self.centerx
        self.x += diff
        self.endx += diff

    @property
    def centery(self):
        return (self.y + self.endy) / 2

    @centery.setter
    def centery(self, value):
        diff = value - self.centery
        self.y += diff
        self.endy += diff

    @property
    def center(self):
        return self.centerx, self.centery

    @center.setter
    def center(self, value):
        self.centerx, self.centery = value

    def __getitem__(self, item):
        return (*self.pos, *self.endpos)[item]

    def __str__(self):
        _dict = self.__dict__.copy()

        for key in list(_dict.keys()):
            if key.startswith('_'):
                del _dict[key]

        _dict['centerx'], _dict['centery'] = self.centerx, self.centery

        return f'<{self.__class__.__name__}({_dict})>'

    __repr__ = __str__

    def collide(self, shape) -> bool:
        if isinstance(shape, (Line, list, tuple)):
            denominator = (self.endx - self.x) * (shape[3] - shape[1]) - (self.endy - self.y) * (shape[2] - shape[0])
            numerator1 = (self.y - shape[1]) * (shape[2] - shape[0]) - (self.x - shape[0]) * (shape[3] - shape[1])
            numerator2 = (self.y - shape[1]) * (self.endx - self.x) - (self.x - shape[0]) * (self.endy - self.y)
            # denominator = (self.endx - self.x) * (shape.endy - shape.y) - (self.endy - self.y) * (shape.endx - shape.x)
            # numerator1 = (self.y - shape.y) * (shape.endx - shape.x) - (self.x - shape.x) * (shape.endy - shape.y)
            # numerator2 = (self.y - shape.y) * (self.endx - self.x) - (self.x - shape.x) * (self.endy - self.y)

            if denominator == 0:
                return numerator1 == 0 and numerator2 == 0

            return 0 <= numerator1 / denominator <= 1 and 0 <= numerator2 / denominator <= 1
        elif isinstance(shape, Circle):
            linelen = distance(self.pos, self.endpos)
            dx, dy = (self.endx - self.x) / linelen, (self.endy - self.y) / linelen
            t = dx * (shape.centerx - self.x) + dy * (shape.centery - self.y)
            distance_between = distance((t * dx + self.x, t * dy + self.y), shape.center)

            if distance_between < shape.radius:
                dt = math.sqrt(shape.radius ** 2 - distance_between ** 2)
                return ((t + dt) * dy + self.y) >= self.y and ((t - dt) * dy + self.y) <= self.endy
            else:
                return distance_between == shape.radius
        elif isinstance(shape, _Rect_types):
            return self.collide(Line(shape.x, shape.y, shape.x, shape.bottom))\
                   or self.collide(Line(shape.x, shape.y, shape.right, shape.bottom))\
                   or self.collide(Line(shape.right, shape.y, shape.right, shape.bottom))\
                   or self.collide(Line(shape.x, shape.bottom, shape.right, shape.bottom))\
                   or shape.collidepoint(*self.pos) or shape.collidepoint(*self.endpos)
        else:
            return shape.collide(self)

    def collidepoint(self, x: Union[int, float], y: Union[int, float]) -> bool:
        lx, ly = self.endx - self.x, self.endy - self.y
        dx, dy = x - self.x, y - self.y
        l = math.sqrt(lx ** 2 + ly ** 2)
        d = math.sqrt(dx ** 2 + dy ** 2)
        q = d / l
        return d <= l and abs(q * lx - dx) < 1 and abs(q * ly - dy) < 1


class Triangle(_Shape):
    def __init__(
            self,
            apos: Tuple[Union[int, float], Union[int, float]] = (0, 0),
            bpos: Tuple[Union[int, float], Union[int, float]] = (50, 100),
            cpos: Tuple[Union[int, float], Union[int, float]] = (0, 100)
    ):
        super().__init__()
        self.apos = apos
        self.bpos = bpos
        self.cpos = cpos

    @property
    def apos(self) -> Tuple[Union[int, float], Union[int, float]]:
        return self.ax, self.ay

    @apos.setter
    def apos(self, value: Tuple[Union[int, float], Union[int, float]]):
        self.ax, self.ay = value

    @property
    def bpos(self) -> Tuple[Union[int, float], Union[int, float]]:
        return self.bx, self.by

    @bpos.setter
    def bpos(self, value: Tuple[Union[int, float], Union[int, float]]):
        self.bx, self.by = value

    @property
    def cpos(self) -> Tuple[Union[int, float], Union[int, float]]:
        return self.cx, self.cy

    @cpos.setter
    def cpos(self, value: Tuple[Union[int, float], Union[int, float]]):
        self.cx, self.cy = value

    def __getitem__(self, item):
        return (*self.apos, *self.bpos, *self.cpos)[item]

    def collide(self, shape) -> bool:
        aline = Line(*self.apos, *self.bpos)
        bline = Line(*self.bpos, *self.cpos)
        cline = Line(*self.cpos, *self.apos)
        if isinstance(shape, (Triangle, list, tuple)):
            lines = (aline, bline, cline)
            return Line(*shape[:4]).collidelist(lines) != -1 or Line(*shape[2:]).collidelist(lines) != -1 \
                or Line(*shape[4:], *shape[:2]).collidelist(lines) != -1 or self.collidepoint(*shape[:2]) \
                or self.collidepoint(*shape[2:4]) or self.collidepoint(*shape[4:6])

    def collidepoint(self, x: Union[int, float], y: Union[int, float]) -> bool:
        area_orig = abs((self.bx - self.ax) * (self.cy - self.ay) - (self.cx - self.ax) * (self.by - self.ay))
        area1 = abs((self.ax - x) * (self.by - y) - (self.bx - x) * (self.ay - y))
        area2 = abs((self.bx - x) * (self.cy - y) - (self.cx - x) * (self.by - y))
        area3 = abs((self.cx - x) * (self.ay - y) - (self.ax - x) * (self.cy - y))

        return (area1 + area2 + area3) == area_orig


_shapes_types = (Point, *_Rect_types, Circle, Line, Triangle)


def is_shape(shape) -> bool:
    return isinstance(shape, _shapes_types)


def draw(shape, color=..., surface: Surface = ..., collide_border: bool = False, *args, **kwargs) -> Surface:
    if surface in (None, ...):
        surface = display.get_surface()

    if color in (None, ...):
        color = (0, 0, 0) if collide_border else (40, 40, 240)

    if isinstance(shape, _Rect_types):
        if collide_border:
            _draw.rect(surface, color, shape[:], width=1, *args, **kwargs)
        else:
            _draw.rect(surface, color, shape[:], *args, **kwargs)
    elif isinstance(shape, Circle):
        if collide_border:
            _draw.circle(surface, color, shape.center, shape.radius, width=1, *args, **kwargs)
        else:
            _draw.circle(surface, color, shape.center, shape.radius, *args, **kwargs)
    elif isinstance(shape, Line):
        if 'antialiased' in kwargs and kwargs['antialiased']:
            del kwargs['antialiased']
            if 'width' in kwargs: del kwargs['width']

            _draw.aaline(surface, color, shape.pos, shape.endpos, *args, **kwargs)
        else:
            if 'blend' in kwargs: del kwargs['blend']

            _draw.line(surface, color, shape.pos, shape.endpos, *args, **kwargs)
    elif isinstance(shape, Triangle):
        if collide_border:
            _draw.polygon(surface, color, (shape.apos, shape.bpos, shape.cpos), width=1)
        else:
            _draw.polygon(surface, color, (shape.apos, shape.bpos, shape.cpos), *args, **kwargs)
    elif isinstance(shape, Point):
        surface.set_at(shape.pos, color)

    return surface


def gradient(rect: Rect, colors=..., surface: Surface = ..., horizontal: bool = True) -> Surface:
    if surface in (None, ...):
        surface = display.get_surface()

    if colors in (None, ...):
        colors = []

    if len(colors) == 0:
        return surface

    if not horizontal:
        _gradient = Surface((1, len(colors)))

        for i in range(len(colors)):
            _gradient.set_at((0, i), colors[i])
    else:
        _gradient = Surface((len(colors), 1))

        for i in range(len(colors)):
            _gradient.set_at((i, 0), colors[i])

    surface.blit(transform.smoothscale(_gradient, rect[2:]), rect[:2])

    return surface


__all__ = (
    'Point',
    'Rect',
    'Circle',
    'Line',
    'Triangle',
    'is_shape',
    'draw',
    'gradient'
)
