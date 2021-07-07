from shape import is_shape, Rect
from utilities.string import printwarning
from node.node import Node


# TODO: append auto collide support


class _CollisionShape(Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def collide(self, other) -> bool:
        shape = get_shape(self)
        return False if shape is None else shape.collide(other)

    def collidepoint(self, x, y) -> bool:
        shape = get_shape(self)
        return False if shape is None else shape.collidepoint(x, y)


class CollisionShape(_CollisionShape):
    def __init__(self, *args, shape=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.shape = shape


class CollisionRect(_CollisionShape):
    def __init__(self, *args, rect: Rect = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.rect = rect


def get_shape(collisionshape, adjust_position: bool = True):
    shape = None

    if 'shape' in collisionshape.__dir__():
        shape = collisionshape.shape
    elif 'rect' in collisionshape.__dir__():
        shape = collisionshape.rect

    if adjust_position and is_shape(shape):
            shape = shape.copy()
            shape.pos = collisionshape.rx + shape.x, collisionshape.ry + shape.y

    return shape if shape is not ... else None


def flip():
    printwarning(f'Warning: Function \'flip\' in \"{__file__}\" is incomplete')


__all__ = (
    '_CollisionShape',
    'CollisionShape',
    'CollisionRect',
    'get_shape',
    'flip'
)
