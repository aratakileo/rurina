from constants import MAX_ALPHA, MAX_SCALE
from prefabs.rmath import move_negativity


def hovered(node, status: bool, alpha_difference: int = 100):
    node.alpha = MAX_ALPHA + (-alpha_difference if status else 0)


def pressed(node, status: bool, scale_difference=(0.1, 0.1)):
    node.scale = (
        move_negativity(scale_difference[0], MAX_SCALE) + (-scale_difference[0] if status else 0),
        move_negativity(scale_difference[1], MAX_SCALE) + (-scale_difference[1] if status else 0)
    )


__all__ = [
    'hovered',
    'pressed'
]
