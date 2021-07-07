from additionalmath import distance
from math import pi
from node import *


class CollisionShape(Node):
    def __init__(self, *args, enabled: bool = True, **kwargs):
        self.enabled = enabled
        super().__init__(*args, **kwargs)


class Rect(CollisionShape):
    def __init__(self, *args, width: int = 0, height: int = 0, **kwargs):
        self.width, self.height = width, height
        super().__init__(*args, **kwargs)

    @property
    def left(self):
        return self.x

    @left.setter
    def left(self, value):
        self.x = value

    @property
    def top(self):
        return self.y

    @top.setter
    def top(self, value):
        self.y = value

    @property
    def right(self):
        return self.x + self.width

    @right.setter
    def right(self, value):
        self.x = value - self.width

    @property
    def bottom(self):
        return self.y + self.height

    @bottom.setter
    def bottom(self, value):
        self.y = value - self.height

    def collide(self, rect):
        return self.right >= rect.left \
               and self.left <= rect.right \
               and self.bottom >= rect.top \
               and self.top <= rect.bottom

    def collide_point(self, x, y):
        return self.right >= x >= self.left \
               and self.bottom >= y >= self.top


class Circle(CollisionShape):
    def __init__(self, *args, radius=0, **kwargs):
        self.radius = radius
        super().__init__(*args, **kwargs)

    @property
    def diameter(self):
        return 2 * self.radius

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def length(self):
        return pi * self.diameter

    @length.setter
    def length(self, value):
        self.diameter = value / pi

    def collide(self, circle):
        return distance(*self.pos, *circle.pos) <= self.radius + circle.radius

    def collide_point(self, x, y):
        return distance(*self.pos, x, y) <= self.radius


class Collision:
    rect = Rect
    circle = Circle


__all__ = ['Node', 'nodes_core', 'Collision']

if __name__ == '__main__':
    r1 = Rect(width=50, height=50)
    r2 = Rect(width=50, height=50)
    r1.x = r1.y = 5
    r2.x = 10
    r2.y = 5
    print(r1.collide_point(*r2.pos))
