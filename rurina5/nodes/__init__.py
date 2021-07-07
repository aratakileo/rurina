from .collisionshape import CollisionShapeType, CollisionShape, CollisionRect, remove as _collisionshaperemove, get_shape
from .control import Control, get_init, init, remove as _controlremove
from .camera import Camera, remove as _cameraremove, active_camera
from node.nodetype import remove as _noderemove, flip, scene
from node.node import Node, generic_position


camera = Camera()


def remove(node: Node):
    if isinstance(node, Camera):
        _cameraremove(node)
    elif isinstance(node, CollisionShapeType):
        _collisionshaperemove(node)
    elif isinstance(node, Control):
        _controlremove(node)
    else:
        _noderemove(node)


__all__ = (
    'Node',
    'Camera',
    'CollisionShape',
    'CollisionRect',
    'Control',
    'flip',
    'remove',
    'get_shape',
    'generic_position',
    'active_camera',
    'get_init',
    'init',
    'scene',
    'camera',
)
