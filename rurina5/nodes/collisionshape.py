from node.nodetype import remove as _baseremove
from node.node import Node, generic_position
from typing import Sequence, Optional, Union
from shape import ShapeType, Rect
from pygame.event import Event


_collisionshapes = []


class CollisionShapeType(Node):
    collided_collisionshape: Optional['CollisionShapeType'] = None

    def __init__(self, *args, collisable: bool = True, **kwargs):
        super().__init__(*args, **kwargs)

        self.collisable = collisable

    @property
    def collided(self) -> bool:
        return self.collided_collisionshape not in (None, ...)

    def input(self, event: Sequence[Event]):
        self.collided_collisionshape = None

        if self.enabled:
            super().input(event)

            if self.collisable:
                for collisionshape in _collisionshapes:
                    if collisionshape.collisable and get_shape(self).collide(get_shape(collisionshape)):
                        self.collided_collisionshape = collisionshape
                        break


class CollisionShape(CollisionShapeType):
    def __init__(self, *args, shape: ShapeType = Rect(), **kwargs):
        super().__init__(*args, **kwargs)
        self.shape = shape


class CollisionRect(CollisionShapeType):
    def __init__(self, *args, rect: Rect = Rect(), **kwargs):
        super().__init__(*args, **kwargs)
        self.rect = rect


def get_shape(node, adjust_position: bool = False) -> Union[ShapeType, None]:
    returned_shape = None
    __dir__ = node.__dir__()

    if 'shape' in __dir__:
        returned_shape = node.shape
    elif 'rect' in __dir__:
        returned_shape = node.rect

    if returned_shape not in (None, ...) and adjust_position:
        returned_shape = returned_shape.copy()
        if isinstance(returned_shape, Rect):
            returned_shape.position += generic_position(node)

    return returned_shape


def remove(collisionshape: CollisionShapeType):
    _baseremove(collisionshape)
    _collisionshapes.remove(collisionshape)

    if collisionshape.collided:
        collisionshape.collided_collisionshape.collided_collisionshape = None
        collisionshape.collided_collisionshape = None


__all__ = (
    'CollisionShapeType',
    'CollisionShape',
    'CollisionRect',
    'get_shape',
    'remove'
)
