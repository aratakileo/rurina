import math


def in_interval(value, min=..., max=...):
    if min in (None, ...):
        min = value

    if max in (None, ...):
        max = value

    return min <= value <= max


def by_interval(value, min=..., max=...):
    if min in (None, ...):
        min = value

    if max in (None, ...):
        max = value

    if value < min:
        return min

    if value > max:
        return max

    return value


def distance(pos1, pos2) -> float:
    return math.sqrt(
        (pos1[0] - pos2[0]) ** 2 +
        (pos1[1] - pos2[1]) ** 2
    )


__all__ = (
    'in_interval',
    'by_interval',
    'distance'
)
