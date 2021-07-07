from prefabs.rmath import distance


class Shape:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.node = None

    def __str__(self):
        return f'Shape: {self.__class__.__name__}'

    def __repr__(self):
        return str(self)

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, value):
        self.x, self.y = value

    @property
    def fx(self):
        if self.node is not None:
            return self.x + self.node.fx
        return self.x

    @fx.setter
    def fx(self, value):
        if self.node is not None:
            self.x = value - self.node.fx
        self.x = value

    @property
    def fy(self):
        if self.node is not None:
            return self.y + self.node.fy
        return self.y

    @fy.setter
    def fy(self, value):
        if self.node is not None:
            self.y = value - self.node.fy
        self.y = value

    @property
    def fpos(self):
        return self.fx, self.fy

    @fpos.setter
    def fpos(self, value):
        self.fx, self.fy = value

    @property
    def rx(self):
        if self.node is not None:
            return self.x + self.node.rx
        return self.x

    @rx.setter
    def rx(self, value):
        if self.node is not None:
            self.x = value - self.node.rx
        self.x = value

    @property
    def ry(self):
        if self.node is not None:
            return self.y + self.node.ry
        return self.y

    @ry.setter
    def ry(self, value):
        if self.node is not None:
            self.y = value - self.node.ry
        self.y = value

    @property
    def rpos(self):
        return self.rx, self.ry

    @rpos.setter
    def rpos(self, value):
        self.rx, self.ry = value


class Rect(Shape):
    def __init__(self, x, y, width: int, height: int):
        super().__init__(x=x, y=y)
        self.width, self.height = width, height

    @property
    def size(self):
        return self.width, self.height

    @size.setter
    def size(self, value):
        self.width, self.height = value

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

    @property
    def centerx(self):
        return self.x + self.width / 2

    @centerx.setter
    def centerx(self, value):
        self.x = value - self.width / 2

    @property
    def centery(self):
        return self.y + self.height / 2

    @centery.setter
    def centery(self, value):
        self.y = value - self.height / 2

    @property
    def center(self):
        return self.centerx, self.centery

    @center.setter
    def center(self, value):
        self.centerx, self.centery = value

    @property
    def fright(self):
        return self.fx + self.width

    @fright.setter
    def fright(self, value):
        self.fx = value - self.width

    @property
    def rright(self):
        return self.rx + self.width

    @rright.setter
    def rright(self, value):
        self.rx = value - self.width

    @property
    def fbottom(self):
        return self.fy + self.height

    @fbottom.setter
    def fbottom(self, value):
        self.fy = value - self.height

    @property
    def rbottom(self):
        return self.ry + self.height

    @rbottom.setter
    def rbottom(self, value):
        self.ry = value - self.height

    @property
    def fcenterx(self):
        return self.fx + self.width / 2

    @fcenterx.setter
    def fcenterx(self, value):
        self.fx = value - self.width / 2

    @property
    def fcentery(self):
        return self.fy + self.height / 2

    @fcentery.setter
    def fcentery(self, value):
        self.fy = value - self.height / 2

    @property
    def fcenter(self):
        return self.fcenterx, self.fcentery

    @fcenter.setter
    def fcenter(self, value):
        self.fcenterx, self.fcentery = value

    def collide(self, shape, by_rpos: bool = True):
        if isinstance(shape, Rect):
            if by_rpos:
                return self.rx <= shape.rright \
                       and self.ry <= shape.rbottom \
                       and self.rright >= shape.rx \
                       and self.rbottom >= shape.ry
            else:
                return self.fx <= shape.fright \
                           and self.fy <= shape.fbottom \
                           and self.fright >= shape.fx \
                           and self.fbottom >= shape.fy
        else:
            return shape.collide(self, by_rpos=by_rpos)

    def collide_point(self, x, y, by_rpos: bool = True):
        if by_rpos:
            return self.rx <= x <= self.rright and self.ry <= y <= self.rbottom
        else:
            return self.fx <= x <= self.fright and self.fy <= y <= self.fbottom


class Circle(Shape):
    def __init__(self, x, y, radius: int,):
        super().__init__(x=x, y=y)
        self.radius = radius

    @property
    def diameter(self) -> int:
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = int(value / 2)

    def collide(self, shape, by_rpos: bool = True):
        if isinstance(shape, Circle):
            if by_rpos:
                return distance(*self.rpos, *shape.rpos) < self.radius + shape.radius
            else:
                return distance(*self.fpos, *shape.fpos) < self.radius + shape.radius
        elif isinstance(shape, Rect):
            if by_rpos:
                dx, dy = abs(self.fx - shape.fx), abs(self.fy - shape.fy)

                if (dx > (shape.width / 2 + self.radius)) or (dy > (shape.height / 2 + self.radius)):
                    return False

                if (dx <= (shape.width / 2)) or (dy <= (shape.height / 2)):
                    return True

                dist = (dx - shape.width / 2) ** 2 + (dy - shape.height / 2) ** 2

                return dist <= (self.radius ** 2)
            else:
                dx, dy = abs(self.rx - shape.rx), abs(self.ry - shape.ry)

                if (dx > (shape.width / 2 + self.radius)) or (dy > (shape.height / 2 + self.radius)):
                    return False

                if (dx <= (shape.width / 2)) or (dy <= (shape.height / 2)):
                    return True

                dist = (dx - shape.width / 2) ** 2 + (dy - shape.height / 2) ** 2

                return dist <= (self.radius ** 2)
        else:
            return shape.collide(self, by_rpos=by_rpos)

    def collide_point(self, x, y, by_rpos: bool = True):
        if by_rpos:
            return distance(*self.rpos, x, y) < self.radius
        else:
            return distance(*self.fpos, x, y) < self.radius


def get_offset(shape):
    if isinstance(shape, Circle):
        return shape.radius, shape.radius

    return 0, 0


def get_rpos(shape):
    ox, oy = get_offset(shape)

    return shape.rx - ox, shape.ry - oy


def get_size(shape):
    if isinstance(shape, Rect):
        return shape.size
    elif isinstance(shape, Circle):
        return shape.diameter, shape.diameter


def set_size(shape, width: int, height: int):
    if isinstance(shape, Rect):
        shape.size = width, height
    elif isinstance(shape, Circle):
        shape.diameter = (width + height) / 2


def get_shape(node):
    try:
        return node.shape
    except AttributeError:
        try:
            return node.rect
        except AttributeError:
            pass


__all__ = [
    'Rect',
    'Circle',
    'get_offset',
    'get_rpos',
    'get_size',
    'set_size',
    'get_shape'
]
