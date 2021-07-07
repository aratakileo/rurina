from utilities.math import Vector2, _pyi_Vector2Type_type
from shape import _ShapeBase, Rect, Polygon
from pygame.display import get_window_size
from nodes.camera import active_camera
from node.nodetype import NodeType


class Node(NodeType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def rendering_position(self) -> Vector2:
        if active_camera() is not None:
            return generic_position(self) - generic_position(active_camera())

        return generic_position(self)

    @rendering_position.setter
    def rendering_position(self, value: _pyi_Vector2Type_type):
        if active_camera() is not None:
            self.position = value
            return

        self.position = generic_position(active_camera()) + value

    def __visible__(self) -> bool:
        inwindow = True
        shape = get_shape(self, True)

        if shape is not None:
            inwindow = Rect(0, 0, *get_window_size()).collide(shape)

        return super().__visible__() and inwindow


def generic_position(node: NodeType) -> Vector2:
    if 'parent' not in node.__dir__():
        return node.position

    return node.position + generic_position(node.parent)


def get_shape(node: Node, adjust_position: bool = False) -> _ShapeBase:
    returned_shape = None

    if hasattr(node, 'shape'):
        returned_shape = node.shape
    elif hasattr(node, 'rect'):
        returned_shape = node.rect
    elif hasattr(node, 'polygon'):
        returned_shape = node.polygon

    if adjust_position and returned_shape not in (None, ...):
        returned_shape = returned_shape.copy()

        if isinstance(returned_shape, Rect):
            returned_shape.position += node.rendering_position
        elif isinstance(returned_shape, Polygon):
            for i in range(len(returned_shape)):
                returned_shape[i] = Vector2(returned_shape[i]) + node.rendering_position

    return returned_shape


__all__ = (
    'Node',
    'generic_position',
    'get_shape'
)
