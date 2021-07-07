from .camera import Camera, active_camera, remove as _cameraremove
from node.nodetype import scene, flip, remove as _baseremove, NodeType
from node.node import Node, generic_position


def remove(node: NodeType):
    if isinstance(node, Camera):
        _cameraremove(node)
    else:
        _baseremove(node)


camera = Camera()


__all__ = (
    'Node',
    'Camera',
    'active_camera',
    'flip',
    'remove',
    'generic_position',
    'scene',
    'camera'
)
