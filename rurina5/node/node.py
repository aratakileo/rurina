from utilities.math import Vector2, _pyi_Vector2_type
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
    def rendering_position(self, value: _pyi_Vector2_type):
        if active_camera() is not None:
            self.position = value
            return

        self.position = generic_position(active_camera()) + value


def generic_position(node: NodeType) -> Vector2:
    if 'parent' not in node.__dir__():
        return node.position

    return node.position + generic_position(node.parent)


__all__ = (
    'Node',
    'generic_position',
)
